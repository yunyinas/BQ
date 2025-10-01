#!/data/user/0/com.termux/files/usr/bin/bash
#!/bin/bash

# 定义音乐文件路径
MUSIC_DIR="/data/data/com.termux/files/home/BQ/music/"

# 确保音乐目录存在
if [ ! -d "$MUSIC_DIR" ]; then
    echo -e "\033[1;31m音乐目录不存在，请检查路径！\033[0m"
    exit 1
fi

# 获取音乐文件列表
music_files=($(ls "$MUSIC_DIR" | grep -E '\.mp3$|\.wav$|\.ogg$'))  # 支持 mp3、wav、ogg 格式
if [ ${#music_files[@]} -eq 0 ]; then
    echo -e "\033[1;31m音乐目录中没有找到音乐文件！\033[0m"
    exit 1
fi

# 全局变量
current_music_pid_file="music_pid"

function switch_music {
    local music_file=$1
    local music_name=$(basename "$music_file")
    music_name=${music_name%.*}  # 去掉后缀
    echo -e "\033[1;32m正在播放: $music_name\033[0m"

    # 停止当前播放的音乐
    if [ -f "$current_music_pid_file" ]; then
        local pid=$(cat "$current_music_pid_file")
        kill -0 "$pid" 2>/dev/null && kill "$pid" || true
        rm "$current_music_pid_file"
    fi

    # 播放新选择的音乐
    nohup mpv --no-terminal --loop-file=inf "$music_file" > /dev/null 2>&1 &
    echo $! > "$current_music_pid_file"
}

function play_custom_music {
    echo -e "\033[1;32m请输入自定义音乐文件的路径：\033[0m"
    read custom_music_path
    if [ -f "$custom_music_path" ]; then
        switch_music "$custom_music_path"
    else
        echo -e "\033[1;31m文件不存在，请检查路径！\033[0m"
    fi
}

# 主函数
function music {
    clear
    echo -e "\033[1;33m-----------------------------------\033[0m"
    echo -e "      \033[1;32m      背景音乐\033[0m"
    echo -e "\033[1;33m-----------------------------------\033[0m"
    echo " "
    echo -e "\033[1;32m设置背景音乐\033[0m"

    PS3="请选择操作: "
    select musicopt in "${music_files[@]}" "自定义背景音乐" "退出"
    do
        case $musicopt in
            "自定义背景音乐")
                play_custom_music
                ;;
            "退出")

                break
                ;;
            *)
                if [[ -n $musicopt ]]; then
                    switch_music "$MUSIC_DIR$musicopt"
                else
                    echo -e "\033[1;31m无效选项，请重新选择！\033[0m"
                fi
                ;;
        esac
    done
    echo -e "\033[1;33m程序运行结束\033[0m"
}

# 如果直接运行脚本，则调用主函数
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    music
fi

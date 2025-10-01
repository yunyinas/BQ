import os
import shutil

def clean_comments(file_path, comment_char='#'):
    """清理单个文件的#注释，保留备份"""
    # 创建备份文件
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    print(f"\n✅ 已创建备份: {os.path.basename(backup_path)}")

    # 清理注释并写回
    cleaned_lines = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            comment_idx = line.find(comment_char)
            if comment_idx != -1:
                cleaned_line = line[:comment_idx].strip()
                if cleaned_line:
                    cleaned_lines.append(cleaned_line)
            else:
                cleaned_line = line.strip()
                if cleaned_line:
                    cleaned_lines.append(cleaned_line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_lines))
    print(f"✅ {os.path.basename(file_path)} 清理完成！")

def scan_and_select_files(target_dir):
    """扫描目标路径，展示文件列表供用户选择"""
    # 检查路径是否存在
    if not os.path.exists(target_dir):
        print(f"❌ 路径不存在: {target_dir}")
        return []

    # 筛选目标文件（默认处理.txt，可扩展其他后缀）
    target_extensions = ['.txt', '.ini', '.conf']  # 常见配置文件后缀
    file_list = []
    print(f"\n📂 正在扫描路径: {target_dir}")
    print("="*50)
    for root, _, files in os.walk(target_dir):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in target_extensions:
                full_path = os.path.join(root, file)
                file_list.append(full_path)
                # 显示文件序号和名称（简化路径，只显示文件名和上级目录）
                rel_path = os.path.relpath(full_path, target_dir)
                print(f"{len(file_list)}. {rel_path}")

    if not file_list:
        print("❌ 未找到可清理的配置文件（支持.txt/.ini/.conf）")
        return []

    # 让用户选择文件
    print("="*50)
    while True:
        user_input = input("请输入要清理的文件序号（多个序号用逗号分隔，如1,3）：")
        # 处理输入，提取合法序号
        try:
            selected_nums = [int(num.strip()) for num in user_input.split(',')]
            # 验证序号有效性
            valid_nums = [num for num in selected_nums if 1 <= num <= len(file_list)]
            if not valid_nums:
                print(f"❌ 请输入1-{len(file_list)}之间的有效序号！")
                continue
            # 返回选中的文件路径
            selected_files = [file_list[num-1] for num in valid_nums]
            print(f"\n🔍 你选择了 {len(selected_files)} 个文件：")
            for idx, file in enumerate(selected_files, 1):
                print(f"{idx}. {os.path.basename(file)}")
            return selected_files
        except ValueError:
            print("❌ 输入格式错误！请用逗号分隔序号（如1,3）。")

if __name__ == "__main__":
    # 固定扫描目标路径
    SCAN_DIR = "/storage/emulated/0/云吟工作区/配置文件/"
    print("="*60)
    print("         📝 配置文件注释清理工具")
    print("="*60)

    # 扫描并选择文件
    selected_files = scan_and_select_files(SCAN_DIR)
    if not selected_files:
        exit()

    # 确认清理
    confirm = input("\n⚠️  确认要清理选中文件的注释吗？（y/n）：").lower()
    if confirm != 'y':
        print("\n🚫 操作已取消！")
        exit()

    # 批量清理
    print("\n🚀 开始清理...")
    for file in selected_files:
        clean_comments(file)
    print("\n🎉 所有选中文件清理完成！")

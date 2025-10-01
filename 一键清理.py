import os
def clean_workspace(workspace_path):
    # 检查目录是否存在
    if not os.path.exists(workspace_path):
        print(f"目录 {workspace_path} 不存在")
        return
    
    # 遍历目录下的所有项
    for item in os.listdir(workspace_path):
        item_path = os.path.join(workspace_path, item)
        # 关键：跳过"配置文件"文件夹，不进行清理
        if item == "配置文件" and os.path.isdir(item_path):
            print(f"跳过保护目录: {item_path}")
            continue  # 直接进入下一次循环，不执行后续清理逻辑
        # 只处理其他文件夹（排除了"配置文件"）
        if os.path.isdir(item_path):
            print(f"正在清理文件夹: {item_path}")
            # 遍历文件夹内的所有文件并删除
            for file in os.listdir(item_path):
                file_path = os.path.join(item_path, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"已删除文件: {file_path}")
    print("清理完成!")
if __name__ == "__main__":
    workspace = "/storage/emulated/0/云吟工作区/"
    clean_workspace(workspace)

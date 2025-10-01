#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
create_dirs.py
一次性创建指定目录，并实时打印成功/失败信息
"""

import os

# ---------- 目录列表 ----------
DIRS_TO_CREATE = [
    "/storage/emulated/0/云吟工作区/dat存放区",
    "/storage/emulated/0/云吟工作区/dat打包",
    "/storage/emulated/0/云吟工作区/dat解包",
    "/storage/emulated/0/云吟工作区/paks",
   "/storage/emulated/0/云吟工作区/uexp解包打包/uexp打包",
    "/storage/emulated/0/云吟工作区/uexp解包打包/uexp解包",
    "/storage/emulated/0/云吟工作区/uexp小包存放区/载具小包",
    "/storage/emulated/0/云吟工作区/uexp小包存放区/伪实体小包",
     "/storage/emulated/0/云吟工作区/特征码",
     "/storage/emulated/0/云吟工作区/配置文件",
     "/storage/emulated/0/云吟工作区/自动提取dat",
      "/storage/emulated/0/云吟工作区/偷配置区域/【放入原版PAK】一键全自动偷配置",  
    "/storage/emulated/0/云吟工作区/偷配置区域/原版小包文件夹",    
    "/storage/emulated/0/云吟工作区/偷配置区域/改版小包文件夹",
    "/storage/emulated/0/云吟工作区/偷配置区域/【放入要偷的PAK】一键全自动偷配置",
        "/storage/emulated/0/云吟工作区/制作天线文件【放入PAK】",
       "/storage/emulated/0/云吟工作区/自写升级枪",
]

# ---------- 主逻辑 ----------
def main():
    success_count = 0
    total_count   = len(DIRS_TO_CREATE)

    for d in DIRS_TO_CREATE:
        try:
            os.makedirs(d, exist_ok=True)
            # 再次确认目录是否真的存在
            if os.path.isdir(d):
                print(f"✅ 创建成功：{d}")
                success_count += 1
            else:
                raise OSError("目录创建后仍不存在")
        except Exception as e:
            print(f"❌ 创建失败：{d}  原因：{e}")

    print("\n" + "="*50)
    print(f"全部任务完成！成功：{success_count} / 总计：{total_count}")
    if success_count == total_count:
        print("🎉 所有目录均已成功创建！")
    else:
        print("⚠️  部分目录创建失败，请检查权限或路径！")
    print("="*50)

if __name__ == "__main__":
    main()

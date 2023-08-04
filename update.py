import os
import sys
import zipfile

# 临时文件夹路径
tmp_dir = os.getenv("TEMP")
# 更新文件路径
zip_path = os.path.join(tmp_dir, "update.zip")
# txt文件名（假设为delete_list.txt）
txt_file_name = "delete_list.txt"

# 程序目录
save_path = os.path.dirname(os.path.realpath(sys.executable))
os.system("taskkill /f /im 'server.exe'")
os.system("taskkill /f /im 'HoYoGameLauncher.exe'")
# 解压文件
print("开始解压...")
try:
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        # 解压txt文件到程序目录
        zip_ref.extract(txt_file_name, save_path)
        print("解压完成。")

        # 读取txt文件
        txt_file_path = os.path.join(save_path, txt_file_name)
        with open(txt_file_path, "r") as f:
            file_list = f.read().splitlines()

        # 删除文件
        for file_to_delete in file_list:
            file_path = os.path.join(save_path, file_to_delete)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"文件 {file_to_delete} 已删除。")
            else:
                print(f"文件 {file_to_delete} 不存在。")

        # 删除txt文件
        os.remove(txt_file_path)
        print(f"文件 {txt_file_name} 已删除。")
except Exception as e:
    print(f"解压或删除文件失败：{str(e)}")

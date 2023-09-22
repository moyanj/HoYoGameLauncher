import os

# 获取当前版本号
with open('./version.txt', 'r') as version_file:
    current_version = int(version_file.read())

# 更新版本号（例如递增一个数字）
new_version = current_version + 1

# 将新的版本号写回到version.txt文件中
with open('./version.txt', 'w') as version_file:
    version_file.write(str(new_version))

# 提交version.txt文件的变更
os.system('git add version.txt')
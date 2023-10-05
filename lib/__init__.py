import secrets
from http.cookies import SimpleCookie
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
import zipfile
import os
import subprocess as sub


def encrypt(key, data):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    return iv + ciphertext


def decrypt(key, data):
    iv = data[: AES.block_size]
    ciphertext = data[AES.block_size :]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext


def generate_random_key(length):
    # 生成指定长度的随机字节
    random_bytes = secrets.token_bytes(length)
    # 使用Base64对随机字节进行编码
    encoded_key = b64encode(random_bytes)

    # 将编码后的字节转换为文本形式
    key_text = encoded_key.decode("utf-8")
    # 返回随机字节作为密钥
    return key_text


def load_cookie(ck):
    ck_dict = {}
    cookie = SimpleCookie()
    cookie.load(ck)
    # 遍历解析后的 cookie
    for key, morsel in cookie.items():
        ck_key = key  # cookie 名称
        ck_value = morsel.value  # cookie 值
        ck_dict[ck_key] = ck_value
    return ck_dict


def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()
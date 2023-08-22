import secrets
from http.cookies import SimpleCookie
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode


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

import hashlib
def MaHoaMD5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    md5_hash = md5.hexdigest()
    return md5_hash

def Run():
    userName = "Phạm Đức Thành"  # Dữ liệu bạn muốn mã hoá
    password = "Huflit"

    md5_hash = MaHoaMD5(userName)
    print("Mã băm MD5 của ",userName," là:", md5_hash)

    md5_hash = MaHoaMD5(password)
    print("Mã băm MD5 của ",password," là:", md5_hash)

if __name__ == '__main__':
    Run()

import hashlib

while True:
    str = input('请输入要进行MD5计算的值：')
    if str != 'quit':
        m = hashlib.md5()
        m.update(str.encode('UTF-8'))
        md = m.hexdigest()
        print('32位MD5值：'+md)
        print('16位MD5值：'+md[8:24])
    elif str == 'quit':
        print('退出程序')
        break

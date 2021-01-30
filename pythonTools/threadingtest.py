import threading
import time

import threading
import time

def test1(num):
    print("num: "+num)
def main():
    num = '2';
    t1 = threading.Thread(target=test1,args=(num,))
    t1.start()
if __name__ == '__main__':
    main()

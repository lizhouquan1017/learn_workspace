# coding:utf-8

import os

def test():
    fis = None
    try:
        fis = open('a.txt')
    except OSError as e:
        print(e.strerror)
        # return 语句强制方法返回
        # return
        os._exit(1)
    finally:
        if fis is not None:
            try:
                # 关闭资源
                fis.close()
            except OSError as ioe:
                print(ioe.strerror)
        print('执行finally块里的资源回收')


if __name__ == '__main__':
    test()

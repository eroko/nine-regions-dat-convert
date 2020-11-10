import os
import sys

if len(sys.argv) != 2:
    print('At least one parameter is needed!')
    print('D for Decode, E for Encode')
    exit()
else:
    arg = sys.argv[1]
    print(arg)

basepath = '.\\dat\\'
filepath = os.listdir(basepath)


def decode():
    for file in filepath:
        print(file)
        fpath = basepath + file
        size = os.path.getsize(fpath)
        print(size)
        with open(fpath, 'rb+') as f:
            if f.read(1) == b'\x00':
                _file = f.read()
                _file2 = _file[1:]
                f.flush()
                f.seek(0)
                f.write(_file)
                f.truncate(size - 1)
                f.close()
                print("File %s is Fixed" % f.name)

            else:
                print("File %s has Already Fixed" % f.name)

    print("All Tasks Done!")


def encode():
    for file in filepath:
        print(file)
        fpath = basepath + file
        size = os.path.getsize(fpath)
        print(size)
        with open(fpath, 'rb+') as f:

            if f.read(1) == b'\x00':
                print('File %s Already Restored' % f.name)
                f.close()

            else:
                old = f.read()
                f.seek(0)
                f.write(b'\x00' + b'U' + old)
                f.close()
                print('File %s Restored' % f.name)

    print("All Tasks Done!")


if arg == "D":
    decode()

elif arg == "E":
    encode()

else:
    print("Parameter is illegal")

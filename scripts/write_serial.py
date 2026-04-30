import time

while True:
    try:
        data = open(r'D:\Prace\Wlasne\furnace-physical-ym\out\build\x64-Debug\regs_sys0.bin','rb').read()
        print(f"\r{len(data):4}B  0x{data[8:24].hex(' ',1)}",end='')
    except:
        print("\rno file ",end='')
    time.sleep(0.002)
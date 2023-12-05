import serial
import time
from serial.tools import list_ports

def list_available_ports():
    ports = list_ports.comports()
    return ports

def main():
    # 列出所有可用的串口
    ports = list_available_ports()
    if not ports:
        print("没有找到任何可用的串口。")
        return

    # 打印所有找到的串口
    print("找到以下可用的串口：")
    for idx, port in enumerate(ports, start=1):
        print(f"{idx}. {port.device} - {port.description}")

    # 让用户从列表中选择一个串口
    choice = -1
    while choice not in range(1, len(ports)+1):
        try:
            choice = int(input("请选择一个串口 (输入对应的数字): "))
        except ValueError:
            pass

    selected_port = ports[choice-1]

    # 使用选定的串口
    with serial.Serial(port=selected_port.device, baudrate=9600, timeout=1) as ser:
        print(f"已打开串口: {ser.name}")

        try:
            while True:
                line = ser.readline().decode('utf-8').strip()
                if line:
                    print(line)
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("停止从串口读取数据。")

if __name__ == '__main__':
    main()

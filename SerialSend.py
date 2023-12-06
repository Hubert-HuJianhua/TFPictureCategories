import serial
import time

# Define the serial port and baud rate
serial_port = "COM5"
baud_rate = 9600  # You should set this to match your device's baud rate

try:
    # Create a serial connection
    ser = serial.Serial(serial_port, baud_rate)
    ser.close()
    time.sleep(1)
    # Open the serial connection
    ser.open()
    
    while True:

        # Send data
        data_to_send = "Hello, Arduino!"  # Replace with your data
        ser.write(data_to_send.encode())
        time.sleep(0.1)
    
    # Close the serial connection when done
    
    
except serial.SerialException as e:
    ser.close()
    print("An error occurred:", str(e))

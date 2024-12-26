import serial

try:
    arduino = serial.Serial(port='/dev/cu.usbserial-120', baudrate=9600, timeout=1)
    print("Conexão bem-sucedida!")
except serial.SerialException as e:
    print(f"Erro ao acessar o dispositivo: {e}")

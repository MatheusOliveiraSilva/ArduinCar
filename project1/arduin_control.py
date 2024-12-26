import serial
import time

# Configuração da conexão com o Arduino
arduino = serial.Serial(port='/dev/cu.usbserial-120', baudrate=9600, timeout=1)

def enviar_comando(comando):
    """Envia um comando para o Arduino via serial"""
    arduino.write(comando.encode())  # Envia o comando como texto codificado
    time.sleep(0.5)  # Aguarde um breve momento para o Arduino processar
    resposta = arduino.readline().decode('utf-8').strip()  # Lê a resposta do Arduino
    return resposta

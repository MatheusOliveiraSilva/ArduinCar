import serial
import time

# Configuração da porta serial
# arduino = serial.Serial(port='/dev/cu.usbmodemXXXX', baudrate=9600, timeout=1)
time.sleep(2)  # Aguarde 2 segundos para inicializar a comunicação

def led_control(state):
    """Envia comando para ligar/desligar o LED"""
    # arduino.write(state.encode())

    comando = ""
    if state == '1':
        comando = "LED ligado"
    elif state == '0':
        comando = "LED desligado"

    return f"Comando enviado: {comando}"


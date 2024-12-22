char command;

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);
    Serial.println("Pronto para receber comandos!");
}

void loop() {
    if (Serial.available()) {
        command = Serial.read();
        if (command == '1') {
            digitalWrite(13, HIGH);
            Serial.println("LED ligado!");
        } else if (command == '0') {
            digitalWrite(13, LOW);
            Serial.println("LED desligado!");
        } else {
            Serial.println("Comando inválido. Use '1' para ligar e '0' para desligar.");
        }
    }
}

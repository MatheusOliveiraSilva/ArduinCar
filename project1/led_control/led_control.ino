char command; // Variável para armazenar o comando recebido

void setup() {
    pinMode(13, OUTPUT); // Configura o pino 13 como saída
    Serial.begin(9600);  // Inicializa a comunicação serial a 9600 baud
    Serial.println("Pronto para receber comandos!"); // Mensagem inicial
}

void loop() {
    // Verifica se há dados disponíveis na comunicação serial
    if (Serial.available()) {
        command = Serial.read(); // Lê o comando enviado
        if (command == '1') {
            digitalWrite(13, HIGH); // Liga o LED
            Serial.println("LED ligado!");
        } else if (command == '0') {
            digitalWrite(13, LOW);  // Desliga o LED
            Serial.println("LED desligado!");
        } else {
            Serial.println("Comando inválido. Use '1' para ligar e '0' para desligar.");
        }
    }
}

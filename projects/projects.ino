#include <Arduino_FreeRTOS.h>
#include <semphr.h>

SemaphoreHandle_t xSerialSemaphore;

void taskSerialSend(void *pvParameters) {
  (void) pvParameters;

  const uint8_t PREFIX_A = 0xAA;
  const uint8_t PREFIX_B = 0xBB;
  const uint8_t PREFIX_C = 0xCC;

  uint16_t dataID = 0; // Starting ID

  for (;;) {
    uint16_t variableData = random(100, 1000); // Generate a random 3-digit value for XXX
    uint8_t lowBits = random(0, 999); // Generate random 3 low bits

    char sendData[13]; // AABBCCIDXXX\0

    snprintf(sendData, sizeof(sendData), "%02X%02X%02X%1X%03X\n", PREFIX_A, PREFIX_B, PREFIX_C, dataID++, lowBits, variableData);

    xSemaphoreTake(xSerialSemaphore, portMAX_DELAY);
    Serial.println(sendData);
    xSemaphoreGive(xSerialSemaphore);

    vTaskDelay(1000 / portTICK_PERIOD_MS); // send data every 1000 milliseconds
  }
}

void setup() {
  Serial.begin(9600);

  xSerialSemaphore = xSemaphoreCreateMutex();

  xTaskCreate(taskSerialSend, "SerialSend", 128, NULL, 1, NULL);

  vTaskStartScheduler();
}

void loop() {
  // Code in the loop will not be executed.
}

# Sistema de Riego con Raspberry y Arduino

Sistema de control de riego

*  Control de relés de electroválvulas y relé bomba de riego
*  Medida de condiciones atmosféricas: Temperatura, humedad y presión usando un sensor BME280
*  Se muestra el estado en un lcd 20x4
*  Se envía el estado (relés y sensores) bajo petición por el puerto serie
*  Se define el array de los pines a los que están conectados los N relés
*  Se controla si los relés son de conexión directa o invertida (estado Low los activa)


Pensado para que lo controle una Rapsberry Pi

[Código Arduino V1.6](./RiegoRaspberryArduino/RiegoRaspberryArduino.ino)

TODO:

Módulo Arduino

* Establecer la hora de Arduino desde serie     -       V1.8
* Mostrar hora en el LCD                       -       V1.8
* Programación  de activación a horarios       -       V2.0
* Medida de humedad del suelo                   -      V3.0  


Módulo Raspberry

* Control vía Telegram
* Visualización de estadísticas

Licencia CC by SA by @javacasm

Junio de 2020
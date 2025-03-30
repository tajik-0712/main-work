import objc
from Foundation import *

# Создаем объект для работы с iPhone
device = objc.classForName("IDEVICE").alloc().init()

# Определяем функцию для отправки сообщений
def send_message(message):
    # Создаем объект для отправки сообщений
    message_obj = objc.classForName("NSAppleEventDescriptor").alloc().init()
    message_obj.setStringValue_(message)
    
    # Отправляем сообщение
    device.sendMessage_(message_obj)

# Определяем функцию для проверки подключения устройств
def check_device_connection():
    # Получаем список подключенных устройств
    devices = device.getConnectedDevices()
    
    # Проверяем, есть ли подключенные устройства
    if devices:
        # Отправляем сообщение о подключении устройств
        send_message("К iPhone подключено устройство")
    else:
        # Отправляем сообщение о том, что устройств не подключено
        send_message("Устройств не подключено")

# Запускаем функцию для проверки подключения устройств
check_device_connection()
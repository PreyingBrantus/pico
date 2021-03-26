from machine import ADC, Timer, Pin

led = Pin(25, Pin.OUT)
temp_sensor = ADC(2)
onBoardSensor = ADC(4)
to_volts = 3.3/65535

tim = Timer()


def tick(timer):
    
    led.toggle()
    temperature = temp_sensor.read_u16()
#     print ("ADC: " + str(temperature))

    temperature = temperature * to_volts

#     print("Volts: " + str(temperature))
    print("Sensor [C]: " + str(temperature*100))

    cpuTemp = onBoardSensor.read_u16() * to_volts
    celsius = 27 - (cpuTemp - 0.706) / 0.001721
    print("CPU    [C]: " + str(celsius))
    led.toggle()

tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)




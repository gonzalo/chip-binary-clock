import threading, datetime
import CHIP_IO.GPIO as GPIO

#configure list of leds for each variable
hour_leds = ['LCD-D2','LCD-D3','LCD-D4','LCD-D5','LCD-D6','LCD-D7']
minute_leds = ['LCD-D10','LCD-D11','LCD-D12','LCD-D13','LCD-D14','LCD-D15']
second_leds = ['LCD-D18','LCD-D19','LCD-D20','LCD-D21','LCD-D22','LCD-D23']

def do_every (interval, worker_func, iterations = 0):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ()

  worker_func ()

def print_time():
    current_time = datetime.datetime.now().time()
    print str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second)

def get_binary_time():
    current_time = datetime.datetime.now().time()

    binary_hour_temp = [int(x) for x in list('{0:0b}'.format(current_time.hour))]
    binary_hour = [0] * (6 - len(binary_hour_temp))
    binary_hour.extend(binary_hour_temp)

    binary_minute_temp = [int(x) for x in list('{0:0b}'.format(current_time.minute))]
    binary_minute = [0] * (6 - len(binary_minute_temp))
    binary_minute.extend(binary_minute_temp)

    binary_second_temp = [int(x) for x in list('{0:0b}'.format(current_time.second))]
    binary_second = [0] * (6 - len(binary_second_temp))
    binary_second.extend(binary_second_temp)

    binary_time = dict([('hour',binary_hour),('minute',binary_minute),('second',binary_second)])

    return binary_time

def update_clock_leds():
    binary_time = get_binary_time()

    #load values into pins
    for index in range(0,5):
        GPIO.setup(hour_leds[index], GPIO.OUT)
        GPIO.output(hour_leds[index], binary_time["hour"][index])
        GPIO.setup(minute_leds[index], GPIO.OUT)
        GPIO.output(minute_leds[index], binary_time["minute"][index])
        GPIO.setup(second_leds[index], GPIO.OUT)
        GPIO.output(second_leds[index], binary_time["second"][index])

do_every(1, update_clock_leds)

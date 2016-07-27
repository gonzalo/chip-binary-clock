import threading, datetime, sys, signal
import CHIP_IO.GPIO as GPIO

#configure list of leds for each variable
hour_leds = ['XIO-P0','XIO-P1','XIO-P2','XIO-P3','XIO-P4','XIO-P5']
minute_leds = ['LCD-D10','LCD-D11','LCD-D12','LCD-D13','LCD-D14','LCD-D15']
second_leds = ['LCD-D18','LCD-D19','LCD-D20','LCD-D21','LCD-D22','LCD-D23']

def configure_pins():
  GPIO.cleanup()
  for index in range(0,5):
    GPIO.setup(hour_leds[index], GPIO.OUT)
    GPIO.setup(minute_leds[index], GPIO.OUT)
    GPIO.setup(second_leds[index], GPIO.OUT)

#capture Ctrl-C and free pins before exit
def exit_gracefully(signal, frame):
  GPIO.cleanup()
  print "Clean exit"
  sys.exit(0)

#scheduler function
def do_every (interval, worker_func, iterations = 0):
  if iterations != 1:
    threading.Timer (
      interval,
      do_every, [interval, worker_func, 0 if iterations == 0 else iterations-1]
    ).start ()

  worker_func ()

#printer time function
def print_time():
    current_time = datetime.datetime.now().time()
    print str(current_time.hour) + " : " + str(current_time.minute) + " : " + str(current_time.second)



#get time a turn it into binary
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

#get binary time and write it into leds
def update_clock_leds():
    binary_time = get_binary_time()

    print_time()
    #load values into pins
    for index in range(0,5):
        GPIO.output(hour_leds[index], binary_time["hour"][index])
        GPIO.output(minute_leds[index], binary_time["minute"][index])
        GPIO.output(second_leds[index], binary_time["second"][index])

#MAIN 

#capture ctrl-c event
signal.signal(signal.SIGINT, exit_gracefully)

#configure pins
configure_pins()

#run main loop
do_every(1, update_clock_leds)

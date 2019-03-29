from datetime import datetime
from time import sleep
subscript = 0
time_zero = datetime.now()

for message in range(2000):
    subscript += 1
    print(subscript)
    sleep(.18)
    if subscript == 5:
        time_now = datetime.now()
        td = time_now - time_zero
        subscript = 0
        if td.days == 0 and td.seconds == 0 and td.microseconds < 800000:
            raise Exception('Bot detected')
    
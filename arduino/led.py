import pyfirmata
from pyfirmata import ArduinoMega, util
import time

board = pyfirmata.Arduino('/dev/ttyUSB1')
print("Connection successfully!")

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    board.digital[13].write(1)
    time.sleep(2)
    board.digital[13].write(0)
    time.sleep(2)

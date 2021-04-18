from pyfirmata import ArduinoMega,util
import time

board = ArduinoMega("/dev/ttyUSB1")
it = util.Iterator(board)
it.start()
print("Connection Succesfully!")

# m1r_en = board.get_pin("d:22:o")
# m1l_en = board.get_pin("d:24:o")
# motor1r = board.get_pin("d:2:p")
# motor1l = board.get_pin("d:3:p")
# m1r_en.write(1)
# m1l_en.write(1)

m2r_en = board.get_pin("d:38:o")
m2l_en = board.get_pin("d:40:o")
motor2r = board.get_pin("d:13:p")
motor2l = board.get_pin("d:12:p")
m2r_en.write(1)
m2l_en.write(1)

# m3r_en = board.get_pin("d:22:o") #30
# m3l_en = board.get_pin("d:24:o") #32
# motor3r = board.get_pin("d:3:p") #11
# motor3l = board.get_pin("d:2:p") #10
# m3r_en.write(1)
# m3l_en.write(1)

def clockwise():
    # motor1r.write(0.3)
    # motor1l.write(0)
    motor2r.write(0.3)
    motor2l.write(0)
    # motor3r.write(0.3)
    # motor3l.write(0)
    time.sleep(5)
def stop():
    # motor1r.write(0)
    # motor1l.write(0)
    motor2r.write(0)
    motor2l.write(0)
    # motor3r.write(0)
    # motor3l.write(0)
    time.sleep(2)
def counterclockwise():
    # motor1r.write(0)
    # motor1l.write(0.3)
    motor2r.write(0)
    motor2l.write(0.3)
    # motor3r.write(0)
    # motor3l.write(0.3)
    time.sleep(5)
while True:
    clockwise()
    time.sleep(5)
    stop()
    counterclockwise()
    time.sleep(5)
    stop()
board.exit()
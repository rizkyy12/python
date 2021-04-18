import rospy
from pyfirmata import ArduinoMega, util

def setup():
    try:
        board = ArduinoMega('/dev/ttyUSB0')
        print("Connection Succesfully!")
        it = util.Iterator(board)
        it.start()
    except:
        print("PORT Not Connected")
    
    encA = board.get_pin("d:2:i")
    encB = board.get_pin("d:3:i")
    motor1r = board.get_pin("d:4:p")
    motor1l = board.get_pin("d:5:p")


def readEnc():
    pos = 0
    b = encA.read()
    if b > 0:
        pos+=1
    else:
        pos-=1

if __name__ == '__main__':
    setup()
    print("pos: ", pos)
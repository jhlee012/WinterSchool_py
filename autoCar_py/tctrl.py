# Car Total_Control Full Lib
# Used 'xhat' as based Library - For Simpler Code
# github@jhlee012 / Winterschool_py / autocCar.py (dir)


# Imports
import xhat as hw


# Main Class
class Ctrl:
    def __init__(self):
        self.speed1 = 0
        self.speed2 = 0
        self.moving = False
        self.state = 'Init'

    def clear(self):
        hw.motor_clean()
        self.speed2 = 0
        self.speed1 = 0
        self.moving = False
        self.state = 'Cleared'

    def movecheck(self):  # In While, MovingListener / Also returns Boolean (same as self.moving, also boolean)
        if not self.moving:
            if self.speed2 != 0 or self.speed1 != 0:
                self.moving = True
                return True
            else:
                return False
        else:
            if self.speed1 == 0 and self.speed2 == 0:
                self.moving = False
                return False
            else:
                return True

    def setspeed(self, motor1: int, motor2: int):  # Just set Motor Speed. Not Add, Just SET as individual
        self.speed1 = motor1
        self.speed2 = motor2
        hw.motor_one_speed(motor1)
        print('Runned Motor 1')
        hw.motor_two_speed(motor2)
        print('Runned Motor 2')

    def setdefspeed(self):
        # **WARN**
        # for inherited, Reset motor speed as self.speed1, .speed2
        # This method does not reset self.speed1 as .this
        # to do reset, use .setspeed() Method Instead.
        hw.motor_one_speed(self.speed1)
        hw.motor_two_speed(self.speed2)

    def front(self, speed):  # go front as same speed - Clearance Init.
        self.state = 'front'
        self.setspeed(speed, speed)

    def back(self, speed):  # go front as same speed - Clearance Init.
        self.state = 'back'
        self.setspeed(-speed, -speed)

    def left(self, mainspeed, subspeed):  # turn left - use MotorOne as main motor - Clearance Init
        self.setspeed(mainspeed, subspeed)
        self.state = 'left'

    def right(self, mainspeed, subspeed):  # turn right - use MotorTwo as main motor - Clearance Init
        self.setspeed(subspeed, mainspeed)
        self.state = 'right'

    def addAll(self, speed):  # Add MotorSpeed
        self.speed1 += speed
        self.speed2 += speed
        self.setdefspeed()

    def add1(self, speed): # Add speed of Right Motor (Motor One) - Viewed as TPP - ONLY 1
        self.speed1 += speed
        self.setdefspeed()

    def add2(self, speed):  # Add speed of Left Motor (Motor Two) - Viewed as TPP
        self.speed2 += speed
        self.setdefspeed()

    def leftadd(self, mainadd, subadd):
        self.speed1 += mainadd
        self.speed2 += subadd
        self.setdefspeed()
        if self.state != 'left':
            print('::WARN::\nCurrent State is not LEFT')

    def rightadd(self, mainadd, subadd):
        self.setspeed(self.speed1 + subadd, self.speed2 + mainadd)
        if self.state != 'right':
            print('::WARN:: \nCurrent State is not RIGHT')


if __name__ == '__main__':
    main = Ctrl()
    print('-------------')
    main.setspeed(100, 100)

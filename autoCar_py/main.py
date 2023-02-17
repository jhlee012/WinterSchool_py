# github@jhlee012
# for Gaon-HighSchool's Winterschool Project with SunMoon Univ. 2023 Feb
# Using 'xhat' as Default Lib.
# Using 'tctrl' as Personal Contorl Simplification Lib. (Also Use 'xhat' as def)

# Default Imports
import tctrl
import cv2

# cv2 Config - Default Images
img = cv2.imread('images.png')
cv2.imshow('image', img)

# Setting / Default Variables
start_flag = False
speed1 = 0
speed2 = 0

# Main TCtrl
main = tctrl.Ctrl()

# main Config
# Default - .speed1, .speed2 = 0 | .moving = False | .state = 'init'

while True:
    k = cv2.waitKey(5)

    if k == -1:
        continue  # Blank Input

    print(k)  # Print KeyInput

    if k == ord('q'):  # exit
        main.clear()
        break  # => motor clean & destroy all windows

    elif k == ord('s'):  # start 토글 커맨드
        main.__init__()
        if start_flag:
            start_flag = False
            main.clear()
            main.state = 'Stopped'
        else:
            start_flag = True

    # -- DEPRECATED --
    # elif k == 82:  # Front
    #     speed1 = 50
    #     speed2 = 50
    # elif k == 84:  # Back
    #     speed1 = -50
    #     speed2 = -50
    # elif k == 81:  # Turn Left
    #     speed1 = 100
    #     speed2 = 10
    # elif k == 83:  # Turn Right - Default
    #     speed1 = 10
    #     speed2 = 100
    #
    # if start_flag:
    #     hw.motor_one_speed(speed1)
    #     hw.motor_two_speed(speed2)
    # else:
    #     hw.motor_one_speed(0)
    #     hw.motor_two_speed(0)

    elif k == 82:
        if main.state == 'front':
            main.addAll(25)  # Front ADD
        else:
            main.front(50)  # Front INIT

    elif k == 83:
        if main.state == 'left':
            main.leftadd(5, 0)  # LEFT ADD
        else:
            main.left(5, 100)  # LEFT INIT

    elif k == 81:
        if main.state == 'right':
            main.rightadd(5, 0)  # RIGHT ADD
        else:
            main.right(5, 100)  # RIGHT INIT

    elif k == 84 or k == 181:
        if main.state == 'back':
            main.addAll(-25)  # BACK ADD
        else:
            main.back(50)  # BACK

    elif k == 180:
        if main.state == 'right':
            main.rightadd(-5, 0)
        else:
            main.right(-5, -100)
    elif k == 182:
        if main.state == 'left':
            main.leftadd(-5, 0)
        else:
            main.left(-5, -100)


cv2.destroyAllWindows()

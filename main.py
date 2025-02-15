from microbit import *
import maqueen

# Initialize Maqueen (no arguments needed)
maqueen.init()

# Line Follower
def line_follower():
    while True:
        left_sensor = maqueen.read_patrol(0)  # Left line sensor
        right_sensor = maqueen.read_patrol(1) # Right line sensor

        if left_sensor == 0 and right_sensor == 0:  # On the line
            maqueen.motor_run(0, 60)  # Left motor forward
            maqueen.motor_run(1, 60)  # Right motor forward
        elif left_sensor == 1 and right_sensor == 0:  # Left off line, right on line
            maqueen.motor_run(0, 40)  # Turn left slightly
            maqueen.motor_run(1, 80)
        elif left_sensor == 0 and right_sensor == 1:  # Left on line, right off line
            maqueen.motor_run(0, 80)  # Turn right slightly
            maqueen.motor_run(1, 40)
        elif left_sensor == 1 and right_sensor == 1:  # Both off line (lost line)
            maqueen.motor_run(0, 50) # Go forward or adjust as needed
            maqueen.motor_run(1, 50)
        
        if button_a.is_pressed(): # Exit line following mode
            break
        sleep(20)  # Adjust delay for sensitivity

# Obstacle Avoidance
def obstacle_avoidance():
    while True:
        distance = maqueen.ultrasonic(2) # Ultrasonic sensor on pin2

        if distance < 20:  # Adjust threshold as needed
            maqueen.motor_run(0, -60)  # Reverse left
            maqueen.motor_run(1, 60)   # Turn right
            sleep(500) # Adjust turn duration
        else:
            maqueen.motor_run(0, 60)  # Go forward
            maqueen.motor_run(1, 60)

        if button_b.is_pressed(): # Exit obstacle avoidance
            break
        sleep(20) # Adjust delay

# Light Following (adjust pin as needed)
def light_following():
    while True:
      light_level =  analog_read(pin1) # Corrected: analog_read(pin)

      if light_level > 500: # Adjust threshold
        maqueen.motor_run(0, 80)
        maqueen.motor_run(1, 80)
      else:
        maqueen.motor_run(0, 0)
        maqueen.motor_run(1, 0)

      if button_a.is_pressed(): # Exit light following
          break
      sleep(20)

while True:
    if button_a.is_pressed():
        display.scroll("Line")
        line_follower()
    elif button_b.is_pressed():
        display.scroll("Obstacle")
        obstacle_avoidance()
    elif pin0.is_touched():  # Example: pin0 touched for light following
        display.scroll("Light")
        light_following()
    else:
        maqueen.motor_run(0, 0)  # Stop if no mode is selected
        maqueen.motor_run(1, 0)
    sleep(20)
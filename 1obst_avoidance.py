# This is a basic example of reactive obstacle avoidance using Trilobot's ultrasound
# distance sensor only (no camera). The robot drives forward and, whenever something
# is detected closer than AVOID_DISTANCE, it stops and turns until the way ahead is
# clear again, then carries on driving forward.
# Stop the example by pressing button A.

import time
from trilobot import Trilobot, BUTTON_A

print("Trilobot Example: Obstacle Avoidance\n")

tbot = Trilobot()

AVOID_DISTANCE = 30    # distance in cm at which the robot starts avoiding an obstacle
DRIVE_SPEED = 0.6      # speed used to drive forward
TURN_SPEED = 0.6       # speed used to turn away from an obstacle
TURN_TIME = 0.4        # seconds spent turning before checking the distance again

try:
    while not tbot.read_button(BUTTON_A):

        try:
            distance = tbot.read_distance(timeout=50, samples=3)

        except Exception as e:
            print("Sensor error:", e)
            tbot.disable_motors()
            time.sleep(0.1)
            continue

            print("front distance: {:.1f} cm".format(distance))

             #check wether the sensor reeturned a valid reading
            if distance < 0:
                print("Invalid distance. stopping for safety.")
                tbot.disable_motors()
                time.sleep(0.2)

            #obstacle detected
            elif distance < AVOID_DISTANCE:
                print("Obstacle detected!")
                tbot.disable_motors()
                time.sleep(0.2)

                print("Decision: Turn right")  
                tbot.turn_right(TURN_SPEED)
                time.sleep(TURN_TIME)

                tbot.disable_motors()
                time.sleep(0.2)

            #clear path
        else:
            print("Path clear. Driving forward.")
            tbot.drive_forward(DRIVE_SPEED)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("program interrupted")

finally:
    tbot.disable_motors()
print("Done")
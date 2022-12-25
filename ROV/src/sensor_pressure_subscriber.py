

import rospy
from sensor_msgs.msg import FluidPressure


def sensorInfoCallback(data):
    rospy.loginfo('pressure reading from the sensor is: %f', data.fluid_pressure)


def sensorInfoListener():
    rospy.init_node('sensor_pressure_subscriber', anonymous=False)
    rospy.Subscriber('/rexrov/pressure', FluidPressure, sensorInfoCallback)
    rospy.spin()

    
if __name__ == '__main__':
    sensorInfoListener()

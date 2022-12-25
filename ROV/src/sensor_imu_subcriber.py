

import rospy
from sensor_msgs.msg import Imu


def sensorInfoCallback(data):
    sensor_reading = data
    rospy.loginfo('imu reading from the sensor is: %f', sensor_reading)


def sensorInfoListener():
    rospy.init_node('sensor_imu_subscriber', anonymous=False)
    rospy.Subscriber('/rexrov/imu', Imu, sensorInfoCallback)
    rospy.spin()

    
if __name__ == '__main__':
    sensorInfoListener()

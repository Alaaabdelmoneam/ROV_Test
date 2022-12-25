import rospy
from std_msgs.msg import Header


def sensorInfoCallback(data):
    rospy.loginfo('thruster reading from the sensor is: %f', data.data)


def sensorInfoListener():
    rospy.init_node('thruster1', anonymous=False)
    rospy.Subscriber('/rexrov/thrusters/1/thrust', Header, sensorInfoCallback)
    rospy.spin()


if __name__ == '__main__':
    sensorInfoListener()

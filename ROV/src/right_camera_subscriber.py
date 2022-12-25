

import rospy
from sensor_msgs.msg import Image


def sensorInfoCallback(data):
    image = data
    # rospy.loginfo('imu reading from the sensor is: %f', image)


def sensorInfoListener():
    rospy.init_node('right_image_subscriber', anonymous=False)
    rospy.Subscriber('/rexrov/rexrov/cameraright/camera_image', Image, sensorInfoCallback)
    rospy.spin()
    
if __name__ == '__main__':
    sensorInfoListener()

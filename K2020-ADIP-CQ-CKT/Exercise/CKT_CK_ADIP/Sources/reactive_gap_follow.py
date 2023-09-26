#!/usr/bin/env python
from __future__ import print_function
import sys
import math
import numpy as np

#ROS Imports
import rospy
from sensor_msgs.msg import Image, LaserScan
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

class reactive_follow_gap:
    def __init__(self):
    # Chủ đề và Đăng ký
    lidarscan_topic = '/scan'
    drive_topic = '/nav'

    self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback)  # Đăng ký subscriber cho LiDAR
    self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size=1)  # Publisher cho AckermannDriveStamped

    def preprocess_lidar(self, ranges):
        """ Tiền xử lý mảng quét LiDAR. Cài đặt chuyên gia bao gồm:
            1. Đặt giá trị mỗi phần tử là trung bình trên một cửa sổ
            2. Loại bỏ các giá trị cao (ví dụ: > 3m)
        """
        window_size = 5  # Kích thước cửa sổ trung bình (tùy chỉnh theo nhu cầu)
        proc_ranges = np.copy(ranges)

        # Đặt giá trị mỗi phần tử là trung bình trên một cửa sổ
        for i in range(window_size, len(proc_ranges) - window_size):
            proc_ranges[i] = np.mean(ranges[i - window_size: i + window_size])

        # Loại bỏ các giá trị cao
        max_range_threshold = 3.0  # Ngưỡng giá trị cao (tùy chỉnh theo nhu cầu)
        proc_ranges[proc_ranges > max_range_threshold] = 0.0

        return proc_ranges

    def find_max_gap(self, free_space_ranges):
         """ Trả về chỉ số bắt đầu và kết thúc của khoảng trống lớn nhất trong free_space_ranges
        """
        max_gap_start = 0
        max_gap_end = 0
        current_gap_start = 0
        current_gap_end = 0
        max_gap_length = 0
        current_gap_length = 0

        for i in range(len(free_space_ranges)):
            if free_space_ranges[i] == 0.0:
                # Nếu gặp điểm không tồn tại trong khoảng trống
                if current_gap_length > max_gap_length:
                    # Nếu khoảng trống hiện tại lớn hơn khoảng trống lớn nhất đã tìm thấy trước đó, cập nhật thông tin
                    max_gap_start = current_gap_start
                    max_gap_end = current_gap_end
                    max_gap_length = current_gap_length
                current_gap_length = 0
            else:
                # Nếu gặp điểm tồn tại trong khoảng trống
                if current_gap_length == 0:
                    # Nếu đây là điểm đầu khoảng trống mới, cập nhật thông tin
                    current_gap_start = i
                current_gap_end = i
                current_gap_length += 1

        return max_gap_start, max_gap_end
    
    def find_best_point(self, start_i, end_i, ranges):
        """ start_i và end_i là chỉ số bắt đầu và kết thúc của khoảng trống lớn nhất, tương ứng.
            Trả về chỉ số của điểm tốt nhất trong ranges.
            Naive: Chọn điểm xa nhất trong khoảng và điều khiển tới đó.
        """
        best_point_index = start_i
        max_range = 0.0

        for i in range(start_i, end_i + 1):
            if ranges[i] > max_range:
                best_point_index = i
                max_range = ranges[i]

        return best_point_index

    def lidar_callback(self, data):
        """ Process each LiDAR scan as per the Follow Gap algorithm & publish an AckermannDriveStamped Message
        """
        ranges = data.ranges
        proc_ranges = self.preprocess_lidar(ranges)
	
	# Tìm điểm gần nhất với LiDAR
        closest_point_index = np.argmin(proc_ranges)

        # Loại bỏ tất cả các điểm trong 'bubble' (đặt giá trị của chúng là 0) 
        bubble_radius = 0.5  # Đặt bán kính bubble là 0.5m (tùy chỉnh theo nhu cầu)
        bubble_indices = np.where(proc_ranges < bubble_radius)[0]
        proc_ranges[bubble_indices] = 0.0

        # Tìm khoảng trống dài nhất 
        max_gap_start, max_gap_end = self.find_max_gap(proc_ranges)

        # Tìm điểm tốt nhất trong khoảng trống 
        best_point_index = self.find_best_point(max_gap_start, max_gap_end, proc_ranges)

        # Xuất bản thông điệp Drive
        drive_msg = AckermannDriveStamped()
        drive_msg.header = data.header
        drive_msg.drive.steering_angle = 0.0  # Đặt góc lái là 0 (thẳng)
        drive_msg.drive.speed = proc_ranges[best_point_index]  # Đặt tốc độ bằng khoảng cách tới điểm tốt nhất
        self.drive_pub.publish(drive_msg)

def main(args):
    rospy.init_node("FollowGap_node", anonymous=True)
    rfgs = reactive_follow_gap()
    rospy.sleep(0.1)
    rospy.spin()

if __name__ == '__main__':
    main(sys.argv)

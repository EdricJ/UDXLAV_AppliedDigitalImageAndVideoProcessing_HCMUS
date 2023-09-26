import cv2  #sử dụng thư viện open-cv
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path as p
from pathlib import Path

def Read_Img():
    #lấy địa chỉ thư mục để đọc vào ảnh
    curPath = p.dirname(Path(__file__).parent.absolute().parent)

    while True:
        path = input("Enter your file picture name (file from Data/binary_image): ") #nhap vao ten file ảnh  
        file_dir = Path(curPath + '\\Data\\' + '\\binary_image\\' + path)

        # kiểm tra xem tập tin có tồn tại hay không
        if os.path.isfile(str(file_dir)):
            break 
        else:
            print("Tập tin không tồn tại trong thư mục hiện tại")

    # Đọc ảnh đầu vào đen trắng nhị phân
    img = cv2.imread(str(file_dir), cv2.IMREAD_GRAYSCALE)

    # chuyển đổi ảnh sang dạng nhị phân với ngưỡng 127
    _, binary_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    return binary_img, path

# defining the kernel i.e. Structuring element, tạo ra nhiều lớp mặt nạ kernel khác nhau
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))     #sử dụng để tạo ra một kernel hình elip (ellipse) với kích thước 5x5, và các số 1 tạo thành hình ellipse
kernel_one = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  #mặt nạ kernel hình chữ nhật 3x3
kernel_two = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 3))  #mặt nạ kernel hình chữ nhật 6x3
kernel_thr = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))   #mặt nạ kernel hình chữ thập 5x5
ker = np.array([[0, 1, 0], 
            [1, 1, 1], 
            [0, 1, 0]], dtype=np.uint8)   #mặt nạ kernel hình chữ thập 3x3
kerl = np.ones((5,5),np.uint8)      #mặt nạ kernel hình chữ nhật 5x5

def Choose_Kernel():
    while True:
        exe = input("Enter your kernel (kernel / kernel_one / kernel_two / kernel_thr / ker / kerl): ")     #nhập lựa chọn 1 trong 6 mặt nạ
        
        if exe == "kernel" or exe == "kernel_one" or exe == "kernel_two" or exe == "kernel_thr" or exe == "ker" or exe == "kerl":
            break
    
    return exe

#hàm switch case cho việc chọn lựa các mặt nạ kernel phục vụ cho các phép toán tử
def Kernel(argument): 
    switcher = { 
        "kernel": kernel, 
        "kernel_one": kernel_one, 
        "kernel_two": kernel_two, 
        "kernel_thr": kernel_thr,
        "ker": ker,
        "kerl": kerl
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 
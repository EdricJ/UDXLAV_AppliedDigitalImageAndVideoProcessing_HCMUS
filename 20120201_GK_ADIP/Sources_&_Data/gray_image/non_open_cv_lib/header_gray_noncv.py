from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import os.path as p
from pathlib import Path

def Read_Img():
    #lấy địa chỉ thư mục để đọc vào ảnh
    curPath = p.dirname(Path(__file__).parent.absolute().parent)

    while True:
        path = input("Enter your file picture name (file from Data/gray_image): ") #nhap vao ten file ảnh  
        file_dir = Path(curPath + '\\Data\\' + '\\gray_image\\' + path)

        # kiểm tra xem tập tin có tồn tại hay không
        if os.path.isfile(str(file_dir)):
            break 
        else:
            print("Tập tin không tồn tại trong thư mục hiện tại")

    #đọc vào ảnh màu
    #img_color = cv2.imread(str(file_dir), cv2.IMREAD_COLOR)

    #chuyển xám
    #img_gr = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    # Đọc ảnh đầu vào đen trắng độ xám
    img = Image.open(str(file_dir)).convert('L')

    return img

# defining the kernel, tạo ra nhiều lớp mặt nạ kernel khác nhau
kernel_1 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
kernel_2 = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]])
kernel_3 = np.array([[0, 1, 0], [1, -1, 1], [0, 1, 0]])
kernel_4 = np.ones((5,5),np.uint8)      #mặt nạ kernel hình chữ nhật 5x5
mask = [[1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]      

def Choose_Kernel():
    while True:
        exe = input("Enter your kernel (kernel_1 / kernel_2 / kernel_3 / kernel_4 / mask): ")     #nhập lựa chọn 1 trong 6 mặt nạ
        
        if exe == "kernel_1" or exe == "kernel_2" or exe == "kernel_3" or exe == "kernel_4" or exe == "mask":
            break
    
    return exe

#hàm switch case cho việc chọn lựa các mặt nạ kernel phục vụ cho các phép toán tử
def Kernel(argument): 
    switcher = { 
        "kernel_1": kernel_1, 
        "kernel_2": kernel_2, 
        "kernel_3": kernel_3, 
        "kernel_4": kernel_4,
        "mask": mask
    } 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "nothing") 
from header_binary import *

def main():
    binary_img, _ = Read_Img()
    exe = Choose_Kernel()

    # Tham số iterations quyết định số lần quá trình bào mòn với lớp mặt nạ kernel 
    # Thực hiện toán tử dilation
    dilation = cv2.dilate(binary_img, Kernel(exe), iterations = 1)  #iterations = 1 nghĩa là bào mòn 1 lần

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Dilation"), plt.imshow(dilation, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
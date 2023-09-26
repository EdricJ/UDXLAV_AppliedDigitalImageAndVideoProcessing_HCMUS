from header_binary import *

def main():
    binary_img, _ = Read_Img()
    exe = Choose_Kernel()

    #Thực hiện toán tử tìm biên
    erode = cv2.erode(binary_img, Kernel(exe), iterations = 1)  #co đối tượng lại
    boun_ext = binary_img - erode   #áp dụng công thức

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Boundary Extraction"), plt.imshow(boun_ext, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Thực hiện toán tử opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, Kernel(exe))

    # Perform Grayscale smoothing
    smooth = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, Kernel(exe))    #thực hiện tiếp với ảnh sau khi biến đổi với toán tử opening theo công thức

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Grayscale Smoothing"),plt.imshow(smooth, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

if __name__ == "__main__":
    main()

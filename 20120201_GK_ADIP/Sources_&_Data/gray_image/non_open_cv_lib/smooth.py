from header_gray_noncv import *
from opening import opening
from closing import closing

def smooth_cvt(image, kernel):
    # Thực hiện toán tử opening
    opening_img = opening(image, kernel)

    return closing(np.array(opening_img), kernel)

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Perform Grayscale smoothing
    smooth = smooth_cvt(np.array(img), np.array(Kernel(exe)))    #thực hiện tiếp với ảnh sau khi biến đổi với toán tử opening theo công thức

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Grayscale Smoothing"),plt.imshow(smooth, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

if __name__ == "__main__":
    main()
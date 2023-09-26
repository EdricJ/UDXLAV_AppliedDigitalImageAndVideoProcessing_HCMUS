from header_gray_noncv import *
from opening import opening
from closing import closing

def granulometry_cvt(image, kernel):
    # Thực hiện toán tử opening
    opening_img = opening(image, kernel)
    # Thực hiện toán tử closing
    clos_img = closing(image, kernel)

    return clos_img - opening_img

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Tính toán tử Granulometry bằng cách trừ ảnh đóng và ảnh mở
    granulometry = granulometry_cvt(np.array(img), np.array(Kernel(exe)))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Granulometry"), plt.imshow(granulometry, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
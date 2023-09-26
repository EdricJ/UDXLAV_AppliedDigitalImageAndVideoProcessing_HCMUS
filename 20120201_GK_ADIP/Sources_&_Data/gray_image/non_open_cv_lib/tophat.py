from header_gray_noncv import *
from closing import closing
from opening import opening

def Top_Hat(image, kernel):
    # Thực hiện toán tử opening
    opening_img = opening(image, kernel)

    return image - opening_img

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    top_hat = Top_Hat(np.array(img), np.array(Kernel(exe)))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Top Hat"), plt.imshow(top_hat, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
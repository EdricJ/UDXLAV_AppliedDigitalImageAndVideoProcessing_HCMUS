from header_binary import *

def main():
    binary_img, _ = Read_Img()

    # Áp dụng toán tử thinning
    thinned = cv2.ximgproc.thinning(binary_img, None, cv2.ximgproc.THINNING_ZHANGSUEN)

    #Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Thinning"), plt.imshow(thinned, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
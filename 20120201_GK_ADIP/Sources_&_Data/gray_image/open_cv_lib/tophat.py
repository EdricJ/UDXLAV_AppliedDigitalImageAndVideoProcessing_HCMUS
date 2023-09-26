from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    #thực hiện toán tử Top-hat transformation
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, Kernel(exe))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Top Hat"), plt.imshow(tophat, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
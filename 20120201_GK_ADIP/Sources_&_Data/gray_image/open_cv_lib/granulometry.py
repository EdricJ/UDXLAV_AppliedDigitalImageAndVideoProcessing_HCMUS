from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Thực hiện toán tử opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, Kernel(exe))

    # Thực hiện toán tử closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, Kernel(exe))

    # Tính toán tử Granulometry bằng cách trừ ảnh đóng và ảnh mở
    granulometry = closing - opening

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Granulometry"), plt.imshow(granulometry, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Thực hiện toán tử closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, Kernel(exe))

    #thực hiện toán tử phân đoạn vân
    text_seg = cv2.morphologyEx(closing, cv2.MORPH_OPEN, Kernel(exe))   #thực hiện tiếp với ảnh sau khi biến đổi với toán tử closing theo công thức

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.title("Textural Segmentation"),plt.imshow(text_seg, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

if __name__ == "__main__":
    main()



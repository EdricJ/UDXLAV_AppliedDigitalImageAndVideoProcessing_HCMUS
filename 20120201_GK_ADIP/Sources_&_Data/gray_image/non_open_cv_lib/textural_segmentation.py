from header_gray_noncv import *
from closing import closing
from opening import opening

def textural(image, kernel):
    # Thực hiện toán tử closing
    closing_img = closing(image, kernel)

    return opening(np.array(closing_img), kernel)

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    #thực hiện toán tử phân đoạn vân
    text_seg = textural(np.array(img), np.array(Kernel(exe)))   #thực hiện tiếp với ảnh sau khi biến đổi với toán tử closing theo công thức

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.title("Textural Segmentation"),plt.imshow(text_seg, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

if __name__ == "__main__":
    main()



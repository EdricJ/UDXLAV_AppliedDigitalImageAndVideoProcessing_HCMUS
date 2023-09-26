from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Tham số iterations quyết định số lần quá trình bào mòn với lớp mặt nạ kernel 
    #Thực hiện toán tử tìm biên
    boun_ext = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, Kernel(exe))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Gradient Morphology"), plt.imshow(boun_ext, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
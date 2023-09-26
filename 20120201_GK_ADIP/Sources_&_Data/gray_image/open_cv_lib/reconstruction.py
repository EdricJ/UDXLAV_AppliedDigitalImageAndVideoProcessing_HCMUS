from header_gray import *

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    recon = np.copy(img)
    prev = np.zeros_like(img)

    # Lặp lại quá trình tái tạo cho đến khi không còn thay đổi
    while not np.array_equal(prev, recon):
        prev = np.copy(recon)
        # Áp dụng toán dilation giữa G và B
        dilation = cv2.dilate(recon, Kernel(exe), iterations = 1 )
        # Áp dụng toán erosion giữa kết quả và ảnh đầu vào f
        recon = cv2.bitwise_and(dilation, img)

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Reconstruction"), plt.imshow(recon, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
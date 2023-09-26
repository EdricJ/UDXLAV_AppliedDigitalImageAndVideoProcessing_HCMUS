from header_gray_noncv import *
from dilation import convolution_dilation
from erosion import erosion

#hàm để tính tích chập
def convolve(img, kernel):

    H = (kernel.shape[0] - 1) // 2
    W = (kernel.shape[1] - 1) // 2

    #loại bỏ những giá trị 0 ở viền của ảnh kết quả
    #out = np.zeros((img.shape[0] - kernel.shape[0] + 1, img.shape[1] - kernel.shape[1] + 1))
    #hoặc để padding zero ở viền ảnh gốc để đảm bảo ảnh đầu ra không bị thu nhỏ
    out = np.zeros((img.shape[0], img.shape[1]))

    #Hai vòng lặp ngoài cùng biến đếm i cho hàng, j cho cột, thay đổi để dịch chuyển ma trận mặt nạ kernel
    for i in range(H, img.shape[0] - H):
        for j in range(W, img.shape[1] - W):
            sum = 0
            #Hai vòng lặp k, l thực hiện phép dot product giữa ma trận cửa sổ với kernel
            for k in range(-H, H + 1):
                for l in range(-W, W + 1):
                    a = img[i - k, j - l]
                    w = kernel[H + k, W + l]
                    sum += (w * a)              #g(x, y) =  f(x - i, y - j)*h(i, j) 
            out[i, j] = sum
    return out

def gradient_morp(image, kernel):
    dx = convolve(image, np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]))
    dy = convolve(image, np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]))
    gradient_magnitude = np.sqrt(np.square(dx) + np.square(dy))
    edges = convolve(gradient_magnitude, kernel)

    return edges

def gradient(image, kernel):
    return convolution_dilation(kernel, image) - erosion(image, kernel)


def main():
    img = Read_Img()
    exe = Choose_Kernel()

    # Tham số iterations quyết định số lần quá trình bào mòn với lớp mặt nạ kernel 
    #Thực hiện toán tử tìm biên
    boun_ext = gradient_morp(np.array(img), np.array(Kernel(exe)))
    grad = gradient(np.array(img), np.array(Kernel(exe)))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Gradient Morphology"), plt.imshow(grad, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
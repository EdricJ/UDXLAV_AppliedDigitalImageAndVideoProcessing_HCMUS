from header_bin_noncv import *
from opening import opening
from closing import closing

def main():
    binary_im, _ = Read_Img()
    exe = Choose_Kernel()

    binary_img = np.array(binary_im)
    #Xử lý khi ảnh bị nhiễu
    #white noise & black noise
    noise = np.random.randint(0,2, size = binary_img.shape[:2])
    white_noise_img = noise * 255 + binary_img      #chèn thêm độ nhiễu sáng vào ảnh nhị phân
    black_noise_img = noise * -255 + binary_img
    black_noise_img[black_noise_img <= -245] = 0    #cho độ nhiễu trong phạm vi đối tượng

    #execute noising with morphology Open and Close
    af_noise = opening(np.array(white_noise_img.astype(np.float32)), np.array(Kernel(exe)))
    af_black_nois = closing(np.array(black_noise_img.astype(np.float32)), np.array(Kernel(exe)))

    #show results
    plt.subplot(2,2,1), plt.title("White Noise Image"),plt.imshow(white_noise_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(2,2,2), plt.title("Execute White with Opening"), plt.imshow(af_noise, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3), plt.title("Black Noise Image"), plt.imshow(black_noise_img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4), plt.title("Execute Black with Closing"), plt.imshow(af_black_nois, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
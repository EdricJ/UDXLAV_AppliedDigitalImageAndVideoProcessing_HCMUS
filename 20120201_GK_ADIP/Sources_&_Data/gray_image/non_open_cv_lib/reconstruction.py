from header_gray_noncv import *
from dilation import convolution_dilation
from erosion import erosion

def reconstruction(image, kernel):
    # Khởi tạo kết quả ban đầu là hình ảnh đầu vào
    result = image.copy()
    
    # Thực hiện dilation ban đầu
    dilation = np.zeros_like(result)
    dilation = convolution_dilation(kernel, result)
    
    # Lặp lại quá trình thực hiện dilation và erosion cho đến khi không còn thay đổi nào nữa
    while not np.array_equal(result, dilation):
        result = dilation.copy()
        dilation = convolution_dilation(kernel, result)
        dilation = erosion(dilation, kernel)
    
    return result

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    im_reco = reconstruction(np.array(img), np.array(Kernel(exe)))

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Reconstruction"), plt.imshow(im_reco, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
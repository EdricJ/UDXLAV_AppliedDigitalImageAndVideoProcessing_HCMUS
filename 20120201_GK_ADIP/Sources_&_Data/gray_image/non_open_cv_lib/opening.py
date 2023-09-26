from header_gray_noncv import *
from dilation import convolution_dilation
from erosion import erosion

# Function to perform opening on image
def opening(image, kernel):
    #image_eroded = erosion(image, kernel)
    return convolution_dilation(kernel, np.array(erosion(image, kernel)))

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    im_opening = opening(np.array(img), np.array(Kernel(exe)))
    #pil_img_o = Image.fromarray(im_opening).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Opening Transform"), plt.imshow(im_opening, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()



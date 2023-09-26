from header_gray_noncv import *
from dilation import convolution_dilation
from erosion import erosion

# Function to perform closing on image, given image, structuring element and origin
def closing(image, kernel):
    #image_dilated = convolution_dilation(kernel, image)
    #op_img = erosion(image_dilated, kernel)
    return erosion(np.array(convolution_dilation(kernel, image)), kernel)

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    im_closing = closing(np.array(img), np.array(Kernel(exe)))
    #pil_img_c = Image.fromarray(im_closing).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Closing Transform"), plt.imshow(im_closing, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()


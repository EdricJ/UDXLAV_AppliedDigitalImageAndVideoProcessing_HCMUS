from header_gray_noncv import *

# thực hiện phép tích chập 2D với ma trận kernel và ảnh đầu vào
def convolution_dilation(ker_mat,img):
    h, w = img.shape
    out = np.zeros((h, w), np.uint8)
    ksize = ker_mat.shape[0]
    pad_size = ksize // 2
    img_pad = np.pad(img, (pad_size, pad_size), mode='edge')
    for i in range(h):
        for j in range(w):
            out[i, j] = np.max(img_pad[i:i+ksize, j:j+ksize] * ker_mat)
    return out

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    im_dilation = convolution_dilation(np.array(Kernel(exe)), np.array(img))
    #pil_img_d=Image.fromarracols(im_dilation).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Dilation"), plt.imshow(im_dilation, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
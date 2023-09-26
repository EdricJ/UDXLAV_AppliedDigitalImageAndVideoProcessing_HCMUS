from header_bin_noncv import *

# thực hiện phép tích chập 2D với ma trận kernel và ảnh đầu vào
def convolution_dilation(ker_mat,img):
    #lấy kích thước của ma trận kernel ker_mat
    k_rows, k_cols = ker_mat.shape   
    #lấy kích thước của ảnh đầu vào img
    rows, cols = img.shape

    # tạo ma trận padded image với giá trị 0
    img_pad=np.zeros((rows + k_rows - 1, cols + k_cols - 1))
    img_pad[k_rows-int(k_rows / 2) - 1: k_rows - 1 - int(k_rows / 2) + rows, k_cols - int(k_cols / 2) - 1: k_cols - int(k_cols / 2) - 1 + cols] = img
    
    # tạo ma trận output với giá trị 0
    op_img=np.zeros_like(img)

    # thực hiện dilation bằng cách tính tổng giá trị của các phần tử kernel và pirowsel ảnh tại vị trí tương ứng
    for i in range(int(k_rows / 2), int(k_rows / 2) + rows):
        for j in range(int(k_cols / 2), int(k_cols / 2) + cols):
                window = (ker_mat * img_pad[i - int(k_rows / 2): i - int(k_rows / 2) + k_rows, j - int(k_cols / 2): j - int(k_cols / 2) + k_cols]).sum()

                # Check if the kernel is fully contained within the image
                if(window > 0):
                    op_img[i-int(k_rows/2),j-int(k_cols/2)] = 1
                else:
                    op_img[i-int(k_rows/2),j-int(k_cols/2)] = 0
    
    return op_img

def main():
    binary_img, _ = Read_Img()
    exe = Choose_Kernel()

    im_dilation = convolution_dilation(np.array(Kernel(exe)), np.array(binary_img))
    #pil_img_d=Image.fromarracols(im_dilation).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Dilation"), plt.imshow(im_dilation, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
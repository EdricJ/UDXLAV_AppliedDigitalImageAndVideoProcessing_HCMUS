from header_gray_noncv import *

def erosion(img, kernel):
    # Lấy kích thước ảnh và kernel
    rows, cols = img.shape
    k_rows, k_cols = kernel.shape
    
    # Khởi tạo ảnh kết quả
    result = np.zeros((rows, cols))
    
    # Duyệt qua từng pixel của ảnh đầu vào
    for i in range(rows):
        for j in range(cols):
            # Tìm giá trị nhỏ nhất trong vùng lân cận
            min_val = 255
            for m in range(k_rows):
                for n in range(k_cols):
                    if kernel[m, n] != 0:
                        x = i + m - k_rows // 2
                        y = j + n - k_cols // 2
                        if x >= 0 and x < rows and y >= 0 and y < cols:
                            if img[x, y] < min_val:
                                min_val = img[x, y]
            result[i, j] = min_val
            
    return result.astype(np.uint8)

def main():
    img = Read_Img()
    exe = Choose_Kernel()

    im_erosion = erosion(np.array(img), np.array(Kernel(exe)))
    #pil_img_e=Image.fromarray(im_erosion).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Erosion"), plt.imshow(im_erosion, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
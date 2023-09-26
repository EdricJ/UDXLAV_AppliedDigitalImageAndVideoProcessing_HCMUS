from header_bin_noncv import *
from dilation import convolution_dilation
from erosion import erosion

def hit_or_miss(img, kernel):
    """Hit or Miss operator for binary image"""
    # Tạo các bản sao của kernel
    b1 = kernel.copy()
    b2 = kernel.copy()
    
    # Thay đổi giá trị -1 thành 0 trong bản sao b1 của kernel
    b1[b1==-1] = 0
    # Thay đổi giá trị -1 thành 1 và 0 thành -1 trong bản sao b2 của kernel
    b2[b2==-1] = 1
    b2[b2==0] = -1

    # Thực hiện phép xói mòn với kernel b1, b2 trên ảnh đầu vào
    a = erosion(img,b1)
    b = erosion(~(np.where(img == 255, 1, img)), b2)
    
    # Lấy phép giao giữa 2 ảnh đã xói mòn
    hitmiss_img = np.logical_and(a,b)
    return np.uint8(hitmiss_img)

def main():
    binary_img, _ = Read_Img()
    exe = Choose_Kernel()

    hit_miss = hit_or_miss(np.array(binary_img), np.array(Kernel(exe)))
    #pil_img_hm = Image.fromarray(hit_miss).convert('RGB')

    #Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Hit or Miss"), plt.imshow(hit_miss, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()

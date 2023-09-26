from header_bin_noncv import *
from erosion import erosion

def boundary_extraction(image, kernel):
    #Thực hiện toán tử tìm biên
    erode = erosion(image, kernel)
    return image - erode

def main():
    binary_img, _ = Read_Img()
    exe = Choose_Kernel()

    boun_ext = boundary_extraction(np.array(binary_img), np.array(Kernel(exe)))
    #pil_img_be = Image.fromarray(im_boun).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Boundary Extraction"), plt.imshow(boun_ext, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
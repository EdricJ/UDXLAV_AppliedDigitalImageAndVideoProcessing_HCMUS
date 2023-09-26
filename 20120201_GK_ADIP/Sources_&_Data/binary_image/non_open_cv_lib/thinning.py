from header_bin_noncv import *
from erosion import erosion
from hit_or_miss import hit_or_miss

def thinning(img):
    """
    Thinning morphology using Zhang-Suen algorithm.
    """
    skeleton = np.zeros(img.shape, np.uint8)
    skeleton[img > 0] = 1 # Lấy ảnh nền đen và chuyển thành ảnh trắng
    skeleton = 1 - skeleton # Đảo ngược ảnh để tiện thao tác

    while True:
        to_delete = []

        # Step 1: Loại bỏ các điểm không cần thiết
        for i in range(1, skeleton.shape[0] - 1):
            for j in range(1, skeleton.shape[1] - 1):
                if skeleton[i][j] == 0:
                    continue

                # Tính số lượng điểm lân cận
                neighbors = [skeleton[i-1][j], skeleton[i-1][j+1], skeleton[i][j+1],
                             skeleton[i+1][j+1], skeleton[i+1][j], skeleton[i+1][j-1],
                             skeleton[i][j-1], skeleton[i-1][j-1]]

                # Kiểm tra số lượng điểm lân cận có thoả mãn yêu cầu không
                if sum(neighbors) < 2 or sum(neighbors) > 6:
                    continue

                # Kiểm tra số lượng điểm lân cận thay đổi từ 0 sang 1 có chính xác 1 lần không
                trans = 0
                for k in range(len(neighbors) - 1):
                    if neighbors[k] == 0 and neighbors[k+1] == 1:
                        trans += 1
                if neighbors[-1] == 0 and neighbors[0] == 1:
                    trans += 1

                if trans != 1:
                    continue

                to_delete.append((i, j))

        # Xóa các điểm không cần thiết
        for i, j in to_delete:
            skeleton[i][j] = 0

        # Step 2: Loại bỏ các điểm không cần thiết
        to_delete = []
        for i in range(1, skeleton.shape[0] - 1):
            for j in range(1, skeleton.shape[1] - 1):
                if skeleton[i][j] == 0:
                    continue

                # Tính số lượng điểm lân cận
                neighbors = [skeleton[i-1][j], skeleton[i-1][j+1], skeleton[i][j+1],
                             skeleton[i+1][j+1], skeleton[i+1][j], skeleton[i+1][j-1],
                             skeleton[i][j-1], skeleton[i-1][j-1]]

                # Kiểm tra số lượng điểm lân cận có thoả mãn yêu cầu không
                if sum(neighbors) < 2 or sum(neighbors) > 6:
                    continue

                # Kiểm tra số lượng điểm lân cận thay đổi từ 0 sang 1 có chính xác 1 lần không
                trans = 0
                for k in range(len(neighbors) - 1):
                    if neighbors[k] == 0 and neighbors[k+1] == 1:
                        trans += 1
                if neighbors[-1] == 0 and neighbors[0] == 1:
                    trans += 1

                if trans != 1:
                    continue

                to_delete.append((i, j))

        for i, j in to_delete:
            skeleton[i][j] = 0

        if len(to_delete) == 0:
            break

    skeleton = 1 - skeleton
    return skeleton

def main():
    binary_img, _ = Read_Img()
    #exe = Choose_Kernel()

    thin = thinning(np.array(binary_img))
    #pil_img_t = Image.fromarray(im_thin).convert('RGB')

    #Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Thinning"), plt.imshow(thin, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
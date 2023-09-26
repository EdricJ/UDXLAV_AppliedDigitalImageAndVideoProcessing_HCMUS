from header_bin_noncv import *

# def fill(labels, i, j, label, img):
#     weight, height = img.size
#     if i < 0 or j < 0 or i >= labels.shape[0] or j >= labels.shape[1]:
#         return
#     if labels[i,j] > 0 or img[i,j] == 0:
#         return
#     labels[i,j] = label
#     fill(labels, i+1, j, label, img)
#     fill(labels, i-1, j, label, img)
#     fill(labels, i, j+1, label, img)
#     fill(labels, i, j-1, label, img)

def connected_components(image):
    # Tạo một ma trận lưu trữ kết quả
    labels = np.zeros_like(image)
    label = 1

    # Duyệt qua từng pixel của hình ảnh
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Nếu pixel đã được gán nhãn, bỏ qua
            if image[i][j] == 0 or labels[i][j] != 0:
                continue
            
            # Khởi tạo danh sách liên thông ban đầu
            stack = [(i, j)]
            
            # Lặp qua danh sách liên thông
            while stack:
                # Lấy một pixel từ danh sách liên thông
                pixel = stack.pop()
                x, y = pixel
                
                # Gán nhãn cho pixel
                labels[x][y] = label
                
                # Kiểm tra các pixel lân cận
                neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                for neighbor in neighbors:
                    nx, ny = neighbor
                    # Kiểm tra xem pixel lân cận có nằm trong hình ảnh và chưa được gán nhãn
                    if 0 <= nx < image.shape[0] and 0 <= ny < image.shape[1] and image[nx][ny] != 0 and labels[nx][ny] == 0:
                        # Thêm pixel vào danh sách liên thông
                        stack.append((nx, ny))
            
            # Tăng nhãn lên 1 để gán nhãn cho liên thông tiếp theo
            label += 1
    
    # Đếm số lượng thành phần liên thông và trả về kết quả
    num_labels = label
    return labels, num_labels

def main():
    binary_img, path = Read_Img()
    #exe = Choose_Kernel()

    labels, num_labels = connected_components(np.array(binary_img))

    # Hiển thị ảnh kết quả
    plt.subplot(1,1,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

    # hiển thị ảnh kết quả cho toán tử liên thông 
    if path != "quote.png" and path != "noise.jpg" and  path != "test.jpeg":    #vì ảnh có nhiều thành phần liên thông nên sẽ dẫn đến việc hiển thị nhiều cửa sổ nên không thực hiện
        for i in range(1, num_labels):
            component = np.uint8(labels == i) * 255     #làm sáng các thành phần được chọn
            cv2.imshow('Component ' + str(i), component)    #thể hiện từng thành phần liên thông

            cv2.waitKey(0)  #bổ trợ cho hàm cv2.imshow
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
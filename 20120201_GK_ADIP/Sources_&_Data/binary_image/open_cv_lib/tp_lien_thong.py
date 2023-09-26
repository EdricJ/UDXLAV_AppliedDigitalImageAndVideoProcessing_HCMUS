from header_binary import *

def main():
    binary_img, path = Read_Img()
    #exe = Choose_Kernel()

    # Tham số iterations quyết định số lần quá trình bào mòn với lớp mặt nạ kernel 
    # tìm các đối tượng kết nối bằng cách sử dụng toán tử liên thông
    num_labels, labels = cv2.connectedComponents(binary_img)

    # Hiển thị ảnh kết quả
    plt.subplot(1,1,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

    # hiển thị ảnh kết quả cho toán tử liên thông 
    if path != "quote.png" and path != "noise.jpg" and  path != "test.jpeg" and path != "input3.jpg":    #vì ảnh có nhiều thành phần liên thông nên sẽ dẫn đến việc hiển thị nhiều cửa sổ nên không thực hiện
        for i in range(1, num_labels):
            component = np.uint8(labels == i) * 255     #làm sáng các thành phần được chọn
            cv2.imshow('Component ' + str(i), component)    #thể hiện từng thành phần liên thông

            cv2.waitKey(0)  #bổ trợ cho hàm cv2.imshow
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


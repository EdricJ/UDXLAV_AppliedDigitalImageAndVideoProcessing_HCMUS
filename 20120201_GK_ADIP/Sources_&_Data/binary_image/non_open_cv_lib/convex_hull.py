from header_bin_noncv import *

def compute_convex_hull(image):
    # Lấy tọa độ của các điểm trên đường biên của hình ảnh
    y, x = np.where(image > 0)
    points = np.column_stack((x, y))
    
    # Tính Convex Hull của các điểm
    hull = []
    #duyệt qua các điểm trên đường biên của hình ảnh
    for i in range(len(points)):
        #kiểm tra các điểm trên Convex Hull hiện tại
        while len(hull) >= 2 and np.cross(hull[-1] - hull[-2], points[i] - hull[-2]) <= 0:
            hull.pop()  #xóa điểm cuối cùng của Convex Hull nếu điểm này không nằm trên đường convex
        hull.append(points[i])
        
    #chọn vì điểm cuối cùng đã được thêm vào Convex Hull ở vòng lặp trước
    for i in range(len(points)-2, -1, -1):
        while len(hull) >= 2 and np.cross(hull[-1] - hull[-2], points[i] - hull[-2]) <= 0:
            hull.pop()
        hull.append(points[i])
        
    return np.array(hull)

def main():
    binary_img, _ = Read_Img()
    #exe = Choose_Kernel()

    con_hull = compute_convex_hull(np.array(binary_img))
    #pil_img_ch = Image.fromarray(im_convexhull).convert('RGB')

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"), plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.title("Convex Hull"), plt.plot(con_hull[:, 0], con_hull[:, 1], 'r'), plt.xticks([]), plt.yticks([])
    plt.show()

    

    # img = cv2.convertScaleAbs(con_hull)  #convert the image to an 8-bit unsigned integer to show 

    # cv2.imshow("Convex", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
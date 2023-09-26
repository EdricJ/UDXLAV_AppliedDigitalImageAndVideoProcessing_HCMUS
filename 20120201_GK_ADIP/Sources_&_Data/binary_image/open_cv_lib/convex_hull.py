from header_binary import *

def main():
    binary_img, _ = Read_Img()

    blur = cv2.blur(binary_img, (3, 3)) #blur the image

    _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY) #apply binary thresholding for blur

    # tìm contour trong ảnh threshhold
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Tìm Convex Hull của các contour
    hull = []
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))
    
    # Vẽ Convex Hull lên hình ảnh gốc
    # create an empty black image
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    
    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        # draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)

    # Hiển thị ảnh kết quả
    plt.subplot(1,2,1), plt.title("Original"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(1,2,2), plt.title("Convex Hull"), plt.imshow(drawing, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()
from header_binary import *

def main():
    binary_img, _ = Read_Img()
    #exe = Choose_Kernel()
    
    #thực hiện toán tử Region Filling
    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.
    th_, img_in = cv2.threshold(binary_img, 220, 255, cv2.THRESH_BINARY_INV)
    
    # Copy the thresholded image.
    im_floodfill = img_in.copy()

    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = img_in.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255);
    
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    
    # Combine the two images to get the foreground.
    im_out = img_in | im_floodfill_inv

    # Hiển thị ảnh kết quả
    plt.subplot(2,2,1), plt.title("Thresholded Image"),plt.imshow(img_in, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2), plt.title("Floodfilled Image"),plt.imshow(im_floodfill, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3), plt.title("Inverted Floodfilled Image"),plt.imshow(im_floodfill_inv, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.subplot(2,2,4), plt.title("Foreground"),plt.imshow(im_out, cmap = "gray"), plt.xticks([]), plt.yticks([]) 
    plt.show()

if __name__ == "__main__":
    main()
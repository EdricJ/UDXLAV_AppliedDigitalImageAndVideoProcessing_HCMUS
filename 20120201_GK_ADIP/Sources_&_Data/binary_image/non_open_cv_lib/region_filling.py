from header_bin_noncv import *

def flood_fill(image, start_pixel, fill_color):
    """
    Fill the region starting from start_pixel with fill_color
    """
    # create a copy of the input image
    filled_image = image.copy()

    # get the dimensions of the input image
    height, width = filled_image.shape[:2]

    # define the directions we will search around the start_pixel
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # create a queue to keep track of pixels to be filled
    queue = [start_pixel]

    # get the color of the start_pixel
    start_color = filled_image[start_pixel[0], start_pixel[1]]

    # loop until the queue is empty
    while queue:
        # get the next pixel to fill
        x, y = queue.pop(0)

        # if the pixel is outside the image, skip it
        if x < 0 or x >= height or y < 0 or y >= width:
            continue

        # if the pixel has already been filled or does not match the start color, skip it
        if filled_image[x, y] == fill_color or filled_image[x, y] != start_color:
            continue

        # fill the pixel with the fill color
        filled_image[x, y] = fill_color

        # add the neighboring pixels to the queue to be filled
        for dx, dy in directions:
            queue.append((x + dx, y + dy))

    # return the filled image
    return filled_image

def main():
    # Load the image
    binary_img, _ = Read_Img()

    # Define the starting pixel and fill color
    start_pixel = (100, 100)
    fill_color = 255

    # Fill the region starting from the starting pixel with the fill color
    rg_fill = flood_fill(np.array(binary_img), start_pixel, fill_color)
    #pil_img_rg = Image.fromarray(im_region).convert('RGB')

    # Display image
    plt.subplot(1,2,1), plt.title("Original Image"),plt.imshow(binary_img, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.title("Floodfilled Image"),plt.imshow(rg_fill, cmap = "gray"), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()



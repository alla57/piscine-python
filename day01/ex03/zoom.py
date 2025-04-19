from load_image import ft_load
import sys
import matplotlib.pyplot as plt


def main():
    """Loads 'animal.jpeg', prints info, calculates a zoom region,
    extracts and prints info about the zoomed region (first channel only),
    and displays this zoomed region using Matplotlib with a grayscale colormap.

    The zoom region is calculated as a 400x400 square centered in the
    original image. The extracted region specifically takes the first
    color channel but maintains a 3rd dimension of size 1 (shape HxWx1).

    Prints original pixel data, the shape and pixel data of the zoomed
    region, and displays the zoomed region in a separate window.

    Handles potential exceptions during loading, processing, or display
    by printing an error message to standard output.
    """
    try:
        image_path = "animal.jpeg"
        pixel_data = ft_load(image_path)
        print(pixel_data)
        height, width, _ = pixel_data.shape

        zoom_y = 400
        zoom_x = 400
        y_center, x_center = height // 2, width // 2
        y_start = max(0, y_center - zoom_y // 2)
        y_end = min(height, y_center + zoom_y // 2)
        x_start = max(0, x_center - zoom_x // 2)
        x_end = min(width, x_center + zoom_x // 2)

        new_pixel_data = pixel_data[y_start:y_end, x_start:x_end, 0:1]
        print(f"New shape after slicing: {new_pixel_data.shape} \
              or ({zoom_y}, {zoom_x})")
        print(new_pixel_data)

        plt.imshow(new_pixel_data, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An unexpected error occured: {type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

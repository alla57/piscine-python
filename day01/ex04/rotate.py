from load_image import ft_load
import sys
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Image Transposer

    This program loads an image using a custom `ft_load` function,
    extracts a centered
    zoomed-in region of fixed size (e.g., 400x400 pixels),
    and manually transposes
    the image without using any built-in library functions for transposition.

    The program supports both grayscale (single channel)
    and RGB (three channels)
    images. When grayscale mode is enabled, only one color channel is used.
    The resulting transposed image is displayed using matplotlib.

    Features:
    - Loads an image from disk
    - Crops a zoomed-in region from the center
    - Supports both grayscale and RGB modes
    - Manually transposes the image (no NumPy transpose)
    - Displays the final result using matplotlib

    Dependencies:
    - matplotlib
    - numpy
    - A custom `ft_load()` function (expected to return a NumPy array)

    Usage:
    - Set the `use_grayscale` flag in the script to `True` or `False`
    to control the mode.
    - Make sure the `animal.jpeg` image exists in the working directory.
    - Run the script using a Python interpreter.

    Example:
        python3 image_transposer.py
    """
    try:
        image_path = "animal.jpeg"
        pixel_data = ft_load(image_path)
        height, width, _ = pixel_data.shape

        zoom_y = 400
        zoom_x = 400
        y_start, y_end = 100, 500
        x_start, x_end = 450, 850

        new_pixel_data = pixel_data[y_start:y_end, x_start:x_end, 0:1]
        print(f"The shape of the image is: {new_pixel_data.shape}"
              f" or ({zoom_y}, {zoom_x})")
        print(new_pixel_data)

        y, x, c = new_pixel_data.shape
        transposed_data = [
            [[0 for _ in range(c)] for _ in range(y)] for _ in range(x)]
        for i in range(y):
            for j in range(x):
                for k in range(c):
                    transposed_data[j][i][k] = new_pixel_data[i][j][k]
        transposed_data = np.array(transposed_data)
        transposed_data = transposed_data[:, :, 0]
        # new_pixel_data = np.transpose(new_pixel_data)
        print(f"New shape after Transpose: {transposed_data.shape}")
        print(transposed_data)

        plt.imshow(transposed_data, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An unexpected error occured: {type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

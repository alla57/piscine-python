from load_image import ft_load
import sys
import matplotlib.pyplot as plt


def main():
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

        new_pixel_data = pixel_data[y_start:y_end, x_start:x_end]
        print(f"New shape after slicing: {new_pixel_data.shape} \
              or ({zoom_y}, {zoom_x})")
        print(new_pixel_data)

        tmp = new_pixel_data
        y, x, c = tmp.shape
        for i in range(y):
            for j in range(x):
                for k in range(3):
                    new_pixel_data[i][j][k] = tmp[j][i][k]
        print(f"After transpose")
        print(new_pixel_data)

        plt.imshow(new_pixel_data, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An unexpected error occured: {type(e).__name__}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

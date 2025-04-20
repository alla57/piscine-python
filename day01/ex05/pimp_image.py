import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    image = np.copy(array)
    y, x = image.shape[:2]
    for i in range(y):
        for j in range(x):
            image[i][j][0] = 255 - image[i][j][0]
            image[i][j][1] = 255 - image[i][j][1]
            image[i][j][2] = 255 - image[i][j][2]
    plt.imshow(image)
    plt.show()
    return image


def ft_red(array: np.ndarray) -> np.ndarray:
    """Apply a red filter on the image received."""
    image = np.copy(array)
    image[:, :, 1] = 0
    image[:, :, 2] = 0
    plt.imshow(image)
    plt.show()
    return image


def ft_green(array: np.ndarray) -> np.ndarray:
    """Apply a green filter on the image received."""
    image = np.copy(array)
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    plt.imshow(image)
    plt.show()
    return image


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Apply a blue filter on the image received."""
    image = np.copy(array)
    image[:, :, 0] = 0
    image[:, :, 1] = 0
    plt.imshow(image)
    plt.show()
    return image


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Apply a grey scale filter on the image received."""
    image = np.copy(array)
    y, x = image.shape[:2]
    for i in range(y):
        for j in range(x):
            gray = image[i][j][1]
            image[i][j][0] = gray
            image[i][j][1] = gray
            image[i][j][2] = gray
    plt.imshow(image)
    plt.show()
    return image

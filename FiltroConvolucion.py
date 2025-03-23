import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_custom_filter(image, kernel, padding='same'):
    if padding == 'same':
        pad_y, pad_x = kernel.shape[0] // 2, kernel.shape[1] // 2
        image_padded = cv2.copyMakeBorder(image, pad_y, pad_y, pad_x, pad_x, cv2.BORDER_REPLICATE)
        filtered = cv2.filter2D(image_padded, -1, kernel)
        # Recortar para volver al tamaño original
        filtered = filtered[pad_y:-pad_y, pad_x:-pad_x]
    elif padding == 'valid':
        filtered = cv2.filter2D(image, -1, kernel)
    else:
        raise ValueError("Padding debe ser 'same' o 'valid'")
    return filtered

def get_filtered_images(image_path='radio.jpg', padding='same'):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    results = []

    # Sobel X
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_x_img = apply_custom_filter(image, sobel_x, padding)
    results.append(('Sobel X', sobel_x_img))

    # Sobel Y
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    sobel_y_img = apply_custom_filter(image, sobel_y, padding)
    results.append(('Sobel Y', sobel_y_img))

    # Laplacian
    laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    laplacian_img = apply_custom_filter(image, laplacian, padding)
    results.append(('Laplacian', laplacian_img))

    # Sharpen
    sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpen_img = apply_custom_filter(image, sharpen, padding)
    results.append(('Sharpen', sharpen_img))

    # Gaussian Blur
    gaussian = (1/16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    gaussian_img = apply_custom_filter(image, gaussian, padding)
    results.append(('Gaussian Blur', gaussian_img))

    # Mean Filter
    mean = (1/9) * np.ones((3, 3))
    mean_img = apply_custom_filter(image, mean, padding)
    results.append(('Mean Filter', mean_img))

    # Anomaly Detection (no aplica padding porque usa métodos distintos)
    eq_image = cv2.equalizeHist(image)
    lap = cv2.Laplacian(eq_image, cv2.CV_64F)
    lap = np.uint8(np.abs(lap))
    gauss1 = cv2.GaussianBlur(eq_image, (5, 5), 1)
    gauss2 = cv2.GaussianBlur(eq_image, (5, 5), 2)
    dog = cv2.absdiff(gauss1, gauss2)
    anomaly = cv2.addWeighted(lap, 0.5, dog, 0.5, 0)
    results.append(('Anomaly Detection', anomaly))

    return image, results

def show_all_filters(image_path='radio.jpg', padding='same'):
    image, filtered_results = get_filtered_images(image_path, padding)
    total = len(filtered_results) + 1  # +1 for original image

    plt.figure(figsize=(18, 10))
    plt.subplot(3, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original')
    plt.axis('off')

    for i, (title, img) in enumerate(filtered_results, start=2):
        plt.subplot(3, 3, i)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Ejemplo de uso con padding 'same' o 'valid':
show_all_filters(padding='same')  # o cambia a 'valid'

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_custom_filter(image, kernel, padding='same'):
    if padding == 'same':
        pad_y, pad_x = kernel.shape[0] // 2, kernel.shape[1] // 2
        image_padded = cv2.copyMakeBorder(image, pad_y, pad_y, pad_x, pad_x, cv2.BORDER_REPLICATE)
        filtered = cv2.filter2D(image_padded, -1, kernel)
        filtered = filtered[pad_y:-pad_y, pad_x:-pad_x]  # Recortar al tamaño original
    elif padding == 'valid':
        filtered = cv2.filter2D(image, -1, kernel)
    else:
        raise ValueError("Padding debe ser 'same' o 'valid'")
    return filtered

def get_filtered_images(image_path='radio.jpg', padding='same'):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    results = []

    # Histogram Equalization
    equalized_img = cv2.equalizeHist(image)
    results.append(('Histogram Equalization', equalized_img))

    # CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(image)
    results.append(('CLAHE', clahe_img))

    return image, results

def show_all_filters(image_path='radio.jpg', padding='same'):
    image, filtered_results = get_filtered_images(image_path, padding)
    total = len(filtered_results) + 1  # +1 for original image

    plt.figure(figsize=(10, 5))
    plt.subplot(1, total, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original')
    plt.axis('off')

    for i, (title, img) in enumerate(filtered_results, start=2):
        plt.subplot(1, total, i)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

# Ejecutar con mejora de contraste
show_all_filters(padding='same')

import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_filter(kernel, title, image_path='radio.jpg'):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    filtered_image = cv2.filter2D(image, -1, kernel)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original')
    
    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title(title)
    plt.show()

def sobel_filter(image_path='radio.jpg'):
    sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    apply_filter(sobel_x, 'Sobel X', image_path)
    apply_filter(sobel_y, 'Sobel Y', image_path)

def laplacian_filter(image_path='radio.jpg'):
    laplacian = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    apply_filter(laplacian, 'Laplacian', image_path)

def sharpen_filter(image_path='radio.jpg'):
    sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    apply_filter(sharpen, 'Sharpen', image_path)

def gaussian_filter(image_path='radio.jpg'):
    gaussian = (1/16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
    apply_filter(gaussian, 'Gaussian Blur', image_path)

def mean_filter(image_path='radio.jpg'):
    mean = (1/9) * np.ones((3, 3))
    apply_filter(mean, 'Mean Filter', image_path)

def anomaly_filter(image_path='radio.jpg'):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Ecualización de histograma para mejorar contraste
    eq_image = cv2.equalizeHist(image)
    
    # Aplicar filtro Laplaciano para resaltar bordes
    laplacian = cv2.Laplacian(eq_image, cv2.CV_64F)
    laplacian = np.uint8(np.abs(laplacian))
    
    # Aplicar diferencia de Gauss (DoG) para resaltar anomalías
    gauss1 = cv2.GaussianBlur(eq_image, (5, 5), 1)
    gauss2 = cv2.GaussianBlur(eq_image, (5, 5), 2)
    dog = cv2.absdiff(gauss1, gauss2)
    
    # Combinación de resultados
    result = cv2.addWeighted(laplacian, 0.5, dog, 0.5, 0)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original')
    
    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title('Anomaly Detection')
    plt.show()

# Ejemplo de uso:
sobel_filter()
laplacian_filter()
sharpen_filter()
gaussian_filter()
mean_filter()
anomaly_filter()

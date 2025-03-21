import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def apply_convolution(image_path, kernel, average=False, verbose=False, padding=True):
    try:
        original_image = Image.open(image_path)  # Cargar la imagen en color
        gray_image = original_image.convert('L')  # Convertir a escala de grises
        image = np.array(gray_image)  # Convertir la imagen en un array de NumPy
    except Exception as e:
        raise ValueError(f"Error: No se pudo cargar la imagen. {e}")
    
    if average:
        kernel = kernel / np.sum(kernel)
    
    kernel_row, kernel_col = kernel.shape
    pad_height = kernel_row // 2
    pad_width = kernel_col // 2
    
    if padding:
        image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant', constant_values=0)
    
    output = cv2.filter2D(image, -1, kernel)
    
    if verbose:
        fig, axs = plt.subplots(1, 3, figsize=(15, 5))
        axs[0].imshow(original_image)
        axs[0].set_title("Original Image (Color)")
        axs[0].axis('off')
        
        axs[1].imshow(gray_image, cmap='gray')
        axs[1].set_title("Original Image (Grayscale)")
        axs[1].axis('off')
        
        axs[2].imshow(output, cmap='gray')
        axs[2].set_title("Filtered Image (Convolution with Padding)")
        axs[2].axis('off')
        
        plt.show()
    
    return output

# Ejemplo de uso
kernel = np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]])
apply_convolution("Turquia.jpg", kernel, verbose=True)

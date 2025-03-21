import numpy as np
import cv2
import matplotlib.pyplot as plt

def convolve_with_padding(image, kernel, padding_type='zero', average=False, verbose=False):
    if len(image.shape) == 3:
        print(f"Original image with {image.shape[2]} channels.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Converted to grayscale. Shape: {image.shape}")
    else:
        print(f"Grayscale image. Shape: {image.shape}")

    # Rotar kernel 180° para convolución real
    kernel = np.flipud(np.fliplr(kernel))
    print(f"Kernel rotated. Shape: {kernel.shape}")

    if verbose:
        plt.imshow(image, cmap='gray')
        plt.title("Input Image")
        plt.show()

    iH, iW = image.shape
    kH, kW = kernel.shape
    pad_h = kH // 2
    pad_w = kW // 2

    # Elegir tipo de padding
    if padding_type == 'zero':
        padded = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_CONSTANT, value=0)
    elif padding_type == 'replicate':
        padded = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_REPLICATE)
    elif padding_type == 'reflect':
        padded = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_REFLECT)
    elif padding_type == 'wrap':
        padded = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_WRAP)
    else:
        raise ValueError("Padding type not recognized. Use 'zero', 'replicate', 'reflect', or 'wrap'.")

    print(f"Padding type: {padding_type}, Padded shape: {padded.shape}")

    if verbose:
        plt.imshow(padded, cmap='gray')
        plt.title(f"Padded Image ({padding_type})")
        plt.show()

    # Crear imagen de salida
    output = np.zeros_like(image, dtype=float)

    # Aplicar convolución
    for y in range(iH):
        for x in range(iW):
            region = padded[y:y + kH, x:x + kW]
            value = np.sum(region * kernel)
            if average:
                value /= (kH * kW)
            output[y, x] = value

    print(f"Output Image Shape: {output.shape}")

    if verbose:
        plt.imshow(output, cmap='gray')
        plt.title(f"Convolved Output ({padding_type})")
        plt.show()

    return output

# Cargar imagen REAL (asegúrate de tener una imagen .jpg, .png en la misma carpeta)
img = cv2.imread('Turquia.jpg')  # Cambia por el nombre real de tu imagen

if img is None:
    print("⚠️ Error: No se pudo cargar la imagen. Verifica la ruta y nombre del archivo.")
    exit()

# Kernel de desenfoque 3x3
kernel = np.ones((3, 3))

# Padding tipo 'reflect' y visualización activada
resultado = convolve_with_padding(img, kernel, padding_type='reflect', average=True, verbose=True)

# Guardar imagen resultante
cv2.imwrite('resultado_reflect.jpg', resultado.astype(np.uint8))

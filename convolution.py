import numpy as np
import cv2
import matplotlib.pyplot as plt

def convolve_image(image, kernel, average=False, verbose=False):
    if len(image.shape) == 3:
        print(f"Original image with {image.shape[2]} channels.")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(f"Converted to grayscale. Shape: {image.shape}")
    else:
        print(f"Grayscale image. Shape: {image.shape}")

    kernel = np.flipud(np.fliplr(kernel))  # Rotar 180° el kernel
    print(f"Kernel rotated. Shape: {kernel.shape}")

    if verbose:
        plt.imshow(image, cmap='gray')
        plt.title("Input Image")
        plt.show()

    iH, iW = image.shape
    kH, kW = kernel.shape

    pad_h = kH // 2
    pad_w = kW // 2
    padded = cv2.copyMakeBorder(image, pad_h, pad_h, pad_w, pad_w, cv2.BORDER_CONSTANT, value=0)

    if verbose:
        plt.imshow(padded, cmap='gray')
        plt.title("Padded Image")
        plt.show()

    output = np.zeros_like(image, dtype=float)

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
        plt.title("Convolved Output")
        plt.show()

    return output

# -------------------
# ⬇️ EJEMPLO DE USO ⬇️
# -------------------

# Leer imagen
img = cv2.imread('Turquia.jpg')  # Cambia 'tu_imagen.jpg' por la ruta de tu imagen

# Crear un kernel de desenfoque 3x3
kernel = np.ones((3, 3))

# Llamar a la función de convolución
resultado = convolve_image(img, kernel, average=True, verbose=True)

# Guardar resultado (opcional)
cv2.imwrite('resultado.jpg', resultado)

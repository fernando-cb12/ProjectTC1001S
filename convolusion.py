import numpy as np
import cv2

def apply_convolution(image, kernel, padding):
    # Add padding to the image
    if padding > 0:
        image = np.pad(image, ((padding, padding), (padding, padding)), mode='constant', constant_values=0)

    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    for y in range(output_height):
        for x in range(output_width):
            region = image[y:y + kernel_height, x:x + kernel_width]
            output[y, x] = np.sum(region * kernel)

    return output

# Load the image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("The image file 'image.jpg' was not found or could not be loaded.")

# Define a kernel (example: edge detection)
kernel = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])

# Apply convolution with padding
padding = 1
convolved_image = apply_convolution(image, kernel, padding)

# Save the result
cv2.imwrite('output_image.jpg', convolved_image)

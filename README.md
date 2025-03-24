# Detección de Bordes con Convolución en Python

## Descripción del Proyecto

Este proyecto implementa un **filtro de detección de bordes** mediante convolución en Python. Se aplica un kernel de realce de bordes a una imagen en escala de grises utilizando operaciones matriciales.

## Estructura del Proyecto

```
│── convolution.py  # Script principal
│── image.jpg       # Imagen de prueba
│── output_image.jpg # Imagen resultante después de la convolución
│── README.md       # Documentación
```

## Instalación y Ejecución

### Requisitos Previos

Es necesario tener instalado Python y las siguientes librerías:

```sh
pip install numpy opencv-python
```

### Ejecución del Proyecto

Para ejecutar el script y aplicar el filtro de detección de bordes a la imagen, usa el siguiente comando en la terminal:

```sh
python convolution.py
```

El script procesará la imagen `image.jpg`, aplicará el filtro y guardará la imagen resultante como `output_image.jpg`.

## Fundamentos Teóricos - Detección de Bordes

El proceso de detección de bordes en imágenes se basa en la aplicación de un **kernel de convolución**. En este caso, se usa un kernel de realce de bordes:

\[
K = \begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}
\]

Este kernel resalta los cambios abruptos en la intensidad de los píxeles, lo que ayuda a detectar los bordes de los objetos en la imagen.

## Bibliografía

_(Espacio para insertar referencias)_

## Colaborador

- **Fernando Camou Bejarano** - A01255376

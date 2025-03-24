# Filtro de Convolución - Contrast Enhancement

## Descripción del Proyecto

Este proyecto implementa un filtro de convolución en Python para mejorar el contraste de una imagen. Utiliza operaciones de procesamiento digital de imágenes para resaltar los detalles visuales y mejorar la calidad de la imagen original.

## Estructura del Proyecto

```
resources/
│── Figure_1.png  # Resultado del filtro aplicado a 'radio.jpg'
│── Figure_2.png  # Resultado del filtro aplicado a 'boca.png'
│── boca.png      # Imagen de prueba
│── radio.jpg     # Imagen de prueba
│── FiltroConvolucion.py  # Script principal
│── README.md  # Documentación
```

## Instalación y Ejecución

### Requisitos Previos

Asegúrate de tener instalado Python y las siguientes librerías:

```sh
pip install numpy opencv-python matplotlib
```

### Ejecución del Proyecto

Para ejecutar el código y aplicar el filtro a una imagen, usa el siguiente comando en la terminal:

```sh
python FiltroConvolucion.py
```

El script tomará una imagen de prueba, aplicará el filtro de convolución y generará las salidas en la carpeta `resources/`.

## Fundamentos Teóricos - Convolución y Mejora de Contraste

El filtro de convolución es una operación matemática utilizada en el procesamiento de imágenes para modificar ciertas características de la imagen, como el contraste o la detección de bordes. En este caso, se implementa un **filtro de realce de contraste**, el cual enfatiza las diferencias entre las regiones claras y oscuras de una imagen.

**Definición de Convolución**:
La convolución en procesamiento de imágenes se define como:

\[ I'(x,y) = \sum*{i=-k}^{k} \sum*{j=-k}^{k} I(x+i, y+j) \cdot K(i,j) \]

donde:

- \( I(x,y) \) es la imagen original,
- \( K(i,j) \) es el kernel (matriz de convolución),
- \( I'(x,y) \) es la imagen resultante.

El kernel utilizado en este proyecto resalta los bordes y mejora la percepción de detalles en la imagen.

## Bibliografía

## Colaboradores

- **Antonio Jesús Calderón Burgos** - A01255264
- **Fernando Camou Bejarano** - A01255376
- **Marco Antonio Ibarra Yedra**
- **Luis Carlos Mares Rivera**

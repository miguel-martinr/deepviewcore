# deepviewcore

Este repositorio contiene el código del núcleo de procesamiento de imágenes **DeepView**, mi Trabajo de Fin de Grado (TFG) para obtener el título de Ingeniero Informático por la Universidad de La Laguna.

## Introducción
Este paquete contiene las clases y funciones necesarias para procesar imágenes submarinas y detectar la biomasa presente en las escenas.


## 0.1.5 Detección de eventos
Detección simple de eventos. Ahora el callback de la función `Video.process()` es llamado con un array con la forma `[objects, events]`, donde `objects` son objetos iguales a los utilizados hasta el momento y `events` un diccionario donde las keys representan un segundo del vídeo y los valores representan una lista con los eventos detectados.

Estos eventos son objetos con la misma forma que los de `objects`.

Para especificar un área mínima a partir de la cual considerar un objeto como "evento" se utiliza el parámetro `options` de la siguiente forma:

```Python
options = {
  "events": { "minArea": 200 }
}
Video.process(... options = options)
```


El valor por defecto es 100.


## 0.1.6 Corrección de errores
* Se corrigió un error de iteradores que provocaba la no detección de partículas.

## Enlaces de interés
[DeepView: Backend](https://github.com/miguel-martinr/DeepView)

[DeepView: Frontend](https://github.com/miguel-martinr/DeepView)
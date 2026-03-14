# Clonador de Voz Local con XTTS v2

Este proyecto permite clonar voces a partir de un archivo de audio de referencia y generar audios largos (más de 10 minutos) en múltiples idiomas, funcionando de forma totalmente local.

## Características

- **Clonación de voz multilingüe:** Utiliza el modelo XTTS v2 de Coqui TTS.
- **Soporte para audios largos:** Divide automáticamente el texto en fragmentos para evitar errores de memoria y procesar textos extensos.
- **Múltiples idiomas:** Soporta español, inglés, francés, alemán, italiano, portugués, entre otros.
- **Optimizado para hardware modesto:** Funciona en GPUs con poca VRAM (como la GTX 1060 3GB) o en CPU como fallback.
- **Modular y extensible:** Código organizado en módulos para fácil mantenimiento.

## Requisitos de Hardware

- **CPU:** Intel i5 8va generación o superior (recomendado).
- **GPU:** Nvidia GTX 1060 3GB VRAM o superior (Opcional, pero recomendado para velocidad).
- **RAM:** 16GB.
- **Espacio en disco:** ~5GB para el modelo y dependencias.

## Instalación Paso a Paso

### 1. Instalación de Python
Descarga e instala Python 3.9 o 3.10 desde [python.org](https://www.python.org/downloads/). Asegúrate de marcar la casilla "Add Python to PATH" durante la instalación.

### 2. Instalación de FFmpeg
Este proyecto requiere FFmpeg para manipular archivos de audio.
- Descarga FFmpeg desde [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
- Descomprime y añade la carpeta `bin` a las variables de entorno (PATH) de tu sistema.

### 3. Crear Entorno Virtual
Abre una terminal en la carpeta del proyecto y ejecuta:
```bash
python -m venv venv
```
Actívalo:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

### 4. Instalación de Dependencias
Con el entorno virtual activo, instala las librerías necesarias:
```bash
pip install -r requirements.txt
```

*Nota: Si tienes una GPU Nvidia, asegúrate de tener instalados los drivers de CUDA compatibles con tu versión de PyTorch.*

## Uso del Programa

Para iniciar la aplicación, ejecuta:
```bash
python main.py
```

El programa te guiará a través de los siguientes pasos:
1. **Ruta del archivo de voz:** Introduce la ruta de un archivo `.wav` de 6 a 10 segundos con la voz que quieres clonar.
2. **Entrada de texto:** Puedes escribir el texto manualmente o proporcionar la ruta de un archivo `.txt`.
3. **Idioma:** Escribe el código del idioma (ej: `es` para español, `en` para inglés).
4. **Nombre de salida:** El nombre que tendrá tu archivo generado en la carpeta `/output`.

## Estructura del Proyecto

- `main.py`: Punto de entrada de la aplicación (CLI).
- `tts_engine.py`: Lógica de carga del modelo XTTS v2 y síntesis.
- `audio_utils.py`: Herramientas para procesar y unir archivos de audio.
- `text_chunker.py`: Algoritmo para dividir textos largos de forma inteligente.
- `config.py`: Configuraciones globales y rutas.
- `/voices`: Carpeta sugerida para guardar tus muestras de voz.
- `/output`: Carpeta donde se guardan los audios generados.

## Consejos para Mejor Calidad de Voz

1. **Audio de referencia limpio:** Asegúrate de que el audio de referencia no tenga ruido de fondo, música ni múltiples personas hablando.
2. **Duración óptima:** Un clip de 10 segundos es generalmente ideal.
3. **Formato:** Usa preferiblemente archivos `.wav` mono a 22050Hz o 24000Hz.
4. **Puntuación:** El modelo XTTS v2 responde muy bien a la puntuación adecuada (. , ! ?) para la entonación.

## Solución de Errores Comunes

- **"Out of Memory" (OOM) en GPU:** Si recibes este error, intenta reducir el `CHUNK_SIZE` en `config.py` a 150 o 200.
- **Error con FFmpeg:** Asegúrate de que `ffmpeg` está correctamente instalado y accesible desde la terminal (escribe `ffmpeg -version` para probar).
- **Descarga del modelo:** La primera vez que ejecutes el programa, se descargará el modelo XTTS v2 (~2GB). Asegúrate de tener una conexión a internet estable.

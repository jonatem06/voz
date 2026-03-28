import os
import sys
import config
from tts_engine import TTSEngine
from text_chunker import split_text
from audio_utils import combine_audios, validate_audio, normalize_audio
from tqdm import tqdm

def main():
    print("=========================================")
    print("   Clonador de Voz XTTS v2 - Local TTS   ")
    print("=========================================")

    # 1. Voice selection
    speaker_wav = input("Ruta del archivo de voz de referencia (.wav): ").strip()
    if not speaker_wav:
        print("Error: Se requiere un archivo de voz.")
        return

    valid, msg = validate_audio(speaker_wav)
    if not valid:
        print(f"Error: {msg}")
        return

    # Normalize voice for better results
    print("--- Normalizando audio de referencia ---")
    speaker_wav = normalize_audio(speaker_wav)

    # 2. Text input
    input_type = input("¿Ingresar texto manual (m) o cargar archivo txt (f)? [m/f]: ").lower().strip()
    text = ""
    if input_type == 'f':
        txt_path = input("Ruta del archivo .txt: ").strip()
        try:
            # Try UTF-8 first, fallback to latin-1 for Windows-style files
            try:
                with open(txt_path, 'r', encoding='utf-8') as f:
                    text = f.read()
            except UnicodeDecodeError:
                with open(txt_path, 'r', encoding='latin-1') as f:
                    text = f.read()
        except FileNotFoundError:
            print(f"Error: El archivo {txt_path} no fue encontrado.")
            return
        except Exception as e:
            print(f"Error al leer el archivo de texto: {e}")
            return
    else:
        text = input("Ingrese el texto a generar: ").strip()

    if not text:
        print("Error: No hay texto para procesar.")
        return

    # 3. Language
    print(f"Idiomas soportados: {', '.join(config.SUPPORTED_LANGUAGES)}")
    language = input(f"Elija el idioma (default '{config.DEFAULT_LANGUAGE}'): ").strip() or config.DEFAULT_LANGUAGE

    # 4. Output filename
    output_filename = input("Nombre del archivo de salida (sin extensión): ").strip() or "output_audio"
    output_format = input("Elija el formato de salida (wav/mp3) [default wav]: ").lower().strip() or "wav"
    output_path = os.path.join(config.OUTPUT_DIR, f"{output_filename}.wav")

    # Initialize Engine
    try:
        engine = TTSEngine()
    except Exception as e:
        print(f"No se pudo inicializar el motor TTS: {e}")
        return

    # Process Chunks
    print("--- Dividiendo texto en fragmentos ---")
    chunks = split_text(text, chunk_size=config.CHUNK_SIZE)
    print(f"Total de fragmentos: {len(chunks)}")

    temp_files = []

    print("--- Generando audio ---")
    for i, chunk in enumerate(tqdm(chunks)):
        temp_file = os.path.join(config.OUTPUT_DIR, f"temp_{i}.wav")
        success = engine.generate_speech(
            text=chunk,
            speaker_wav=speaker_wav,
            language=language,
            output_path=temp_file
        )
        if success:
            temp_files.append(temp_file)
        else:
            print(f"Error generando fragmento {i}")

    # Combine
    if temp_files:
        print("--- Uniendo audios finales ---")
        try:
            final_path_wav = combine_audios(temp_files, output_path)
        except Exception as e:
            print(f"Error al combinar audios: {e}")
            return

        # Clean up temp files
        for f in temp_files:
            if os.path.exists(f):
                os.remove(f)

        final_path = final_path_wav
        if output_format == "mp3":
            from audio_utils import convert_to_format
            print("--- Convirtiendo a MP3 ---")
            final_path = convert_to_format(final_path_wav, "mp3")
            if os.path.exists(final_path_wav):
                os.remove(final_path_wav)

        print(f"¡Proceso completado! Audio guardado en: {final_path}")
    else:
        print("No se generó ningún audio.")

if __name__ == "__main__":
    main()

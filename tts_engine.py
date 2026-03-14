import os
import torch
from TTS.api import TTS
import config

class TTSEngine:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"--- Cargando modelo XTTS v2 en {self.device} ---")

        # XTTS v2 requires agreement to terms
        # This will download the model if not present
        try:
            # Check if we have GPU and if it is 1060 3GB, we might want to be careful
            # but XTTS v2 usually fits in 3GB if chunks are small.
            # XTTS v2 requires agreement to terms of use.
            self.tts = TTS(model_name=config.MODEL_NAME, gpu=(self.device == "cuda"))
            print("--- Modelo cargado correctamente ---")
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            raise e

    def generate_speech(self, text, speaker_wav, language, output_path):
        """
        Generates speech for a single chunk of text.
        """
        try:
            self.tts.tts_to_file(
                text=text,
                speaker_wav=speaker_wav,
                language=language,
                file_path=output_path
            )
            return True
        except Exception as e:
            print(f"Error en generación: {e}")
            return False

    def get_supported_languages(self):
        return self.tts.languages

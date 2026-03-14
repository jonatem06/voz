import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VOICES_DIR = os.path.join(BASE_DIR, "voices")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
EXAMPLES_DIR = os.path.join(BASE_DIR, "examples")

# Ensure directories exist
for folder in [VOICES_DIR, OUTPUT_DIR, EXAMPLES_DIR]:
    os.makedirs(folder, exist_ok=True)

# TTS Configuration
MODEL_NAME = "tts_models/multilingual/multi-dataset/xtts_v2"
DEFAULT_LANGUAGE = "es"
CHUNK_SIZE = 250  # Character count for text splitting

# Supported languages by XTTS v2
SUPPORTED_LANGUAGES = [
    "en", "es", "fr", "de", "it", "pt", "pl", "tr", "ru", "nl", "cs", "ar", "zh-cn", "hu", "ko", "ja"
]

# Audio Configuration
SAMPLE_RATE = 24000  # XTTS v2 default sample rate
OUTPUT_FORMAT = "wav" # Default format

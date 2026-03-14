from pydub import AudioSegment
import os
import librosa
import soundfile as sf

def combine_audios(audio_files, output_path):
    """
    Combines several audio files into a single one using pydub.
    """
    if not audio_files:
        return None

    combined = AudioSegment.empty()
    for file in audio_files:
        audio = AudioSegment.from_file(file)
        combined += audio

    combined.export(output_path, format="wav")
    return output_path

def convert_to_format(input_path, output_format="mp3"):
    """
    Converts audio to another format (e.g., wav to mp3).
    """
    audio = AudioSegment.from_file(input_path)
    output_path = os.path.splitext(input_path)[0] + f".{output_format}"
    audio.export(output_path, format=output_format)
    return output_path

def validate_audio(file_path):
    """
    Validates if the audio file exists and is readable.
    """
    if not os.path.exists(file_path):
        return False, f"El archivo {file_path} no existe."

    try:
        data, samplerate = sf.read(file_path)
        return True, "Audio válido."
    except Exception as e:
        return False, f"Error al leer el audio: {e}"

def normalize_audio(file_path, target_sr=24000):
    """
    Normalizes audio to a target sample rate and mono.
    """
    try:
        y, sr = librosa.load(file_path, sr=target_sr, mono=True)
        norm_path = os.path.splitext(file_path)[0] + "_norm.wav"
        sf.write(norm_path, y, sr)
        return norm_path
    except Exception as e:
        print(f"Error al normalizar: {e}")
        return file_path

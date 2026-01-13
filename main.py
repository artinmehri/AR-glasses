from camera_module import capture_image
from ai_client import analyzeImageAndAudio
from display_module import scroll_text
from mic_module import record_audio

if __name__ == "__main__":
    audio_bytes = record_audio()
    image_bytes = capture_image()
    text = analyzeImageAndAudio(image_bytes, audio_bytes)
    scroll_text(text)
from camera_module import capture_image
from ai_client import analyzeImage
from display_module import scroll_text

if __name__ == "__main__":
    image_bytes = capture_image()
    text = analyzeImage(image_bytes)
    scroll_text(text)
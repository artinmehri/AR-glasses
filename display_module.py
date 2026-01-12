import board
import busio
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from ai_client import getResponse

# 1. Setup Display
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

def scroll_text(long_text):
    # Font settings (default load)
    font = ImageFont.load_default()
    line_height = 12
    
    # 2. Wrap text into lines so it fits the 128px width
    words = long_text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line + word) < 22: # Approx 22 chars for default font
            current_line += word + " "
        else:
            lines.append(current_line)
            current_line = word + " "
    lines.append(current_line)

    # 3. Create a tall image to hold the entire message
    total_height = len(lines) * line_height
    # We add 64px padding so it scrolls completely off the top
    canvas_height = total_height + 64
    tall_image = Image.new("1", (128, canvas_height))
    draw = ImageDraw.Draw(tall_image)

    # 4. Draw all lines onto our tall "virtual" canvas
    for i, line in enumerate(lines):
        draw.text((0, i * line_height), line, font=font, fill=255)

    # 5. The Scroll Loop
    # Slides a 128x64 window down the tall image
    for y in range(total_height):
        # Crop out the current frame
        frame = tall_image.crop((0, y, 128, y + 64))
        oled.image(frame)
        oled.show()
     # Adjust speed here (lower = faster)

# --- Execution ---
oled.fill(0)
oled.show()
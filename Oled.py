

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class display:
    def __init__(self):
        # Define the Reset Pin
        oled_reset = digitalio.DigitalInOut(board.D4)

        # Change these
        # to the right size for your display!
        self.WIDTH = 128
        self.HEIGHT = 64  # Change to 64 if needed

        # Use for I2C.
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(self.WIDTH, self.HEIGHT, i2c, addr=0x3C, reset=oled_reset)

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        self.image = Image.new('1', (self.oled.width, self.oled.height))

        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)

    def displayText(self,text,x,y):
        # Draw Some Text
        (font_width, font_height) = font.getsize(text)
        self.draw.text(x,y,text, font=font, fill=255)

    def clear(self):
        # Clear display.
        self.oled.fill(0)
        self.oled.show()
    def show(self):
        # Display image
        self.oled.image(self.image)
        self.oled.show()

def main():
    screen=display()
    screen.clear()
    screen.displayText("Hello World",0,16)
    screen.show()

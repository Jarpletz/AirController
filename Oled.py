

import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class display:

    def __init__(self):#setup everything
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

       

    def displayText(self,text,x,y):#Add text to image at coords (x,y)
        # Draw Some Text
        #(font_width, font_height) = font.getsize(text)
        font = ImageFont.load_default()
        self.draw.text((x,y),text, font=font, fill=255)

    def clear(self):#Erase everything on the oled
        # Clear display.
        self.image = Image.new('1', (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)
        self.oled.fill(0)
        self.oled.show()
        print("Clearing")
    def show(self):#display the current image
        # Display image
        self.oled.image(self.image)
        self.oled.show()
        




#EXAMPLE:

#screen = display()
#screen.clear()
#screen. displayText("Hello there!",0,0)
#screen.show()
#print("Displayed 'Hello there!' on the OLED!")

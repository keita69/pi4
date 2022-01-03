import board
import time
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


def disp(now, temperature):
    i2c = board.I2C()
    oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

    # Clear display.
    oled.fill(0)
    time.sleep(1)
    oled.show()

    # Create blank image for drawing.
    image = Image.new("1", (oled.width, oled.height))
    draw = ImageDraw.Draw(image)

    # font

    # font = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-DemiLight.ttc", 13)
    # font2 = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-DemiLight.ttc", 10)
    font = ImageFont.truetype(
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 20)
    font2 = ImageFont.truetype(
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 12)

    # ex) '2021-12-08 11:42:33'
    mmdd = str(now)[5:10]
    hhmmss = str(now)[11:19]
    hhmm = str(now)[11:16]

    # Draw the text
    draw.text((0, 2), str(temperature)[0:4] + "℃", font=font, fill=255)
    # draw.text((68, 2), mmdd, font=font2, fill=255)
    # draw.text((68, 15), hhmmss, font=font2, fill=255)

    draw.text((68, 2), hhmm, font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

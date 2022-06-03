from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="images/encoded_image.jpg"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0,0,0)

    decoded_image.save("images/decoded.jpg")

def write_text(text_to_write, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode, template="images/100kb.jpg"):
    template = Image.open(template)
    red_template = template.split()[0]
    green_template = template.split()[1]
    blue_template = template.split()[2]

    x = template.size[0]
    y = template.size[1]

    image_text = write_text(text_to_encode, template.size)
    bw_encode = image_text.convert('1')

    encoded_image = Image.new("RGB", (x, y))
    pixels = encoded_image.load()
    for i in range(x):
        for j in range(y):
            red_px = bin(red_template.getpixel((i,j)))
            px = bin(bw_encode.getpixel((i,j)))

            if px[-1] == '1':
                red_px = red_px[:-1] + '1'
            else:
                red_px = red_px[:-1] + '0'
            pixels[i, j] = (int(red_px, 2), green_template.getpixel((i,j)), blue_template.getpixel((i,j)))

    encoded_image.save("images/encoded_image.jpg")

if __name__ == '__main__':
    print("Decoding the image...")
    decode_image()

    print("Encoding the image...")
    encode_image('Hello')
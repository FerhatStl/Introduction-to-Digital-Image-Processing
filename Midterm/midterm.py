from PIL import Image
import numpy

def get_the_message(image, sentinel):
    image = Image.open(image)
    width, height = image.size
    bitplane = numpy.zeros((height, width))
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            lsb = pixel & 1
            bitplane[y, x] = lsb

    message = ""
    bitbuffer = ""
    for i in range(height):
        for j in range(width):
            bitbuffer = bitbuffer + str(int(bitplane[i,j]))
            if len(bitbuffer) == 8:
                character = chr(int(bitbuffer, 2))
                if character == sentinel:
                    break
                else:
                    message = message + str(character)
                    bitbuffer = ""

    return message

print(get_the_message('67.tif', '%'))
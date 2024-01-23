from PIL import Image, ImageFilter

image1 = Image.open('example.jpg')
image1.show()
image1.save('example.png')

size = (300, 300)
image2 = image1.copy()
image2.thumbnail(size)
image2.save('resized.png')
image2.show()

image3 = image1.copy()
image3.filter(ImageFilter.BLUR).save('filtered.png')
image3.show()
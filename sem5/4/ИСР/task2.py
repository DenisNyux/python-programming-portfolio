import pyqrcode

img = pyqrcode.create(input('Введите текст:\t'))
img.svg('your_text.svg')
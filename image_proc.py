from PIL import Image
from ocr.tesseract_parser import TesseractParser

parser = TesseractParser(70)
boxes = parser.get_tesseract_boxes('/Users/eudvazquez/personal/FauxTrans/data/image/Faux/out-0.jpg')

img = Image.open('/Users/eudvazquez/personal/FauxTrans/data/image/Faux/out-0.jpg')
pixels = img.load()

for box in boxes:
    for i in range(box.left, box.left + box.width): 
        for j in range(box.top, box.top + box.height):
            pixels[i, j] = (0, 255, 0)

img.save("ouput.jpg")
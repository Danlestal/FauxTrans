import pytesseract
from ocr.tesseract_parser import TesseractParser
from ocr.tesseract_cluster import TesseractCluster
from pdf.converter import Converter
from PIL import Image, ImageEnhance
from image.image_processor import ImageProcessor

converter = Converter()

converter.to_jpg('./data/Guild/Stat Cards/M3E_Gld_Arc_Augmented_CharlesHoffman.pdf','./data/image/Faux')




im = Image.open('./data/image/Faux/out-1.jpg')
enh = ImageEnhance.Sharpness(im)
im = enh.enhance(2)

# enh = ImageEnhance.Contrast(im)
# im = enh.enhance(2)

im.save('./data/image/Faux/out-1-post.jpg')




parser = TesseractParser(70)
raw_data = parser.get_tesseract_boxes('./data/image/Faux/out-1-post.jpg')
cluster = TesseractCluster(50, 34)
translation_boxes = cluster.cluster_boxes(raw_data)
for translation_box in translation_boxes:
    print(translation_box)
    print('--')

proc = ImageProcessor()
proc.clear_text_from_image('./data/image/Faux/out-1.jpg', translation_boxes, './data/image/Faux/out-1-clear.jpg')



# print(pytesseract.image_to_data(Image.open('./data/image/Faux/out-1.jpg')))
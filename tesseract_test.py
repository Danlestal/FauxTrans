import pytesseract
from ocr.tesseract_parser import TesseractParser
from ocr.tesseract_cluster import TesseractCluster
from pdf.converter import Converter
from PIL import Image


converter = Converter()

# converter.to_jpg('./data/Guild/Stat Cards/M3E_Gld_Arc_Augmented_CharlesHoffman.pdf','./data/image/Faux')
# parser = TesseractParser(50)
# raw_data = parser.get_tesseract_boxes('./data/image/Faux/out-1.jpg')
# cluster = TesseractCluster(40, 40)
# translation_boxes = cluster.cluster_boxes(raw_data)
# for translation_box in translation_boxes:
#     print(translation_box)
#     print('--')



print(pytesseract.image_to_data(Image.open('./data/image/Faux/out-1.jpg')))
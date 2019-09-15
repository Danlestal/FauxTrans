from googletrans import Translator
from ocr.tesseract import Tesseract
from pdf.converter import Converter


tess = Tesseract()
converter = Converter()

# converter.to_jpg('./data/Guild/Stat Cards/M3E_Gld_Arc_Augmented_CharlesHoffman.pdf','./data/image/Faux')


# text_boxes = tess.get_tesseract_boxes('./data/image/out-0.jpg')
# translation_boxes = tess.extract_translation_boxes(text_boxes)
# translation_boxes = tess.join_paragraphs(translation_boxes, 36)
# print(translation_boxes)




# converter.to_jpg('./data/Vampire/Brujah.pdf','./data/image/Vampire')
text_boxes = tess.get_tesseract_boxes('./data/image/Vampire/out-0.jpg')
print(text_boxes)
# translation_boxes = tess.extract_translation_boxes(text_boxes)
# translation_boxes = tess.join_paragraphs(translation_boxes, 36)
# print(translation_boxes)








import pytesseract
import re
from PIL import Image
from ocr.tesseract_box import TesseractBox

class TesseractParser:

    def __init__(self, minimum_confidence):
        self.minimum_confidence = minimum_confidence
        
    def raw_tesseract(path):
        return pytesseract.image_to_data(Image.open(path))

    def get_tesseract_boxes(self, path):
            tesseract_boxes = TesseractParser.raw_tesseract(path)
            tesseract_lines = tesseract_boxes.splitlines()
            # level   page_num        block_num       par_num line_num        word_num        left    top     width   height  conf    text
            result = []
            for line in tesseract_lines[1:]:
                re.split("( )", line)
                split_line = re.split("\t", line)

                if (len(split_line) > 11 ):
                    raw_text= split_line[11]
                else:
                    raw_text = None

                if raw_text:
                    raw_text=raw_text.strip()

                raw_confidence = int(float(split_line[10]))
                if raw_text and (raw_confidence > self.minimum_confidence):
                    tesseract_box = TesseractBox(   raw_confidence, 
                                                    split_line[6], 
                                                    split_line[7], 
                                                    split_line[8], 
                                                    split_line[9],
                                                    raw_text)

                    result.append(tesseract_box)


            return result


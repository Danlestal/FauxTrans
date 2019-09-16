
from PIL import Image
import pytesseract
import re

class Tesseract:

    def __init__(self, *args, **kwargs):
        pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
        self.horizontal_margin = 20
        self.vertical_margin = 36
        super().__init__(*args, **kwargs)

    def join_paragraphs(self, translation_boxes, line_separation):
        result = list()
        paragraph={}
        previous_translation_box = None
        for translation_box in translation_boxes:
            if (previous_translation_box is None):
                previous_translation_box = translation_box
                self.init_paragraph(translation_box, paragraph)
                continue

            previous_end = previous_translation_box['init_top'] + previous_translation_box['height']
            if (previous_end + line_separation >= translation_box['init_top']):
                paragraph['height'] = paragraph['height'] + translation_box['height']
                paragraph['text'] = paragraph['text'] +'\n'+ translation_box['text']
                if (translation_box['width'] > paragraph['width']):
                    paragraph['width'] = translation_box['width']
                previous_translation_box = translation_box
            else:
                result.append(paragraph.copy())
                previous_translation_box = translation_box
                self.init_paragraph(translation_box, paragraph)
        
        result.append(paragraph.copy())
        return result

    def init_paragraph(self, translation_box, paragraph):
        paragraph['init_top'] = translation_box['init_top']
        paragraph['text'] = translation_box['text']
        paragraph['height'] = translation_box['height']
        paragraph['width'] = translation_box['width']

    def raw_tesseract(path):
        return pytesseract.image_to_data(Image.open(path))

    def get_tesseract_boxes(self, path):
        tesseract_boxes = Tesseract.raw_tesseract(path)
        tesseract_lines = tesseract_boxes.splitlines()
        # level   page_num        block_num       par_num line_num        word_num        left    top     width   height  conf    text
        result = []
        for line in tesseract_lines[1:]:
            re.split("( )", line)
            split_line = re.split("\t", line)
            tesseract_box = {}
            tesseract_box['conf'] = int(float(split_line[10]))
            tesseract_box['left'] = split_line[6]
            tesseract_box['top'] = split_line[7]
            tesseract_box['width'] = split_line[8]
            tesseract_box['height'] = split_line[9]
            if (len(split_line) > 11 ):
                tesseract_box['text'] = split_line[11]
            else:
                tesseract_box['text'] = ''
            result.append(tesseract_box)


        return result

    def extract_translation_boxes(self, tesseract_boxes):
        translation_box = {}
        result = []
        for box in tesseract_boxes:
            if box['conf'] < 60:
                if box['text'].strip() == "":
                    if ('init_top' in translation_box and translation_box['init_top'] != -1):
                        result.append(translation_box)
                    translation_box ={}
                    translation_box['text'] = ""
                    translation_box['init_top'] = -1
            else:
                if (translation_box['init_top'] == -1):
                    translation_box['init_top']=int(float(box['top']))
                    translation_box['height']=int(float(box['height']))

                translation_box['text'] = translation_box['text'] + " " + box['text']
                if 'width' not in translation_box:
                    translation_box['width'] = int(float(box['width']))
                else:
                    translation_box['width'] += int(float(box['width']))

        return result


    #a method to detect if two boxes are near enough horizontally. 
    def are_near_enough_horizontally(self, first_box, second_box):
        
        vertical_difference = abs(int(first_box['top']) - int(second_box['top']))
        if vertical_difference > self.vertical_margin:
            return False

        left_horizontal_end = int(first_box['left']) + int(first_box['width'])
        
        if ((int(left_horizontal_end) + self.horizontal_margin) > int(second_box['left'])):
            return True
        else:
            return False

    #a method to detect if two boxes are near enough vertically. 
    def are_near_enough_vertically(self, first_box, second_box):

        horizontal_difference = abs(int(first_box['left']) - int(second_box['left']))
        if horizontal_difference > self.vertical_margin:
            return False

        first_vertical_end = int(first_box['top']) + int(first_box['height'])
        
        if ((int(first_vertical_end) + self.vertical_margin) > int(second_box['top'])):
            return True
        else:
            return False

    def update_translation_box_horizontally(self, first_box, second_box):
        first_box['width'] = int(first_box['width']) + int(second_box['width'])
        first_box['text'] = first_box['text'] + ' ' + second_box['text']

    def update_translation_box_vertically(self, first_box, second_box):
        first_box['height'] = int(first_box['height']) + int(second_box['height'])
        first_box['text'] = first_box['text'] + '\n' + second_box['text']

    def get_translation_boxes(self, tesseract_boxes):
        translation_boxes = [tesseract_boxes[0].copy()]
        for tesseract_box in tesseract_boxes[1:]:
            joined = False
            for translation_box in translation_boxes:

                
                if self.are_near_enough_horizontally(translation_box ,tesseract_box):
                    self.update_translation_box_horizontally(translation_box, tesseract_box)
                    joined = True
                    break

                if self.are_near_enough_vertically(translation_box , tesseract_box):
                    self.update_translation_box_vertically(translation_box, tesseract_box)
                    joined = True
                    break

            
            if joined is False:
                translation_boxes.append(tesseract_box.copy())
        
        return translation_boxes



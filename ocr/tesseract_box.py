class TesseractBox:

    def __init__(self, *args, **kwargs):
        self.confidence = int(float(split_line[10]))
        self.left = int(split_line[6])

            tesseract_box['left'] = split_line[6]
            tesseract_box['top'] = split_line[7]
            tesseract_box['width'] = split_line[8]
            tesseract_box['height'] = split_line[9]

        super().__init__(*args, **kwargs)
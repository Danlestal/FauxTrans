class TesseractBox:

    def __init__(self, confidence, left, top, width, height, text):
        self.confidence = int(confidence)
        self.left = int(left)
        self.top = int(top)
        self.width = int(width)
        self.height = int(height)
        self.text = text



import math

class TesseractBox:

    def __init__(self, confidence, left, top, width, height, text):
        self.confidence = int(confidence)
        self.left = int(left)
        self.top = int(top)
        self.width = int(width)
        self.height = int(height)
        self.text = text

    def horizontal_distance(self, other_box):
        if other_box.left >= self.left:
            return  abs((self.left + self.width) - other_box.left)
        else:
            return  abs((other_box.left + other_box.width) - self.left)

    def vertical_distance(self, other_box):
        if other_box.top >= self.top:
            return  abs((self.top + self.height) - other_box.top)
        else:
            return  abs((other_box.top + other_box.height) - self.top)

    def vertical_center(self):
        return self.top + (self.height /2)

    def horizontal_center(self):
        return self.left + (self.width /2)
        
    def distance(self, other_box):
        x_distance = math.pow( (self.horizontal_center() - other_box.horizontal_center()), 2)
        y_distance = math.pow((self.vertical_center() - other_box.vertical_center()), 2)
        return math.sqrt(x_distance + y_distance)
 
    def join_horizontally(self, other_box):
        new_end = other_box.left + other_box.width
        new_width = new_end - self.left
        self.text = self.text + ' '+ other_box.text
        self.width = new_width

    def join_vertically(self, other_box):
        new_end = other_box.top + other_box.height
        new_height = new_end - self.top
        self.text = self.text + '\n'+ other_box.text
        self.height = new_height

    def __str__(self):
        return self.text




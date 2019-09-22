
import unittest
from ocr.tesseract_box import TesseractBox
from unittest.mock import MagicMock

class Test_TesseractBox(unittest.TestCase):

        def test_horizontal_distance(self):
            first_box = TesseractBox(90,20,20,100,32,'Primera caja')
            second_box = TesseractBox(90,500,20,100,32,'Segunda Caja')
            distance = first_box.horizontal_distance(second_box)
            self.assertEquals(380, distance)

        def test_horizontal_distance_conmutative(self):
            first_box = TesseractBox(90,20,20,100,32,'Primera caja')
            second_box = TesseractBox(90,500,20,100,32,'Segunda Caja')
            distance = second_box.horizontal_distance(first_box)
            self.assertEquals(380, distance)

import unittest
from ocr.tesseract_parser import TesseractParser
from unittest.mock import MagicMock

class Test_TesseractParser(unittest.TestCase):

	def test_get_tesseract_boxes(self):
		file = open('./data/test/raw_data.txt',mode='r')
		raw_tesseract = file.read()
		file.close()

		tess = TesseractParser(45)
		TesseractParser.raw_tesseract = MagicMock(return_value=raw_tesseract)
		mock_file = 'lel'
		result = tess.get_tesseract_boxes(mock_file)

		self.assertEqual(len(result), 121)
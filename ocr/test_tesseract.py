
import unittest
from ocr.tesseract import Tesseract

class Test_Tesseract(unittest.TestCase):

    def test_join_paragraphs_happy_path(self):
        test_paragraph_data = [
            {'text': ' ARMOR +2: Reduce all damage suffered by this model by +2.', 'init_top': 1389, 'height': 32, 'width': 1117},

            {'text': ' PoweER At the start of this model’s Activation,', 'init_top': 1465, 'height': 34, 'width': 880}, 
            {'text': ' every friendly Construct within gains a Power Token.', 'init_top': 1534, 'height': 35, 'width': 1029}, 
            {'text': ' Before performing a duel, this model may discard a Power', 'init_top': 1577, 'height': 39, 'width': 1096}, 
            {'text': ' Token from itself or a friendly Construct within @6 to', 'init_top': 1636, 'height': 37, 'width': 1023}, 
            {'text': ' receive either a @ or a suit of its choice to that duel.', 'init_top': 1698, 'height': 34, 'width': 926},

            {'text': ' PROTECTED After this model is targeted', 'init_top': 1776, 'height': 33, 'width': 795}, 
            {'text': ' by an enemy Attack Action, it may discard a card to change', 'init_top': 1829, 'height': 50, 'width': 1104}, 
            {'text': ' the target to a friendly Construct model within 2” of this', 'init_top': 1887, 'height': 39, 'width': 1060}, 
            {'text': ' model (ignoring range, LoS, and targeting restrictions).', 'init_top': 1946, 'height': 38, 'width': 1070},

            {'text': ' CREATIVE SALVAGE: Enemy models killed by this model', 'init_top': 2028, 'height': 34, 'width': 1114},
            {'text': ' Drop a Scrap Marker in addition to any other Markers', 'init_top': 2085, 'height': 46, 'width': 1023}
        ]

        tess = Tesseract()
        paragraphs = tess.join_paragraphs(test_paragraph_data, 40)
        self.assertEqual(len(paragraphs), 4)
        self.assertEqual(paragraphs[1]['width'], 1096)
        self.assertEqual(paragraphs[2]['init_top'], 1776)

    def test_join_paragraphs_only_one_line(self):
        test_paragraph_data = [
            {'text': ' ARMOR +2: Reduce all damage suffered by this model by +2.', 'init_top': 1389, 'height': 32, 'width': 1117},
        ]

        tess = Tesseract()
        paragraphs = tess.join_paragraphs(test_paragraph_data, 40)
        self.assertEqual(len(paragraphs), 1)
        self.assertEqual(paragraphs[0]['width'], 1117)
        self.assertEqual(paragraphs[0]['init_top'], 1389)
        self.assertEqual(paragraphs[0]['height'], 32)

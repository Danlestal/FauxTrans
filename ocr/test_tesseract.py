
import unittest   # The test framework
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

    def test_extract_translation_boxes_multicolumn(self):
        self.assertEqual(1, 1)
        vampire_boxes = [
            {'conf': 92, 'left': '279', 'top': '1817', 'width': '283', 'height': '46', 'text': 'Camarilla'},
            {'conf': 96, 'left': '581', 'top': '1817', 'width': '181', 'height': '46', 'text': 'Prince'},
            {'conf': 95, 'left': '781', 'top': '1817', 'width': '59', 'height': '46', 'text': 'of'},
            {'conf': 96, 'left': '855', 'top': '1817', 'width': '185', 'height': '46', 'text': 'Rome:'},

            {'conf': 88, 'left': '1060', 'top': '1817', 'width': '268', 'height': '46', 'text': 'Constanza'},
            {'conf': 0, 'left': '1390', 'top': '1876', 'width': '3', 'height': '5', 'text': '#'},

                            {'conf': 91, 'left': '1520', 'top': '1817', 'width': '283', 'height': '46', 'text': 'Camarilla'},
                            {'conf': 96, 'left': '1822', 'top': '1817', 'width': '181', 'height': '46', 'text': 'Prince'},
                            {'conf': 95, 'left': '2021', 'top': '1817', 'width': '60', 'height': '46', 'text': 'of'},
                            {'conf': 95, 'left': '2095', 'top': '1817', 'width': '185', 'height': '46', 'text': 'Rome:'},
                            {'conf': 96, 'left': '2301', 'top': '1817', 'width': '267', 'height': '46', 'text': 'Constanza'},

                            {'conf': 7, 'left': '2630', 'top': '1877', 'width': '3', 'height': '3', 'text': '{ij'},
                            {'conf': 91, 'left': '2761', 'top': '1817', 'width': '283', 'height': '46', 'text': 'Camarilla'},
                            {'conf': 96, 'left': '3063', 'top': '1817', 'width': '181', 'height': '46', 'text': 'Prince'},
                            {'conf': 96, 'left': '3262', 'top': '1817', 'width': '60', 'height': '46', 'text': 'of'},
                            {'conf': 96, 'left': '3336', 'top': '1817', 'width': '185', 'height': '46', 'text': 'Rome:'},
                            {'conf': 96, 'left': '3542', 'top': '1817', 'width': '267', 'height': '46', 'text': 'Constanza'},

                            {'conf': -1, 'left': '276', 'top': '1882', 'width': '3503', 'height': '61', 'text': ''},

                            {'conf': 96, 'left': '276', 'top': '1892', 'width': '102', 'height': '51', 'text': 'gets'},
                            {'conf': 96, 'left': '400', 'top': '1882', 'width': '65', 'height': '46', 'text': '+2'},
                            {'conf': 95, 'left': '488', 'top': '1882', 'width': '133', 'height': '46', 'text': 'bleed'},
                            {'conf': 95, 'left': '641', 'top': '1885', 'width': '173', 'height': '58', 'text': 'against'},
                            {'conf': 96, 'left': '832', 'top': '1897', 'width': '26', 'height': '31', 'text': 'a'},
                            {'conf': 95, 'left': '879', 'top': '1882', 'width': '286', 'height': '46', 'text': 'Methuselah'},
                            {'conf': 95, 'left': '1185', 'top': '1882', 'width': '112', 'height': '46', 'text': 'who'},
                            {'conf': 96, 'left': '1517', 'top': '1892', 'width': '102', 'height': '51', 'text': 'gets'},
                            {'conf': 96, 'left': '1641', 'top': '1882', 'width': '65', 'height': '46', 'text': '+2'},
                            {'conf': 95, 'left': '1728', 'top': '1882', 'width': '133', 'height': '46', 'text': 'bleed'},
                            {'conf': 96, 'left': '1882', 'top': '1886', 'width': '173', 'height': '57', 'text': 'against'},
                            {'conf': 96, 'left': '2072', 'top': '1897', 'width': '26', 'height': '31', 'text': 'a'},
                            {'conf': 96, 'left': '2120', 'top': '1882', 'width': '285', 'height': '46', 'text': 'Methuselah'},
                            {'conf': 96, 'left': '2426', 'top': '1882', 'width': '112', 'height': '46', 'text': 'who'},
                            {'conf': 96, 'left': '2758', 'top': '1892', 'width': '102', 'height': '51', 'text': 'gets'},
                            {'conf': 96, 'left': '2882', 'top': '1882', 'width': '65', 'height': '46', 'text': '+2'},
                            {'conf': 96, 'left': '2969', 'top': '1882', 'width': '133', 'height': '46', 'text': 'bleed'},
                            {'conf': 96, 'left': '3124', 'top': '1886', 'width': '172', 'height': '57', 'text': 'against'},
                            {'conf': 96, 'left': '3313', 'top': '1897', 'width': '26', 'height': '31', 'text': 'a'},
                            {'conf': 96, 'left': '3361', 'top': '1882', 'width': '285', 'height': '46', 'text': 'Methuselah'},
                            {'conf': 96, 'left': '3667', 'top': '1882', 'width': '112', 'height': '46', 'text': 'who'},
                            {'conf': -1, 'left': '279', 'top': '1947', 'width': '3129', 'height': '61', 'text': ''},
                            {'conf': 96, 'left': '279', 'top': '1947', 'width': '209', 'height': '46', 'text': 'controls'},
                            {'conf': 95, 'left': '509', 'top': '1962', 'width': '25', 'height': '31', 'text': 'a'},
                            {'conf': 93, 'left': '555', 'top': '1947', 'width': '139', 'height': '61', 'text': 'ready'},
                            {'conf': 92, 'left': '710', 'top': '1947', 'width': '217', 'height': '46', 'text': 'Ventrue.'},
                            {'conf': 96, 'left': '1520', 'top': '1947', 'width': '209', 'height': '46', 'text': 'controls'},
                            {'conf': 94, 'left': '1749', 'top': '1962', 'width': '26', 'height': '31', 'text': 'a'},
                            {'conf': 93, 'left': '1796', 'top': '1947', 'width': '139', 'height': '61', 'text': 'ready'},
                            {'conf': 92, 'left': '1951', 'top': '1947', 'width': '216', 'height': '46', 'text': 'Ventrue.'},
                            {'conf': 96, 'left': '2761', 'top': '1947', 'width': '209', 'height': '46', 'text': 'controls'},
                            {'conf': 95, 'left': '2990', 'top': '1962', 'width': '26', 'height': '31', 'text': 'a'},
                            {'conf': 93, 'left': '3037', 'top': '1947', 'width': '139', 'height': '61', 'text': 'ready'},
                            {'conf': 92, 'left': '3192', 'top': '1947', 'width': '216', 'height': '46', 'text': 'Ventrue.'}]
        tess = Tesseract()
        translation_boxes = tess.get_translation_boxes(vampire_boxes)
        self.assertEqual(len(translation_boxes), 6)
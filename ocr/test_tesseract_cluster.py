
import unittest
from ocr.tesseract_parser import TesseractParser
from ocr.tesseract_cluster import TesseractCluster
from ocr.tesseract_box import TesseractBox
from unittest.mock import MagicMock

class Test_TesseractCluster(unittest.TestCase):

        def test_cluster_boxes_horizontally(self):
                boxes = [
                        TesseractBox(90,20,20,100,32,'Primera caja'),
                        TesseractBox(90,140,20,100,32,'es muy bonita'),
                        TesseractBox(90,500,20,100,32,'Segunda Caja'),
                ]

                cluster = TesseractCluster(32, 12)
                joined_boxes = cluster.cluster_boxes(boxes)
                self.assertEquals(len(joined_boxes), 2)
                self.assertEquals(joined_boxes[0].text, 'Primera caja es muy bonita' )

        def test_cluster_boxes_vertically(self):
                boxes = [
                        TesseractBox(90, 20, 20,100,32,'Primera caja'),
                        TesseractBox(90, 22, 54,100,32,'es muy bonita'),
                        TesseractBox(90,500,20,100,32,'Segunda Caja'),
                ]

                cluster = TesseractCluster(32, 12)
                joined_boxes = cluster.cluster_boxes(boxes)
                self.assertEquals(len(joined_boxes), 2)
                self.assertEquals(joined_boxes[0].text, 'Primera caja\nes muy bonita' )

        def test_cluster_boxes_mix(self):
                boxes = [
                        TesseractBox(90, 20, 20,100,32,'Primera caja'),
                        TesseractBox(90,140,20,100,32, 'de color'),
                        TesseractBox(90, 22, 54,100,32,'es muy bonita'),
                        TesseractBox(90,500,20,100,32,'Segunda Caja'),
                ]

                cluster = TesseractCluster(32, 12)
                joined_boxes = cluster.cluster_boxes(boxes)
                self.assertEquals(len(joined_boxes), 2)
                self.assertEquals(joined_boxes[0].text, 'Primera caja de color\nes muy bonita' )

        def test_get_tesseract_boxes_integration(self):
                file = open('./data/test/raw_data_Hoff_2.txt',mode='r')
                raw_tesseract = file.read()
                file.close()

                tess = TesseractParser(65)
                TesseractParser.raw_tesseract = MagicMock(return_value=raw_tesseract)
                mock_file = 'lel'
                result = tess.get_tesseract_boxes(mock_file)
                
                cluster = TesseractCluster(60,40)
                result = cluster.cluster_boxes(result)

                TesseractParser.print_tesseract_collectio(result)
                self.assertEqual(result[0].text, 'CHARLES HOFFMAN')


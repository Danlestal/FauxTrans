
import unittest
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
class TesseractCluster:

    def __init__(self, maximun_x_distance, maximun_y_distance):
        self._cluster_boxes = []
        self._maximun_x_distance = maximun_x_distance
        self._maximun_y_distance = maximun_y_distance

    def _find_box_close_enough_horizontally(self, box_to_join):
        for big_box in self._cluster_boxes:
            if big_box.horizontal_distance(box_to_join) < self._maximun_x_distance:
                return big_box

    def _find_box_close_enough_vertically(self, box_to_join):
        for big_box in self._cluster_boxes:
            if big_box.vertical_distance(box_to_join) < self._maximun_y_distance:
                return big_box

    

    def cluster_boxes(self, tesseract_boxes):
        for box_to_join in tesseract_boxes:
            horizontal_box = self._find_box_close_enough_horizontally(box_to_join)
            if horizontal_box:
                horizontal_box.join_horizontally(box_to_join)
            else:
                vertical_box = self._find_box_close_enough_vertically(box_to_join)
                if vertical_box:
                    vertical_box.join_vertically(box_to_join)
                else:
                    self._cluster_boxes.append(box_to_join)
        
        return self._cluster_boxes
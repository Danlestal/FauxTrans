import copy

class TesseractCluster:

    def __init__(self, maximun_x_distance, maximun_y_distance):
        self._cluster_boxes = []
        self._maximun_x_distance = maximun_x_distance
        self._maximun_y_distance = maximun_y_distance

    def _find_box_close_enough_horizontally(self, box_to_join, current_list):
        for big_box in current_list:
            if big_box.horizontal_distance(box_to_join) < self._maximun_x_distance:
                if abs(big_box.top - box_to_join.top) < self._maximun_y_distance:
                    return big_box

    def _find_box_close_enough_vertically(self, box_to_join):
        for big_box in self._cluster_boxes:
            if big_box.vertical_distance(box_to_join) < self._maximun_y_distance:
                return big_box

    
    def cluster_boxes(self, tesseract_boxes):
        tesseract_boxes = self._cluster_boxes_horizontally(tesseract_boxes)
        return self._cluster_paragraphs(tesseract_boxes)

    def _cluster_boxes_horizontally(self, tesseract_boxes):
        current_list = []
        for box_to_join in tesseract_boxes:
            horizontal_box = self._find_box_close_enough_horizontally(box_to_join, current_list)
            if horizontal_box:
                horizontal_box.join_horizontally(box_to_join)
            else:
                current_list.append(box_to_join)

        return current_list

    def _cluster_paragraphs(self, tesseract_boxes):
        result = [copy.copy(tesseract_boxes[0])]
        for box_to_join in tesseract_boxes[1:]:
            last_paragraph_end = result[-1].top + result[-1].height
            if abs(box_to_join.top - last_paragraph_end) < self._maximun_y_distance:
                result[-1].join_vertically(box_to_join)
            else:
                result.append(copy.copy(box_to_join))
                continue

        return result
            
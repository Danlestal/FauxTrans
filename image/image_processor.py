from PIL import Image

class ImageProcessor:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clear_text_from_image(self, image_path, text_boxes, output_path):
        img = Image.open(image_path)
        pixels = img.load()

        for box in text_boxes:
            for i in range(box.left, box.left + box.width): 
                for j in range(box.top, box.top + box.height):
                    pixels[i, j] = (0, 255, 0)

        img.save(output_path)



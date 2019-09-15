from pdf2image import convert_from_path

class Converter:
    """A class to convert Pdfs formats"""

    def to_jpg(self, pdf_file_path, destination_folder):
        pages = convert_from_path(pdf_file_path, 500, first_page=1)
        index = 0
        for page in pages:
            page.save(destination_folder + '/out-' + str(index) + '.jpg', 'JPEG')
            index = index + 1
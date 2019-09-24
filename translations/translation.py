

class Translation:
    def __init__(self, language, text):
        self.language = language
        self.text = text

class OriginalString:

    def __init__(self, original_string):
        self.original_string = original_string
        self.translation = {}
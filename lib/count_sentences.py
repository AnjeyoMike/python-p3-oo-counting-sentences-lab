#!/usr/bin/env python3

# class MyString:
#   pass

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re
        # Split the string by sentence-ending punctuation marks
        sentences = re.split(r'[.!?]', self.value)
        # Filter out empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

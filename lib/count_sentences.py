#!/usr/bin/env python3
import re
class MyString:
  
  def __init__(self, value =''):

    self._value = ""
    self.value = value
    pass

  @property
  def value(self):
        return self._value

  @value.setter
  def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")



      

  def is_sentence(self):
    if self.value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False
  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else:
      return False
  def count_sentences(self):
    # Use regular expression to split on ., ! or ? followed by space or end of string
        if not isinstance(self.value, str) or self.value.strip() == "":
            return 0
        sentences = re.split(r'[.!?]+', self.value)
        # Remove empty strings that can occur after splitting
        return len([s for s in sentences if s.strip()])














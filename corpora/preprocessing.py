"""
code for preprocessing the manually processed
corpus data comprising of raw text from the
selected sample novels

Manual processing includes removal of
metadata, acnowledgements, indexes, etc.
from the downloaded raw files

It is then sent to this code file for
the preprocessing, including:
file handling, punctuation removal,
stop word removal in accordance to the
nltk package, which is then finally followed by
the generation of a frequency dictionary for each
significant word in the text
"""

"""
NLTK is one of the most prominently used
language toolkits applied in the study of
texts via stylometry
It is used to work with human language data,
alongside many corpora and lexical resources

here we import the stopwords corpora
from the many available resources to
work around our own corpus preprocessing
"""

from nltk.corpus import stopwords

from string import punctuation, digits

class Preprocessing:
  """
  Preprocessing documented text string for initialization, 
  preparing, and increasing the usability of a utf-8
  encoded raw input

  Parameters
  ----------
  filename: string
    The sent variable string from the class call line
    with the file name of the raw text file
  """

  def __init__(self, filename):
    # Over-writing the filename variable with the path of the specified file name
    if filename == 'rom1':
      self.filename = r'D:/git_repos/Stylometric-Visualizations/corpora/test1-romance/rom1_TheProblemWithForever.txt'
    elif filename == 'rom2':
      self.filename = r'D:/git_repos/Stylometric-Visualizations/corpora/test1-romance/rom2_ItEndsWithUs.txt'
    elif filename == 'crime1':
      self.filename = r'D:/git_repos/Stylometric-Visualizations/corpora/test2-crime/crime1_GoneGirl.txt'
    elif filename == 'crime2':
      self.filename = r'D:/git_repos/Stylometric-Visualizations/corpora/test2-crime/crime2_TheABCMurders.txt'

  def read_files_into_string(self, file):
    with open(file, encoding="utf8") as f:
      content = f.read()
    return content.lower()

  def stop_words(self, word_list):
    """
    
    """
    
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in word_list if not word in stop_words]
    return filtered

  def remove_punctuations(self, text):
      exc_list = punctuation + digits + "”“—\n-"
      without_punctuations = str.maketrans(exc_list, " " * len(exc_list))
      new_words = text.translate(without_punctuations).split()
      return new_words

  def frequency_dictionary(self, token_list):
      fdist = {}
      for token in token_list:
        fdist[token] = fdist.get(token, 0) + 1
      return fdist

  def preprocessing(self):
      text = self.read_files_into_string(self.filename)
      removed_punctuations = self.remove_punctuations(text)
      filter_stop_words = self.stop_words(removed_punctuations)
      frequency = self.frequency_dictionary(filter_stop_words)
      return frequency
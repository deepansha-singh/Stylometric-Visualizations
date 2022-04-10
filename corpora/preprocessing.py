from nltk.corpus import stopwords
from nltk.probability import FreqDist

from string import punctuation, digits

class Preprocessing:
  def __init__(self, filename):
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
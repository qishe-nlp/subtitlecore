import webvtt
import re
from os import path
from subtitlecore.sentencizer import Sentencizer

def filter_typos(sentence):
  filtered = sentence.replace("♪","").replace("\n", " ").replace("-", "")
  filtered = re.sub(r'[\[\{].*[\}\]]:?', "", filtered).replace("  ", " ")
  return filtered.strip()


class Subtitle:
  def __init__(self, f, lang="en"):
    if path.exists(f) and path.isfile(f):
      self.file = f
      self.fname, self.fext = path.splitext(path.basename(f))
      self.lang = lang
      self.sentencizer = Sentencizer(lang)
      self._init_content()

  def sentenize(self, choice):
    #TODO: choice to be formalized into constances
    return self.sentencizer.mark(self.content, choice)
  
  def _init_content(self, dest="./"):
    self.content = []
    obj = webvtt.from_srt(self.file)

    for index, caption in enumerate(obj.captions):
      self.content.append({
        "start": caption.start,
        "end": caption.end,
        "text": filter_typos(caption.text),
        "identifier": str(index+1)
      })


import webvtt
from os import path
from subtitlecore.sentencizer import Sentencizer

class Subtitle:
  def __init__(self, f, lang="en"):
    if path.exists(f) and path.isfile(f):
      self.file = f
      self.fname, self.fext = path.splitext(path.basename(f))
      self.lang = lang
      self.sentencizer = Sentencizer(lang)
      self._init_content()

  def sentenize(self):
    return self.sentencizer.mark(self.content)
  
  def _init_content(self, dest="./"):
    self.content = []
    obj = webvtt.from_srt(self.file)

    for index, caption in enumerate(obj.captions):
      self.content.append({
        "start": caption.start,
        "end": caption.end,
        "text": caption.text,
        "identifier": str(index+1)
      })


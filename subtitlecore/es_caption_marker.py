import spacy

class ESCaptionMarker:

  @classmethod
  def mark(self, line):
    """
    e.g,
    return [{text: '', confidence: 1.0}, {text: '', confidence: 0.5}]
    """
    nlp = spacy.load("es_core_news_md")
    _line = line.replace("\n", " ").replace("-", " ")
    print("Analyze: {}".format(_line))
    doc = nlp(_line)
    _temp = list(doc.sents)
    sens = []
    for s in _temp:
      e = {"text": s.text, "confidence": 1.0}
      sens.append(e)
    print(sens)
    return sens 


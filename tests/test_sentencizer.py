from subtitlecore import Sentencizer

def test_sentencizer():
  lang = "en"
  line = "This is the great day. I have dreamed this for a long time."
  s = Sentencizer(lang)
  sens = s.mark(line)
  print(sens)
  assert len(sens) == 2
  assert sens[0] == "This is the great day."
  assert sens[1] == "I have dreamed this for a long time."
  

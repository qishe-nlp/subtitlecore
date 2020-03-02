from subtitlecore.subtitle import Subtitle
import sys

def play(fname, lang):
    st = Subtitle(fname, lang)
    st.srt_to_vtt()
    captions = st.scize()
    for s in captions:
        print(s.sens)

def run():
    if len(sys.argv) < 2:
        print("srt file and language needed.")
        return
    fname = sys.argv[1] 
    lang = sys.argv[2] if len(sys.argv) >= 3 else "en"
    play(fname, lang)

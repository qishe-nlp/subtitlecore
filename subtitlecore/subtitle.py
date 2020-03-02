import webvtt
from os import path
from subtitlecore.sentencizer import Sentencizer
#from subtitlecore.configuration import scizercfg

class Subtitle:
    def __init__(self, f, lang="en"):
        if path.exists(f) and path.isfile(f):
            self.file = f
            self.fname, self.fext = path.splitext(path.basename(f))
            self.lang = lang
            self.sentencizer = Sentencizer

    def srt_to_vtt(self, dest="./"):
        srt_obj = webvtt.from_srt(self.file)

        for index, caption in enumerate(srt_obj.captions):
            caption.identifier = str(index+1)

        self.vttfile = path.join(dest, self.fname+".vtt")
        srt_obj.save(self.vttfile)


    def scize(self):
        vtt_obj = webvtt.read(self.vttfile) 
        return self.sentencizer.get_sens(vtt_obj, self.lang) 

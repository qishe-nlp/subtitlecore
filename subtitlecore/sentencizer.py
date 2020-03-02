from importlib import import_module

class Sentencizer:

    @classmethod
    def get_sens(cls, vtt_obj, lang):
        module = import_module("subtitlecore.{}_caption_marker".format(lang.lower()))
        marker = getattr(module, "{}CaptionMarker".format(lang.upper()))

        tmp = []
        for caption in vtt_obj:
            tmp.append(marker(caption))
        sens = []
        sub = Sen()
        for cm in tmp:
            # print("{}\t{}".format(caption.isSen, caption.sens))
            sub.add(cm)
            if cm.isSen == 1.0:
                sens.append(sub)
                sub.setSens()
                sub = Sen() 
        return sens

class Sen:
    
    def __init__(self):
       self.caption_marks = [] 

    def add(self, cm):
        self.caption_marks.append(cm)

    def setSens(self):
        cmlen = len(self.caption_marks)
        if  cmlen == 1:
            self.sens = self.caption_marks[0].sens
        else:
            self.sens = [" ".join([e.sens[0] for e in self.caption_marks])]
            for e in self.caption_marks: 
                if len(e.sens) > 1:
                    self.sens += e.sens[1:]


class ENCaptionMarker:

    def __init__(self, caption):
        self.caption = caption
        self.mark()

    def mark(self):
        """
        1. Are Multiple sentences ? --> {possibility: 1.0, sens:[]}
        2. Is one sentence ? --> {possibility: 1.0, sens:""} 
        3. Is not one sentence ? --> {possibility: 0.0, sens: ""}
        """
        sen_ending = [".", "!", "?", "...", "\"", ")"]
        sen_not_ending = [",", "("]

        self.sens = self.caption.text.split("\n")
        if len(self.sens) > 1:
            self.isSen = 1.0
        elif self.caption.text[-1] in sen_ending:
            self.isSen = 1.0
        elif self.caption.text[-1] in sen_not_ending:
            self.isSen = 0.0
        else:
            self.isSen = 0.5


    def __str__(self):
        return "(start: {}, end: {}, isSen: {}, sens: {})".format(self.caption.start, self.caption.end, self.isSen, self.sens)

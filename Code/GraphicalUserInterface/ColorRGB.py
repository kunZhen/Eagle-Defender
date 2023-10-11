class ColorRGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getHex(self):
        r = max(0, min(255, self.r))
        g = max(0, min(255, self.g))
        b = max(0, min(255, self.b))

        codHex = "#{:02x}{:02x}{:02x}".format(r, g, b)

        return codHex

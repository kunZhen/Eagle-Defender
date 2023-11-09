from ColorRGB import ColorRGB


class GeneratePalette:
    def __init__(self, colorHex):
        self.r = int(colorHex[1:3], 16)
        self.g = int(colorHex[3:5], 16)
        self.b = int(colorHex[5:7], 16)

        self.palette = [colorHex]

    def GenerateColors(self):
        if self.r < 50 or self.g < 50 or self.b < 50:
            factor = 2.5
            newR = int(self.r * factor)
            newG = int(self.g * factor)
            newB = int(self.b * factor)
        else:
            factor = 2 / 5
            newR = int(self.r * factor)
            newG = int(self.g * factor)
            newB = int(self.b * factor)

        newColor = ColorRGB(newR, newG, newB).getHex()
        self.palette.append(newColor)

        print(self.palette)
        return self.palette

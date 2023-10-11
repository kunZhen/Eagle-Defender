from ColorRGB import ColorRGB


class GeneratePalette:
    def __init__(self, colorHex):
        self.r = int(colorHex[1:3], 16)
        self.g = int(colorHex[3:5], 16)
        self.b = int(colorHex[5:7], 16)

        self.palette = [colorHex]

    def GenerateColors(self):
        for i in range(2):
            factor = (5 - i) / 6.0
            newR = int(self.r * factor)
            newG = int(self.g * factor)
            newB = int(self.b * factor)

            newColor = ColorRGB(newR, newG, newB).getHex()
            self.palette.append(newColor)

        self.palette.append("#000000")
        self.palette.append("#ffffff")

        print(self.palette)
        return self.palette
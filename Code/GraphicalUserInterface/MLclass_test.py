import unittest

from musicLogic import musicLogic

class MusicLogicClassTest(unittest.TestCase):

    instance = musicLogic()
    # Saves a youtube url to test, a list with two names(one from youtube and the other from spotify), time in seconds of the song
    song = {"url": "https://www.youtube.com/watch?v=2f3s53Uzxx4", "name": ["Rihanna - Diamonds (Slowed + Reverb).mp4", "Diamonds Rihanna"], "time": 277}
    values = {"poisson": 0.9, "pow": 0.6}

    def test_Cocinero(self):
        self.assertEqual(int(self.instance.generateTimer(self.song["name"][1], self.song["time"])), 29156)

    def test_getPoisson(self):
        self.assertGreater(round(musicLogic.getPoisson(self.values["poisson"]), 2), 0.35 )
        self.assertLess(round(musicLogic.getPoisson(self.values["poisson"]), 2), 0.38 )

    def test_getExponential(self):
        self.assertGreater(round(musicLogic.getExponential(self.values["pow"]), 2), 0.32 )
        self.assertLess(round(musicLogic.getExponential(self.values["pow"]), 2), 0.35 )

    def test_getDuration(self):
        self.assertEqual(self.instance.duration(self.song["url"]), self.song["time"])

    def test_getName(self):
        self.assertEqual(self.instance.getName(self.song["url"]), self.song["name"][0])

if __name__=="__main__":
    unittest.main()
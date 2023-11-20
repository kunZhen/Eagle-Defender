import unittest

from versusGame import versusGame

class VersusGameLogicTest(unittest.TestCase):
    attackerpoints = 100
    defenderblocks = [2, 7, 3]

    def test_MediaArmonicaDefender(self):
        # Compares program calculation with result of calculator of the current values
        self.assertGreaterEqual(versusGame.calculatePoints(self.defenderblocks[0], self.defenderblocks[1], self.defenderblocks[2]),820)

    def test_MediaArmonicaAttacker(self):
        # Compares program calculation with result of calculator of the current values
        self.assertGreaterEqual(versusGame.calculatePoints(self.attackerpoints, None, None),500)

if __name__=="__main__":
    unittest.main()
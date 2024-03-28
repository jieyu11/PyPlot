import unittest
from pyplot.dist import DistPlot

class UpdateFigsize(unittest.TestCase):

    def test_update_figsize(self):
        dp = DistPlot()
        new_figsize = (11.098, 12.575)
        dp.reset("figure.figsize", new_figsize)
        self.assertEqual(dp.plt.rcParams['figure.figsize'], new_figsize)

unittest.main()
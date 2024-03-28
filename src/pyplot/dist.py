from pyplot.base import Base
import matplotlib.pyplot as plt
import seaborn as sns
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

class DistPlot(Base):
    def __init__(self):
        super().__init__()
    
    def draw_hue(self, df, x, hue, outname=None, **kwargs):
        # figsize is not correctly read from plt.rcParams
        # using h and asp to make it work.
        h = self.plt_config["figure.figsize"][1]
        asp = self.plt_config["figure.figsize"][0] / h 
        for key, value in kwargs.items():
            logger.info(f"Using argument: {key}={value}")
        sns.displot(df, x=x, hue=hue, height=h, aspect=asp, **kwargs)
        if outname is not None:
            plt.savefig(outname)
    
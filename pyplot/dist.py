from pyplot.plt_setup import set_plt_default, default_configure
import matplotlib.pyplot as plt
import seaborn as sns
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

class DistPlot:
    def __init__(self):
        self._plt = set_plt_default() 
        self.config = default_configure()
    
    @property
    def plt(self):
        return self._plt
    
    def reset(self, parameter: str, value):
        if parameter not in self.config:
            logger.warning(f"Parameter: {parameter} is not found.")
            return
        self.config[parameter] = value
        logger.info(f"setting parameter ({parameter}) value to {value}")
    
    def draw_hue(self, df, x, hue, outname=None):
        h = self.config["figure.figsize"][1]
        asp = self.config["figure.figsize"][0] / h 
        sns.displot(df, x=x, kind="kde", hue=hue, height=h, aspect=asp)
        plt.savefig(outname)
        return plt
    
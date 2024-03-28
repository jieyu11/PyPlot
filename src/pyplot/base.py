import matplotlib.pyplot as plt
import seaborn as sns
import logging
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

class Base:
    def __init__(self):
        self._plt_config = self.set_plt_default() 
 
    def set_plt_default(self):
        # https://matplotlib.org/stable/api/matplotlib_configuration_api.html
        plt.style.use('classic')
        plt.rcParams['figure.figsize'] = (8.0, 5.0)
        plt.rcParams['figure.facecolor']='w'
        plt.rcParams['xtick.labelsize']=14
        plt.rcParams['ytick.labelsize']=14
        plt.rcParams['axes.labelsize']=15
        plt.rcParams['axes.titlesize']=16
        plt.rcParams['legend.fontsize']=12
        plt.rcParams['grid.color'] = 'k'
        plt.rcParams['grid.linestyle'] = ':'
        plt.rcParams['grid.linewidth'] = 0.5
        return plt.rcParams

    @property
    def plt_config(self):
        return self._plt_config

    def reset(self, parameter: str, value):
        if parameter not in self.plt_config:
            logger.warning(f"Parameter: {parameter} is not found.")
            return
        self.plt_config[parameter] = value
        logger.info(f"setting parameter ({parameter}) value to {value}")

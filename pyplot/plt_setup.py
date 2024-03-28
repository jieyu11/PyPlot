import matplotlib.pyplot as plt

def set_plt_default():
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
    return plt

def default_configure():
    # https://matplotlib.org/stable/api/matplotlib_configuration_api.html
    config = {
        "figure.figsize": (8.0, 5.0),
        "font_size": 14,
        "font_scale": 1.4,
        "cmap" : "YlGnBu",
    }
    return config
"""
Data loaders and utility functions.
"""
from pathlib import Path

from matplotlib.pyplot import rcParams
from numpy import log10
from pandas import DataFrame, Series, read_csv
from scipy.special import logit
from scipy.stats import linregress
from seaborn import regplot

DATADIR = Path(__file__).resolve().parent.parent / 'data'
FIGSIZE = (9,3)
PARTIES = {'democratic':'blue', 'republican':'red', 'other':'green'}

# Global settings for matplotlib
#COLORMAP = plt.get_cmap('bwr')
rcParams['figure.figsize'] = FIGSIZE


def bar_votes(votes,stacked=True):
    votes.sort_values('red').plot.bar(color=votes.columns,stacked=stacked)


def scatter_votes(x,votes):
    for color,series in votes.items():
        ax = regplot(x,series,color=color)
    ax.set(ylabel='popularity')


def regression(x,y):
    return { k:round(v,4) for k,v in linregress(x,y)._asdict().items() }


class Election:
    """
    Extract relevant values from raw data on local disk.
    """

    def __init__(self, year, datadir=DATADIR):
        self.datadir = Path(datadir).resolve()
        self.year = int(year)

    def __repr__(self):
        return f"{type(self).__name__}({self.year}, datadir={self.datadir})"

    @property
    def folder(self):
        """ Path: Path to raw data folder for selected year. """
        return self.datadir / str(self.year)

    def frame(self):
        """ DataFrame: Join relevant columns. """
        return self.votes.join(self.trucks).join(self.people)

    @property
    def people(self):
        """ Series: Population of each state. """
        path = self.folder / 'people.csv'
        column = str(self.year)

        return read_csv(path, index_col='state').pop(column).rename('people')

    @property
    def trucks(self):
        """ Series: Pickup trucks in each state. """
        path = self.folder / 'trucks.csv'

        return read_csv(path, index_col='state').pop('pickup').rename('trucks')

    @property
    def votes(self):
        """ Series: Votes for each major party in each state. """
        path = self.folder / 'votes.csv'

        return read_csv(path, index_col='state').rename(columns=PARTIES)













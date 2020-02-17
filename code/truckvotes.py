"""

"""
from pathlib import Path

from matplotlib.pyplot import rcParams
from numpy import log10
from pandas import DataFrame, Series, read_csv
from scipy.special import logit
from scipy.stats import linregress
from seaborn import regplot

DATADIR = Path(__file__).resolve() / 'data'
FIGSIZE = (9,3)

#COLORMAP = plt.get_cmap('bwr')
#VOTECOLOR = {'Democratic':'blue','Republican':'red','Other':'green'}

rcParams['figure.figsize'] = FIGSIZE

def read_table(year,name):
    """ DataFrame: Read selected table from selected year. """
    path = (DATADIR/str(year)/name).with_suffix('.csv')
    data = pd.read_csv(path,index_col='State').astype(float)

    return data

def read_votes(year):
    return read_table(year,'votes').rename(columns=VOTECOLOR)

def read_trucks(year):
    return read_table(year,'trucks').pop('Pickup').rename('trucks')

def read_people(year):
    return read_table(year,'people').pop(str(year)).rename('people')

def bar_votes(votes,stacked=True):
    votes.sort_values('red').plot.bar(color=votes.columns,stacked=stacked)

def scatter_votes(x,votes):
    for color,series in votes.items():
        ax = regplot(x,series,color=color)
    ax.set(ylabel='popularity')

def regression(x,y):
    return { k:round(v,4) for k,v in linregress(x,y)._asdict().items() }










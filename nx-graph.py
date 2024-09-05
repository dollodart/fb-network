import sys
import networkx as nx
import matplotlib.pyplot as plt
import pathlib
import pickle
import pandas as pd
from time import time
from secretenv import OUT_DIRECTORY

path = pathlib.Path(OUT_DIRECTORY)
data = []
for f in path.iterdir():
    with open(f, 'rb') as _:
        l = pickle.load(_)
    name = str(f).split('/')[-1].rstrip('.pickle')
    data.extend([(name, x) for x in l])

df = pd.DataFrame(data, columns=['friends', 'friends of friends'])
df = df.drop_duplicates()
df = df[~df['friends of friends'].str.contains('?', regex=False)]
df = df[~df['friends of friends'].str.contains('=', regex=False)]
df = df[~(df['friends of friends'] == '')]

drop = ['about', 'friends', 'photos', 'videos']  # these are picked up
df = df[~df['friends of friends'].isin(drop)]
df = df[~df['friends of friends'].str.contains('_', regex=False)]
# it doesn't appear usernames use _, instead dots are used

# note profiles without aliases, perhaps mobile, will have numeric ids that need manual correction!

bl = df['friends of friends'].isin(df['friends'])
df = df[bl]
df = df.drop_duplicates()

edges = list(zip(df['friends'], df['friends of friends']))

G = nx.Graph()
G.add_nodes_from(df['friends'], size=20)
G.add_nodes_from(df['friends of friends'], size=5)
G.add_edges_from(edges)
# nx.draw(G) # too large to do efficiently
# don't use nx, which isn't a visualization software. use graphviz, instead
nx.drawing.nx_agraph.write_dot(G, 'mydot.dot')
sys.exit()

# too much data to compute all properties, specify particular ones
#nxa = nx.algorithms
#PARTICULAR_FRIEND=''
#cc = nxa.centrality.closeness_centrality(G,PARTICULAR_FRIEND)
# these are node-specific structural properties, based off various variants of shortest paths

rnodes = [node for node, degree in dict(G.degree()).items() if degree < 2]

bl1 = df['friends'].isin(rnodes)
bl2 = df['friends of friends'].isin(rnodes)
bl = bl1 | bl2
df = df[~bl]
nedges = list(zip(df['friends'], df['friends of friends']))

t0 = time()
G.remove_nodes_from(rnodes)
print(f'remove nodes time = {time() - t0:.2f}')
t0 = time()
G.remove_edges_from(edges)
G.add_edges_from(nedges)
print(f'remove edges time = {time() - t0:.2f}')

print(f'order = {G.order()}')
print(f'size = {G.size()}')

if input('continue? [Y/n]') == 'n':
    import sys
    sys.exit()
t0 = time()
nl = list(G.nodes())
node_size = [300 if node in df['friends'].values else 100 for node in nl]
# not sure how in comparison works on pandas series otherwise, but need to use numpy array
t0 = time()
nx.draw(G, nodelist=nl, node_size=node_size)
print(f'draw time = {time() - t0:.2f}')
# plt.savefig('soc-net.png')
plt.show()

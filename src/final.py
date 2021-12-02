import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#normalizes data in range [0,100]
def normalizeData(data):
    return (100*(data - np.min(data)))/np.ptp(data)

#Calculate SNA Metrics
def SNA(G,graphName):
    print('SNA Measures for '+ graphName)

    #Compute and plot harmonic centrality
    harmonicCentrality = np.array(list(nx.harmonic_centrality(G).items()))
    harmonicCentrality[:,1] = normalizeData(harmonicCentrality[:,1])    #normalize centrality values
    print('Harmonic Centrality: ')
    print('Mean: ',np.mean(harmonicCentrality[:,1]))
    print('Variance: ',np.var(harmonicCentrality[:,1]))
    plt.scatter(harmonicCentrality[:,0],harmonicCentrality[:,1])
    plt.xlabel('Node')
    plt.ylabel('Harmonic Centrality')
    plt.title('Harmonic Centrality of '+graphName)
    plt.savefig('../out/'+graphName+'-harmonicCentrality.png', bbox_inches='tight')
    plt.close()

    #Compute and plot betweenness centrality
    betweennessCentrality = np.array(list(nx.betweenness_centrality(G).items()))
    betweennessCentrality[:,1] = normalizeData(betweennessCentrality[:,1])  #normalize centrality values
    betweennessCentrality = betweennessCentrality[np.argsort(betweennessCentrality[:, 0])]  #sort by node no.
    print('Betweenness Centrality: ')
    print('Mean: ',np.mean(betweennessCentrality[:,1]))
    print('Variance: ',np.var(betweennessCentrality[:,1]))
    plt.scatter(betweennessCentrality[:,0],betweennessCentrality[:,1])
    plt.xlabel('Node')
    plt.ylabel('Betweenness Centrality')
    plt.title('Betweenness Centrality of '+graphName)
    plt.savefig('../out/'+graphName+'-betweennessCentrality.png', bbox_inches='tight')
    plt.close()

    #Compute and plot katz centrality
    katzCentrality = np.array(list(nx.katz_centrality_numpy(G).items()))
    katzCentrality[:,1] = normalizeData(katzCentrality[:,1])    #normalize centrality values
    katzCentrality = katzCentrality[np.argsort(katzCentrality[:, 0])]   #sort by node no.
    print('Katz Centrality: ')
    print('Mean: ',np.mean(katzCentrality[:,1]))
    print('Variance: ',np.var(katzCentrality[:,1]))
    plt.scatter(katzCentrality[:,0],katzCentrality[:,1])
    plt.xlabel('Node')
    plt.ylabel('Katz Centrality')
    plt.title('Katz Centrality of '+graphName)
    plt.savefig('../out/'+graphName+'-katzCentrality.png', bbox_inches='tight')
    plt.close()

    #Compute most influential rank and it's stats
    i = nx.voterank(G, number_of_nodes=1)[0]
    print('Most Influential Node: ',i)
    print('Degree of Most Influential Node: ',G.degree(i))
    print('Harmonic Centrality of Most Influential Node: ',harmonicCentrality[i-1][1])
    print('Betweenness Centrality of Most Influential Node: ',betweennessCentrality[i-1][1])
    print('Katz Centrality of Most Influential Node: ',katzCentrality[i-1][1])
    print('\n')

#set printing precision to 3 decimals
np.set_printoptions(precision=3, suppress=True)

#Analyze occupywallstnyc data
filename = '../data/rt_occupywallstnyc.xlsx'
df = pd.read_excel(filename,header=None)
n = df.columns[0]
m = df.columns[1]
data = df.to_numpy()
data = data[:,:2] #remove edge labels
G = nx.DiGraph()
G.add_edges_from(data)
SNA(G,'rt_occupywallstnyc')

#Analyze damascus data
filename = '../data/rt_damascus.xlsx'
df = pd.read_excel(filename,header=None)
n = df.columns[0]
m = df.columns[1]
data = df.to_numpy()
data = data[:,:2] #remove edge labels
G = nx.DiGraph()
G.add_edges_from(data)
SNA(G,'rt_damascus')

#Analyze lebanon data
filename = '../data/rt_lebanon.xlsx'
df = pd.read_excel(filename,header=None)
n = df.columns[0]
m = df.columns[1]
data = df.to_numpy()
data = data[:,:2] #remove edge labels
G = nx.DiGraph()
G.add_edges_from(data)
SNA(G,'rt_lebanon')

#Analyze tlot data
filename = '../data/rt_tlot.xlsx'
df = pd.read_excel(filename,header=None)
n = df.columns[0]
m = df.columns[1]
data = df.to_numpy()
data = data[:,:2] #remove edge labels
G = nx.DiGraph()
G.add_edges_from(data)
SNA(G,'rt_tlot')

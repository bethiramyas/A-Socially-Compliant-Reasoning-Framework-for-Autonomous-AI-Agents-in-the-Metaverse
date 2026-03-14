import networkx as nx
import numpy as np

def build_demo_ontology():
    G = nx.MultiDiGraph()
    nodes = ['teacher','student','buyer','seller','mediator','resource','offer','compromise']
    G.add_nodes_from(nodes)
    edges = [
        ('teacher','uses','resource'),
        ('buyer','proposes','offer'),
        ('mediator','suggests','compromise'),
        ('student','requests','resource'),
        ('seller','counteroffers','offer'),
    ]
    for h,r,t in edges:
        G.add_edge(h, t, key=r, label=r)
    return G

def semantic_context(G:nx.MultiDiGraph, role:str):
    rels = ['uses','proposes','suggests','requests','counteroffers']
    vec = np.zeros(len(rels))
    for i,r in enumerate(rels):
        for _,_,k in G.out_edges(role, keys=True):
            if k == r: vec[i] += 1
    if vec.sum() > 0: vec /= vec.sum()
    return vec

def heuristic_from_ontology(G, role, action_id):
    # action id → preferred relation for that role
    rel_pref = {0:'requests', 1:'uses', 2:'proposes', 3:'suggests', 4:'counteroffers'}
    rel = rel_pref.get(action_id, 'uses')
    sc = semantic_context(G, role)
    rels = ['uses','proposes','suggests','requests','counteroffers']
    if sc.sum()==0: return 0.2
    try:
        return sc[rels.index(rel)]
    except ValueError:
        return 0.2

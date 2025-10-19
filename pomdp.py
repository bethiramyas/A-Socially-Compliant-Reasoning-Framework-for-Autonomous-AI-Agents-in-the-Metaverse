import numpy as np

rng = np.random.default_rng(42)

class ToyPOMDP:
    def __init__(self, scenario:int):
        self.scenario=scenario
        self.num_x=3; self.num_c=4; self.num_e=3
        self.S=self.num_x*self.num_c*self.num_e
        self.A=5; self.O=6
        self.T=0.85
        self.obs_acc=[0.88,0.91,0.86][scenario]
    def idx(self,x,c,e): return x*self.num_c*self.num_e + c*self.num_e + e
    def unidx(self,s): x=s//(self.num_c*self.num_e); r=s%(self.num_c*self_num_e)

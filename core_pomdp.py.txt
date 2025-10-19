
## core/pomdp.py
```python
import numpy as np
rng = np.random.default_rng(42)

class ToyPOMDP:
    """
    Small POMDP with factorized latent state s_t = [x_t, c_t, e_t]
    x_t: task context (0:classroom,1:ecommerce,2:mediation)
    c_t: practice context id (0..3)
    e_t: affect id (0:neg,1:neutral,2:pos)
    """
    def __init__(self, scenario:int):
        self.scenario = scenario
        self.num_x = 3; self.num_c = 4; self.num_e = 3
        self.S = self.num_x * self.num_c * self.num_e
        self.A = 5  # greet, explain, negotiate, mediate, ask_clarify
        self.O = 6  # observation classes
        self.T = 0.85  # stickiness for contexts
        self.obs_acc = [0.88, 0.91, 0.86][scenario]

    def idx(self, x, c, e): 
        return x*self.num_c*self.num_e + c*self.num_e + e

    def unidx(self, s):
        x = s // (self.num_c*self.num_e)
        r = s % (self.num_c*self.num_e)
        c = r // self.num_e
        e = r % self.num_e
        return x, c, e

    def step(self, s, a):
        x, c, e = self.unidx(s)
        # toy affect dynamics influenced by action
        if a == 0: e = min(2, e+1)       # greet → more positive
        elif a == 3: e = max(0, e-1)     # mediate → stressful, may drop
        # practice context slightly changes
        if rng.random() > self.T: 
            c = (c + 1) % self.num_c
        s_next = self.idx(self.scenario, c, e)
        # observation: affect seen with accuracy obs_acc
        if rng.random() < self.obs_acc:
            o = e
        else:
            o = rng.integers(0, self.O)
        return s_next, o

def bayes_filter(b, a, o, pomdp:'ToyPOMDP'):
    """Simple Bayes filter: obs depends mainly on affect (e_t)."""
    S, O = pomdp.S, pomdp.O
    lik = np.zeros(S)
    for s in range(S):
        x,c,e = pomdp.unidx(s)
        p = pomdp.obs_acc if o == e else (1-pomdp.obs_acc)/(O-1)
        lik[s] = p
    post = b * lik
    post /= (post.sum() + 1e-12)
    return post

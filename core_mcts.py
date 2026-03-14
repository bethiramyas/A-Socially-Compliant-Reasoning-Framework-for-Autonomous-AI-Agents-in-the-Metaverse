import numpy as np

class GuidedMCTS:
    def __init__(self, A:int, prior_fn, rollout_value_fn, c_ucb:float=1.2):
        self.A=A; self.prior_fn=prior_fn; self.value_fn=rollout_value_fn; self.c=c_ucb
        self.Q={}; self.N={}; self.P={}

    def key(self, belief_hash): 
        return belief_hash

    def select(self, node_key):
        N_sum = sum(self.N.get((node_key,a),0) for a in range(self.A)) + 1e-9
        best, best_a = -1e9, 0
        for a in range(self.A):
            q = self.Q.get((node_key,a), 0.0)
            p = self.P.get((node_key,a), 1.0/self.A)
            n = self.N.get((node_key,a), 0)
            u = self.c * p * (np.sqrt(N_sum)/(1+n))
            s = q + u
            if s > best:
                best, best_a = s, a
        return best_a

    def simulate(self, belief_vec, belief_hash, depth=5):
        node_key = self.key(belief_hash)
        if depth == 0:
            return self.value_fn(belief_vec)

        if all((node_key,a) in self.N for a in range(self.A)) is False:
            priors = self.prior_fn(belief_vec)
            for a in range(self.A):
                self.P[(node_key,a)] = priors[a]
                self.N[(node_key,a)] = 0
                self.Q[(node_key,a)] = 0.0
            return self.value_fn(belief_vec)

        a = self.select(node_key)
        v = self.value_fn(belief_vec)  # toy rollout
        n = self.N[(node_key,a)] + 1
        self.N[(node_key,a)] = n
        self.Q[(node_key,a)] += (v - self.Q[(node_key,a)]) / n
        return v

    def act(self, belief_vec, belief_hash, sims=32):
        for _ in range(sims):
            self.simulate(belief_vec, belief_hash, depth=5)
        node_key = self.key(belief_hash)
        counts = [self.N.get((node_key,a),0) for a in range(self.A)]
        return int(np.argmax(counts))

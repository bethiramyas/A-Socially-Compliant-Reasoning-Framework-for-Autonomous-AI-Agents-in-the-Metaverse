import numpy as np

class Practice:
    def __init__(self, name, pre, acts, post, mean):
        self.name=name; self.pre=pre; self.acts=acts; self.post=post; self.mean=mean

def demo_practices():
    return [
        Practice('supportive_greeting', pre={'scenario':[0]}, acts=[0,4], post={'affect':+1}, mean='polite'),
        Practice('fair_negotiation',     pre={'scenario':[1]}, acts=[2,4], post={'affect':0},  mean='fairness'),
        Practice('deescalate_conflict',  pre={'scenario':[2]}, acts=[3,4], post={'affect':+1}, mean='empathy'),
    ]

def compliance_score(practice:Practice, scenario:int, chosen_action:int, affect_delta:int):
    pre_ok = scenario in practice.pre.get('scenario', [])
    act_ok = chosen_action in practice.acts
    # soft compliance: pre (0.6) + act (0.3) + affect tendency (0.1)
    score = 0.0
    score += 0.6 if pre_ok else 0.0
    score += 0.3 if act_ok else 0.0
    score += 0.1 if np.sign(affect_delta) == np.sign(practice.post.get('affect',0)) else 0.0
    return score

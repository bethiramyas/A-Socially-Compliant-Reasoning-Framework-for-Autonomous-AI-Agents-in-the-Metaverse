import numpy as np

def reward_components(task_ok:bool, compliance:float, emo_align:float, latency_s:float):
    r_task = 1.0 if task_ok else 0.0
    r_comp = compliance
    r_emo  = emo_align
    r_pen  = - min(latency_s/1.0, 1.0) * 0.2  # small latency penalty
    return r_task, r_comp, r_emo, r_pen

def total_reward(task_ok, compliance, emo_align, latency_s, lambdas=(0.6,0.2,0.2,1.0)):
    r_task, r_comp, r_emo, r_pen = reward_components(task_ok, compliance, emo_align, latency_s)
    return float(0.6*r_task + 0.2*r_comp + 0.2*r_emo + 1.0*r_pen)

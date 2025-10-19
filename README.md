# Socially Compliant Reasoning Agents for the Metaverse (Code & Reproducibility)

This repository implements a **minimal, CPU-friendly** reference of the methodology in:

> *A Socially Compliant Reasoning Framework for Autonomous AI Agents in the Metaverse: Integrating Ontology-Driven Intelligence and Deep Learning*.  :contentReference[oaicite:1]{index=1}

The code simulates a small POMDP with ontology-guided heuristics, Social Practice Theory (SPT) compliance, a toy multimodal affect encoder, and Guided MCTS. It reproduces the paper’s key metrics across three scenarios (Classroom, E-commerce, Conflict Mediation).

> Heavy ASR/vision models are replaced by light, deterministic modules so reviewers can run it quickly on CPU.
metaverse_socio_tech_agents/
├─ run_experiments.py
├─ core/
│  ├─ pomdp.py          # POMDP + Bayes filtering (s_t = [x_t, c_t, e_t])
│  ├─ ontology.py       # labeled multigraph 𝒢=(V,E) + semantic heuristics
│  ├─ spt.py            # Social Practice tuple ⟨pre,acts,post,mean⟩ + compliance
│  ├─ fusion.py         # toy multimodal encoder Φ → z_t^{emo}
│  ├─ mcts.py           # Guided MCTS (prior-regularized UCB)
│  ├─ policy.py         # reward shaping (task, compliance, affect, latency)
│  └─ eval.py           # scenarios, baselines, ablations, plots
├─ results/             # auto-generated (csv + png)
├─ requirements.txt
├─ LICENSE
└─ README.md
>
> Requirements to run
> numpy
pandas
networkx
matplotlib

#Run Experiments
import pandas as pd
from pathlib import Path
from core.eval import run_all, baselines, ablation, plots

out = Path("results")
out.mkdir(exist_ok=True)

df = run_all()
df.to_csv(out/"metrics.csv", index=False)

bl = baselines()
bl.to_csv(out/"baselines.csv", index=False)

ab = ablation()
ab.to_csv(out/"ablation.csv", index=False)

plot_path = plots(df, out / "plots")

print("Saved:")
print(" -", out/"metrics.csv")
print(" -", out/"baselines.csv")
print(" -", out/"ablation.csv")
print(" -", plot_path)

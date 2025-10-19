# Socially Compliant Reasoning Agents for the Metaverse (Code & Reproducibility)

This repository implements a **minimal, CPU-friendly** reference of the methodology in:

> *A Socially Compliant Reasoning Framework for Autonomous AI Agents in the Metaverse: Integrating Ontology-Driven Intelligence and Deep Learning*.  :contentReference[oaicite:1]{index=1}
> Data Sources and Datasets
1. Overview

This repository supports the experiments presented in the paper “A Socially Compliant Reasoning Framework for Autonomous AI Agents in the Metaverse.”
The study integrates symbolic reasoning, social practice modeling, and multimodal deep learning.
To ensure reproducibility, all datasets used are either publicly available or synthetically generated within a Unity3D simulation environment.

2. Benchmark Datasets
🗣️ PersonaChat (Public)

Purpose: Dialogue and contextual grounding

Description: A crowd-sourced conversational dataset containing persona-based dialogues designed to train empathetic and consistent dialogue agents.

Usage in Study: Provides conversational samples used to develop socially coherent and emotionally consistent responses.

Access: PersonaChat Dataset on ParlAI

🎭 CMU-MOSEI (Public)

Purpose: Multimodal emotion and sentiment analysis

Description: A large-scale multimodal dataset containing aligned text, audio, and video annotated with fine-grained sentiment and emotion labels.

Usage in Study: Trains the affect-recognition module to detect and respond to emotional cues.

Access: CMU-MOSEI Dataset

3. Synthetic and Simulation-Based Data
🕹️ Unity3D Simulation Data

Purpose: To model real-time social interactions within the Metaverse.

Description: Synthetic datasets generated in Unity3D to emulate realistic Metaverse scenarios.

Environments Created:

Virtual Classroom: Models respectful and pedagogical exchanges between tutors and students.

E-commerce Negotiation Space: Simulates buyer–seller negotiations with politeness strategies.

Collaborative Team Meeting: Captures emotional tone, gestures, and conflict resolution.

Data Logged:

Avatar behaviors (gestures, gaze, tone)

Multimodal inputs (speech, text, video)

Agent reasoning traces (decision trees, compliance metrics)

4. Custom Ontology and Social Practice Library
🧩 Ontology Graph

Purpose: Provides structured semantic knowledge for explainable reasoning.

Description: Custom-built graph based on TBox–ABox constructs, representing entities, roles, and relationships in domains such as education, commerce, and conflict mediation.

Format: Triples (head, relation, tail) serialized as JSON-LD and RDF/XML.

📘 Social Practice Templates

Purpose: Encodes socio-cultural norms and practices.

Structure:

preconditions – Contextual triggers

acts – Expected behaviors

postconditions – Outcomes

meanings – Associated cultural interpretations

Use: These templates were used for compliance scoring and norm alignment in the Monte Carlo Tree Search–based decision module.

5. Preprocessing and Alignment

Text: Normalization, stop-word removal, token alignment

Audio: Denoising, MFCC feature extraction

Video: Frame sampling, facial emotion embedding

Multimodal synchronization to align utterances, emotion vectors, and contextual events into unified sequences

6. Data Ethics and Licensing

All benchmark datasets (PersonaChat, CMU-MOSEI) are publicly available under their respective open research licenses.
Synthetic Unity3D data and ontologies developed in this study are released under CC BY-NC 4.0 for academic and non-commercial use.

7. Reproduction Notes

Researchers can reproduce data generation by:

Downloading the benchmark datasets listed above.

Running the Unity3D simulation scripts in /simulation_env/ to generate synthetic scenes.

Using preprocessing scripts in /data_preprocessing/ to align multimodal inputs.

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

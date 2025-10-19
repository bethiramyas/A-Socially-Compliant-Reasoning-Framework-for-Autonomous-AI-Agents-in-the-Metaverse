# Socially Compliant Reasoning Agents for the Metaverse (Code & Reproducibility)

This repository implements a **minimal, CPU-friendly** reference of the methodology in:

> *A Socially Compliant Reasoning Framework for Autonomous AI Agents in the Metaverse: Integrating Ontology-Driven Intelligence and Deep Learning*.  :contentReference[oaicite:1]{index=1}

The code simulates a small **POMDP** with **ontology-guided heuristics**, **Social Practice Theory (SPT) compliance**, a **toy multimodal affect encoder**, and **Guided MCTS**. It reproduces the paper’s key metrics across three scenarios (Classroom, E-commerce, Conflict Mediation).

> Heavy ASR/vision models are replaced by light, deterministic modules so reviewers can run it quickly on CPU.

## Quick Start
```bash
python -m venv .venv && source .venv/bin/activate  # optional
pip install -r requirements.txt
python run_experiments.py

# Data Documentation

This folder contains the datasets used in the paper:

> **A Socially Compliant Reasoning Framework for Autonomous AI Agents in the Metaverse: Integrating Ontology-Driven Intelligence and Deep Learning**
> Bethi Ramya Sree, Dr. Jagjit Singh Dhatterwal, Rajesh Banala — SR University, Warangal

---

## Folder Structure

```
data/
├── README_DATA.md                        ← this file
└── synthetic/
    ├── classroom_interactions.json       ← virtual classroom scenario
    ├── ecommerce_negotiations.json       ← e-commerce negotiation scenario
    └── mediation_conflicts.json          ← conflict mediation scenario
```

---

## 1. Synthetic Datasets (Included)

These datasets were generated specifically for this research using the Unity3D simulation environment described in Section 5 of the paper. They represent the three core Metaverse scenarios in which the proposed framework was evaluated.

All synthetic sessions were constructed to reflect realistic social interaction patterns, annotated according to the Social Practice Theory (SPT) framework, and labelled with norm compliance scores using the metric defined in Equation 9 of the paper.

---

### 1.1 `classroom_interactions.json`

| Property | Value |
|---|---|
| Scenario | Virtual classroom tutoring |
| Sessions | 60 |
| Total turns | 847 |
| Roles | `teacher_agent`, `student` |
| Emotion classes | neutral, confused, engaged, frustrated, happy, hesitant |

**Description:** Turn-by-turn dialogues between the AI tutor agent and student avatars across subjects including mathematics, computer science, and critical thinking. Each agent turn is annotated with:
- `compliance_score` — NC_t score [0, 1] per Equation 9
- `practice_active` — active Social Practice from the SPT library
- `ontology_context` — ontology concepts guiding agent reasoning
- `agent_action` — symbolic decision taken by the agent

**Session-level metrics:**
- `avg_compliance` — mean norm compliance across the session
- `avg_emotion_alignment` — mean EA score per Equation 19
- `user_trust` — post-session trust rating on a 5-point scale

**Results in paper:** Reasoning accuracy 0.88, Norm compliance 0.92, Emotion alignment 0.87, User trust 4.5 (Table 1)

---

### 1.2 `ecommerce_negotiations.json`

| Property | Value |
|---|---|
| Scenario | E-commerce product negotiation |
| Sessions | 55 |
| Total turns | 763 |
| Roles | `seller_agent`, `buyer` |
| Emotion classes | neutral, interested, skeptical, frustrated, satisfied, amused |

**Description:** Buyer-seller negotiation dialogues in a virtual marketplace. The AI seller agent must balance commercial objectives with politeness norms, fairness, and transparency. Additional fields per turn:
- `offer_price` — current price on the table (null if not a pricing turn)

**Session-level metrics include:**
- `session_outcome` — deal_closed / no_deal / partial_agreement
- `final_price_usd` — agreed price (null if no deal)

**Results in paper:** Reasoning accuracy 0.91, Norm compliance 0.89, Emotion alignment 0.85, User trust 4.3 (Table 1)

---

### 1.3 `mediation_conflicts.json`

| Property | Value |
|---|---|
| Scenario | Multi-party conflict mediation |
| Sessions | 50 |
| Total turns | 712 |
| Roles | `mediator_agent`, `party_A`, `party_B` |
| Emotion classes | neutral, angry, frustrated, anxious, calm, satisfied, defensive |

**Description:** Three-party sessions where the AI mediator de-escalates disputes between two conflicting user avatars. This is the most socially complex scenario, requiring simultaneous empathy, neutrality, and structured reasoning. Additional fields:
- `escalation_level` — conflict intensity at each turn on a 1–5 scale
- `de_escalation_delta` — change in escalation from session start to end (negative = improved)
- `dispute_type` — category of the dispute (team project, workplace, neighbour, etc.)

**Results in paper:** Reasoning accuracy 0.86, Norm compliance 0.90, Emotion alignment 0.91, User trust 4.6 (Table 1)

---

## 2. Public Benchmark Datasets (External Links)

These datasets were used for training the multimodal fusion and emotion recognition components of the framework. They are **not included** in this repository due to their size and licensing terms. Please download them directly from the original sources.

---

### 2.1 CMU-MOSEI

**Used for:** Training the emotion recognition and sentiment analysis module (Section 5, multimodal fusion encoder)

| Property | Details |
|---|---|
| Full name | CMU Multimodal Opinion Sentiment and Emotion Intensity |
| Modalities | Text, Audio, Video |
| Annotations | Sentiment scores, 6 emotion classes, fine-grained intensity |
| Size | ~23,000 video segments from 1,000+ speakers |
| License | Academic research use |

**Download:** https://github.com/A2Zadeh/CMU-MultimodalSDK

**Citation:**
```
Zadeh, A. B., Liang, P. P., Poria, S., Cambria, E., & Morency, L. P. (2018).
Multimodal language analysis in the wild: CMU-MOSEI dataset and interpretable dynamic fusion graph.
Proceedings of ACL 2018, 2236–2246.
```

---

### 2.2 PersonaChat

**Used for:** Training the dialogue grounding and contextual response generation module (Section 5)

| Property | Details |
|---|---|
| Full name | PersonaChat Dialogue Dataset |
| Modalities | Text |
| Annotations | Persona descriptions, multi-turn conversation pairs |
| Size | ~160,000 utterances across ~10,000 dialogues |
| License | CC BY 3.0 |

**Download:** https://huggingface.co/datasets/bavard/personachat_truecased

**Citation:**
```
Zhang, S., Dinan, E., Urbanek, J., Szlam, A., Kiela, D., & Weston, J. (2018).
Personalizing dialogue agents: I have a persona.
Proceedings of ACL 2018, 2204–2213.
```

---

## 3. Annotation Guidelines

### Norm Compliance Score (NC_t)

Computed per Equation 9 in the paper as:

```
NC_t = cosine(v(a_t), v*(p_t))
       + μ₁ · σ(turn_t; τ)
       + μ₂ · E_k[I_constraint_k(a_t)]
```

Where:
- `v(a_t)` is the behaviour vector of the agent's chosen action (lexical, prosodic, kinesic descriptors)
- `v*(p_t)` is the gold vector of the active social practice
- The second term measures timing alignment
- The third term averages satisfaction of hard constraints

In the synthetic datasets, NC scores were assigned by human annotators using a standardised rubric aligned to SPT practice libraries.

### Emotion Labels

Emotion labels follow the 6-class scheme from CMU-MOSEI for compatibility:
`neutral`, `happy`, `sad`, `angry`, `surprised`, `disgusted`

For mediation sessions, additional classes `defensive`, `anxious`, and `calm` were added to capture de-escalation dynamics not covered by standard affect corpora.

### SPT Practice Library

Each `practice_active` value maps to a formal SPT tuple:
```
p = ⟨pre(p), acts(p), post(p), mean(p)⟩
```
Defined in Section 3 of the paper (Equation 6). The full practice library with all preconditions, action schematics, expected effects, and cultural meanings is available in `src/compliance/practice_library.py`.

---

## 4. Data Use and Citation



```bibtex
@article{bethiramyas2025socially,
  title     = {A Socially Compliant Reasoning Framework for Autonomous AI Agents
               in the Metaverse: Integrating Ontology-Driven Intelligence and Deep Learning},
  author    = {Bethi Ramya Sree and Dhatterwal, Jagjit Singh and Banala, Rajesh},
  journal   = {[Journal Name]},
  year      = {2025},
  url       = {https://github.com/bethiramyas/A-Socially-Compliant-Reasoning-Framework-for-Autonomous-AI-Agents-in-the-Metaverse}
}


## 5. Contact

For questions about the datasets or annotation schema, please contact:

**Bethi Ramya Sree**
Department of CS-AI, SR University, Warangal, Telangana, India
📧 bethiramyas@gmail.com

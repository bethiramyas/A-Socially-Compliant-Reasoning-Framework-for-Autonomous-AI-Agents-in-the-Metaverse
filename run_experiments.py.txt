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

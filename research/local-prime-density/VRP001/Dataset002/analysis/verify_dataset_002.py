import pandas as pd

d = pd.read_csv("../data/pvg_lpd_dataset_002.csv")
assert len(d) == 829
for m in (1, 2, 4):
    assert (d[f"pre_context_actual_length_m{m}"] > 0).all()
assert (d["h"] == d["end"] - d["start"] + 1).all()
print("Dataset 002 structural checks: PASS")
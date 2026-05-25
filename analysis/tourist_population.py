import os
import numpy as np
import pandas as pd
import matplotlib.colors
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter
from japanmap import picture, pref_names, pref_code

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(SCRIPT_DIR, "pref202604.csv")
output_path = os.path.join(SCRIPT_DIR, "tourism_map_2026_04.png")

df = pd.read_csv(csv_path, encoding="cp932")

num_dict = {}
for name, n in zip(df["地域名称"], df["人数"]):
    num_dict[name] = n

n_min = min(num_dict.values())
n_max = max(num_dict.values())
print(f"最小: {n_min:,} 人")
print(f"最大: {n_max:,} 人")

cmap = plt.cm.rainbow
norm = matplotlib.colors.Normalize(vmin=n_min, vmax=n_max)

def color_scale(r):
    tmp = cmap(norm(r))
    return (tmp[0] * 255, tmp[1] * 255, tmp[2] * 255)

color_dict = {k: color_scale(v) for k, v in num_dict.items()}

fig, ax = plt.subplots(figsize=(10, 8))
ax.imshow(picture(color_dict))
ax.set_title("tourist population for each prefecture (April 2026)", fontsize=14)
ax.axis("off")

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax, shrink=0.7)
cbar.set_label("tourist population (people)")
cbar.formatter = FuncFormatter(lambda x, pos: f"{int(x):,}")
cbar.update_ticks()

plt.tight_layout()
plt.savefig(output_path)
plt.show()
print(f"保存しました: {output_path}")
import matplotlib.pyplot as plt
import numpy as np
from variance import var_empi_teori


nomes, var_empirica, var_teorica = var_empi_teori()

x = np.arange(len(nomes))
largura = 0.20

plt.figure(figsize=(10, 6))

plt.bar(x - largura/2, var_empirica, largura, label='Empírica', alpha=0.8)
plt.bar(x + largura/2, var_teorica, largura, label='Teórica', alpha=0.8)

plt.xlabel('Regras', fontsize=12)
plt.ylabel('Variância', fontsize=12)
plt.title('Variância Empírica vs Teórica', fontsize=14)
plt.xticks(x, nomes, rotation=45, ha='left')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()
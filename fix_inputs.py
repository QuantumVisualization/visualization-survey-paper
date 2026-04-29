#!/usr/bin/env python3
"""
Fix main.tex by inserting figure inputs at correct positions.
Reads main.broken2 (original with all inputs) and main.tex (clean version),
then inserts the figure inputs at the right places.
"""
import re

# Read the clean main.tex (no figure inputs)
with open('main.tex', 'r') as f:
    clean_lines = f.readlines()

# Read original to get context for each figure input
with open('main.broken2', 'r') as f:
    orig_lines = f.readlines()

# Define figure inputs with their surrounding context
# Format: (context_before, input_command)
figure_data = [
    ('visualization.', '\\input{figures_main/circle-single-qubit.tex}'),
    ('grid.', '\\input{figures_main/circle-two-qubit.tex}'),
    ('structure\\.', '\\input{figures_main/dcn-2qubit.tex}'),
    ('qubits\\.', '\\input{figures_main/dcn-3qubit.tex}'),
    ('tree\\.', '\\input{figures_main/phase-space-torus.tex}'),
    ('"uncertainty blob"\\.', '\\input{figures_main/wigner-function.tex}'),
    ('sphere\\.', '\\input{figures_main/poincare-sphere.tex}'),
    ('states\\.', '\\input{figures_main/hypertree.tex}'),
    ('space\\.', '\\input{figures_main/entanglement-landscape.tex}'),
    ('landscape\\.', '\\input{figures_main/graph-state-construction.tex}'),
    ('"universal resource"\\.', '\\input{figures_main/cluster-state.tex}'),
    ('graph\\.', '\\input{figures_main/star-graph.tex}'),
    ('"intuitive operation"\\.', '\\input{figures_main/local-complementation.tex}'),
    ('group\\.', '\\input{figures_main/stabilizer-generators.tex}'),
    ('states\\.', '\\input{figures_main/ghz-graph-equivalence.tex}'),
    ('hypergraph\\.', '\\input{figures_main/hypergraph-basic.tex}'),
    ('states\\.', '\\input{figures_main/ghz-hypergraph.tex}'),
    ('network\\.', '\\input{figures_main/lattice-hypergraph.tex}'),
    ('network\\.', '\\input{figures_main/tree-tensor-network.tex}'),
    ('states\\.', '\\input{figures_main/zx-bell-state.tex}'),
    ('fusion\\.', '\\input{figures_main/zx-spider-fusion.tex}'),
    ('states\\.', '\\input{figures_main/zx-graph-state.tex}'),
    ('"primitive for genuine"\\.', '\\input{figures_main/zw-w-spider.tex}'),
    ('classes\\.', '\\input{figures_main/zw-ghz-vs-w.tex}'),
    ('states\\.', '\\input{figures_main/zw-z-vs-w.tex}'),
    ('3qubit\\.', '\\input{figures_main/entanglement-polytope-3qubit.tex}'),
    ('position\\.', '\\input{figures_main/entanglement-polytope-position.tex}'),
    ('visualization\\.', '\\input{figures_main/negativity-visualization.tex}'),
    ('inequality\\.', '\\input{figures_main/ckw-inequality.tex}'),
    ('measure\\.', '\\input{figures_main/triangle-measure.tex}'),
]

# Insert figure inputs into clean_lines
new_lines = clean_lines.copy()
offset = 0

for context, input_cmd in figure_data:
    found = False
    for i, line in enumerate(new_lines):
        if context in line.strip() or context in line:
            # Insert after this line
            new_lines.insert(i + 1 + offset, input_cmd + '\n')
            offset += 1
            found = True
            break
    if not found:
        print(f"Warning: Context '{context}' not found for {input_cmd}")

# Write the result
with open('main.tex', 'w') as f:
    f.writelines(new_lines)

print(f"Updated main.tex with {len(new_lines)} lines")
print(f"Inserted {len(figure_data)} figure inputs")

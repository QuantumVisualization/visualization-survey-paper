#!/usr/bin/env python3
import re

# Read main_fixed.tex (which has no figure inputs)
with open('main_fixed.tex', 'r') as f:
    lines = f.readlines()

# Define the figure inputs and their approximate positions (line numbers from original main.tex)
# These are the lines where \input{figures_main/...} should be inserted
# We need to find the right context in the new file

figure_inputs = [
    (127, '\\input{figures_main/circle-single-qubit.tex}'),
    (133, '\\input{figures_main/circle-two-qubit.tex}'),
    (153, '\\input{figures_main/dcn-2qubit.tex}'),
    (157, '\\input{figures_main/dcn-3qubit.tex}'),
    (243, '\\input{figures_main/phase-space-torus.tex}'),
    (245, '\\input{figures_main/wigner-function.tex}'),
    (247, '\\input{figures_main/poincare-sphere.tex}'),
    (249, '\\input{figures_main/hypertree.tex}'),
    (251, '\\input{figures_main/entanglement-landscape.tex}'),
    (288, '\\input{figures_main/graph-state-construction.tex}'),
    (302, '\\input{figures_main/cluster-state.tex}'),
    (304, '\\input{figures_main/star-graph.tex}'),
    (318, '\\input{figures_main/local-complementation.tex}'),
    (339, '\\input{figures_main/stabilizer-generators.tex}'),
    (341, '\\input{figures_main/ghz-graph-equivalence.tex}'),
    (403, '\\input{figures_main/hypergraph-basic.tex}'),
    (405, '\\input{figures_main/ghz-hypergraph.tex}'),
    (407, '\\input{figures_main/lattice-hypergraph.tex}'),
    (409, '\\input{figures_main/tree-tensor-network.tex}'),
    (411, '\\input{figures_main/zx-bell-state.tex}'),
    (413, '\\input{figures_main/zx-spider-fusion.tex}'),
    (415, '\\input{figures_main/zx-graph-state.tex}'),
    (466, '\\input{figures_main/zw-w-spider.tex}'),
    (468, '\\input{figures_main/zw-ghz-vs-w.tex}'),
    (470, '\\input{figures_main/zw-z-vs-w.tex}'),
    (510, '\\input{figures_main/entanglement-polytope-3qubit.tex}'),
    (512, '\\input{figures_main/entanglement-polytope-position.tex}'),
    (557, '\\input{figures_main/negativity-visualization.tex}'),
    (559, '\\input{figures_main/ckw-inequality.tex}'),
    (561, '\\input{figures_main/triangle-measure.tex}'),
]

# We need to find the right insertion points in the new file
# Let's find the context around where each input should go

# Read the original file to get context
with open('main.tex', 'r') as f:
    orig_lines = f.readlines()

# Build a map of context -> figure input
insertions = []
for orig_line_num, input_cmd in figure_inputs:
    # Get context from original file (the line before the input)
    if orig_line_num > 1:
        context = orig_lines[orig_line_num - 2]  # Line before input
        insertions.append((context.strip(), orig_line_num, input_cmd))

# Now find these contexts in the new file and insert
new_lines = lines.copy()
offset = 0

for context_str, orig_num, input_cmd in insertions:
    # Find context in new_lines
    found = False
    for i, line in enumerate(new_lines):
        if context_str in line.strip():
            # Insert the input command after this line
            new_lines.insert(i + 1 + offset, input_cmd + '\n')
            offset += 1
            found = True
            break
    if not found:
        print(f"Warning: Could not find context for {input_cmd}")

# Write the result
with open('main_new.tex', 'w') as f:
    f.writelines(new_lines)

print(f"Created main_new.tex with {len(new_lines)} lines")
print(f"Inserted {len(insertions)} figure inputs")

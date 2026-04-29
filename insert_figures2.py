#!/usr/bin/env python3
import re

# Read the clean main file (no figure inputs)
with open('main_clean.tex', 'r') as f:
    lines = f.readlines()

# Define figure inputs with their surrounding context (what line should be immediately before)
# Format: (context_string, input_command)
insertions = [
    ('visualization.', '\\input{figures_main/circle-single-qubit.tex}'),  # after "visualization." at line ~127
    ('grid.', '\\input{figures_main/circle-two-qubit.tex}'),  # after "grid." at line ~134
    ('structure.', '\\input{figures_main/dcn-2qubit.tex}'),  # after "structure." at line ~154
    ('qubits.', '\\input{figures_main/dcn-3qubit.tex}'),  # after "qubits." at line ~158
    ('tree.', '\\input{figures_main/phase-space-torus.tex}'),  # after "tree." at line ~244
    ('blob.', '\\input{figures_main/wigner-function.tex}'),  # after "blob." at line ~246
    ('sphere.', '\\input{figures_main/poincare-sphere.tex}'),  # after "sphere." at line ~248
    ('states.', '\\input{figures_main/hypertree.tex}'),  # after "states." at line ~250
    ('space.', '\\input{figures_main/entanglement-landscape.tex}'),  # after "space." at line ~252
    ('landscape.', '\\input{figures_main/graph-state-construction.tex}'),  # after "landscape." at line ~289
    ('cluster.', '\\input{figures_main/cluster-state.tex}'),  # after "cluster." at line ~303
    ('graph.', '\\input{figures_main/star-graph.tex}'),  # after "graph." at line ~305
    ('operation.', '\\input{figures_main/local-complementation.tex}'),  # after "operation." at line ~319
    ('group.', '\\input{figures_main/stabilizer-generators.tex}'),  # after "group." at line ~340
    ('states.', '\\input{figures_main/ghz-graph-equivalence.tex}'),  # after "states." at line ~342
    ('hypergraph.', '\\input{figures_main/hypergraph-basic.tex}'),  # after "hypergraph." at line ~404
    ('states.', '\\input{figures_main/ghz-hypergraph.tex}'),  # after "states." at line ~406
    ('network.', '\\input{figures_main/lattice-hypergraph.tex}'),  # after "network." at line ~408
    ('network.', '\\input{figures_main/tree-tensor-network.tex}'),  # after "network." at line ~410
    ('states.', '\\input{figures_main/zx-bell-state.tex}'),  # after "states." at line ~412
    ('fusion.', '\\input{figures_main/zx-spider-fusion.tex}'),  # after "fusion." at line ~414
    ('states.', '\\input{figures_main/zx-graph-state.tex}'),  # after "states." at line ~416
    ('W.', '\\input{figures_main/zw-w-spider.tex}'),  # after "W." at line ~467
    ('classes.', '\\input{figures_main/zw-ghz-vs-w.tex}'),  # after "classes." at line ~469
    ('states.', '\\input{figures_main/zw-z-vs-w.tex}'),  # after "states." at line ~471
    ('3qubit.', '\\input{figures_main/entanglement-polytope-3qubit.tex}'),  # after "3qubit." at line ~511
    ('position.', '\\input{figures_main/entanglement-polytope-position.tex}'),  # after "position." at line ~513
    ('visualization.', '\\input{figures_main/negativity-visualization.tex}'),  # after "visualization." at line ~558
    ('inequality.', '\\input{figures_main/ckw-inequality.tex}'),  # after "inequality." at line ~560
    ('measure.', '\\input{figures_main/triangle-measure.tex}'),  # after "measure." at line ~562
]

# Insert figure inputs
new_lines = lines.copy()
offset = 0

for context, input_cmd in insertions:
    found = False
    for i, line in enumerate(new_lines):
        if context in line.strip():
            # Insert after this line
            new_lines.insert(i + 1 + offset, input_cmd + '\n')
            offset += 1
            found = True
            break
    if not found:
        print(f"Warning: Context '{context}' not found")

# Write the result
with open('main_new.tex', 'w') as f:
    f.writelines(new_lines)

print(f"Created main_new.tex with {len(new_lines)} lines")
print(f"Inserted {len(insertions)} figure inputs")

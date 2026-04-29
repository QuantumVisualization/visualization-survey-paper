#!/usr/bin/env python3
import re

# Read main.tex
with open('main.tex', 'r') as f:
    content = f.read()

# Find all figure environments and their labels
# Pattern: \begin{figure}...\label{fig:xxx}...\end{figure}
figure_pattern = r'\\begin\{figure\}\[htbp\]\*\n(.*?\\label\{(fig:[^}]*)\}.*?\\end\{figure\}'

# We need to be careful with multiline matching
# Let's use a different approach - find each \begin{figure} and matching \end{figure}
lines = content.split('\n')
i = 0
new_lines = []
figures_to_replace = []

while i < len(lines):
    line = lines[i]
    if '\\begin{figure}[htbp]' in line or '\\begin{figure}' in line:
        # Found start of figure
        fig_start = i
        # Find the matching \end{figure}
        j = i
        while j < len(lines):
            if '\\end{figure}' in lines[j]:
                fig_end = j
                break
            j += 1
        
        # Extract the figure block
        figure_block = '\n'.join(lines[fig_start:fig_end+1])
        
        # Extract the label
        label_match = re.search(r'\\label\{(fig:[^}]*)\}', figure_block)
        if label_match:
            label = label_match.group(1)
            filename = label.replace('fig:', '') + '.tex'
            figures_to_replace.append((fig_start, fig_end, filename))
            # Add the input command instead
            indent = lines[fig_start][:len(lines[fig_start]) - len(lines[fig_start].lstrip())
            new_lines.append(indent + '\\input{figures/' + filename + '}')
        else:
            # No label found, keep original
            new_lines.extend(lines[fig_start:fig_end+1])
        
        i = fig_end + 1
    else:
        new_lines.append(line)
        i += 1

# Write back
with open('main.tex', 'w') as f:
    f.write('\n'.join(new_lines))

print(f"Replaced {len(figures_to_replace)} figures with input commands")
for start, end, filename in figures_to_replace:
    print(f"  - {filename}")

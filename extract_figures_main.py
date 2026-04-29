#!/usr/bin/env python3
import re
import os

# Read main.tex
with open('main.tex', 'r') as f:
    lines = f.readlines()

output_lines = []
i = 0
figure_count = 0

while i < len(lines):
    line = lines[i]
    # Detect start of figure environment
    if re.search(r'\\begin\{figure', line):
        # Found figure start
        figure_start = i
        # Find matching \end{figure}
        j = i
        while j < len(lines):
            if r'\end{figure}' in lines[j]:
                figure_end = j
                break
            j += 1
        else:
            # No end found, just append and break
            output_lines.extend(lines[i:])
            break
        
        # Extract figure block
        figure_block = ''.join(lines[figure_start:figure_end+1])
        
        # Extract label
        label_match = re.search(r'\\label\{(fig:[^}]+)\}', figure_block)
        if label_match:
            label = label_match.group(1)
            # Remove 'fig:' prefix and convert to filename
            filename = label.replace('fig:', '').replace('-', '-') + '.tex'
            # Clean filename (remove any special chars, but keep it simple)
            filename = re.sub(r'[^a-zA-Z0-9_\-\.]', '', filename)
            # Write figure to figures_main/
            figure_file = os.path.join('figures_main', filename)
            with open(figure_file, 'w') as f:
                f.write(figure_block)
            figure_count += 1
            print(f"Extracted {filename}")
            # Replace with \input{figures_main/filename}
            indent = line[:len(line) - len(line.lstrip())]  # preserve indentation
            output_lines.append(indent + '\\input{figures_main/' + filename + '}\n')
        else:
            # No label, keep original
            output_lines.extend(lines[figure_start:figure_end+1])
        
        i = figure_end + 1
    else:
        output_lines.append(line)
        i += 1

# Write updated main.tex
with open('main.tex', 'w') as f:
    f.writelines(output_lines)

print(f"\nDone! Extracted {figure_count} figures to figures_main/")
print("Updated main.tex with \\input{} commands")

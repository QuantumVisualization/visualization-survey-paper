#!/usr/bin/env python3
import re

# Read original main.tex
with open('main.tex', 'r') as f:
    lines = f.readlines()

# Find the line numbers for \begin{document} and \end{document}
begin_doc = None
end_doc = None
for i, line in enumerate(lines):
    if '\\begin{document}' in line or '\\begin{document}' in line or 'begin{document}' in line:
        begin_doc = i
    if '\\end{document}' in line:
        end_doc = i

print(f"begin_document at line {begin_doc}")
print(f"end_document at line {end_doc}")

# Extract preamble (lines 0 to begin_doc)
preamble = lines[:begin_doc]
# Extract body (lines begin_doc+1 to end_doc)
body = lines[begin_doc+1:end_doc]

# Fix the \begin{document} line
preamble[-1] = '\\begin{document}\n'

# Remove all figure inputs from body
clean_body = []
for line in body:
    # Skip lines with \input{figures_main or input{figures_main
    if '\\input{figures_main' in line or 'input{figures_main' in line:
        continue
    clean_body.append(line)

# Write new main_fixed.tex
with open('main_fixed.tex', 'w') as f:
    f.writelines(preamble)
    f.writelines(clean_body)

print("Created main_fixed.tex without figure inputs")
print(f"Preamble lines: {len(preamble)}")
print(f"Body lines: {len(clean_body)}")

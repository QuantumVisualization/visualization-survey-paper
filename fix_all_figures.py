#!/usr/bin/env python3
import re
import os

figures_dir = "figures"

for filename in sorted(os.listdir(figures_dir)):
    if not filename.endswith('.tex'):
        continue
    
    filepath = os.path.join(figures_dir, filename)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Find all nodes that are explanatory boxes
    # Pattern: \node[options] at (coord) { \begin{minipage}...\end{minipage} };
    # Or: \node[options] at (coord) { text };
    
    # We'll search for nodes with "rounded corners" and "fill=" (colored boxes)
    # and also nodes with "draw=none" that contain tabular
    
    # Strategy: find all \node[...] at (...) {...} patterns that span multiple lines
    # We'll use a state machine to parse.
    
    lines = content.split('\n')
    new_lines = []
    i = 0
    box_texts = []
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line starts a node that might be an explanatory box
        node_match = re.search(r'\\node$$([^]]*)$$\s*at\s*$$([^]]*)$$\s*\{', line)
        if node_match:
            options = node_match.group(1)
            # Check if it has rounded corners and fill= (colored box) or is a legend
            if ('rounded corners' in options and 'fill=' in options) or \
               ('draw=none' in options and 'fill=none' in options):
                # This is likely an explanatory box
                # Collect all lines until we find the matching closing brace
                node_lines = [line]
                brace_count = line.count('{') - line.count('}')
                j = i + 1
                while j < len(lines) and brace_count > 0:
                    node_lines.append(lines[j])
                    brace_count += lines[j].count('{') - lines[j].count('}')
                    j += 1
                
                # Now node_lines contains the full node
                node_text = '\n'.join(node_lines)
                
                # Extract text content: look for \begin{minipage}...\end{minipage} or \begin{tabular}...\end{tabular}
                # Or just extract everything between outer braces
                # Try to get the text inside the node (after the coordinate)
                # We'll search for \begin{minipage} or \begin{tabular}
                minipage_match = re.search(r'\\begin{minipage}[^}]*\}(.*?)\\end{minipage}', node_text, re.DOTALL)
                tabular_match = re.search(r'\\begin{tabular}[^}]*\}(.*?)\\end{tabular}', node_text, re.DOTALL)
                
                extracted = ""
                if minipage_match:
                    extracted = minipage_match.group(1).strip()
                elif tabular_match:
                    extracted = tabular_match.group(1).strip()
                else:
                    # Try to get text between { and } (but careful with nested)
                    # Simple: remove the node command part
                    # We'll just skip for now
                    pass
                
                if extracted:
                    # Clean up LaTeX commands
                    # Remove \textbf{...} keep inner
                    extracted = re.sub(r'\\textbf\{([^}]*)\}', r'\1', extracted)
                    # Remove \vspace{...}
                    extracted = re.sub(r'\\vspace\{[^}]*\}', '', extracted)
                    # Remove \hspace{...}
                    extracted = re.sub(r'\\hspace\{[^}]*\}', ' ', extracted)
                    # Remove \\ (newline in tabular)
                    extracted = re.sub(r'\s*\\\\\s*', ' ', extracted)
                    # Remove multiple spaces
                    extracted = re.sub(r'\s+', ' ', extracted).strip()
                    box_texts.append(extracted)
                
                # Skip these lines (don't add to new_lines)
                i = j
                continue
        
        new_lines.append(line)
        i += 1
    
    # Now update caption if we extracted any text
    if box_texts:
        new_content = '\n'.join(new_lines)
        # Find caption
        caption_match = re.search(r'(\\caption\{)(.*?)(\}\s*\\label)', new_content, re.DOTALL)
        if caption_match:
            old_caption = caption_match.group(2)
            # Append box texts
            additional = ' '.join(box_texts)
            # Clean additional
            additional = re.sub(r'\s+', ' ', additional).strip()
            new_caption_text = old_caption + ' ' + additional
            # Replace
            new_content = new_content.replace(
                caption_match.group(0),
                caption_match.group(1) + new_caption_text + caption_match.group(3)
            )
        
        # Write back
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filename}: removed {len(box_texts)} box(es)")
    else:
        # Check if there are still any box nodes (maybe different pattern)
        # For now, just report
        if 'rounded corners' in content and 'fill=yellow' in content or 'fill=green' in content or 'fill=gray' in content:
            print(f"WARNING: {filename} may still have boxes")
        else:
            print(f"OK: {filename}")

print("\nDone!")

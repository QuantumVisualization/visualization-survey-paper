#!/usr/bin/env python3
import re
import os

figures_dir = "figures"

# Process each .tex file in the figures directory
for filename in sorted(os.listdir(figures_dir)):
    if not filename.endswith('.tex'):
        continue
    
    filepath = os.path.join(figures_dir, filename)
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find all explanatory box nodes (yellow, green, gray, purple, blue, etc.)
    # Pattern matches \node[draw, rounded corners, fill=COLOR!XX, ...] at (...,...){
    # Also matches tabular legends without fill color
    
    boxes_to_remove = []
    box_texts = []
    
    # Pattern for nodes with fill colors (yellow, green, gray, purple, blue)
    pattern = r'\\node$$draw[^]]*, rounded corners[^]]*, fill=(?:yellow|green|gray|purple|blue)!\d+[^]]*$$\s*at\s*$$[^]]*$$\s*\{\s*\\begin\{(minipage|tabular)\}'
    
    # Let me use a simpler approach - find nodes with fill=yellow, fill=green, etc.
    lines = content.split('\n')
    new_lines = []
    skip_until_end = False
    brace_count = 0
    current_box_text = ""
    in_box = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect start of explanatory box node
        if re.search(r'\\node$$[^]]*fill=(?:yellow|green|gray|purple|blue)!\d+[^]]*$$\s*at', line) or \
           (re.search(r'\\node$$draw=none[^]]*$$\s*at', line) and 'tabular' in content[max(0,i-5):i+20]):
            
            # Extract the text from this node
            # Find the opening brace and get all text until matching closing brace
            full_text = ""
            j = i
            brace_depth = 0
            found_open = False
            
            while j < len(lines):
                full_text += lines[j] + '\n'
                if '{' in lines[j] and not found_open:
                    brace_depth = lines[j].count('{') - lines[j].count('}')
                    found_open = True
                elif found_open:
                    brace_depth += lines[j].count('{') - lines[j].count('}')
                
                if found_open and brace_depth <= 0:
                    break
                j += 1
            
            # Extract just the text content (remove node wrapper)
            box_content = '\n'.join(lines[i:j+1])
            
            # Extract text between { and matching }
            # Remove \begin{minipage}...\end{minipage} or \begin{tabular}...\end{tabular}
            text_match = re.search(r'\\begin\{(minipage|tabular)\}[^}]*\}(.*?)\\end\{\1\}', box_content, re.DOTALL)
            if text_match:
                extracted_text = text_match.group(2).strip()
                # Clean up LaTeX commands for caption
                extracted_text = re.sub(r'\\textsf\{', '', extracted_text)
                extracted_text = re.sub(r'\\textbf\{(.*?)\}', r'\\textbf{\1}', extracted_text)
                extracted_text = re.sub(r'\\vspace\{[^}]*\}', '', extracted_text)
                extracted_text = re.sub(r'\\hspace\{[^}]*\}', ' ', extracted_text)
                extracted_text = re.sub(r'\\\\\$$', ' ', extracted_text)
                extracted_text = re.sub(r'\s+', ' ', extracted_text).strip()
                box_texts.append(extracted_text)
            
            # Skip all lines of this node
            i = j + 1
            continue
        
        # Check for \node[draw, rounded corners, fill=color with text width pattern
        if re.search(r'fill=(?:yellow|green|gray|purple|blue)!\d+.*text width', line):
            # This is a box node - find its content
            full_block = ""
            j = i
            while j < len(lines):
                full_block += lines[j] + '\n'
                if '};' in lines[j]:
                    break
                j += 1
            
            # Extract text from \textbf{} or other content
            text_match = re.search(r'\\textbf\{([^}]*)\}', full_block)
            if text_match:
                box_texts.append(text_match.group(1))
            
            i = j + 1
            continue
        
        new_lines.append(line)
        i += 1
    
    # Now update the caption with box texts
    new_content = '\n'.join(new_lines)
    
    if box_texts:
        # Find the \caption{...} and append box text
        caption_match = re.search(r'\\caption\{(.*?)\}\\s*\\label', new_content, re.DOTALL)
        if caption_match:
            old_caption = caption_match.group(1)
            # Append box texts to caption
            additional = ' '.join(box_texts)
            # Clean up the additional text
            additional = re.sub(r'\s+', ' ', additional).strip()
            
            # Replace the caption
            new_caption = f'\\caption{{{old_caption} {additional}}}'
            new_content = new_content.replace(
                f'\\caption{{{old_caption}}}',
                new_caption
            )
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(new_content)
    
    if box_texts:
        print(f"Processed {filename}: removed {len(box_texts)} box(es), added to caption")
    else:
        print(f"Processed {filename}: no boxes found")

print("\nDone! All figures processed.")

# AGENTS.md - Guidelines for visualization-survey-paper

## Project Overview

A LaTeX literature survey on visualization of quantum entanglement.

## Files

```
visualization-survey-paper/
├── quantum-entanglement-visualization-survey.tex  # Main LaTeX
├── quantum-entanglement-visualization-survey.aux    # Auto-generated
├── quantum-entanglement-visualization-survey.toc   # Table of contents
├── quantum-entanglement-visualization-survey.pdf    # Compiled PDF
├── quantum-entanglement-visualization-survey.out     # Build output
├── quantum-entanglement-visualization-survey.log   # Build log
└── *.bak*                                      # Backups
```

## Building

### pdflatex (direct)

```bash
cd visualization-survey-paper
pdflatex quantum-entanglement-visualization-survey
pdflatex quantum-entanglement-visualization-survey  # Run twice for TOC
```

### latexmk

```bash
latexmk -pdf quantum-entanglement-visualization-survey.tex
latexmk -c    # Clean aux files
```

## Document Structure

Uses standard `article` class with custom packages:
- `geometry` (page layout)
- `tikz` (figures)
- `physics` (physics notation)
- `hyperref` (cross-references)
- `cleveref` (smart references)

## Sections

| Section | Purpose |
|---------|---------|
| Abstract | Standalone summary (150-300 words) |
| Keywords | Comma-separated terms |
| Intro | Motivation, scope, contribution |
| Geometric Methods | Bloch sphere, state city, etc. |
| Graph-Based | ZX/ZW calculus, entanglement graphs |
| Algebraic | Matrix representations |
| Classification | Polytopes, measures |
| Specialized States | Dicke, stabilizer, etc. |
| Conclusion | Summary, future directions |
| References | Bibliography |

## Literature Review Guidelines

1. **Source primary literature**: arXiv, Phys Rev, etc.
2. **Organize by method**: Group related work
3. **Compare approaches**: Table of features
4. **Identify gaps**: What's missing

## Figures

TikZ-based or PNG. Place in directory:

```latex
\begin{figure}[ht]
  \centering
  \includegraphics[width=0.8\linewidth]{ fig-name .png}
  \caption{Description.}
  \label{fig:label}
\end{figure}
```

## Cross-References

```latex
\section{Introduction}
\label{sec:intro}

See Section~\ref{sec:intro} or Figure~\ref{fig:example}.
```

## Backup Files

`*.bak*` files are automatic backups. Safe to delete:

```bash
rm quantum-entanglement-visualization-survey.bak*
```

## Related Projects

- **quantumviz/**: Implementation examples
- **quantumviz-paper/**: Case study reference

## Submission

This is a survey paper, likely for an journal or arXiv preprint. No specific class required - uses standard `article`.
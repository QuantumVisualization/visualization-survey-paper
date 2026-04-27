# CONTEXT.md - visualization-survey-paper Context

## What This Paper Is

A **comprehensive literature survey** on visualization methods for quantum entanglement. It covers over 70 references across geometric, graph-based, algebraic, and categorical approaches.

## Focus

Survey of visualization techniques for quantum entanglement, particularly **multipartite entanglement** where visualization challenges are most acute due to exponential growth of the state space.

## Key Topics Covered

### Geometric Methods
- Bloch sphere (single qubit)
- State city / density matrices (multi-qubit)
- Majorana representation

### Graph-Based Methods
- Graph states
- Hypergraph representations
- ZX calculus
- ZW calculus

### Algebraic / Categorical Methods
- Matrix representations
- Tensor network visualizations

### Classification Methods
- Entanglement polytopes
- Entanglement measures

### Specialized States
- Dicke states
- Stabilizer states
- Symmetric states

## Target Audience

- Quantum information researchers
- Educators developing intuition
- Developers building visualization tools

## Relationship to Other Work

| Project | Relationship |
|---------|--------------|
| **quantumviz** | Implementation examples cited |
| **paper-scipost-physics-codebases** | Technical case study |

## Key Argument

The survey argues that effective visualization is crucial for:
1. Building intuition about quantum phenomena
2. Debugging quantum circuits
3. Understanding complex quantum protocols
4. Communicating quantum concepts

## References

Survey references major works:
- Graph states (Hein et al.)
- ZX calculus (Coecke, Kissinger)
- Entanglement polytopes (Viehmann et al.)
- Majorana representation

## Figures Included

Several TikZ-based figures showing:
- Bloch sphere geometry
- Graph state examples
- ZX-diagram transformations
- Entanglement polytopes

## Related Papers

This survey provides the **background** for the scipost paper.

The **scipost paper** (quantumviz as codebase) should cite this survey for context on why visualization matters in quantum computing.

## Future Directions

Areas identified for future work:
- Better multi-qubit visualizations
- Real-time circuit visualization
- Integration with quantum simulators
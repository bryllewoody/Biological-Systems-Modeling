# Project 2: Biological and Ecological Modeling Suite

Multi-language implementation of biological systems, demonstrating computational approaches to modeling life sciences phenomena across different scales and domains.

## Implementation Components

### Perl Bacterial Dynamics (`perl_bacterial_dynamics/bacterial_growth.pl`)
**Purpose**: Exponential bacterial growth simulation
- **Model**: N(t) = N₀ × e^(μt)
- **Features**:
  - Time-series simulation over 50 minutes
  - Growth rate parameter μ = 0.092 min⁻¹
  - Tabular output with formatted display
  - Exponential growth kinetics
- **Applications**: Microbiology, bioprocess engineering, population dynamics

### Python Data Analysis (`python_data_analysis/uf_csi.py`)
**Purpose**: Newton's Law of Cooling for forensic analysis
- **Model**: T(t) = C + (T₀ - C) × e^(-kt)
- **Features**:
  - Inverse problem solving (time of death estimation)
  - Scientific visualization with matplotlib
  - Parameter fitting and model validation
  - Real-world forensic application
- **Applications**: Forensic science, heat transfer, temperature modeling

### R Enzyme Kinetics (`r_enzyme_kinetics/michaelis_menten.R`)
**Purpose**: Michaelis-Menten enzyme kinetics modeling
- **Model**: v = (Vₘₐₓ × [S]) / (Kₘ + [S])
- **Features**:
  - Substrate concentration sweep (0-80 mM)
  - Kinetic parameter visualization
  - Publication-quality plots
  - Biochemical parameter analysis
- **Applications**: Biochemistry, enzymology, drug development

### System Dynamics Models (`system_dynamics_models/`)
**Purpose**: Complex systems modeling using VenSim
- **Features**:
  - Prey-predator ecosystem dynamics
  - Population interaction modeling
  - Feedback loop analysis
  - System behavior over time
- **Applications**: Ecology, systems biology, conservation

## Scientific Domains Covered

### 1. **Microbiology & Growth Dynamics**
- Exponential growth patterns
- Population doubling times
- Environmental parameter effects
- Scale-up considerations

### 2. **Thermodynamics & Heat Transfer**
- Newton's Law of Cooling applications
- Parameter estimation techniques
- Inverse problem methodology
- Forensic applications

### 3. **Biochemistry & Enzyme Kinetics**
- Michaelis-Menten equation
- Enzyme-substrate interactions
- Kinetic parameter determination
- Metabolic pathway analysis

### 4. **Ecological Systems**
- Population interactions
- Predator-prey dynamics
- System feedback mechanisms
- Stability analysis

## Computational Approaches

### Data Analysis Pipeline
1. **Model Definition**: Mathematical formulation of biological processes
2. **Parameter Estimation**: Fitting models to experimental data
3. **Simulation**: Forward modeling and prediction
4. **Visualization**: Scientific plotting and data presentation
5. **Validation**: Model verification and sensitivity analysis

### Language-Specific Strengths
- **Perl**: Text processing, bioinformatics pipelines
- **Python**: Scientific computing, data analysis, visualization
- **R**: Statistical modeling, biostatistics, specialized packages
- **VenSim**: System dynamics, complex systems modeling

## Usage Instructions

```bash
# Perl - Bacterial Growth
perl bacterial_growth.pl

# Python - CSI Analysis (requires numpy, matplotlib)
python uf_csi.py

# R - Enzyme Kinetics
Rscript michaelis_menten.R

# VenSim - Load .mdl files in VenSim software
```

## Dependencies

- **Python**: numpy, matplotlib
- **R**: Base R (png graphics)
- **Perl**: Core Perl modules
- **VenSim**: VenSim modeling software

## Research Applications

This suite demonstrates computational modeling techniques applicable to:
- **Bioprocess Engineering**: Fermentation optimization
- **Pharmacokinetics**: Drug metabolism modeling
- **Environmental Science**: Population dynamics
- **Forensic Science**: Time of death determination
- **Systems Biology**: Network analysis and modeling
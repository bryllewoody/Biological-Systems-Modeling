# Project 3: Numerical Methods and Population Dynamics

Advanced computational modeling project focusing on numerical integration methods, comparative analysis, and population growth modeling with comprehensive error quantification.

## Project Structure

### Algorithms (`algorithms/`)

#### Euler Method Implementation (`euler_method.py`)
**Purpose**: First-order numerical integration with comprehensive analysis
- **Features**:
  - Forward Euler implementation
  - High-resolution time series (dt = 0.1)
  - Error analysis vs analytical solution
  - CSV output for further analysis
  - Comparative visualization

#### Runge-Kutta Implementation (`runge_kutta.py`)
**Purpose**: Fourth-order numerical integration for high accuracy
- **Features**:
  - RK4 algorithm implementation
  - Optimal time step analysis
  - Precision matching studies
  - Convergence analysis
  - Error minimization

### Comparative Analysis (`comparative_analysis/`)

#### Method Comparison (`method_comparison.py`)
**Purpose**: Comprehensive comparison of numerical integration methods
- **Methods Analyzed**:
  - Analytical solution (exact)
  - Euler method (1st order)
  - Improved Euler method (2nd order)
  - Runge-Kutta 4th order (4th order)
- **Analysis Features**:
  - Side-by-side comparison tables
  - Error quantification
  - Convergence rate analysis
  - Method stability assessment

### Visualizations (`visualizations/`)

#### Simple Overlay Plotting (`plot_overlay.py`)
**Purpose**: Basic visualization of method comparison
- **Features**:
  - Population growth curves
  - Method overlay plots
  - Statistical summary
  - Publication-ready output

#### Advanced Scientific Plotting (`advanced_plotting.py`)
**Purpose**: Publication-quality visualization and analysis
- **Features**:
  - Multi-panel figure layouts
  - Error analysis subplots
  - Annotation and insights
  - Professional formatting
  - Statistical annotations

## Mathematical Foundation

### Population Growth Model
**Differential Equation**: dN/dt = kN
**Analytical Solution**: N(t) = N₀e^(kt)

### Parameters
- **N₀**: 10.0 (initial population)
- **k**: 0.10 (growth rate)
- **dt**: 0.1 (default time step)
- **T**: 30.0 (simulation time)

### Numerical Methods

#### 1. Euler Method (1st Order)
```
N_{n+1} = N_n + k × N_n × dt
```
- **Advantages**: Simple implementation
- **Disadvantages**: Lower accuracy, potential instability

#### 2. Improved Euler Method (2nd Order)
```
k₁ = k × N_n × dt
k₂ = k × (N_n + k₁) × dt
N_{n+1} = N_n + 0.5(k₁ + k₂)
```
- **Advantages**: Better accuracy than Euler
- **Trade-offs**: More computation per step

#### 3. Runge-Kutta 4th Order
```
k₁ = k × N_n × dt
k₂ = k × (N_n + 0.5k₁) × dt
k₃ = k × (N_n + 0.5k₂) × dt
k₄ = k × (N_n + k₃) × dt
N_{n+1} = N_n + (k₁ + 2k₂ + 2k₃ + k₄)/6
```
- **Advantages**: High accuracy, stability
- **Trade-offs**: Computational complexity

## Error Analysis

### Types of Error Analyzed
1. **Absolute Error**: |Numerical - Analytical|
2. **Relative Error**: |Numerical - Analytical|/|Analytical| × 100%
3. **Cumulative Error**: Error growth over time
4. **Convergence Rate**: Error reduction with smaller time steps

### Key Findings
- **RK4**: Superior accuracy for given time step
- **Improved Euler**: Good balance of accuracy and efficiency  
- **Euler**: Simple but requires very small time steps for accuracy
- **Stability**: RK4 most stable for larger time steps

## Output Files

### Data Files
- `exercise_5_5_results.csv`: Complete numerical results
- `exercise_5_6_results.csv`: Time step sensitivity analysis

### Visualization Files
- `exercise_5_5_comparison.png`: Method comparison plots
- `exercise_5_5_errors.png`: Error analysis plots
- `population_comparison.png`: Advanced comparison visualization
- `relative_error.png`: Relative error analysis

## Usage Instructions

### Running Individual Components
```bash
# Algorithm implementations
python algorithms/euler_method.py
python algorithms/runge_kutta.py

# Comparative analysis
python comparative_analysis/method_comparison.py

# Visualization
python visualizations/plot_overlay.py
python visualizations/advanced_plotting.py
```

### Dependencies
```bash
pip install numpy matplotlib pandas csv
```

## Research Applications

### Engineering Applications
- **Control Systems**: System response analysis
- **Fluid Dynamics**: Flow modeling
- **Heat Transfer**: Temperature distribution
- **Structural Analysis**: Dynamic response

### Biological Applications
- **Population Dynamics**: Species growth modeling
- **Epidemiology**: Disease spread simulation
- **Pharmacokinetics**: Drug concentration modeling
- **Ecosystem Modeling**: Predator-prey interactions

### Computational Considerations
- **Accuracy vs Speed**: Method selection based on requirements
- **Stability**: Choosing appropriate time steps
- **Convergence**: Ensuring numerical solutions approach analytical
- **Validation**: Comparing against known solutions

This project provides a comprehensive framework for understanding numerical methods in computational modeling, with applications spanning engineering, biology, and physical sciences.
# Project 1: Multi-Language Programming Framework

This project demonstrates cross-platform programming capabilities across different languages, showcasing various computational paradigms and language-specific strengths.

## Language Implementations

### Fortran (`fortran/fibonacci.f90`)
**Purpose**: High-performance Fibonacci sequence calculator
- **Features**: 
  - Dynamic memory allocation
  - User input validation
  - Efficient iterative algorithm
  - Scientific computing standards
- **Usage**: Compile with gfortran and run for interactive Fibonacci generation

### Java (`java/PalindromeChecker.java`)
**Purpose**: Object-oriented palindrome checker with robust string handling
- **Features**:
  - Two-pointer algorithm for efficiency
  - Input sanitization (removes non-alphabetic characters)
  - Case-insensitive comparison
  - Resource management with Scanner
- **Usage**: Compile with javac and run for interactive palindrome checking

### Perl (`perl/factorial_calculator.pl`)
**Purpose**: Efficient factorial calculator optimized for large numbers
- **Features**:
  - Recursive implementation
  - Input validation with regular expressions
  - Error handling for invalid inputs
  - Perl's built-in arbitrary precision arithmetic
- **Usage**: Run directly with perl interpreter

### Python (`python/prime_checker.py`)
**Purpose**: Prime number checker with algorithmic optimization
- **Features**:
  - File-based input/output processing
  - Optimized trial division (checks up to √n)
  - Mixed data type handling (floats/integers)
  - Comprehensive error handling
- **Usage**: Requires input file `numbers.txt`, outputs to `results.txt`

### R (`r/dice_sim.R`)
**Purpose**: Statistical dice simulation with probability analysis
- **Features**:
  - Monte Carlo simulation of three dice rolls
  - Statistical frequency analysis
  - Data visualization with barplots
  - Probability distribution calculation
  - PNG output for publication
- **Usage**: Run in R environment, creates `dice_plot.png`

## Key Learning Outcomes

1. **Language Paradigms**: Comparison of imperative (Fortran), object-oriented (Java), scripting (Perl, Python), and statistical (R) approaches
2. **Performance Characteristics**: Understanding computational efficiency across different languages
3. **Memory Management**: From manual (Fortran) to automatic (Python/R) memory handling
4. **I/O Patterns**: Different approaches to user interaction and file processing
5. **Error Handling**: Language-specific approaches to validation and exception management

## Running the Examples

Each language implementation is self-contained and can be run independently:

```bash
# Fortran
gfortran fibonacci.f90 -o fibonacci
./fibonacci

# Java  
javac PalindromeChecker.java
java PalindromeChecker

# Perl
perl factorial_calculator.pl

# Python (create numbers.txt first)
python prime_checker.py

# R
Rscript dice_sim.R
```
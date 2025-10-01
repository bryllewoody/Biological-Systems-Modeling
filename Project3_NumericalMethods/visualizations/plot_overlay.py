#!/usr/bin/env python3
"""
Simple overlay plot of Euler vs RK4 population data
"""

import pandas as pd
import matplotlib.pyplot as plt

# Configure matplotlib for clean appearance
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.figsize': [10, 6]

})

def plot_overlay(filename='vensim.txt'):
    """Create overlay plot of Euler vs RK4 methods"""
    
    # Load data
    df = pd.read_csv(filename, sep='\t')
    df.columns = df.columns.str.strip()
    
    # Create the plot
    plt.figure()
    
    # Plot both methods
    plt.plot(df['Time (Year)'], df['Population : euler'], 
             'b-', linewidth=2, label='Euler Method', alpha=0.8)
    plt.plot(df['Time (Year)'], df['Population : rk4'], 
             'r--', linewidth=2, label='RK4 Method', alpha=0.8)
    
    # Labels and formatting
    plt.xlabel('Time (Years)')
    plt.ylabel('Population')
    plt.title('Population Growth: Euler vs RK4 Methods')
    plt.legend()
    
    # Save the plot
    plt.savefig('population_overlay.png', dpi=300, bbox_inches='tight')
    plt.savefig('population_overlay.pdf', bbox_inches='tight')
    
    # Show statistics
    final_euler = df['Population : euler'].iloc[-1]
    final_rk4 = df['Population : rk4'].iloc[-1]
    difference = final_rk4 - final_euler
    
    print(f"Data points loaded: {len(df)}")
    print(f"Final Population (Euler): {final_euler:.3f}")
    print(f"Final Population (RK4): {final_rk4:.3f}")
    print(f"Difference: {difference:.3f}")
    print(f"Plot saved as 'population_overlay.png' and 'population_overlay.pdf'")
    
    plt.show()

if __name__ == "__main__":
    plot_overlay()
#!/usr/bin/env python3
"""
Plot Vensim population data comparing Euler and RK4 methods
with publication-quality formatting (LaTeX-style without requiring LaTeX)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure matplotlib for publication-quality output
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'legend.fontsize': 12,
    'figure.titlesize': 16,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'axes.axisbelow': True,
    'figure.dpi': 100,
    'savefig.dpi': 300,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 1.2,
    'xtick.major.width': 1.2,
    'ytick.major.width': 1.2
})

def load_vensim_data(filename):
    """Load data from Vensim text file"""
    # Read the tab-separated data
    df = pd.read_csv(filename, sep='\t')
    
    # Clean column names (remove extra spaces)
    df.columns = df.columns.str.strip()
    
    return df

def plot_comparison(df):
    """Create comparison plot of Euler vs RK4 methods"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # Color scheme
    euler_color = '#1f77b4'  # Blue
    rk4_color = '#d62728'    # Red
    diff_color = '#2ca02c'   # Green
    
    # Main comparison plot
    ax1.plot(df['Time (Year)'], df['Population : euler'], 
             color=euler_color, linewidth=2.5, label='Euler Method', alpha=0.9)
    ax1.plot(df['Time (Year)'], df['Population : rk4'], 
             color=rk4_color, linewidth=2, linestyle='--', label='RK4 Method', alpha=0.9)
    
    ax1.set_xlabel('Time (Years)')
    ax1.set_ylabel('Population')
    ax1.set_title('Population Growth: Euler vs RK4 Methods')
    ax1.legend(frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Error plot (difference between methods)
    error = df['Population : rk4'] - df['Population : euler']
    ax2.plot(df['Time (Year)'], error, color=diff_color, linewidth=2.5, label='RK4 - Euler')
    ax2.fill_between(df['Time (Year)'], error, alpha=0.3, color=diff_color)
    
    ax2.set_xlabel('Time (Years)')
    ax2.set_ylabel('Population Difference')
    ax2.set_title('Difference between RK4 and Euler Methods')
    ax2.legend(frameon=True, fancybox=True, shadow=True)
    ax2.grid(True, alpha=0.3, linestyle='-', linewidth=0.5)
    
    # Add annotations for key insights
    max_error_idx = error.abs().idxmax()
    max_error_time = df['Time (Year)'].iloc[max_error_idx]
    max_error_value = error.iloc[max_error_idx]
    
    ax2.annotate(f'Max difference: {max_error_value:.3f}\\nat t = {max_error_time:.1f} years',
                xy=(max_error_time, max_error_value),
                xytext=(max_error_time + 5, max_error_value + max_error_value*0.3),
                arrowprops=dict(arrowstyle='->', color='black', alpha=0.7),
                fontsize=10, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    return fig

def main():
    """Main function to run the plotting script"""
    # Load data
    filename = 'vensim.txt'
    
    try:
        df = load_vensim_data(filename)
        print(f"Successfully loaded {len(df)} data points from {filename}")
        print(f"Time range: {df['Time (Year)'].min():.1f} to {df['Time (Year)'].max():.1f} years")
        
        # Create plots
        print("\n🎨 Creating comparison plot...")
        fig1 = plot_comparison(df)
        fig1.savefig('population_comparison.png', bbox_inches='tight', 
                     facecolor='white', edgecolor='none')
        fig1.savefig('population_comparison.pdf', bbox_inches='tight')
        
        # Display plots
        plt.show()
        
        print(f"\n📈 Plots saved as:")
        print(f"  - population_comparison.png/pdf")
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find file '{filename}'")
        print("Make sure the file is in the same directory as this script.")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
#!/usr/bin/perl
use strict;
use warnings;

# Parameters
my $N0    = 2;       # Initial number of bacteria
my $mu    = 0.092;   # Growth constant (per minute)
my $t_max = 50;      # Simulation time in minutes

# Print header
printf "%-10s %-15s\n", "Time (min)", "Bacteria Count";

# Loop through each minute
for my $t (0 .. $t_max) {
    my $Nt = $N0 * exp($mu * $t);
    printf "%-10d %-15.4f\n", $t, $Nt;
}
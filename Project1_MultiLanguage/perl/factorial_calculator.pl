# factorial_calculator.pl
# Program to compute factorial of a number.

use strict;
use warnings;

sub factorial_calc {
    my ($n) = @_;
    return 1 if $n <= 1;
    return $n * factorial_calc($n - 1);
}

# Ask user for input
print "Enter a non-negative integer: ";
chomp(my $num = <STDIN>);

# Safety check
if ($num !~ /^\d+$/) {
    die "Error: Please enter a valid non-negative integer.\n";
}

# Calculate factorials
my $result = factorial_calc($num);

# Print results
print "Factorial of $num = $result\n";
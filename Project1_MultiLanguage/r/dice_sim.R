# dice_sim.R
# Program simulates rolling two dice N times.

# Ask user for N (number of rolls to simulate)
N <- as.integer(readline(prompt = "Enter number of dice rolls to simulate: "))

# Safety check: stop if input is not a positive integer
if (is.na(N) || N <= 0) {
  stop("Please enter a positive integer for the number of rolls.")
}

# Simulate the dice rolls:
# - die1 and die2 are random values between 1 and 6
die1 <- sample(1:6, N, replace = TRUE)
die2 <- sample(1:6, N, replace = TRUE)
die3 <- sample(1:6, N, replace = TRUE)

# Add the two dice to get the totals
totals <- die1 + die2 + die3

# Create a frequency table for totals
freq <- table(totals)

# Save a barplot of the frequencies as an image file
png("dice_plot.png")   # open PNG device (output file name)
barplot(freq, 
        main = paste("Dice Roll Totals (N =", N, ")"), 
        xlab = "Total", 
        ylab = "Frequency", 
        col = "skyblue")
dev.off()              # close PNG device (saves the file)

# Combine frequencies and probabilities in one table
results <- data.frame(
  Total = names(freq),
  Frequency = as.vector(freq),
  Probability = round(as.vector(prop.table(freq)), 3)
)

print(results, row.names = FALSE)
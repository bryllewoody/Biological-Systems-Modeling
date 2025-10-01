# Parameters
Km    <- 10           # mM
Vmax  <- 0.10         # mM / min

S     <- 0:80         # Substrate concentrations (mM)

v     <- ifelse(S == 0, 0, Vmax * S / (Km + S)) # Michaelis–Menten velocity (set v=0 at S=0 to avoid 0/0)

# Table
mm_table <- data.frame(S_mM = S, v_mM_per_min = round(v, 4))
print(head(mm_table, 10))

# Michaelis–Menten curve 
png("mm_curve.png", width = 900, height = 600, res = 120)
plot(S, v, type = "l", lwd = 3,
     xlab = "Substrate concentration [S] (mM)",
     ylab = "Initial velocity v (mM·min^-1)",
     main = "Michaelis–Menten Kinetics",)
abline(h = Vmax, lty = 2)                 # Vmax
abline(h = Vmax/2, v = Km, lty = 3)       # Vmax/2 at S = Km
text(Km, Vmax/2, labels = "Km", pos = 4, cex = 0.9)
dev.off()
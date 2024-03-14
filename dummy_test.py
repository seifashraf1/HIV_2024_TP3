import matplotlib.pyplot as plt

# Data
n_eval = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 
          950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 
          1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 
          2350, 2400, 2450, 2500, 2550]

f_min_values = [-6.428571E+00, -6.428571E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00,
                -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00, -6.571429E+00]

# Plot
plt.plot(n_eval, f_min_values, marker='o', linestyle='-')
plt.xlabel('n_eval')
plt.ylabel('f_min')
plt.title('Plot of n_eval vs f_min')
plt.grid(True)
plt.show()

# Build the labelled input-output table for the three-sector economy
import numpy as np
import pandas as pd

input_output = np.array([
    [0.2, 0.3, 0.1],  # Agriculture inputs
    [0.3, 0.2, 0.2],  # Manufacturing inputs
    [0.1, 0.2, 0.3]   # Services inputs
])

# Final demand vector (in billions)
final_demand = np.array([100, 150, 200])

# Calculate total output using Leontief inverse: x = (I - A)^{-1} * d
I = np.eye(3)
leontief_inverse = np.linalg.inv(I - input_output)
total_output = leontief_inverse @ final_demand

print("Input-Output Matrix:")
print(input_output)
print("\nLeontief Inverse:")
print(np.round(leontief_inverse, 3))
print("\nTotal Output Required (billions):")
print(np.round(total_output, 2))

# Label the same matrix so the axes carry economic meaning
sectors = ['Agriculture', 'Manufacturing', 'Services']
io_table = pd.DataFrame(input_output, index=sectors, columns=sectors)
io_table.index.name = 'using_sector'
io_table.columns.name = 'supplying_sector'
print(io_table)

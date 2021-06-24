# Importing user defined module
import day11mod
day11mod.list_1[1] = 2
print("Modified list:", day11mod.list_1)

# Importing pandas
import pandas as pd
df = pd.DataFrame({"State": ['Andhra Pradesh', 'Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
                   "Capital": ['Hyderabad', 'Mumbai', 'Bengaluru', 'Trivandrum', 'Chennai'],
                   "Literacy %": [89, 77, 82, 97, 85],
                   "Avg High Temp(c)": [33, 30, 29, 31, 32]})
print("\n", df)

# Importing random module and fetching a random number
import random
print("\n\nPicked random number is",random.randint(1, 100))

# Importing sys package and finding path
import sys
print("\nPath is:",sys.path)

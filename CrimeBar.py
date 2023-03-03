import pandas as pd
import matplotlib.pyplot as plt
fd=pd.read_csv("Crime Statistics Of Bangladesh.csv")
plt.bar(fd["Year"],fd["Total Cases"],label="Total Cases")
plt.xlabel("Year")
plt.ylabel("Crime Cases")
plt.legend()
plt.grid()
plt.show()

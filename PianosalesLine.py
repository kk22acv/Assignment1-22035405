import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("piano_salesone.csv")
plt.plot(df["YEAR"],df["VERTICAL PIANOS"],label="VERTICAL PIANOS")
plt.plot(df["YEAR"],df["GRAND PIANOS"],label="GRAND PIANOS")
plt.plot(df["YEAR"],df["ELECTRONIC"],label="ELECTRONIC")
plt.xlabel("Year")
plt.ylabel("Piano sales")
plt.legend()
plt.grid()
plt.show()

import matplotlib.pyplot as plt 
import pandas as pd
fd=pd.read_csv("CrimePIE.csv")
print(fd)
plt.figure(figsize=(30,10))
plt.pie(fd["Dacoity"],labels=fd["Unit Name"],autopct="%.2f%%")
plt.legend(fontsize=10)
plt.show()
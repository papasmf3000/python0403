import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Define sample data
prodID = np.arange(1, 101)
prodName = ['Product ' + str(i) for i in prodID]
price = np.random.uniform(10, 100, size=100)

# Create DataFrame and save to CSV file
data = {'prodID': prodID, 'prodName': prodName, 'price': price}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)

# Read CSV file and create graph
df = pd.read_csv('data.csv')
plt.plot(df['price'])
plt.xlabel('Product ID')
plt.ylabel('Price')
plt.title('Product Prices')
plt.show()

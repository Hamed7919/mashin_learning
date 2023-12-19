# Raw Package
import numpy as np
import pandas as pd
import json

#Data Source
import yfinance as yf

# Cluster the combined DataFrame using k-means
from sklearn.cluster import KMeans



# Creating a array of 40 cryptocurrency
cryptocurrency = ["BTC","ETH","USDT","BNB","XRP","SOL","USDC","ADA","AVAX","DOGE","DOT","TRX","LINK","MATIC","TON","SHIB","DAI","LTC","BCH","ATOM","UNI","XLM","OKB","LEO","XMR","ETC","ICP","HBAR","KAS","IMX","INJ","CRO","APT","TUSD","FIL","NEAR","VET","TIA","BONK","LDO"]
data = []
for ticker in cryptocurrency:
    df = pd.DataFrame(yf.download(tickers=ticker, period="100d", interval="1d")["Close"])
    data.append(df)

df = pd.concat(data, axis=1)
df.columns = cryptocurrency
print(df)
num_clusters = 3
# Initialize the KMeans model
kmeans = KMeans(n_clusters=num_clusters)

# Fit the model to the data
for data in df:
    kmeans.fit(df)

# Obtain cluster labels for each cryptocurrency
cluster_labels = kmeans.predict(df)
# Add cluster labels to the DataFrame
df["Cluster"] = cluster_labels
# Print the combined DataFrame
print(df)
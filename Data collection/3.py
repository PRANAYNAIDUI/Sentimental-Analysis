import pandas as pd

# Example using the UCI Machine Learning Repository's SMS Spam Collection
url = "https://raw.githubusercontent.com/gyxi/sms-spam-detector/master/data/spotify_dataset.csv"
df = pd.read_csv(url)

# Display the first few rows
print(df.head())
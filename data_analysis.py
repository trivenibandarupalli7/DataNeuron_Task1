import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("DataNeuron_Text_Similarity.csv")

# Basic analysis
print(f"Total pairs: {len(df)}")
print(f"Missing values:\n{df.isnull().sum()}")

# Text length analysis
df['text1_len'] = df['text1'].apply(len)
df['text2_len'] = df['text2'].apply(len)
df[['text1_len', 'text2_len']].hist(bins=30)
plt.title("Text Length Distribution")
plt.show()
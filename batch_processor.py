import pandas as pd
from tqdm import tqdm
from model import compute_similarity

def process_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # Calculate similarity for all pairs
    tqdm.pandas(desc="Processing pairs")
    df['similarity_score'] = df.progress_apply(
        lambda row: compute_similarity(row['text1'], row['text2']), 
        axis=1
    )
    
    # Save results
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

# Usage
process_csv("DataNeuron_Text_Similarity.csv", "results.csv")
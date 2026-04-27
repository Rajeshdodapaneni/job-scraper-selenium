import pandas as pd
import os

def save_to_csv(data):
    os.makedirs("data", exist_ok=True)

    file_path = os.path.abspath("data/jobs.csv")
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)

    print(f"✅ Data saved at: {file_path}")
import pandas as pd
import json
from datetime import datetime
import os

def generate_metadata(df, output_path='metadata.json'):
    metadata = {}

    # Total records
    metadata['total_records'] = len(df)

    # Records per country
    metadata['records_per_country'] = df['country'].value_counts().to_dict()

    # Timestamp
    metadata['processed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Column types and sample values
    column_info = {}
    for col in df.columns:
        column_info[col] = {
            'dtype': str(df[col].dtype),
            'sample_values': [str(val) for val in df[col].dropna().unique()[:5]]
        }
    metadata['columns'] = column_info

    # Save JSON
    with open(output_path, 'w') as f:
        json.dump(metadata, f, indent=4)
    
    print(f"Metadata saved to {output_path}")
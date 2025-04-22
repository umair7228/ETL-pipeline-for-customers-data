import os
import pandas as pd
from datetime import datetime

def clean_data(df):
    # Drop nulls and duplicates
    df = df.dropna().drop_duplicates()
    
    # Convert signup_date to datetime64[ns]
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
    
    # Clean string columns
    string_cols = ['name', 'gender', 'email', 'address', 'country', 'department', 'designation']
    for col in string_cols:
        df[col] = df[col].astype(str).str.strip().str.lower()
    
    # Standardize country names
    df['country'] = df['country'].replace({
        'united states': 'usa', 'us': 'usa', 'usa': 'usa',
        'united kingdom': 'uk', 'england': 'uk', 'uk': 'uk',
        'india': 'india'
    })
    
    return df

def save_by_country(df, output_dir='final_data'):
    os.makedirs(output_dir, exist_ok=True)
    
    for country in ['usa', 'uk', 'india']:
        country_df = df[df['country'] == country].copy()
        
        # Convert date to YYYY-MM-DD format string before saving
        country_df['signup_date'] = country_df['signup_date'].dt.strftime('%Y-%m-%d')
        
        output_path = os.path.join(output_dir, f'country_{country}.csv')
        country_df.to_csv(output_path, index=False)
        print(f"Saved: {output_path}")
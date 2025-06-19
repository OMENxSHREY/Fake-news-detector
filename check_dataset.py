import pandas as pd

# Try different encodings
encodings = ['utf-8', 'cp1252', 'latin1', 'iso-8859-1']

for encoding in encodings:
    try:
        print(f"\nTrying {encoding} encoding...")
        df = pd.read_csv('IFND.csv', encoding=encoding)
        
        # Display basic information
        print("\nDataset Info:")
        print(df.info())
        
        # Display first few rows
        print("\nFirst few rows:")
        print(df.head())
        
        # Display column names
        print("\nColumn names:")
        print(df.columns.tolist())
        
        break  # If successful, exit the loop
        
    except UnicodeDecodeError:
        print(f"Failed with {encoding} encoding")
        continue
import json
from datetime import datetime
from typing import Optional
from pprint import pformat
import os
def process_data():
    # Read the data from the JSON file created by main.py
    with open('dex_data.json', 'r') as json_file:
        href_data = json.load(json_file)
    
    return href_data
    


def save_cleaned_data_to_file(cleaned_data, pair_details):
    # Extract the base token name from pair_details
    base_token_name = pair_details.base_token.name
    
    # Sanitize the base token name to ensure it's a valid filename
    sanitized_name = base_token_name.replace(" ", "_").replace("/", "_")
    
    # Get the current timestamp to append to the file name
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Use the base token name and timestamp in the file name
    file_name = f"{sanitized_name}_{timestamp}_cleaned_data.txt"
    
    folder_path = "data"
    os.makedirs(folder_path, exist_ok=True)
    
    # Join the folder path and file name
    file_path = os.path.join(folder_path, file_name)

    # Use pformat to format the dictionary in a readable way
    formatted_data = pformat(cleaned_data, indent=4)
    
    # Open the file and write the formatted data
    with open(file_path, "w") as file:
        file.write(formatted_data)
    
    print(f"Data saved to {file_path}")


def clean_data(pair_details):
    """
    Clean and structure the token pair details into a simplified and readable format.
    
    Parameters:
        pair_details (TokenPair): The raw data returned by the get_token_pair function.
        
    Returns:
        dict: The cleaned and structured data with only the relevant information.
    """
    cleaned_data = {
        'pair_address': pair_details.pair_address,
        'base_token_name': pair_details.base_token.name,
        'base_token_symbol': pair_details.base_token.symbol,
        'price_native': pair_details.price_native,
        'price_usd': pair_details.price_usd,
        'transactions': {
            'm5': pair_details.transactions.m5,
            'h1': pair_details.transactions.h1,
            'h6': pair_details.transactions.h6,
            'h24': pair_details.transactions.h24
        },
        'volume': {
            'm5': pair_details.volume.m5,
            'h1': pair_details.volume.h1,
            'h6': pair_details.volume.h6,
            'h24': pair_details.volume.h24
        },
        'price_change': {
            'm5': pair_details.price_change.m5,
            'h1': pair_details.price_change.h1,
            'h6': pair_details.price_change.h6,
            'h24': pair_details.price_change.h24
        },
        'liquidity': pair_details.liquidity,
        'fdv': pair_details.fdv,
        'pair_created_at': pair_details.pair_created_at.isoformat() if pair_details.pair_created_at else None  # Convert datetime to ISO format
    }
    
    return cleaned_data



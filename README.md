# anal_coin
analyzing meme coins



main file: render.py
-->iterates through the top tokens (can specify from top 20-1)
    writing each file to a txt document with name timestamped
    
write_data.py is not implemented yet

supportive file: dex.py
-->process_data() processes the data from the website storing each href element into an array called href_data
-->save_cleaned_data_to_file() saves data to an indivudual file within the data folder
-->clean_data() cleans the data into readable data

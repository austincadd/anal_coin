from seleniumbase import Driver
import time
import json
import dex
import write_data
# Initialize the driver with user control (uc=True) to handle CAPTCHA
driver = Driver(uc=True)
url = "https://dexscreener.com/5m"
driver.uc_open_with_reconnect(url, 4)  # Open URL with reconnect on failure
driver.uc_gui_click_captcha()  # Handle CAPTCHA (if present)

# Wait to ensure the page is fully loaded
time.sleep(30)

# Extract the top 20 hrefs from the page
href_elements = driver.find_elements('div.ds-dex-table.ds-dex-table-top a.ds-dex-table-row.ds-dex-table-row-top')  # Find all relevant <a> tags inside the specific <div>

# Extract the href attribute from the first 20 elements
top_20_hrefs = [elem.get_attribute('href').split('/')[-1] for elem in href_elements[:20]]

# Print the top 20 hrefs
with open('dex_data.json', 'w') as json_file:
    json.dump(top_20_hrefs, json_file)


processed_data = dex.process_data()

from dexscreener import DexscreenerClient
client = DexscreenerClient()

for i in range(5):
    #getting the pair details from the pair id that is in the href scarped on dex
    pair_details = client.get_token_pair("solana", processed_data[i])

    #cleaning the data from pair_details to make more readable
    cleaned_data = dex.clean_data(pair_details)

    #saving an individual text file with all the information on the given token
    dex.save_cleaned_data_to_file(cleaned_data, pair_details)



# Optionally, close the driver after extracting the links
driver.quit()

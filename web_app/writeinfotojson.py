import json
from parsepilotinfo import parse_pilot_info
from gettime import current_time
import pandas as pd
from datetime import datetime


def check_if_file_empty():
    # Checks if file exists and is empty.
    try:
        with open("pilot.json", "r") as f:
            check_char = f.read(1)
            f.close()
            if check_char:
                return True
            else:
                return False
    # If file does not exist create it.
    except IOError:
        with open("pilot.json", "w+") as f:
            f.close()
            return False


def check_data_and_write():
    not_empty = check_if_file_empty()
    data = []
    time_stamp = current_time()
    pilot_dict_list = parse_pilot_info()
    df = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Position', 'Time'])

# If file is not empty, check the file contents
    if not_empty:

        with open("pilot.json") as f:
            for line in f:
                entry = json.loads(line)
                # Check time saved for each entry in the file.
                old_time = datetime.strptime(entry['Time'], '%d/%m/%Y %H:%M:%S')
                time_dif = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S') - old_time
                # If current time - time saved for the entry is over 600sec (10 min) entry won't be saved
                if time_dif.total_seconds() < 600:
                    data.append(json.loads(line))
        # Add data read from the file to a pandas dataframe
        if data:
            df = pd.DataFrame(data)
    # Loop over the current dictionaries with pilot information
    for i in range(len(pilot_dict_list)):

        # Set name to be pilots name based on the current index.
        # If name is already in the dataframe get the index of it.
        current_name = pilot_dict_list[i]['Name']
        index_of_name = df[(df['Name'] == current_name)].index.tolist()

        # Based on the name index get corresponding positional value.
        if index_of_name:
            df_position_val = df['Position'].iloc[index_of_name].tolist()

        # If name is not found in the dataframe add it.
        if not (df['Name'] == current_name).any():
            df_temp = pd.DataFrame(pilot_dict_list[i])
            df = pd.concat([df, df_temp])

        # If name is found compare position values of value found in the dataframe to a new position value.
        # Remove the old position value if it is larger than the new value, also update the time.
        elif (df_position_val[0]) > pilot_dict_list[i]['Position']:
            df.loc[index_of_name[0], 'Position'] = pilot_dict_list[i]['Position']
            df.loc[index_of_name[0], 'Time'] = pilot_dict_list[i]['Time'][0]
    # If there is no data in the dataframe return only the columns as HTML.
    # Otherwise, save the dataframe as a JSON file and return a HTML representation of it.
    if df.empty:
        return df.to_html()
    else:
        df.to_json('pilot.json', orient='records', lines=True)
        html_table = df.to_html()
        return html_table

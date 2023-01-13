import json
from parsepilotinfo import parse_pilot_info
from gettime import current_time
import pandas as pd
from datetime import datetime


def check_if_file_empty():
    with open("pilot.json", "r") as f:
        check_char = f.read(1)
        print(check_char)
        f.close()
        if check_char:
            return True
        else:
            return False


def check():
    not_empty = check_if_file_empty()
    print(not_empty)
    data = []
    time_stamp = current_time()
    pilot_dict_list = parse_pilot_info()
    df = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Position', 'Time'])

    if not_empty:

        with open("pilot.json") as f:
            for line in f:
                entry = json.loads(line)
                old_time = datetime.strptime(entry['Time'], '%d/%m/%Y %H:%M:%S')
                time_dif = datetime.strptime(time_stamp, '%d/%m/%Y %H:%M:%S') - old_time
                if time_dif.total_seconds() < 600:
                    data.append(json.loads(line))
        if data:
            df = pd.DataFrame(data)

    for i in range(len(pilot_dict_list)):
        current_name = pilot_dict_list[i]['Name']
        index_of_name = df[(df['Name'] == current_name)].index.tolist()
        if index_of_name:
            df_position_val = df['Position'].iloc[index_of_name].tolist()
            print(df_position_val)
        if not (df['Name'] == current_name).any():
            df_temp = pd.DataFrame(pilot_dict_list[i])
            df = pd.concat([df, df_temp])
        elif df_position_val[0] < pilot_dict_list[i]['Position']:
            df.loc[index_of_name[0], 'Position'] = pilot_dict_list[i]['Position']
            df.loc[index_of_name[0], 'Time'] = time_stamp
            print("Replaced on line {}".format(index_of_name[0]+1))

    if df.empty:
        return df.to_html()
    else:
        df.to_json('pilot.json',orient='records',lines=True)
        html_table = df.to_html()
        return html_table

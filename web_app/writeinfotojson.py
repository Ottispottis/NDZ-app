import json
from parsepilotinfo import parse_pilot_info
import pandas as pd
import datetime


def write_to_file():
    pilot_dict_list = parse_pilot_info()

    if pilot_dict_list:
        for i in range(len(pilot_dict_list)):
            current_name = pilot_dict_list[i]['Name']
            json_string = json.dumps(pilot_dict_list[i])
            is_name = check_file_content(current_name)
            with open("pilot.json", "a+") as f:
                if is_name:
                    f.close()
                else:
                    f.write(json_string)
                    f.write('\n')
                    f.close()


def check_file_content(name):
    file_not_empty = check_if_file_empty()
    if file_not_empty:
        with open("pilot.json") as f:
            if name in f.read():
                return True
    return False


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
    comparison_time = datetime.datetime.now()
    print(comparison_time.hour, comparison_time.minute)
    pilot_dict_list = parse_pilot_info()
    df = pd.DataFrame(columns=['Name', 'Email', 'Phone', 'Position', 'Time'])

    if not_empty:
        with open("pilot.json") as f:
            for line in f:
                data.append(json.loads(line))
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
            print("Replaced on line {}".format(index_of_name[0]+1))


    if df.empty:
        return
    else:
        df.to_json('pilot.json',orient='records',lines=True)







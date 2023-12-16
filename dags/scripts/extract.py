import json
import os
from urllib.request import urlopen
import pandas as pd
import requests
import config
import concurrent.futures


def next_seed(seed):
    # Convert the string to a list of characters
    seed_list = list(seed)

    # Iterate through the characters and increment them
    for i in range(len(seed_list) - 1, -1, -1):
        if seed_list[i] == 'Z':
            seed_list[i] = 'A'
        else:
            seed_list[i] = chr(ord(seed_list[i]) + 1)
            break  # Stop incrementing once a non-'Z' character is found

    # Convert the list back to a string
    permutation_value = ''.join(seed_list)

    return permutation_value


def get_data(seed):
    url = config.API_URL.format(config.SEED)
    print(url)
    try:
        # Make a GET request to the API
        response = requests.get(url)
        print(response)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the JSON data
            response = urlopen(url)
            # storing the JSON response
            # from url in data
            data_json = json.loads(response.read())
            # print the json response
            print(data_json)
        else:
            # Print an error message if the request was not successful
            print(f"Failed to fetch data for seed {seed}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        # Handle exceptions, e.g., network issues
        print(f"Error during request: {e}")
        return None


def import_data():

        config.SEED = next_seed(config.SEED)
        url = config.API_URL.format(config.SEED)
            #print(url)
        try:
            # Make a GET request to the API
            response = requests.get(url)
                #print(response)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Return the JSON data
                response = urlopen(url)
                # storing the JSON response
                # from url in data
                data_json = json.loads(response.read())
            else:
                # Print an error message if the request was not successful
                print(f"Failed to fetch data for seed {config.SEED}. Status code: {response.status_code}")
                return None
        except requests.RequestException as e:
            # Handle exceptions, e.g., network issues
            print(f"Error during request: {e}")
            return None


def get_file_path():
    # should return a os file path with correct destination.
    # Do not change file name
    # filename = "random_user.csv"
    parent_path = config.CSV_FILE_DIR
    isExist = os.path.exists(parent_path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(parent_path)
        print("The new directory is created!")
    filename = 'random_user.csv'
    filepath = os.path.join(parent_path, filename)

    return filepath


def transform_data(data_json):
    # create a pandas data frame
    # do any required pre-processing such as
    # fill-in or remove garbadge value if any
    # return data frame
    if data_json is not None:
        if 'results' in data_json:
                df = pd.json_normalize(data_json, record_path='results')
                print('dataframe is',df)
                print(df.head())
                if df.isnull() is not True:
                    pass
                else:
                    df = df.fillna(0, inplace=True)
                return df


def save_new_data_to_csv(data):
    # save the data to a csv file
    # file should be saved in the defined location
    # filename = get_file_path()
    #print('csv data is', data)
    column_mapping = {
        'gender': 'gender',
        'email': 'email',
        'phone': 'phone',
        'cell': 'cell',
        'nat': 'nat',
        'name.title': 'title',
        'name.first': 'firstname',
        'name.last': 'lastname',
        'location.street.number': 'street_number',
        'location.street.name': 'street_name',
        'location.city': 'city',
        'location.state': 'state',
        'location.country': 'country',
        'location.postcode': 'postcode',
        'location.coordinates.latitude': 'latitude',
        'location.coordinates.longitude': 'longitude',
        'location.timezone.offset': 'timezone_offset',
        'location.timezone.description': 'timezone_description',
        'login.uuid': 'uuid',
        'login.username': 'username',
        'login.password': 'password',
        'login.salt': 'salt',
        'login.md5': 'md5',
        'login.sha1': 'sha1',
        'login.sha256': 'sha256',
        'dob.date': 'dob_date',
        'dob.age': 'dob_age',
        'registered.date': 'registered_date',
        'registered.age': 'registered_age',
        'id.name': 'id_name',
        'id.value': 'id_value',
        'picture.large': 'picture_large',
        'picture.medium': 'picture_medium',
        'picture.thumbnail': 'picture_thumbnail',
    }

    data.rename(columns=column_mapping, inplace=True)

    filename = get_file_path()

    try:
        # If the file exists, open it in append mode without writing the header
        with open(filename, 'r') as f:
            data.to_csv(filename, mode='a', header=False, index=False)
            print('final csv data', data)
    except FileNotFoundError:
        # If the file does not exist, create it and write the header
        data.to_csv(filename, index=False)

    read_csv_data = pd.read_csv(filename)
    #print('csv data', read_csv_data.head())
    # Converting JSON data to a pandas DataFrame
    # df = pd.read_json(json_data)
    # df.to_csv(filepath)
    # print(f"Data saved to: {filename}")


def main():
    next_seed(config.SEED)
    get_data(config.SEED)
    import_data()
    get_file_path()
    filename = get_file_path()
    if os.path.exists(filename):
        os.remove(filename)
    with concurrent.futures.ThreadPoolExecutor():
        for _ in range(50):
            config.SEED = next_seed(config.SEED)
            url = config.API_URL.format(config.SEED)
            response = requests.get(url)
            response = urlopen(url)
            data_json = json.loads(response.read())
            data = pd.json_normalize(data_json, record_path='results')
            print('data is', data)
            transform_data(data_json)
            save_new_data_to_csv(data)


if __name__ == "__main__":
    main()

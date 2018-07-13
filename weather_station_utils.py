"""Miscellaneous functions that help in processing
data coming from WeatherUnderground.
"""
__author__ = 'Sagnik Bhattacharya (github.com/sagnibak)'

from datetime import date, datetime, timedelta
import numpy as np
import os
import pandas as pd


def process_data(data_df):
    """Makes the WeatherUnderground data compatible with DoseNet
    data by
        1. converting time string to Unix timestamp,
        2. converting temperature and dewpoint to degrees Celsius,
        3. converting pressure to millibars (from inches of Hg), and
        4. removing (dropping) unnecessary columns from the DataFrame.
    """
    def deg_f_to_c(deg_f):
        return (5 / 9) * (deg_f - 32)

    def inhg_to_mbar(inhg):
        return 33.863753 * inhg

    for idx, time, tempf, dewf, pressure, *_ in data_df.itertuples():
        data_df.loc[idx, 'Time'] = datetime.strptime(time, '%Y-%m-%d %H:%M:%S').timestamp()
        data_df.loc[idx, 'Temperature'] = deg_f_to_c(tempf)
        data_df.loc[idx, 'Dewpoint'] = deg_f_to_c(dewf)
        data_df.loc[idx, 'Pressure'] = inhg_to_mbar(pressure)

    return data_df.drop(['TemperatureF', 'DewpointF', 'PressureIn', 'Conditions', 'Clouds',
#                          'SolarRadiationWatts/m^2',
                         'SoftwareType', 'DateUTC<br>'], axis=1)


def get_clean_df(location_id, date):
    """Get weather data from `location_id` on `date`, then
    remove all the `<br>` tags in the file.

    `date` should be a list/tuple of 3 strings in the format
    [MM, DD, YYYY].
    """
    url = f'''\
https://www.wunderground.com/weatherstation/WXDailyHistory.asp?\
ID={location_id}&\
day={date[1]}&\
month={date[0]}&\
year={date[2]}&\
graphspan=day&\
format=1'''
    # print(f'Getting data from {url}')
    data = pd.read_csv(url, index_col=False)
    # drop every other row because it contains `<br>`
    return data.drop([2*i + 1 for i in range(data.shape[0] // 2)])


def get_all_binned(interval: int, data_dir: str, location: str):
    """Make a single DataFrame containing all the data we have binned.
    All the data points are aligned, thanks to the binning process.

    :param interval:  interval of binning
    :param data_dir:  directory where the binned data exist
    :param location:  name of the location whose binned data is to be
                      loaded
    :return:          pandas.DataFrame with all the data
    """
    concat_list = []  # list of dataframes to be concatenated

    try:
        co2_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_co2_ppm_{interval}.csv'),
                               header=0, names=['unix_time', 'co2'])
        concat_list.append(co2_data)
    except:
        pass                               

    try:
        radiation_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_cpm_{interval}.csv'),
                                     header=0, names=['unix_time', 'radiation'], usecols=[1])
        concat_list.append(radiation_data)
    except:
        pass                                     

    try:
        pgradiation_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_cpmpg_{interval}.csv'),
                                       header=0, names=['unix_time', 'pgradiation'], usecols=[1])
        concat_list.append(pgradiation_data)
    except:
        pass                                       

    try:
        humidity_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_humidity_{interval}.csv'),
                                    header=0, names=['unix_time', 'humidity'], usecols=[1])
        concat_list.append(humidity_data)
    except:
        pass                                    

    try:
        temperature_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_temperature_{interval}.csv'),
                                       header=0, names=['unix_time', 'temperature'], usecols=[1])
        concat_list.append(temperature_data)
    except:
        pass                                       

    try:
        pressure_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_pressure_{interval}.csv'),
                                    header=0, names=['unix_time', 'pressure'], usecols=[1])
        concat_list.append(pressure_data)
    except:
        pass                                    

    try:
        pm1_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_PM1_{interval}.csv'),
                               header=0, names=['unix_time', 'pm1'], usecols=[1])
        concat_list.append(pm1_data)
    except:
        pass                               

    try:
        pm25_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_PM25_{interval}.csv'),
                                header=0, names=['unix_time', 'pm25'], usecols=[1])
        concat_list.append(pm25_data)
    except:
        pass                                

    try:
        pm10_data = pd.read_csv(os.path.join(data_dir, f'{location}_data_PM10_{interval}.csv'),
                                header=0, names=['unix_time', 'pm10'])
        concat_list.append(pm10_data)
    except:
        pass                                

    # make one awesome DataFrame object containing all the data
    all_data = pd.concat(concat_list, axis=1)

    all_data['unix_time'] = all_data['unix_time'].astype('int')
    all_data = all_data.loc[:, ~all_data.columns.duplicated()]

#     return all_data.dropna(axis=0, how='any')
    return all_data


def get_ws_data_by_time(start_time, end_time, location_id):
    current_time = start_time
    data_df = pd.DataFrame([])
    while current_time < end_time:
        # store the result of the query in dataframe `data_df`
        temporary = process_data(get_clean_df(location_id, [str(current_time.month),
                                                            str(current_time.day),
                                                            str(current_time.year)]))
        temp_cols = list(temporary.columns.values)
        temporary = temporary[[temp_cols[6]] + temp_cols[:6] + temp_cols[7:]]
        data_df = pd.concat([data_df, temporary], ignore_index=True, sort=True)
        current_time = current_time + timedelta(days=1)

    return data_df


"""Script to repeatedly run `time_binning.py` with
different arguments each time.
"""
__author__ = 'Sagnik Bhattacharya (github.com/sagnibak)'
import os
import sys

SECONDS_IN_A_DAY = 60 * 60 * 24
SECONDS_IN_A_HALF_DAY = 60 * 60 * 12
SECONDS_IN_A_QUARTER_DAY = 60 * 60 * 6
SECONDS_IN_ONE_HOUR = 60 * 60


def run_all_binnings(time_interval: int, location: str):
    """Runs `time_binning.py` for all the five
    data types, passing in the argument `time_interval`.
    """
    ws_ = 'ws_'
    # common arguments for all the commands
    args = f'-s binned_data_long_term/ -i {time_interval} -l {location}'
    ws_args = f'-s binned_data_long_term/ -i {time_interval} -l {ws_ + location}'

    # these commands will be run as if they are being run from terminal
    # these should also work on the Windows command prompt
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_weather.csv -c pressure {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_weather.csv -c temperature {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_weather.csv -c humidity {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_d3s.csv -c cpm {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_adc.csv -c co2_ppm {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os.csv -c cpmpg {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_aq.csv -c PM1 {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_aq.csv -c PM25 {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/pinewood_os_aq.csv -c PM10 {args}')

    # os.system(
    #     f'python time_binning.py wunderground_data/data_pine_long_term.csv -c Temperature {ws_args}')
    # os.system(
    #     f'python time_binning.py wunderground_data/data_pine_long_term.csv -c Pressure {ws_args}')
    # os.system(
    #     f'python time_binning.py wunderground_data/data_pine_long_term.csv -c Humidity {ws_args}')
    # os.system(
    #     f'python time_binning.py wunderground_data/data_pine_long_term.csv -c WindDirectionDegrees {ws_args}')
    # os.system(
    #     f'python time_binning.py wunderground_data/data_pine_long_term.csv -c WindSpeedGustMPH {ws_args}')
    os.system(
          f'python time_binning.py wunderground_data/data_pine_long_term.csv -c dailyrainin {ws_args}')

def main():
    loc = sys.argv[1]  # first argument to the script should be the location prefix
    for i in range(1, 29):
        run_all_binnings(i * SECONDS_IN_A_HALF_DAY, loc)


if __name__ == '__main__':
    main()


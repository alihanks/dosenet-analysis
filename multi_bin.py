"""Script to repeatedly run `time_binning.py` with
different arguments each time.
"""
__author__ = 'Sagnik Bhattacharya (github.com/sagnibak)'
import os

SECONDS_IN_A_DAY = 60 * 60 * 24
SECONDS_IN_A_QUARTER_DAY = 60 * 60 * 6
SECONDS_IN_ONE_HOUR = 60 * 60


def run_all_binnings(time_interval):
    """Runs `time_binning.py` for all the five
    data types, passing in the argument `time_interval`.
    """
    args = f'-t 2018-06-29--00:00:01 -s binned_data_10_days/ -i {time_interval}'  # common arguments for all the commands
    ws_args = f'-t 2018-06-29--00:00:01 -s binned_data_10_days/ -i {time_interval}'

    # these commands will be run as if they are being run from terminal
    # these should also work on the Windows command prompt
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_weather.csv -c pressure {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_weather.csv -c temperature {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_weather.csv -c humidity {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_d3s.csv -c cpm {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_adc.csv -c co2_ppm {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof.csv -c cpmpg {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_aq.csv -c PM1 {args}')
    # os.system(
    #     f'python time_binning.py ~/Downloads/etch_roof_aq.csv -c PM25 {args}')

    os.system(
        f'python time_binning.py wunderground_data/data_fire_1.csv -c Temperature {ws_args}')
    os.system(
        f'python time_binning.py wunderground_data/data_fire_1.csv -c Pressure {ws_args}')
    os.system(
        f'python time_binning.py wunderground_data/data_fire_1.csv -c Humidity {ws_args}')
    os.system(
        f'python time_binning.py wunderground_data/data_fire_1.csv -c WindDirectionDegrees {ws_args}')
    os.system(
        f'python time_binning.py wunderground_data/data_fire_1.csv -c WindSpeedMPH {ws_args}')


def main():
    for i in range(1, 5):
        run_all_binnings(i * SECONDS_IN_ONE_HOUR)


if __name__ == '__main__':
    main()

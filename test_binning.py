import numpy as np
import pandas as pd
from time_binning import *


def make_test_data():
    times = np.arange(START_TIME + 1,
                      START_TIME + 41280 * 2000,
                      2000)

    vals = np.full_like(times, fill_value=300.)
    return pd.DataFrame(data={'deviceTime_unix': times,
                              'vals': vals})


if __name__ == '__main__':
    df = make_test_data()

    dg = run_binner(df, 'vals')

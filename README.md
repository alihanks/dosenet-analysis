# dosenet-analysis
Tools for analysis with DoseNet's open access data.

Everything here works right out of the box! You can see correlations between 
data, and as a bonus, the visualizations are beautiful too.

In order to do your own binning, however, you need to download the data from 
the [DoseNet downloads page](https://radwatch.berkeley.edu/dosenet/downloads) 
and select `Etcheverry Roof` from the dropdown menu. If you want to get data 
from another source, you will have to change a lot of filenames in the Ipython 
Notebooks. We might come up with a cleaner solution later on. Once you have 
downloaded the data, you can manually run the [time\_binning.py](time_binning.py) 
script with the necessary parameters, as follows:
```bash
python time_binning.py [optional arguments] <source>
```
where `source` can be a URL or file on your computer that refers to a `.csv` file 
from where you want to bin your data. Type `python time_binning.py -h` to see the 
full list of options.

However, I would strongly recommend you to use [multi\_bin.py](multi_bin.py), which 
automates the process of binning over different intervals of time and over multiple 
files or URLs. It works using Python's built-in [`os.system`](https://docs.python.org/3.6/library/os.html#os.system) 
function. So it is MUCH more readable and beginner-friendly than an ordinary Bash script, 
and it might even work on Windows (unlike bash scripts). The script has adequately good
documentation in its docstrings, and is pretty intuitive even for beginners, so 
feel free to check it out and make modifications to it to suit your use-case!

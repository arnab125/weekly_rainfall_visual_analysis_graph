# Rainfall Analysis

A simple python script to analyze and visualize weekly rainfall data. The script takes user inputs for daily rainfall and calculates the min, max, mean and standard deviation of the data. It also generates a bar chart with the calculated values annotated on it, and saves the chart in a folder called "generated_image" with a unique timestamp.

## Getting Started
1. Clone the repository
```
$ git clone https://github.com/arnab125/rainfall-analysis.git
```

2. Install the required libraries
```
$ pip install -r requirements.txt
```

3. Run the script
```
$ python main.py
```

4 .Follow the on-screen instructions to enter the daily rainfall data.
5.The script will display the calculated min, max, mean, and standard deviation and also save the generated graph in the "generated_image" folder.



## Prerequisites
- Python 3.6 or above
- Matplotlib, os and datetime python libraries.


## Built With
- Python 3.6
- Matplotlib - Python library for data visualization
- os - OS library for file and directory operations.
- datetime - Datetime library for python.


## Notes
- The script will only accept numerical values for the daily rainfall data.
- The file name will be in the format of 'figure_yyyy-mm-dd_hh-mm-ss.png'.
- The graph will be saved in the dpi of 300.





## Sample Image Generated
![Sample Image](https://github.com/arnab125/arnab125-weekly_rainfall_visual_analysis_graph/blob/main/sample_image/figure_2023-01-12_07-36-35.png)




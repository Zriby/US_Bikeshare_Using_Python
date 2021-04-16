
# Python Script to Explore US Bikeshare Data
A Udacity project I have made to help improve and tone my python skills specifically in NumPy, pandas and Time libraries. This project was created on March 2021.

I also provided a snapshot of the feedback I received from the instructor marking 
my work in 'feedback.png'.

## Project Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## Program Execution
Run 'bikeshare.py' on your terminal. You can use the Jupyer Notebook on [Anaconda Navigator](https://www.anaconda.com/) for MAC, Linux or Windows.
:exclamation:**NOTE: unzip _data.zip_ to get all cities dataset before running the script**

## Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
* Gender
* Birth Year

## Statistics Computed
The code will provide the following information:

1. Popular times of travel (i.e., occurs most often in the start time):
- most common month
- most common day of week
- most common hour of day

2. Popular stations and trip:
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration:
- total travel time
- average travel time

4. User info:
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Requirements
* Language: Python 3.6 or above
* Libraries: pandas, numpy, time

## Project Data
* chicago.csv - Stored in data.zip folder, contains dataset bikeshare information for Chicago and is provided by Udacity. 
* new_york_city.csv - Stored in data.zip folder, contains dataset bikeshare information for NYC and is provided by Udacity. 
* washington.csv - Stored in data.zip folder, contains dataset bikeshare information for NYC and is provided by Udacity. This file contains no Gender or Birth Year data.

## Built with
* [Jupyter Notebook 6.0.3](https://jupyter.org/)
* [pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)
* [Time](https://docs.python.org/3/library/time.html)

## Author
* [Ahmed Zribi](https://github.com/Zriby) 

## Acknowledgements
* [Aritra96](https://github.com/Aritra96)- This persons repo helped me in structuring and creating my repo
* [sumankumarsubudhi](https://github.com/sumankumarsubudhi) - This persons repo helped me in structuring and creating my repo
* [Udacity](https://github.com/udacity) - The nanodegree has helped me tremendously understand the field of datascience.


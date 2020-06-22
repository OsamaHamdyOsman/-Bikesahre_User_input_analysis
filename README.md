# Overview
This project is part of the Data Analyst Nanodegree program of Udacity.

> In this project, making use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. Writing code to import the data and answer interesting questions about it by computing descriptive statistics. I will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## What Software Do I Need?
To complete this project, the following software requirements apply:

* You should have Python 3, NumPy, and pandas installed using Anaconda
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

<img scr='./divvy.jpg' width='500'>

# Project Details

## Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.


## Datasets

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (in seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
The Chicago and New York City files also have the following two columns:

Gender
Birth Year


## Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

###  Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

### Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

### Trip duration

* total travel time
* average travel time

### User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)


# An Interactive Experience

The bikeshare.py file is set up as a script that takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?. 
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

Remember that any time you ask users for input, there is a chance they may not enter what you expect, so your code should handle unexpected input well without failing. You need to anticipate raw input errors like using improper upper or lower case, typos, or users misunderstanding what you are expecting. Use the tips provided in the sections of the Scripting lesson in this course to make sure your code does not fail with an execution error due to unexpected raw input.

Your script also needs to prompt the user whether they would like want to see the raw data. If the user answers 'yes,' then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data. The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any more raw data to be displayed.


The data comprises three csv files:
    1. [Washington data](./washington.csv) 
    2. [Chicago data](./chicago.csv)
    3. [NYC data](./new_york_city.csv)
    

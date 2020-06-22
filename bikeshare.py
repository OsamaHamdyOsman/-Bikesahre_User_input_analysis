import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_selection = input('To view the available bikeshare data, type:\n (a) for Chicago\n (b) for New York City\n (c) for Washington\n  ').lower()

    while city_selection not in {'a','b','c'}:
        print('That\'s invalid input.')
        city_selection = input('To view the available bikeshare data, type:\n (a) for Chicago\n (b) for New York City\n (c) for Washington\n  ').lower()

    if city_selection == "a":
        city = 'chicago'
    elif city_selection == "b":
        city = 'new york city'
    elif city_selection == "c":
        city = "washington"

    # get user input for month (all, january, february, ... , june)
    time_frame = input('\n\nWould you like to filter {}\'s data by month, day, both, or not at all? type month or day or both or none: \n'.format(city.title())).lower()

    # validate the user input is as intended.
    while time_frame not in {'none', 'both','month','day'}:
        print('That\'s not a valid choice')
        time_frame = input('\n\nWould you like to filter {}\'s data by month, day, both, or not at all? type month or day or both or none: \n\n'.format(city.title())).lower()

    # Building lists for the possible values for months and days.
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if time_frame == 'none':
        print('\nFiltering for {} for the 6 months period\n\n'.format(city.title()))
        month = 'all'
        day = 'all'

    elif time_frame == 'both':
        month_selection = input('which month? Please type out (January / February / March / April / May / June)\n').lower()
        while month_selection not in months:
            print('Invalid month choice!!')
            month_selection = input('which month? Please type out (January / February / March / April / May / June)\n').lower()
        month = month_selection

        day_selection = input('Which day? Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n').lower()
        while day_selection not in days:
            print('Invalid day choice!!')
            day_selection = input('Which day? Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n').lower()
        day = day_selection

    elif time_frame == 'month':
        month_selection = input('which month? Please type out (January / February / March / April / May / June)\n').lower()
        while month_selection not in months:
            print('Invalid month choice!!')
            month_selection = input('which month? Please type out (January / February / March / April / May / June)\n').lower()
        month = month_selection
        day = 'all'

    elif time_frame == 'day':
        day_selection = input('Which day? Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n').lower()
        while day_selection not in days:
            print('Invalid day choice!!')
            day_selection = input('Which day? Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n').lower()
        month = 'all'
        day = day_selection

    print('-'*40)
    return(city, month, day)

filtered_values = get_filters()
city, month, day = filtered_values

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df

load_data(city, month, day)

df = load_data(city, month, day)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    if month == 'all':
        # find the most popular month
        popular_month = df['month'].mode()[0]
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = months[popular_month - 1]
        print('Most Popular Start Month:', popular_month)

    # display the most common day of week
    if day == 'all':
        popular_day = df['day_of_week'].mode()[0]
        print('Most Popular Start day:', popular_day)

    # display the most common start hour
        # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
        # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

time_stats(df)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index.tolist()[0]
    print('\nMost commonly used end station: ', popular_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_route = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count').sort_values('count',ascending=False).head(1).reset_index()[['Start Station', 'End Station', 'count']]
    print('\nMost frequent combination of start station and end station trip:\n ',most_frequent_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

station_stats(df)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #Define the constants
    SECONDS_PER_MINUTE  = 60
    SECONDS_PER_HOUR    = 3600
    SECONDS_PER_DAY     = 86400

    # display total travel time
    seconds_total = df['Trip Duration'].sum()

    #Calculate the days, hours, minutes and seconds
    days = seconds_total / SECONDS_PER_DAY
    seconds_total = seconds_total % SECONDS_PER_DAY

    hours = seconds_total / SECONDS_PER_HOUR
    seconds_total = seconds_total % SECONDS_PER_HOUR

    minutes = seconds_total / SECONDS_PER_MINUTE
    seconds_total = seconds_total % SECONDS_PER_MINUTE

    #Display the result
    print('Total travel time (d:h:m:s): ', "%d:%02d:%02d:%02d"%(days,hours,minutes,seconds_total))

    # display mean travel time
    seconds_mean = df['Trip Duration'].mean()

    days_m = seconds_mean / SECONDS_PER_DAY
    seconds_mean = seconds_mean % SECONDS_PER_DAY

    hours_m = seconds_mean / SECONDS_PER_HOUR
    seconds_mean = seconds_mean % SECONDS_PER_HOUR

    minutes_m = seconds_mean / SECONDS_PER_MINUTE
    seconds_mean = seconds_total % SECONDS_PER_MINUTE

    print('Average travel time (d:h:m:s): ', "%d:%02d:%02d:%02d"%(days_m,hours_m,minutes_m,seconds_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

trip_duration_stats(df)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts().to_frame()
    print('\nUser types:\n',user_count  )

    try:
        # Display counts of gender
        gender_count = df['Gender'].value_counts().to_frame()
        print('\nBike riders gender split: \n', gender_count)

        # Display earliest, most recent, and most common year of birth
        earliest_yob = df['Birth Year'].min()
        most_recent_yob = df['Birth Year'].max()
        most_common_yob = df['Birth Year'].mode()[0]
        print('\n Earliest birth year :  ',earliest_yob)
        print('\n Most recent birth year :  ',most_recent_yob)
        print('\n Most common birth year :  ',most_common_yob)

    except KeyError:
        print('\n\nSorry, there\'s no gender or birth year data for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

user_stats(df)

def display_raw_data(city):
    """The fuction takes the name of the city produced by the get_filters fuction as input and
    returns the raw data of that city as chunks of 5 rows based upon user input.
    """

    print('\nRaw data is available to check... \n')
    display_raw = input('To View the availbale raw data in chuncks of 5 rows type: Yes \n').lower()
    while display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], index_col = 0 ,chunksize=5):
                print(chunk)
                display_raw = input('To View the availbale raw in chuncks of 5 rows type: Yes\n').lower()
                if display_raw != 'yes':
                    print('Thank You')
                    break
            break

        except KeyboardInterrupt:
            print('Thank you.')

display_raw_data(city)

def main():
    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

if __name__ == "__main__":
    main()

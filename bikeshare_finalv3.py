import time
import pandas as pd
import numpy as np
from statistics import mode

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#city_data is to load my files as a dictionary

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! My name is Laura! Let\'s explore some US bikeshare data.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("What city do you want to explore? ")
    city = city.lower()
    while city not in ["chicago","new york city","washington"]:
        print ("Hmm, looks like something is wrong. Make sure to choose either Chicago, New York City or Washington.\n")
        city = input("\nWhat city do you want to explore? \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("What month do you want to filter by? \nChoose a number for month. i.e. January = 1, February= 2, ... Decemeber = 12. If you don\'t want to filter by month, then type 0.\n")
    month = int(month)
    print('Month Filter: {}'.format(month))
    while month not in [0, 1, 2, 3, 4, 5, 6]:
        print ("\nHmm, looks like something is wrong. Make sure to choose your month as a number.\n")
        month = input("What month do you want to filter by?\n")
        month = int(month)
        print('Month Filter: {}'.format(month))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What day do you want to filter by? If no filter, then type All. If you require a filter then type Monday, Tuesday, etc.")
    day = day.title()


    print('Day Filter: {}'.format(day))
    while day not in ["All","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]:
        print ("\nHmm, looks like something is wrong. Make sure to choose either Monday, Tuesday ... or Sunday.\n")
        day = input("What day do you want to filter by?")
        day = day[0].upper()+day[1:].lower()
        print('Day Filter: {}'.format(day))

    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city]) #load csv to data frame

    #convert start time to a datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # convert start time to extract month
    df['month'] = df['Start Time'].dt.month

    #extract day of the weekS
    df['day'] = df['Start Time'].dt.weekday_name

    #extract hour
    df['hour'] = df['Start Time'].dt.hour

    if month != 0:
        df = df[df["month"]== month]

    if day != "All":
        df = df[df["day"]== day]

    counter = 5
    while True:
        show_data = input('Would you like to view your raw data. Type Yes or No: ')
        show_data = show_data.lower()
        if show_data == 'yes':
            print(df.iloc[0:counter])
            counter += 5
        else:
            break

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_mode = df['month'].mode().to_list()
    print('The most common month is :', month_mode)

    # TO DO: display the most common day of week
    mode_day = df['day'].mode().to_list()
    print('The most common day of the week is :', mode_day)

    # TO DO: display the most common start hour
    mode_hour = df['hour'].mode().to_list()
    print('The most common start hour is :', mode_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].value_counts().index[0]
    print('The most common start station is :', mode_start_station)

    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].value_counts().index[0]
    print('The most common end station is : {}'.format(mode_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + df['End Station']
    mode_start_end_station = df['Start and End Station'].value_counts().index[0]
    print('The most commonly used route is : {}'.format(mode_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel Time : {}'.format(total_travel))

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean Travel Time : {}'.format(mean_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].mode().to_list()
    print('User Type: {}'.format(user_types))

    print('User Type Count: \n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].mode().to_list()
        print('Most Common Gender: {}'.format(gender_types))

        print('Gender Count: \n')
        print(df['Gender'].value_counts())
    except KeyError as e:
        print("KeyError: {}".format(e))
        print('Sorry! We do not have user gender data for Washington.')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print('Earliest Birth: {}'.format(earliest_birth))
        recent_birth = df['Birth Year'].max()
        print('Recent Birth: {}'.format(recent_birth))
        mode_birth = df['Birth Year'].mode().to_list()
        print('Most Common birth: {}'.format(mode_birth))
    except KeyError as e:
        print("KeyError: {}".format(e))
        print('Sorry! We do not have user birth data for Washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

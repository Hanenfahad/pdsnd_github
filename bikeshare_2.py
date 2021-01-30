import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'friday']

def bikeshare_input(str,type):
    while True:
        index_input=input(str).lower()
        try:
            if index_input in ['chicago','new york city','washington'] and type==1:
                break
            elif index_input in MONTH_DATA and type==2:
                break
            elif index_input in DAY_DATA and type==3:
                break
            else:
                if type==1:
                    print('I'm Sorry invalid entry, please enter again city.')
                if type==2:
                    print('Sorry invalid entry, please enter again month.')
                if type==3:
                    print('Sorry invalid entry, please enter again day.')

        except ValueError:
            print('Sorry Error Input')
    return index_input

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=bikeshare_input('Which city would you like to see (chicago, new york or weshington)?\n',1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month=bikeshare_input('Which month would you like to see?\n ',2).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=bikeshare_input('Which day of week would you like to see?\n ',3).lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print("\nThe most common month: {}\n".format(most_month))

    # TO DO: display the most common day of week
    most_day_week = df['day_of_week'].mode()[0]
    print("The most common day of week: {}\n".format(most_day_week))

    # TO DO: display the most common start hour
    most_hour = df['hour'].mode()[0]
    print("The most common start hour: {}\n".format(most_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station:\n", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("The most commonly used end station:\n", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' ' + df['End Station']
    frequent_combination = df['combination'].mode()[0]
    print("The most frequent combination of station:\n" , frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time: {}\n".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time: {}\n".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("\nThe counts of user types:\n" + str(user_type_counts))

    # TO DO: Display counts of gender
    if 'Gender' in df:
       gender_counts = df['Gender'].value_counts()
       print("\nThe counts of gender:\n" + str(gender_counts))
    else:
       print('No Gender In This City Please Enter Another City')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       most_common_birth = df['Birth Year'].mode()[0]
       earliest_birth = df['Birth Year'].min()
       most_recent_birth = df['Birth Year'].max()
       print("\nThe most common year of birth: " + str(most_common_birth))
       print("The most recent year of birth: " + str(most_recent_birth))
       print("The earliest year of birth: " + str(earliest_birth))
    else:
       print('No Birth Year In This City Please Enter Another City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()

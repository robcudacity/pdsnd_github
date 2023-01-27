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
    print('Hello! My name is Rob Cocuzzo! Let\'s explore some US bikeshare data together!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input('Please input city name: ').lower()
    
    while city not in ['chicago','new_york_city', 'washington']:
        print ('Data for this city is unavailable. Please enter a valid city: ').lower()
        city = input('Please input city name: ').lower()


    # get user input for month (all, january, february, ... , june)


    month = input('Please input month name: ').lower()

    while month not in ['january', 'february', 'march', 'april', 'may', 'june','all']:
        print ('Please select a month from january through june, or type all to view all months: ').lower()
        month = input('Please input month name: ').lower()

    
    # get user input for day of week (all, monday, tuesday, ... sunday)

      day = input('Please input day of week name: ').lower()

    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','all']:
        print ('Please select a valid day of the week or type all to view all days: ').lower()
        day = input('Please input day of week name: ').lower()

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

    # extract month, day of week, hour from Start Time to create new columns
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

    # display the most common month
    
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print('Most Popular Month:', month)


    # display the most common day of week
     day = df['day_of_week'].mode()[0]
     print('Most Popular Day Of Week:', day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()



    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_start_station)

    

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most End Station:', popular_end_station)

    

    # display most frequent combination of start station and end station trip
    popular_trip = df['Start Station'] + ' to ' + df['End Station']
    print('Most popular trip: ' , {popular_trip.mode()[0]})

   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


def trip_duration_stats(df):
    from datetime import timedelta as td
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()



    # display mean travel time
    average_travel_duration = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    
    # Display counts of gender
    print('Gender Stats:')
    print(df['Gender'].value_counts())
        

    # Display earliest, most recent, and most common year of birth
    print('Birth Year Stats:')
    most_common_year = df['Birth Year'].mode()[0]
    print('Most Common Year:',most_common_year)
    most_recent_year = df['Birth Year'].max()
    print('Most Recent Year:',most_recent_year)
    earliest_year = df['Birth Year'].min()
    print('Earliest Year:',earliest_year)

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

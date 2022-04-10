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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Please choose one of the comming cities: chicago,new york city,washington:").lower()
        if city not in CITY_DATA:
             print("Please Enter a valid city name")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("Please Enter the month name from January to June. or Enter all:").lower()
        all_months=["january","february","march","april","may","june","all"]
        if month not in all_months:
            print("Please Enter a valid month name  or Enter all")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
    	day=input("Please Enter one day of the week like: monday,tuesday, .. sunday. or Enter all:").lower()
    	all_days=["saturday","sunday","monday","tuesday","wednsday","thursday","friday","all"]
    	if day not in all_days:
    		print("Please Enter a valid day of week. or Enter all")
    	else:
    		break

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
    # Read csv file
    df=pd.read_csv(CITY_DATA[city])
    # Convert start time to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # Extract day and month from the Start Time column 
    df['day_of_week']=df['Start Time'].dt.day#day_name
    df['month']=df['Start Time'].dt.month
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
#the function is not final answer it need a condition to make 5 row then if i enter yes it continue showing another 5 row else break
def show_data(df):
     view_data=input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
     if view_data == 'yes':
        x = 0
        while True:
            print(df.iloc[x:x+5])
            x+=5
            again=input("Do you wish to continue? yes or no:").lower()
            if again != 'yes':
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe Most common month is:',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe Most common day is:',common_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nMost commonly used start station is:',common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station is:',common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    common_trip = (df['Start Station']+" "+"to"+" "+df['End Station']).mode()[0]
    print("\nCommon trip is:",common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal travel time is:',total_travel_time)

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('\nAverage travel time is:',avg_travel_time)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count of user types:\n',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()
        print('\nCount of each gender is:\n',gender_count)  

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        #print("The earliest year is:{}.and the most recent year is:{}.and the common year is:{}.".format(earliest_year,recent_year,common_year))
        print(f'\nThe earliest year is : {earliest_year}')
        print(f'\nThe recent year is : {recent_year}')
        print(f'\nThe common year is : {common_year}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        show_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
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
    city = input('Please Enter the City : ').lower() # to make it case insensitive
    
    while city not in ['chicago', 'new_york_city', 'washington']:
          city = input ("Kindly enter a city between new_york_city, washington or chicago: ").lower()

        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('Please Enter the Month :').lower()
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input(' Kindly enter a month between january, february, march, april, may , june : ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please Enter the Day of the Week :').lower() # Taking the user input
    while day not in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input(' Kindly enter a day between monday, tuesday, wednesday , thursday , friday , saturday , and sunday : ').lower()
 

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
    data = pd.read_csv('{}.csv'.format(city))
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    data['End Time'] = pd.to_datetime(data['End Time'])
    
    # we need to get the month from the start time so we need to use dt.month
    data['month'] = data['Start Time'].dt.month
    
    while month != 'all':
        
        if month == 'january':
            month = 1
         # updating the month column with integers        
            data = data[data['month'] == month]
            break
            
        if month == 'february':
            month= 2
         # updating the month column with integers        
            data = data[data['month'] == month]            
            break
            
        if month== 'march':
            month= 3
         # updating the month column with integers        
            data = data[data['month'] == month]           
            break
            
        if month== 'april':
            month= 4
         # updating the month column with integers        
            data = data[data['month'] == month]            
            break
            
        if month == 'may':
            month = 5
         # updating the month column with integers        
            data = data[data['month'] == month]
            break
            
        if month == 'june':
            month = 6
         # updating the month column with integers        
            data = data[data['month'] == month]            
            break
            

    
    # we need to get the day from the start time so we need to use dt.strftime() since st.weekday_name didn't work with me
    data['weekday'] = data['Start Time'].dt.strftime("%A")
    
    if day != 'all':
        
        data['weekday']= data[data['weekday']== day.title()]

    return data    
    


def time_stats(data):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(" the most common month is :", data['month'].value_counts().idxmax())
    


    # TO DO: display the most common day of week
    print(" the most common day is :" , data['weekday'].value_counts().idxmax())
    


    # TO DO: display the most common start hour
    # we use dt.hour function to get the hours from start time column
    
    data['hour'] = data['Start Time'].dt.hour
    print("The most common hour is: ", data['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most common start station is :", data['Start Station'].value_counts().idxmax())


    # TO DO: display most commonly used end station
    print("the most common end station is :", data['End Station'].value_counts().idxmax())
    


    # TO DO: display most frequent combination of start station and end station trip
    data["Start-End station"] = data['Start Station'] +" - "+ data["End Station"]
    
    print("the most common start-end station trip is :", data['Start-End station'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # to get trip duration in hours we divide it by 3600
    
    print("total trip duration is : ", data['Trip Duration'].sum() / 3600.0)


    # TO DO: display mean travel time
    print("the avergae trip duration is : ", data['Trip Duration'].mean() / 3600.0)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def user_stats(data , city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(' Counts of user types are', data['User Type'].value_counts())
    

    if city != 'washington':
        # TO DO: Display counts of gender
        print("Counts of gender are ", data['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth

        print('the earliest year of birth is' , data['Birth Year'].min())
        print('the most recent year of birth is', data['Birth Year'].max())
        print(' the most common year of bearth is ', data['Birth Year'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data (data):
    
    answer = 'yes'
    x = 0
    while ( answer != 'no'):
        answer= input('\nWould you like to see the row data ? Enter yes or no.\n')
        if answer== 'no':
            break
        print(tabulate(data.iloc[np.arange(0+x,5+x)], headers ="keys"))
        x +=5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
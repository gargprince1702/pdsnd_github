import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
input_city = ["chicago","new york city","washington"]
input_month = ('january', 'february', 'march', 'april', 'may', 'june')
input_days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')
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
        city = str(input("Enter a city which you want to explore bikeshare data (chicago,new york city,washington)\n").strip().lower())
        if city not in ("chicago","new york city","washington"):
            print("wrong Input Please input city from this list {} ".format(input_city))
            continue;
        else:
            print("Nice Choice, I think you like {} ".format(city))
            break;
        # TO DO: get user input for month (all, january, february, ... , june)
        print("")
    while True:
        month = str(input("Enter a month which you want to explore bikeshare data ( january, february, ... , june)\n").strip().lower())
        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print("Invalid Input Please enter valid input e.g. {}".format(input_month))
            continue
        else:
            print("Your favourate Month is {}".format(month))
            break;
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print(" ")
    while True:
        day = str(input("Enter a day which you want to explore bikeshare data (sunday,monday,.....,saturday)\n").strip().lower())
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday'):
            print("Invalid Input Please enter valid input e.g. {}".format(input_days))
            continue
        else:
            print("Nice choice ,Your day selected is {}".format(day))
            break;
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
   
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])

    # create columns to display statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
   # df['Weekday'] = df['Start Time'].dt.day_name
    df['Weekday'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour


    df = df[df['Month'] == (input_month.index(month)+1)]

    df = df[df['Weekday'] == day.title()]
    
    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]
    print("most_common_month is = {}".format(input_month[most_common_month-1]))

    # TO DO: display the most common day of week
    most_common_day = df['Weekday'].mode()[0]
    print("The most common day of week is =  {}".format(most_common_day))

    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Hour'].mode()[0]
    print("most_common_start_hour is = {}".format(most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("most_common_start_station is {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("most_common_start_station is {}".format(most_common_start_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_comb = df['Start Station'] +" "+ df['End Station']
    print("most frequent combination of start station and end station trip is {}".format(most_frequent_comb.mode()[0]))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')
    print('Total Travel time is {} '.format(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')
    print('Mean travel time is {} .'.format(mean_travel_time))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""


    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)

    # Display counts of gender
    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender:")
        print(gender_distribution)
    except KeyError:
        print("We're sorry! There is no data of user genders for {}."
              .format(city.title()))

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one "
              "bike was born in: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one "
              "bike was born in: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst "
              "riders is: " + most_common_birth_year)
    except:
        print("We're sorry! There is no data of birth year for {}."
              .format(city.title()))

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)
   
def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """
    print('\nCalculating raw data...\n')
    start_time = time.time()
    count = 0

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 
        if answer=='yes':
            for i in range(count,len(df.index)):
                print(" ")
                print(df.iloc[count:count+5])
                print(" ")
                count+=5
                print("-"*100)
                break;
        else:
             break;
                
        # otherwise break
    
    print("\nThis took {} seconds.".format((time.time() - start_time)))    
    print('-'*40)
        
def main():
    while True:
        '''
        Here we get Input From user In which base that want to filter data
        '''
        city, month, day = get_filters() 
        while True:
            print("**********Your selected city,month,day is mentioned Below **********")
            print("Your Selected City  is = {}.".format(city))
            print("Your Selected Month is = {}.".format(month))
            print("Your Selected Day   is = {}".format(day))
            verify = str(input("If above show data is right enter 'y' else 'n'\n "))
            print("")
            if verify== 'n':
                print("*****************Let's Try Again**********")
                get_filters()
                continue
            else:
                print("\t\tGreat we are ready to go ahead >>>")
                break;
            
        print("*"*100)  
        #load the city,month and day which user provide    
        df = load_data(city, month, day)
        print()
        print()
        print("\t\tThe Bikeshare Data represent based on Your filter applied mentoned Below")
        # Display the Data based on user applied filter
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)
        # Ask For user to continue or not
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        else:
            print("\t\tLets Explore Bikeshare data again :)")
            print("Ready to Go >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


if __name__ == "__main__":
	main()

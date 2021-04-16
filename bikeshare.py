
import time
import pandas as pd
import numpy as np
import calendar
import datetime
import timeit

def intro_me(): #introduction about me, will appear when code is terminated
     """Gives a small introduction about the author of the code when code is terminated"""
     undr_scr()
     a="""
     Hello! My name is Ahmed Zribi and I got my Masters of Electrical and Computer Engineering from Canada.\n
     I am very passionate about this field which is why I am doing this nanodegree.\n
     It would be great if you can help recommend me to a job or even hire me!\n
     
     This is my linkedin:
     https://www.linkedin.com/in/ahmed-zribi-eng/
     
     I hope you like my code. I learned python only these 4 weeks! Thanks. \n
     
     PS: you can delete this comment by simply removing the intro_me() function in the main()
     """
     print(a)
     undr_scr()
    
def undr_scr(): #control the underscore length
    """Controls the underscore length of lines in the output. This is done by simple changing the interger value to what ever the user wants """
    print('_'*110)

def get_filters():
    """receives raw input for city and type of filter the user wants and displays the chosen options"""
    global month
    
    undr_scr()
    undr_scr()
    print('\n\nHello! Let\'s explore some US bikeshare data!\n')
    
    
#forces user to only enter what is given
    city=input("Would you like to see the data for Chicago, New York, or Washington? (not case sensitive): " )
    city=city.lower()

    while (city !="chicago") and (city !="new york") and (city !="washington"):
        city=input("Please enter Chicago, New York, or Washington only (not case sensitive): " )
        city=city.lower()
     
    
    
        
    filter_t=input("Would you like to filter the date by month, day, both or not at all? Type 'none' for no time filter: " )
    filter_t=filter_t.lower()

    while (filter_t !="none") and (filter_t !="month") and (filter_t !="day") and (filter_t !="both") :
        filter_t=input("Please enter correct value. Would you like to filter the date by month, day, both or not at all? Type 'none' for no time filter:" )
        filter_t=filter_t.lower()
     
    global month #to make it global in both this function and main function (define it the same for all)
    global day 
    global dday
    month=0 #to avoid unbound error in main function
    day=0
    
    
    
    if filter_t=='month':
        month=int(input("which month? Please type your response as an integer (e.g. 1=January). Months are available up to 6=June: " ))
        while month >6 or month <1:
            month=int(input("Only input months from 1=Jan to 6=June: "))
                
    elif filter_t=='day':
        day=int(input("which day? Please type your response as an integer (e.g. 1=Monday):" ))
        while day <1 or day >7:
            day=int(input("Only input days from 1=Monday to 7=Sunday:"))
        
    elif filter_t=='both':
        month=int(input("which month? Please type your response as an integer (e.g. 1=January). Months are available up to 6=June: " ))
        while month >6 or month <1:
            month=int(input("Only input months from 1=Jan to 6=June: "))

        day=int(input("which day? Please type your response as an integer (e.g. 1=Monday):" ))
        while day <1 or day >7:
            day=int(input("Only input days from 1=Monday to 7=Sunday:"))  
            
            
    
    print("\nCity Selected:",city.capitalize())
    print("Filter Selected:",filter_t.capitalize()) 
    
    if (filter_t=='month') or (filter_t=='both'):
        month_name = datetime.date(2015, month, 1).strftime('%B')
        print("Month Selected:",month_name)
    
    if (filter_t=='day') or (filter_t=='both'):
        months = ['Monday', 'Tuesday','wednesday','Thursday','Friday','Saturday','Sunday']
        dday=day-1
        print("Day Selected:",months[dday])

        
    undr_scr()
    return city,filter_t

def load_data(city,filter_t):
    """reads the desired file and filters the data based on month,day,none or both"""
    
    #make new york like filename default name
    if city =="new york":
        city ="new_york_city"
    
    #read the file from the directory
    df = pd.read_csv(city+".csv")
    
    #convert argument to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    if filter_t=='month':#filter by month
        df = df[df['month'] == month]
    
    if filter_t=='day':#filter by day
        df = df[df['day_of_week'] == dday]
        
    if filter_t=='both':#filter by month and day
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == dday]
        
    return df

def first5col(df): #shows you the first 5 rows of data if you want
    """displays the first 5 rows and keeps displaying 5 rows until the user asks the function to stop doing so"""

    f_rows=input("\nWould you like to display the first 5 rows of data? yes/no: " )
    f_rows=f_rows.lower()

    x=5
    while (f_rows !="yes") and (f_rows !="no"):
        f_rows=input("Enter Yes or no only: " )
        f_rows=f_rows.lower()
    while f_rows=='yes': 
        print(df.iloc[0:x,:])
        x+=5
        f_rows=input("Would you like to display 5 more rows? Enter yes to display 5 more rows and anything else to stop displaying: " )
        f_rows=f_rows.lower()



    undr_scr()
        
def time_stats(df,filter_t):
    """based on the dataframe filter, most common month,day and hour is displayed"""
    
    start_time = timeit.default_timer() #start counter
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     


    print('\n#1 Popular times of travel:')
    
    
    if filter_t =='none' or filter_t=='day': #most common month appears only for 'none' and 'day' filter option
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]

        month_num = popular_month
        month_name = datetime.date(2015, month_num, 1).strftime('%B')
        print(" Most common month:", month_name)

    if filter_t =='none' or filter_t=='month':  #most common day appears only for 'none' and 'month' filter option 
        df['day'] = df['Start Time'].dt.day_name()
        popular_day = df['day'].mode()[0]
        print(' Most common day:', popular_day)


    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0] 
    print(' Most common hour:', popular_hour)
    
    
    print("\nThis took %s seconds." % (timeit.default_timer() - start_time)) #end counter
    undr_scr()
    
def station_stats(df):
    """based on the dataframe filter, most common start,end and trips are displayed"""
    
    start_time = timeit.default_timer()
    
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    popular_start_station=df['Start Station'].mode()[0]
    popular_end_station=df['End Station'].mode()[0]
    st_en_comb=df.groupby(['Start Station','End Station']).size().idxmax()
    
    print('\n#2 Popular stations and trip:\n','Most common start station:', popular_start_station)
    print(' Most common end station:', popular_end_station)   
    print(' Most common trip from start to end:  ', st_en_comb)  
    
    print("\nThis took %s seconds." % (timeit.default_timer() - start_time))
    

    undr_scr()
    
def trip_duration_stats(df):
    """based on the dataframe filter, total and average time is displayed"""

    start_time = timeit.default_timer()
    
    total_ride_time = np.sum(df['Trip Duration']) 
    
    years,days,hours,minutes,seconds=sec2day(total_ride_time) #convert from seconds to years,hour,day,second format
    print('\n#3 Trip duration:\n',"Total travel time:",years,"years and",days,"days and",hours , "hours and", minutes, "minutes and", seconds, "seconds")

    avg_ride_time=total_ride_time//len(df)
    years,days,hours,minutes,seconds=sec2day(avg_ride_time)
    print(" Average travel time:", minutes, "minutes and", seconds, "seconds")
    
    print("\nThis took %s seconds." % (timeit.default_timer() - start_time))
    undr_scr()

def sec2day(x): #convert from seconds to years,hour,day,second format
 """convert from seconds to years,hour,day,second format"""
 years=x/(365.25*24*60*60)
 years_left=years-int(years)
 time = years_left * (365*24*60*60)
 years=int(years)


 time=int(time)
 days = time // (24 * 3600)
 time = time % (24 * 3600)
 hours = time // 3600
 time %= 3600
 minutes = time // 60
 time %= 60
 seconds = time

 return(years,days,hours,minutes,seconds) 

def user_stats(df,city):
    """based on the dataframe filter, user type is shown. For chicago and NYC it shows the gender and birth year information"""
    
    start_time = timeit.default_timer()    

    
    print("\n#4 User info:","\nCounts of each user type:")
    user_types = df['User Type'].value_counts()
    print(user_types)
    
    #print gender and birth year only for chicago and new_york_city
    if city != 'washington': # or    if city =='chicago' or city == 'new_york_city': 
        print('\nCounts of each gender:')
        user_types = df['Gender'].value_counts()
        print(user_types)

        earliest_year=df['Birth Year'].min()
        mrecent_year=df['Birth Year'].max()
        popular_year = df['Birth Year'].mode() 
        print('\nEarliest birth year:', int(earliest_year)) 
        print('Most recent birth year:', int(mrecent_year))
        print('Most common birth year:', int(popular_year))
        
        
    print("\nThis took %s seconds." % (timeit.default_timer() - start_time))
    undr_scr()




        
   
 
def main():
     """This is the main function and calls other functions to find the information needed. It also has a restart option."""
    
     city,filter_t=get_filters()


     df=load_data(city,filter_t)
    
    
     first5col(df)
        
     time_stats(df,filter_t)
    
     station_stats(df)
        
     trip_duration_stats(df)
    
     user_stats(df,city)
        
 #asks user if they want to restart or not
     restart = input('\nWould you like to restart? Enter yes to restart and anything else to end program.\n')
     if restart.lower() != 'yes':
            print('')     
     else:
         main()
            
     intro_me()#you can delete this, won't affect code, simply is introduction about me

          
    
if __name__ == "__main__": #tells python to start from here
	main()
    
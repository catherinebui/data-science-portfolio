# Bikeshare Trips

## Data Information

  Original data has information on member type, bike idenitification, start station, end station, timestamp, and duration in seconds.
  
  I then use external sources of data such as bike station latitude and longitude, census tract identification, and income level.
  
  I create new features such as duration in minutes, day, and time categories, estimated distance, census tract, income bins, 
  major user type, average duration in minutes, etc.

## Technologies

  Pandas, numpy, HTML, CSS, Javascript, Flask, Census Tract API, geopandas, matplotlib, seaborn, Tableau

## How to use the web app

  1. >>> . venv/bin/activate   
        -inside the app folder once you CD into the app folder
  2. >>> Pip install Flask 
  3. >>> Export FLASK_APP=main.py
  4. >>> Flask run
  5. Open the server link into a web browser
  
## Methodology

I only filter for trips within the Washington DC borders. There are trips going out of the Washington DC areas into nearby neighborhoods. Most of the trips are concentrated inside the Washington DC borders. 


## Findings 

1. High concentration of the rides start from a few census tracts around (-77.05-77.0) and (38.875-38.925). Columbus Circle / Union Station, Massachusetts Ave & Dupont Circle NW, Lincoln Memorial, 15th & P St NW, Jefferson Dr & 14th St SW are the most popular stations. 

2. Casual riders have a higher average duration than that of the member riders. On the same day, casual riders have average duration in 37.90 minutes so they are on average will have 2 dollars extra fee. On the same day, member riders have average duration in 11.84 minutes so they paid no extra fees.

    For rides that extend two consecutive days, casual riders took average 226.140183 in minutes and members took average 128.118178 in minutes so casual riders on average pay 46 dollars extra which is 54% of the annual membership cost and members on average pay 16.50 dollars extra.

    There are 19043331 same day trips and 74254 two days trips. 0.4% of trips are on consecutive days and 48.92% of those trips are from casual bikers. 99.6% of trips are on the same days.


3. Duration of the trip is longer in the weekend than it is in the weekdays.

4. Stations with majority casual riders are concentrated in one area of nearby tracts. This is area where Lincoln Memorial and government buildings are located.

5. Stations located in 120000+ income census tract has more casual users than member users at the start. 85.24% of trips with major casual users are in 120000+ census tracts. And the casual users would end up in different end stations all around Washington DC metro area.

6. There are more member trips on the weekdays than there are member trips on the weekends.

7. Low income tracts (less than 30000 median income) tend to be near the north and east borders of the Washington DC area.

8. 89.59% of all trips are under 30 minutes so they didn't have to pay an additional fee, just the initial fee. This means that 89.59% of all trips have 0 extra fare.

    3.05% of the member trips in 2016 are more than 30 minutes and have additional fees. This means that 96.95% of the member trips don't have extra fees.

    39.38% of the casual trips in 2016 are more than 30 minutes and have additional fees. This means that 60.62% of casual trips don't have extra fees.


9. Casual bikers pay more additional fees than member do on additional fees.

    Casual bikers' maximum additional fees goes up to 370 dollars and members' maximum additional fees goes up to 280.50 dollars.

10. Member bikers take less longer than 30 minutes trips than casual bikers so they benefit from no-charge additional trips. Casual bikers are more likely to be subject to additional costs.

11. Duration of trips began to decrease starting July. It began to increase at the beginning of the year-January until July. It peaked in April and July. The historical expected average temperature goes from 35F in January increasing to 80F in July. It peaked during summer, and began decreasing to 40F in December. This expected average temperature trend is correlated to the trend of duration of trips. So during warm weather, bikers stay out longer than they do in cold weather.

    Thus, July is the most popular month for trips, and January is the least popular month. 

12. No trips incur a lost fee of 1200 dollars for going over 24 hours.

13. There's no linear relationship between additional fare and estimated great circle distance from start station to end station. There's no linear relationship between duration and estimated great circle distance from start station to end station. This must mean that bikers go longer trips closeby less than 10 miles.
    Most trips are less than 10 miles.

14. 10AM-4PM is the most popular time for casual trips.

15. There are less trips when it rains so precipitation affects usage of bikes.

16. Using Tableau, I was able to visualize the distribution of casual and member users at each station. It was then that I realized that I should filter for the major user at each station and found that there is a clustering of casual bikers in one area while member bikers are spread out.

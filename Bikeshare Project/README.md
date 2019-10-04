# Bikeshare Trips

## Data Information

  Original data has information on member type, bike idenitification, start station, end station, timestamp, and duration in seconds.
  
  I then use external sources of data such as bike station latitude and longitude, census tract identification, and income level.
  
  I create new features such as duration in minutes, day, and time categories, estimated distance, census tract, income bins, 
  major user type, average duration in minutes, etc.

## Technologies

  Pandas, numpy, HTML, CSS, Javascript, Flask, Census Tract API, geopandas, matplotlib, seaborn

## How to use the web app

  1. >>> . venv/bin/activate   
        -inside the app folder once you CD into the app folder
  2. >>> Pip install Flask 
  3. >>> Export FLASK_APP=main.py
  4. >>> Flask run
  5. Open the server link into a web browser

## Findings

1. High concentration of the rides start from a few census tracts around (-77.05-77.0) and (38.875-38.925)

2. Casual riders have a higher average duration than that of the member rider.

3. Duration of the trip is longer in the weekend than it is in the weekdays.

4. Stations with majority casual riders are concentrated in one area of nearby tracts. This is area where Lincoln Memorial and government buildings are located.

5. Stations located in 120000+ income census tract has more casual users than member users at the start. And the casual users would end up in different end stations all around Washington DC metro area.

6. There are more member trips on the weekdays than there are member trips on the weekends.

7. Low income tracts (less than 30000 median income) tend to be near the north and east borders of the Washington DC area.

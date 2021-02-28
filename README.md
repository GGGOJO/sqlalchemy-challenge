# sqlalchemy-challenge
This week's challenge had two parts. 
* Use sqlalchemy for Hawaii climate analysis 
* Use Flask to create an API for the Hawaii climate analysis.

# PART 1 - CLIMATE ANALYSIS AND EXPLORATION
In the jupyter notebook file named: "SQLAlchemy_Challenge_Surfs_Up.ipynb", I needed to set up the data to conduct the analysis:

Data was pulled from the hawaii.sqlite database file (stored in Resourses. Also in this same folder are two separate CSV files because there are two data tables called Measurement and Stations). 

I completed the following: 
* used SQLalchemy to create_engine to connect to the sqlite database.
* use SQLalchemy to automap_base() to reflect the database tables into classes for python and then save a reference to those classes, which were named "Measurement" and "Station."
* Link Python to the database by creating an SQLAlchemy session.
* Close out the session at the end of the notebook.

Two Analyses on temperature and then station for the last year of data.

## PRECIPITATION ANALYSIS
I did the following:
* found the most recent date in the data set, which was 2017-08-23
* With this date, retrieved the last 12 months of precipitation data by querying the 12 preceding months of data. 
* Selected only the date and prcp values.
* Loaded the query results into a Pandas DataFrame and set the index to the date column.
* Sorted the DataFrame values by date.
* Plotted the results using the DataFrame plot method.
* Used Pandas to print the summary statistics for the precipitation data.

## STATION ANALYSIS
I completed the following:
* Designed a query to calculate the total number of stations in the dataset.
* Designed a query to find the most active stations (i.e. which stations have the most rows?).
  * Listed the stations and observation counts in descending order.
  * Found the station id has the highest number of observations? The answer is "USC00519281" station.
  * Used this most active station id to calculate the lowest, highest, and average temperature by using SQLAlchemy functions: func.min, func.avg., func.max.
* Designed a session query to retrieve the last 12 months of temperature observation data (TOBS).
  * Filtered by the station with the highest number of observations.
  * Queried the last 12 months of temperature observation data for this station.
  * Plot the results as a histogram with bins=12.

# PART 2 - CLIMATE APP
Once the initial analysis was completed, I designed a Flask API based on the queries.

The following Flask Routes were created along with instructions on the data it should return in a JSON response object (used jsonify):
* /
  *  Home page
  *  List of all routes for this API

* /api/v1.0/precipitation
  *  Convert the query to a dictionary using 'date' as the key and 'prcp' as the value
  *  Return the JSON representation of your dictionary

* /api/v1.0/stations
  *  Return a JSON list of stations from the dataset

* /api/v1.0/tobs
  *  Query the dates and temperature observations of the most active station for the last year of data
  *  Return a JSON list of temperature observations (TOBS) for the previous year

* /api/v1.0/<start> and /api/v1.0/<start>/<end>
  * Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
  * When the user gives the start date only, calculate and return the TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
  * When the user give both the start and the end dates, calculate adn return the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.





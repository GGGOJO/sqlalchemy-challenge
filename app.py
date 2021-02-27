import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Database SetUp
engine = create_engine("sqlite:///./Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(bind=engine)

# Flask setup
app = Flask(__name__)

# Flask routes endpoints home page and all routes that are available


@app.route("/")
def welcome():
    return(
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available API Data Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/ api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
    )

# PRECIPITATION: First API route
# Query precipitation data using date as the key
# Return the precipitation data from last year in JSON reprepresentation


@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()

    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# STATIONS: Second API route
# Return a JSON list of stations from the dataset


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()

    stations = list(np.ravel(results))
    return jsonify(stations)

# TOBS (Temperature Obervations): Third API route
# For the most active station, query the dates and tob for the last year of data
# Return a JSON list of tob for the last year of data


@app.route("/api/v1.0/tobs")
def temp_last_year():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    temps = list(np.ravel(results))
    return jsonify(temps)

# TEMP STATISTICS: Fourth and Fifth API route
# Calculate the temperature's minimum (TMIN), average (TAVG), and maximum (TMAX) for any given date.
# As a dynamic API, user inputs the start date in the API url.
# User could also input both start and end dates in the API url.


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(
        Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()

        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    temps = list(np.ravel(results))
    return jsonify(temps)


if __name__ == '__main__':
    app.run()

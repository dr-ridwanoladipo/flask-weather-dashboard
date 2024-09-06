from flask import Flask, render_template
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load station data from CSV
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    """
    Render the home page with the list of stations.
    """
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    """
    Get the temperature for a specific station and date.

    Args:
        station (str): Station ID.
        date (str): Date in YYYY-MM-DD format.

    Returns:
        dict: Station ID, date, and temperature in Celsius.
    """
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }


@app.route("/api/v1/<station>")
def all_data(station):
    """
    Get all temperature data for a specific station.

    Args:
        station (str): Station ID.

    Returns:
        list of dict: All temperature records for the specified station.
    """
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    """
    Get yearly temperature data for a specific station and year.

    Args:
        station (str): Station ID.
        year (str): Year in YYYY format.

    Returns:
        list of dict: Temperature records for the specified year.
    """
    filename = f"data_small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(str(year))].to_dict(orient="records")
    return result


if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, port=5001)



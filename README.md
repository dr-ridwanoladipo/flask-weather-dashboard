# Weather Data API

This Flask application provides a RESTful API to access historical weather data for various weather stations across Europe. It supports retrieving temperature information for specific dates, stations, and years. 

## Features

- **Home Page**: Displays a table of weather stations.
- **API Endpoints**:
  - `/api/v1/<station>/<date>`: Get temperature for a specific station and date.
  - `/api/v1/<station>`: Get all temperature data for a specific station.
  - `/api/v1/yearly/<station>/<year>`: Get temperature data for a specific station and year.

The data used in this project covers weather stations throughout Europe.

## Example URLs

- **Get temperature for a specific date**: `http://127.0.0.1:5001/api/v1/10/1988-10-25`
- **Get all data for a station**: `http://127.0.0.1:5001/api/v1/10`
- **Get yearly data for a station**: `http://127.0.0.1:5001/api/v1/yearly/10/1998`

This project demonstrates proficiency in Flask, API development, and handling weather data.

## Contact

For more details about my work or to discuss potential opportunities, feel free to reach out via [LinkedIn](#),
[GitHub profile](#), or email me at [dr.ridwan.oladipo@gmail.com](mailto:your.email@example.com).

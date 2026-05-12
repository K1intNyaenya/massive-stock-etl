# Massive Stock ETL

A complete Extract-Transform-Load (ETL) pipeline for retrieving and processing stock exchange data from the massive.com API and loading it into a PostgreSQL database.

## Project Overview

This project implements an automated ETL pipeline that:
- **Extracts** stock exchange data from the Polygon.io API
- **Transforms** the raw JSON data into a clean, structured format
- **Loads** the processed data into a PostgreSQL database (Aiven Service)

## Pipeline Architecture

```
massive.com API → Extract → raw_data.json → Transform → PostgreSQL Database
```

### Pipeline Steps

1. **Extract** (`extract.py`)
   - Fetches stock exchange data from massive.com API
   - Requires an API key for authentication
   - Saves raw response to `raw_data.json`

2. **Transform** (`transform.py`)
   - Loads raw JSON data
   - Normalizes nested JSON structure into a pandas DataFrame
   - Cleans and renames columns for clarity
   - Handles missing values
   - Selects relevant fields: `exchange_id`, `exchange_name`, `exchange_type`, `asset_class`, `locale`, `mic_code`, `operating_mic_code`, `participant_id`, `website`

3. **Load** (`load.py`)
   - Loads transformed data into PostgreSQL
   - Creates/replaces the `exchanges` table
   - Uses SQLAlchemy for database connectivity

## Setup & Installation

### Prerequisites
- Python 3.10+
- PostgreSQL database (or Aiven PostgreSQL instance)
- massive.com API key

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd massive-stock-etl
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv massenv
   source massenv/bin/activate  # On Windows: massenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root:
   ```
   API_KEY=<your-polygon-io-api-key>
   AIVEN_DB_URL=postgresql://<user>:<password>@<host>:<port>/<database>
   ```

## Usage

### Run the entire pipeline
```bash
python load.py
```

### Run individual steps

Extract data from API:
```bash
python extract.py
```

Transform raw data:
```bash
python transform.py
```

Load data to database:
```bash
python load.py
```

## Project Structure

```
massive-stock-etl/
├── extract.py           # Data extraction from Polygon.io API
├── transform.py         # Data transformation and cleaning
├── load.py             # Data loading to PostgreSQL
├── raw_data.json       # Raw API response (generated)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── massenv/            # Virtual environment directory
```

## Dependencies

- **pandas** - Data manipulation and analysis
- **requests** - HTTP client for API calls
- **SQLAlchemy** - Database ORM and connectivity
- **psycopg2-binary** - PostgreSQL adapter
- **python-dotenv** - Environment variable management
- **polygon-api-client** - Polygon.io API client
- **numpy**, **pytz**, **python-dateutil** - Data processing utilities

See `requirements.txt` for complete list and versions.

## Database Schema

The pipeline creates an `exchanges` table with the following columns:
- `exchange_id` - Unique exchange identifier
- `exchange_name` - Exchange name
- `exchange_type` - Type of exchange
- `asset_class` - Asset class (e.g., stocks)
- `locale` - Locale/region
- `mic_code` - Market Identifier Code
- `operating_mic_code` - Operating MIC code
- `participant_id` - Participant identifier
- `website` - Exchange website URL

## Configuration

### Environment Variables
- `API_KEY` - Polygon.io API key for data access
- `AIVEN_DB_URL` - PostgreSQL connection URL for Aiven database

### Data Processing
Column selection, renaming, and null value handling are configured in `transform.py`.

## Notes

- Raw data is saved to `raw_data.json` for inspection and debugging
- Missing columns are automatically filled with NaN values during transformation
- Null values in the final dataset are replaced with "N/A" for consistency
- Database operations use `if_exists="replace"` to overwrite existing data

## Author

Created as part of a data engineering project for stock market data analysis.

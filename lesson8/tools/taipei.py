import requests
from requests import Response
from requests.exceptions import RequestException, HTTPError
from io import StringIO
from csv import DictReader
import streamlit as st

@st.cache_data
def get_youbikes() -> list[dict]:
    """
    Fetch YouBike station data from New Taipei City open data portal.
    Returns:
        list[dict]: List of YouBike stations with their details
    """
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        response: Response = requests.request('GET', url)
        response.raise_for_status()
    except HTTPError:
        raise Exception("Server Error")
    except RequestException:
        raise Exception("Connection Error")
    else:
        print('Success')
        
        csv_data = StringIO(response.text)
        reader = DictReader(csv_data)
        bike_stations: list[dict] = list(reader)
        return bike_stations

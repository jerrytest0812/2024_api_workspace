import requests
from requests import Response
from requests.exceptions import RequestException , HTTPError
from io import StringIO
from csv import DictReader

def get_youbikes()->list[dict]:
    url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000'

    try:
        r: Response = requests.request('GET',url)
        r.raise_for_status()
    except HTTPError as e:
        raise Exception("Server Error")
    except RequestException as e:
        return Exception("Connection Error")
    else:
        print('Success')

        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader:list[dict] = list(reader)
        return list_reader
import pandas as pd
import requests
from config import api_key
import json

url="https://api.open.fec.gov/v1/candidates/"
params={
    "has_raised_funds":True,
    "sort_null_only":False,
    "election_year":2018,
    "office":"S",
    "api_key":api_key,
    "party":"Dem"
}
data=requests.get(url=url,params=params).json()

candidate_page_1=pd.DataFrame(data["results"])
candidate_page_1.head()

url="https://api.open.fec.gov/v1/candidates/"
params_2={
    "has_raised_funds":True,
    "sort_null_only":False,
    "election_year":2018,
    "office":"S",
    "api_key":api_key,
    "party":"Dem",
    "page":2
}
page_2=requests.get(url=url,params=params_2).json()

url="https://api.open.fec.gov/v1/candidates/"
params_3={
    "has_raised_funds":True,
    "sort_null_only":False,
    "election_year":2018,
    "office":"S",
    "api_key":api_key,
    "party":"Dem",
    "page":3
}
page_3=requests.get(url=url,params=params_3).json()
candidate_page_3=pd.DataFrame(page_3["results"])
candidate_page_3.head()

url="https://api.open.fec.gov/v1/candidates/"
params_4={
    "has_raised_funds":True,
    "sort_null_only":False,
    "election_year":2018,
    "office":"S",
    "api_key":api_key,
    "party":"Dem",
    "page":4
}
page_4=requests.get(url=url,params=params_4).json()
candidate_page_4=pd.DataFrame(page_4["results"])
candidate_page_4.head()

url="https://api.open.fec.gov/v1/candidates/"
params_5={
    "has_raised_funds":True,
    "sort_null_only":False,
    "election_year":2018,
    "office":"S",
    "api_key":api_key,
    "party":"Dem",
    "page":5
}
page_5=requests.get(url=url,params=params_5).json()
candidate_page_5=pd.DataFrame(page_5["results"])
candidate_page_5.head()


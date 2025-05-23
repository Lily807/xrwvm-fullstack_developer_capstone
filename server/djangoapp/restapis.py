# Uncomment the imports below before you add the function code
import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    log = logging.getLogger('urllib3')
    log.setLevel(logging.DEBUG)
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"
            request_url = backend_url+endpoint+"?"+params
    else:
        request_url = backend_url+endpoint

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print(f"response={response}")
        return response.json()
    except Exception as err:
        print(f"Exception occurred {err=} of type {type(err)}")


# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        print(f"response={response}")
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")


# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    print("POST from {} ".format(request_url))
    try:
        response = requests.post(request_url, json=data_dict)
        print(f"response={response}")
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Exception occurred {err=} of type {type(err)}")

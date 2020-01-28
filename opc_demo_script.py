# @author ben matare ben.a.matare@gmail.com
# script to print out kanye west qoutes

import requests

BASE_URL: str = 'https://api.kanye.rest/'

## Function that prints out a qoute that kanye has said at some point in time
# creates a text box around it to make it pretty
#
# @param qoute str qoute that kanye has actually said
#
# @returns None
def output_kanye_qoute(qoute: str):
    rows = len(qoute)
    height = ''.join(['+'] + ['-' * rows] + ['+'])
    final_output = height + '\n'"|"+ qoute + "|"'\n' + height
    print(final_output)

## Function to take the response and extract the qoute from the response object
# 
# @param response_object dict the http response object
#
# returns None
def find_out_what_kanye_is_saying(response_object: dict):
    kanye_west_no_qoute = "i ain't got nothing"

    response_object_to_json = response_object.json()
    
    ## uncomment this out to simulate if the response we got back was empty
    # response_object_to_json = []

    kanye_west_qoute = response_object_to_json['quote']

    if not response_object_to_json:
        print(f"Response empty :: response={response_object_to_json}")
        output_kanye_qoute(kanye_west_no_qoute)
    else:
        output_kanye_qoute(kanye_west_qoute)

## Function that makes the http request to an endpoint 
#
# returns None
def error_and_exception_handling_request():
    try:
        response = requests.get(BASE_URL)

        # enables us to have http error codes throw exceptions
        response.raise_for_status()

        ## Uncomment these out to simulate different types of errors!
        
        # raise requests.exceptions.Timeout('Simulated timeout error')
        # raise requests.exceptions.HTTPError('Simulated HTTP error')
        # raise requests.exceptions.RequestException('Simulated request error')
        # raise requests.exceptions.ConnectionError('Simulated connection error')

    except requests.HTTPError as http_error:
        print(f"HTTP Error :: status_code={response.status_code}, error={str(http_error)}, url={BASE_URL}")

    except requests.ConnectionError as connection_error:
        print(f"Connection Error :: status_code={response.status_code}, error={str(connection_error)}, url={BASE_URL}")

    except requests.Timeout as timeout_error:
        print(f"Timeout Error :: status_code={response.status_code}, error={str(timeout_error)}, url={BASE_URL}")

    except requests.RequestException as requests_lib_error:
        print(f"Requests Library Exception Error, shutting down :: status_code={response.status_code}")

    # we didn't hit any of the errors/exceptions we were looking at, so lets find out what kanye is saying    
    else:
        print(f'Connection Success :: status_code={response.status_code}, response={response.json()}\n')
        find_out_what_kanye_is_saying(response)


# execute our script
error_and_exception_handling_request()
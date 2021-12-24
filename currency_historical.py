import json,requests

def lambda_handler(event, context):

    date = event["queryStringParameters"]["date"]
    base_currency = event["queryStringParameters"]["base_currency"]
    url = f'http://api.exchangerate.host/{date}?symbols=ARS,EUR&base={base_currency}'
    data = requests.get(url).json()
    del(data['motd'])
    return {
          'statusCode': 200,
            'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
          'body':json.dumps(data)
    }    
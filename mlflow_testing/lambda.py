import json
import urllib3

url = 'http://ec2-3-91-192-121.compute-1.amazonaws.com:8887/invocations'
request = json.dumps({
    "dataframe_split": {
    "columns": ["lat", "lon"],
    "data": [[0,0]]
        }
})

def lambda_handler(event, context):
    
    lon_in = float(event['queryStringParameters']['lon'])
    lat_in = float(event['queryStringParameters']['lat'])
    
    print("lon = " + str(lon_in))
    print("lat = " + str(lat_in))
    
    request = json.dumps({
        "dataframe_split": {
        "columns": ["lat", "lon"],
        "data": [[lon_in, lat_in]]
            }
    })
    
    http = urllib3.PoolManager()
    response = http.request("POST", url,
        headers={'Content-Type': 'application/json'},
        body=request)
        
    print(response.data)
    return {
        'statusCode': 200,
        'body': response.data
    }

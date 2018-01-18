import urllib.request # Python URL functions # Python URL functions
authkey = "193013AKQsrVRodlk5a5a0c23" # Your authentication key.

mobiles = "9550266821,9652413030" # Multiple mobiles numbers separated by comma.

message = "Results ochinay chusko " # Your message to send.

sender = "112233" # Sender ID,While using route4 sender id should be 6 characters long.

route = "default" # Define route

# Prepare you post parameters
values = {
          'authkey' : authkey,
          'mobiles' : mobiles,
          'message' : message,
          'sender' : sender,
          'route' : route
          }

url = "https://control.msg91.com/api/sendhttp.php" # API URL

postdata = urllib.parse.urlencode(values).encode("utf-8") # URL encoding the data here.

req = urllib.request.Request(url, postdata)

response = urllib.request.urlopen(req)

output = response.read() # Get Response

print(output)

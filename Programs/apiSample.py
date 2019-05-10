from requests import get

res = get("http://172.31.31.79:10080/v2/booking/scheduled/allocateVehicle").text
print("Response of the get request = " ,format(res))




res.add_header( 'Authorization', 'AbC123' )

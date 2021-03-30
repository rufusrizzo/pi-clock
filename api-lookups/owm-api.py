
import json
import requests

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=22980,US&appid=d544fd8d46b15dd931ef2f5e3308279c')
owm_json = r.json()

owmw = owm_json['main']

temp = owmw['temp']
tempf  = 9/5*(temp - 273) + 32 
temp_f = int(format(tempf , ".0f"))
temp_max = owmw['temp_max']
tempf_max  = 9/5*(temp_max - 273) + 32 
temp_f_max = int(format(tempf_max , ".0f"))
temp_min = owmw['temp_min']
tempf_min  = 9/5*(temp_min - 273) + 32 
temp_f_min = int(format(tempf_min , ".0f"))

print("Temp")
print(temp_f)
print("Temp Max")
print(temp_f_max)
print("Temp Min")
print(temp_f_min)

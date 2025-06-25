// AI Generated: create an agent to get the current weather

local TOOL_DEFINITION
TOOL_DEFINITION = '{' + ;
  '"type":"function",' + ;
  '"function":{' + ;
    '"name":"get_current_weather",' + ;
    '"description":"Fetches the current weather for a specified location",' + ;
    '"parameters":{' + ;
      '"type":"object",' + ;
      '"properties":{' + ;
        '"location":{' + ;
          '"type":"string",' + ;
          '"description":"The location for which to fetch the weather"' + ;
        '}' + ;
      '},' + ;
      '"required":["location"]' + ;
    '}' + ;
  '}' + ;
'}'

function get_current_weather(location)
    local nr, url, data, json, success

    url = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=c23abaadb797975a3724676833c799a3&units=metric"
    data = "{}" // no data to post for GET, but postData requires data parameter

    nr = createObject("networkrequest")
    success = nr.postData(url, data) // postData returns true if successful

    if success
        data = json_decode( nr.responseText )
        ? str_expand("The weather in {location} is {data['weather'][1].description};
with a temperature of {data['main'].temp}c and a wind speed of {data['wind'].speed}mph")
    else
        ? "Failed to get weather data"
    endif
endfunc

* call the function for testing
//? get_current_weather("London") 




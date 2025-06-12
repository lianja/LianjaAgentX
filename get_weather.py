# Add this line to agents.conf
# get_weather.py=get_current_weather(location)

# The TOOL_DEFINITION is used by the AI Assistant
TOOL_DEFINITION = """
{
  "type":"function",
  "function":{
	  "name": "get_current_weather",
	  "description": "Fetches the current weather for a specified location",
	  "parameters": {
	    "type": "object",
	    "properties": {
	      "location": {
	        "type": "string",
	        "description": "The location for which to fetch the weather"
	      }
	    },
	    "required": ["location"]
	  }
  }
}
"""

# The AGENT_DEFINITION is used when ChatGPT calls a tool on MCP server
AGENT_DEFINITION = """
{
    "name": "get_weather",
    "description": "Get the current weather for a location.",
    "input_schema": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city or place to get the weather for"
        }
      },
      "required": ["location"]
    },
    "output_schema": {
      "type": "object",
      "properties": {
        "temperature": {
          "type": "string"
        },
        "condition": {
          "type": "string"
        }
      }
    }
}
"""

import requests

def get_current_weather(location):
    api_key = "c23abaadb797975a3724676833c799a3"  
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
    	data = response.json()
    	result = f"""
The weather in {location} is {data['weather'][0]['description']} \
with a temperature of {data['main']['temp']}c and a wind speed of \
{data['wind']['speed']}mph\
    	"""
    	return result
    else:
        return "Unable to fetch weather data"



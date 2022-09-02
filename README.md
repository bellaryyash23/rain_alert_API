# ☔Rain Alert🌧 Messaging Program using Requests API of Python

🌟A python program which makes use of API call to fetch weather data for next 12 hours and alerts the user in case there is possisibility of rainfall. The alert 
message is sent to user via their mobile number.

👉In the 'main.py' file, the OpenWeather API is used to GET the weather data for next 12 hours. The received data is then formated and the required fields are only
extracted and stored in a list.

👉Now, from the API documentation the condition for rainfall is found and the list containing the data is itterated and the condition is checked for each hour data field.
If the condition is satisfied a variable is initalized to track its trueness.

👉Next for the alert to be sent, the use of Twilio API & Messaging service is done which generates a Virtual Number to send message to the users number on each proper
API call.

👉The messsage body contains the alert message suggesting the user to carry an umberella. 

![Message Sample](https://github.com/bellaryyash23/rain_alert_API/blob/master/sample.jpeg?raw=true)

👆Sample of Alert Message received on Mobile👆

👉This program run is done daily using the PythonAnywhere platform which hosts python codes and runs them daily on the specified time.

👉Also, the use of Environment Variables is done to ensure safety and security of the sensitive parts of program like the API KEY or the Authenticaton Token.

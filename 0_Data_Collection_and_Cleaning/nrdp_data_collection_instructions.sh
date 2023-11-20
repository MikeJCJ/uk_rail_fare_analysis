# This file contains the steps and commands needed to retrieve the data from the National Rail Data Portal (NRDP)
# https://wiki.openraildata.com/DTD This website contains a rough guide of the process, but the specific commands executed from the command line will be below.

# Step 1 - Create an account with NRDP - https://opendata.nationalrail.co.uk/

# Step 2 - Generate the auth token
    # Paste into terminal
    curl --location --request POST 'https://opendata.nationalrail.co.uk/authenticate' --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode 'username=user1@gmail.com' --data-urlencode 'password=P@55w0rd1'

    # The token will be recieved in the following format:

        {
    "username": "user1@gmail.com",
    "roles": {
        "ROLE_USER": true,
        "ROLE_DTD": true
    },
    "token": "user1@gmail.com:1491312310772:56c56baa3e56d35ff0ede4a6aad1bcfb" # <---- The token needed is here, note personalised token for the next step
    
    # Note: if curl command is not accepted, try running 'Remove-item alias:curl' to fix the issue
    # This token expires 1 hour after the command is run

#Step 3 - Retrieve chosen data source
    # Fares: https://opendata.nationalrail.co.uk/api/staticfeeds/2.0/fares
    # Routeing: https://opendata.nationalrail.co.uk/api/staticfeeds/2.0/routeing
    # Timetable: https://opendata.nationalrail.co.uk/api/staticfeeds/3.0/timetable

    #Paste into terminal
    curl --header User-Agent: --header "Content-Type: application/json" --header "X-Auth-Token: user1@gmail.com:1491312310772:56c56baa3e56d35ff0ede4a6aad1bcfb" https://opendata.nationalrail.co.ukhttps://opendata.nationalrail.co.uk/api/staticfeeds/2.0/routeing --output rail_data.zip
    # ^Replace with auth token from previous stage

#Step 4 - Data is now stored in the zip file
    # If zip file does not open through File Explorer, try using 7zip
    # Data files can be opened as txt files

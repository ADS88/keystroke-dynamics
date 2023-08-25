## What is this application?

This application is designed to determine what other application users someone types most similarly to.

## How does it work?

A user submits a test and is compared to all other previous users based on a combination of typing speed (milliseconds per character) and median dwell time (How long they hold down a key for). The server sends back the names of the three most similar previous users.

## How can I run it?

### Using Docker (Recommended)

The easiest way to run this application locally is using docker.

1. Ensure you have docker installed on your computer
2. Ensure the docker daemon is running (e.g launch docker desktop on mac)
3. In the root directory of the project, run the command '**docker-compose up**'. This will start both the frontend, and the backend of the project. Hot reloading is supported, meaning changes made locally will be reflected in the running application.
4. Once the application is running you can navigate to **http://localhost:5173/** to see the application in action!

### Without Docker (Mac/Linux)

#### Server

1. Install Python 3.11
2. cd to the server directory
3. Create a virtual environment: **python3 -m venv venv**
4. Activate the virtual environment: **source venv/bin/activate**
5. Update your virtual environments pip: **python -m pip install --upgrade pip**
6. Install required dependencies: **pip3 install -r requirements.txt**
7. Start the development server in the server/src directory with the command: **python -m flask run**

#### Client

1. Install Node 20
2. cd into the **client** directory
3. Install required dependencies: **'npm install'**
4. Start the development server: **'npm run dev'**
5. Navigate to **http://localhost:5173/** to see the application in action!

### Without Docker (Other OS)

You should be able to follow same general process as Mac/Linux, however you will need to do some googling for the exact commands to run :).

## Future improvements

### Frontend

- Loading and error states to better show the user the state of the app
- Add testing of user input

### Backend

- Validate strucuture of received requests
- Potentially rename POST sentence endpoint
- Make users not case sensitive
- Deal with extremely unusual data (e.g 1 minute break between characters, only keydowns...)
- Look into not enabling cors for everything
- Don't store everything in memory :)

### Algorithm

- I have assumed the test data is good quality and a realistic representation of. To improve the accuracy of testing, it would
  be good to have a larger dataset, and have the dataset use the same sentences as the application. It would also be nice to
  have the dataset show other events e.g backspaces.
- Investigate different metrics of determining who is typing. Some things that may be interesting to look at are
  - Timing between letter pairs.
  - Flight time: Time between key presses
  - Overlapping: between key presses
  - Number of errors
  - Capital letters and special characters: Do they use caps lock or shift? What about number pad or other unique characters?
  - Pressure of keyboard press (mobile only?)
  - Unique behaviour to users significantly out of the ordinary e.g maybe someone holds down a key for much longer than others?
- Improve the current algorithm
  - Compare the dwell time of each character, rather than the median overall dwell time?
  - Look into grouping by some metric so we don't need to compare a user to every other user. E.g it doesn't really make sense to compare some who types 10wpm to someone who types 100wpm

### Infrastructure

- Register a domain name
- Use HTTPS
- Use a production server for flask (rather than the development one)
- Investigate using cloudfront rather than ecs for frontend

### CI/CD

- Add linting as part of test pipeline
- Automate updating the hosted application on pushes

## What is this application?

This application is designed to determine what other application users someone types most similarly to.

## How can I run it?

### Using Docker (Recommended)

The easiest way to run this application locally is using docker. In the root directory of the project, run the command '**docker-compose up**'. This will start both the frontend, and the backend of the project. Hot reloading is supported, meaning changes made locally will be reflected in the running application.

Once the application is running you can navigate to **http://localhost:5173/** to see the application in action!

### Without Docker (Mac/Linux)

#### Server

1. Install Python 3.11
2. cd to the server directory
3. Create a virtual environment: **python3 -m venv venv**
4. Activate the virtual environment: **source venv/bin/activate**
5. Update your virtual environments pip: **python -m pip install --upgrade pip**
6. Install required dependencies: **pip3 install -r requirements.txt**
7. Start the development server with the command: **python -m flask run**

#### Client

1. Install Node 20
2. cd into the **client** directory
3. Install required dependencies: **'npm install'**
4. Start the development server: **'npm run dev'**
5. Navigate to **http://localhost:5173/** to see the application in action!

### Without Docker (Other OS)

You should be able to follow same general process as Mac/Linux, however you will need to do some googling for the exact commands to run :).

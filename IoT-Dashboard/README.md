# IoT Dashboard Project

## Description

This project is an IoT Dashboard designed to monitor a user's IoT devices by providing real-time data visualization of the relevant system variables.

Although the data is fake and created on the client-side, a server-side login authentication algorithm has been implemented using a MongoDB database.


![dashboard](https://github.com/danielzanelli/Portfolio/assets/83187517/3c581b63-bbfb-4647-8d70-a4ac742b96f4)


## Live Demo

You can try out a live demo of the dasboard by going to <https://demo.automatype.com> and logging in using the following credentials:

    Username: 'user'
    Password: '123456'

## Features

- Real-time data visualization through a personal dashboard.
- Server side authentication through cookies and sessions.
- Reactive styling to fit various screen sizes, including mobile.
- Deployment of live demo on a server using `nginx` and `certbot`.

## Local Use

1. Download and install the `MongoDB Community Edition` database by follwing the steps in <https://www.mongodb.com/try/download/community> for your local operating system.
2. Clone the repository: `git clone https://github.com/danielzanelli/Portfolio.git`
3. Navigate to the IoT Dashboard project directory `IoT-Dashboard` and open two terminals.
4. On one terminal go to the `server` directory, install the dependancies with `npm install`, then run the API locally using `npm start`.
5. On the other terminal go to the `client` directory, install the dependancies with `npm install`, then run the React App `npm start`.
6. Register a new user in the database by accessing the API through the url <http://localhost:5000/api/users/new-user> on your browser.
7. Write down the generated username and password.
8. Navigate to <http://localhost:3000> on your browser to access the IoT Dashboard, where you can log in with your previously generated username and password.

## License

[MIT](https://choosealicense.com/licenses/mit/)

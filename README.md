# Pronunciation Practice App (IlmHub)
The Pronunciation Practice App is a web app that helps users practice their pronunciation of Arabic using the Tashkeel (diacritics) and the Arabic alphabet found in the Quran. This app was built for use by the IlmHub organization with the aim of helping young children (k-8) learn and practice their pronunciation of the Quran. The app is built using the Django framework and is hosted on Heroku. The app is currently in development.

## Table of Contents
[Live Link](#live-link)\
[Documentation](#documentation)\
[Installation](#installation)\
[Usage](#usage)\
[Testing](#testing)

## Live Link
The live link to the app can be found [here](https://pronunciation-practice.herokuapp.com/). Note that the app is currently in development and is not yet ready for use. This live link contains the latest [release](https://github.com/UAlberta-CMPUT401/pronunciation-practice/releases/latest) of the app.

## Documentation
The documentation for the app can be found [here](https://ualberta-cmput401.github.io/pronunciation-practice/).

To view the API documentation:
1. follow the installation instructions below
2. while the backend Django app is running, [click here](http://localhost:8000/swagger/) to view the Swagger documentation for the API

## Installation
1. Clone the repository to your local machine.
2. within the project directory, run `pip install -r requirements.txt` to install the required packages for the backend of the app
3. navigate to the `\backend\IlmHub` directory and create a file called `.env` and add the following environment variables:
    ```
    SECRET_KEY=YOUR_SECRET_KEY
    DB_NAME=ilmhub_db
    DB_USER=ilmhub
    DB_PASSWORD=PASSWORD
    DB_HOST=localhost
    DB_PORT=5432
    DEBUG=TRUE
    ```
    - if you require a secret key, you can generate one using [Djecrety](https://djecrety.ir/)
4. using PostgreSQL, create a local server called `ilmhub` and a database called `ilmhub_db` within the server
    - for info on how to install PostgreSQL on your local machine, [click here](https://www.postgresqltutorial.com/install-postgresql/)
5. in your PostGreSQL server, create a user called `ilmhub` with the same `PASSWORD` as in the .env file and grant all privileges to the `ilmhub_db` database
    - for info on how to create a local server and database in PostgreSQL, [click here](https://www.postgresqltutorial.com/postgresql-create-database/)
6. navigate to the `backend` directory and run `python manage.py migrate` to migrate the database to your PostgreSQL server
7. navigate to the `frontend` directory and run `npm install` to install the required packages for the frontend of the app
8. run `npm start` to start the frontend of the app on `localhost:3000`
9. navigate to the `backend` directory and run `python manage.py runserver` to start the backend of the app on `localhost:8000`
10. [click here](http://localhost:3000) or navigate to `localhost:3000` in your browser to view the frontend of the application
11. [click here](http://localhost:8000/admin/) or navigate to `localhost:8000/admin/` in your browser to view the Django admin panel

## Usage
### Student
- To login, or if you forget your user credentials, contact your teacher for your login username and password
- Once logged in, select any chapter box from the home page coloured yellow to view lessons that have been `assigned` to you that are not yet complete
    - Listen to the audio for a lesson by pressing the 'play' button to the left of the lesson text, then repeat the pronunciation back to yourself
    - Listening to a lesson once will decrease the `repetitions` counter by 1; once it reaches 0, the lesson will be marked as `completed` and your teacher will be notified that you are ready to be tested on the pronunciation at your next in-person meeting
    - `Completed` lessons can still be practiced as much as required even if you've listened to the lesson for the set number of repetitions
- If your teacher is satisfied with your pronunciation of an assigned lesson after testing you on it, they will mark the lesson as `confirmed`
    - If your teacher beleives you need more practice, they will re-assign the lesson to you, and it will appear as an `unfinished` lesson the next time you log in
- If there are no yellow `unfinished` chapters on your home page, you can still practice any lesson by navigating to its associated chapter
    - To view how many lessons are currently assigned to you and how many lessons you've completed, select the user icon in the top right of the screen
- When you are done with your session, select the user icon in the top right of the screen and click the `log out` button to end your session

### Teacher
- To log in to your account for the first time, contact your site admin for login credentials
- Once logged in, select a student from the `students` dropdown in the menubar, or view all your student's progress at once from the home page
    - From either of these pages, you can assign a student a new lesson and the number of repetitions they must listen to the lesson audio for before it is marked as `completed` by navigating to the appropriate lesson tab and chapter for the lesson, then using the `assign` button on the right of the lesson text to assign the lesson to the current student
    - Selecting the `assign all lessons` button at the bottom of each chapter will assign all the lessons in a chapter to the specified student for the set number of repetitions
    - You can also unassign individual lessons from a student if they have been assigned incorrectly using the `unassign` button to the right of the lesson text
    - The `students` dropdown will also show the number of unfinished and finished lessons for each student, allowing you to see which student's require more work at a glance
- When assigning lessons, you can `assign` both new lessons that the student hasn't seen yet, or `reassign` lesson that the student has already `completed` but has not practiced enough to pass the in-person test for that lesson
- If a student's lesson is marked yellow, they have been assigned the lesson but are still practicing it
    - If the lesson is marked red, the student hasn't been assigned the lesson yet and can't view it from their account until you assign it to them
    - If the lesson is marked blue, the student has `completed` the lesson but has yet to be tested on it
- When a student's pronunciation of a `completed` lesson is tested in-person, you can mark the lesson as `confirmed` if their pronunciation is acceptable
    - This will mark the lesson green, indicating that the student has passed the test for that lesson
    - If the pronunciation of the lesson is not acceptable, you can `re-assign` the lesson with a set number of repetitions to colour the lesson yellow and re-add it to the student's list of `unfinished` lessons
- To logout of your account, select the user icon in the top right of the screen and click the `log out` button

### Parent
- To create an account to track your child's progress, contact their teacher to recieve a login username and password
- Once logged in, you will be able to see what chapters your children have been `assigned` (marked yellow) or have `completed` (marked green) on the home page
    - To view a detailed list of your child's progress for a given chapter, select the desired chapter box from the home page
- For a given chapter, `unfinished` lessons are marked in yellow, lessons your child has `completed` will be marked in blue, and lessons your child has finished and been tested on will be marked in blue as `confirmed` by their teacher
- Clicking the `children` dropdown on the menubar will allow you to view an indiviual child's progress
    - This dropdown will also allow you to view how many lessons each child has not yet finished and how many they have successfully finished
- To logout of your account, select the user icon in the top right of the screen and click the `log out` button

### Content Creator
- If you are the admin user for the site, you can login as a content creator using your admin credentials on the deployed site
    - If you are not the site admin, contact the admin to request a new content creator account and use the provided username and password to login
- To add a new lesson tab, first create a `.zip` folder containing named folders for each desired chapter in the lesson tab
    - Each chapter folder should contain all the text/image files you want to upload along with their associated audio files
    - Each item within a chapter folder should have the name `[chapter_number]_[lesson_number]`
- To create a new lesson tab using a `.zip` folder that matches the above format, press the `Upload +` button on the home page menu bar
    - Select the `choose file` button and select your `.zip` folder containing your chapters, then click `upload tab/chapter` to upload the `.zip`
- To add new chapters, first create a `.zip` folder containing the text for each lesson (either as an image or a `.txt` file) and the associated audio file for the lesson
    - Make sure the naming conventions for each file is: `1_[lesson_number]`
- To create a new chapter in an already-existing lesson tab, select the desired lesson tab from the menu bar and click `Upload chapter +` in the lesson tab dropdown
    - Select the `choose file` button and select your `.zip` folder containing your lessons, then click `upload tab/chapter` to upload the `.zip`
- To remove lessons, chapters, or lesson tabs, either login to the site admin page using your admin credentials (if you have admin access) or make a request to the site admin detailing which lesson tabs, chapters, and/or lessons you want to be deleted
- To logout of your account, select the user icon in the top right of the screen and click the `log out` button

### Admin
- If you are setting up your custom instance for the first time, follow the [installation](#installation) instructions in this README and the deployment instructions on the [documentation site](https://ualberta-cmput401.github.io/pronunciation-practice/)
    - After setting up your instance, you can navigate to the `admin` page by following the step 11 in the [installation instructions](#installation).
- On the admin page, you can create new accounts for teachers, content creators, parents, or students using the menu on the left of the screen to select the desired role, then selecting the `add [role]` button in the top right of the screen
    - This will open a new screen where you can fill out the required info for the user
    - When creating a new user, be sure to record the username and password as the user will require both of these credentials to login to the app
- If you are creating a new parent account, you will need to associate it with a student account in order for the parent to be able to view their child's progress
    - Using the same sidebar on the left of the `admin` screen, select the `Parent-Students` button and create a new parent-student object
    - Select the `add parent-student` button in the top right of the screen, then select the parent user and student user you want to associate
    - After adding the new parent-student relationship, the parent user will be able to view their child's progress from their own account
- To modify users or their relationships, select the desired object from the left sidebar of the main admin page (e.g. Teachers) and then select the instance of that object you wish to modify (e.g. Teacher1)
    - To delete accounts or relationships between accounts, follow the above instructions, but select the `delete` button at the bottom of the user's info screen

## Testing
To run the tests for the Django backend, navigate to the `backend` directory and run `python manage.py test`. This will also return a code coverge report visible in the terminal.

To run the tests for the React frontend, navigate to the `frontend` directory and run `npm test`. To view the code coverage report, run `npm run test -- --coverage --watchAll=false`.

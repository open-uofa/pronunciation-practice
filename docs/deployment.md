# Deployment

## Deployment Instructions

### Back-end

### Front-end

#### Heroku (Paid)
- To deploy on Heroku, first create a verified Heroku account from [here](https://devcenter.heroku.com/articles/account-verification). 
- Install the Heroku CLI from [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli) and login to your account and verify installation.
- Create a new app on the Heroku Dashboard from [here](https://dashboard.heroku.com/)
- Once you are done with the above steps, register the newly created app from heroku dashboard in the existing project github repo by using the command `heroku git:remote -a app-name` and then set buildpacks using `heroku buildpacks:set heroku/nodejs`
- Commit and push your changes using `git commit -am "my commit"` and `git subtree push --prefix path/to/subdirectory heroku main`
- `Bonus`: To setup auto deploy using github actions and heroku, checkout [this](https://github.com/marketplace/actions/deploy-to-heroku).

#### Github Pages (Free)
- Install Github pages in `frontend` directory by `npm install gh-pages — save-dev`.
- Add homepage property to package.json file, for github user site, `"homepage": "https://{organization}.github.io"`. Custom domains can also be added by `"homepage": "https://testwebsite.com"`.
- Add deploy scripts to package.json file. `"predeploy": "npm run build", "deploy": "gh-pages -d build"`
- `npm run deploy`
- Check Pages on github settings to see the published url. Remember to change source branch to gh-pages.
- To follow subdirectory troubleshooting, checkout [this Stackoverflow answer](https://stackoverflow.com/questions/51918854/how-to-deploy-create-react-app-to-gh-pages-subfolder)

#### `Bonus`
- An alternate choice can be [Netlify](https://www.netlify.com/blog/2016/07/22/deploy-react-apps-in-less-than-30-seconds/) which is also free for public organization repos.

## User Manual

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

## Job Description

### Full Stack Web Developer
IlmHub is a non-profit education institution focused on educating young students on the Quran and Islam. Our Pronunciation Practice application is a site that allows students of all ages to practice their Arabic pronunciation of the Quran outside of regular lessons with an in-person teacher. The app allows users to view verses of the Quran in Arabic, and play audio files associated with those verses in order to practice and understand the Quran. We require a full-stack web developer who is able to maintain and continue to build onto this application.

### Responsibilities
- Maintain and administer IlmHub's custom instance of the pronunciation app
- Configure cloud setup and maintenance for the backend API of the site
- Work with teachers, content creators, parents, and students to resolve technical problems and configure new user setup
- Continue to build on the existing application by adding new features and improving UI/UX

### Qualifications
- Understanding of cloud architectures and experience deploying and maintaining applications on cloud platforms, preferably with Cybera Rapid Access Cloud and Heroku
- Experience with Javascript and React
- Knowledge of Python, Django, and the Django REST Framework
- Experience with SQL databases, preferably PostgreSQL
- Experience managing and working with Git and Github CI/CD pipelines
- Knowledge of UI/UX principles and best practices

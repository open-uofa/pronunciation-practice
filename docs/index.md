# Project Requirements

## Executive Summary

The Pronunciation Practice Hub is a website that allows young students to learn how to pronounce the verses of the Quran in Arabic. Students will have the ability to practice their pronunciation of verses assigned by their teacher through listening to an audio file, then repeating the verse back to themselves. The app is intended for K-8 students, but can be used by any age-group or demographic. Parents will be able to view their children's progress from their own account. Teachers will be able to assign lessons to their students for them to practice a given number of times. Content creators will be able to upload .zip files containing lesson text and audio files that will then automatically be converted to new lessons within a chapter.

When a school begins using this app, they will be able to upload as many lessons as they'd like in any language, allowing all language schools to be able to use this application. Schools can assign students to teachers or parents using the admin functionality to allow parents and teacher to view a child's progress on the lessons that have been assigned to them. Students will be able to view all lessons that the school content creator has added and that their teacher has assigned to them, allowing for students to learn at their own pace since new lessons won't be assigned to them until their teacher decides they are ready to move on.

## Project Glossary
- **Lesson** - A lesson consists of some text, and an audio recording of the pronunciation.

- **Chapter** - A chapter consists of a lessons on a similar subject, with an accompanying label to describe the lessons.

- **Lesson Tab** - A lesson tab consists of lessons and/or chapters. Lesson tabs aggregate larger concepts and/or languages.

- **Assignment** - A set of lessons assigned to a student account by a teacher account. Tracks the assignees progress.

- **Lesson Status** - The status of a lesson. It can be one of:
    - ***Non-assigned***: Default status indicates a lesson that has not been assigned.
    - ***Assigned***: The lesson has been assigned to the student by a teacher. Lesson is ready to be done.
    - ***Completed***: The lesson has been assigned to and completed by the student. Teacher still needs to confirm whether the lesson needs to be redone or not.
    - ***Confirmed***: Lesson has been completed by the student, and the assigning teacher has confirmed the students progress. Lesson no longer needs to be completed.
    - ***Marked for redo***: Lesson has been completed by the student, and the assigning teacher has decided the student needs to do the assignment again. The assignment will need to be completed by the student again, and the teacher will need to reassess the students progress.
##
- **Student Account** - An account representing a student, may view and do lessons. Can be associated with teacher accounts. Can have lessons assigned to them by a teacher.
    - **Scenario**: _Mohammad logs into their account and sees that they have been **assigned** a few lessons to practice. He also notices that one of his previous lessons has been **marked for redo**. He reads and listens to the lesson a number of times, practicing the lesson between each time the lesson audio plays. After he feels confident about his practice, he marks all the lessons he practiced as **completed**._
##
- **Teacher Account** - An account representing a teacher. Can be associated with student accounts. Can assign lessons to students, and monitor their process.
    - **Scenario**: _Mohammad goes to the school and meets his teacher, Ahmad. Ahmad logs into his account and sees Mohammad's name along with his other students. He clicks on Mohammad's name to view his progress, and sees that Mohammad has marked the lessons Ahmad assigned to him, as well as the lesson Ahmad marked to be redone, as completed. Ahmad then tests Mohammad's pronunciation of all those lessons. Mohammad performs well on all the lessons in this test; Ahmad, is very proud of him! He **confirms** that those lessons have actually been completed by Mohammad. Ahmad then **assigns** Mohammad the next set of lessons that must be completed._
##
- **Parent Account** - An account representing the parent or guardian of a student. May be associated with one or more student accounts. Can view the progress of an associated student.
    - **Scenario**: _Maryam, Mohammad's mother, wants to see her sons' progress on his pronunciation practice. She logs into her account and sees both her sons' names, as they are both registered with the school. She clicks on Mohammad's name, and sees a list of all the lessons Mohammad has completed, whether confirmed by Ahmad or not, as well as the lessons that have been newly assigned to him or ones that have been marked for redo by Ahmad, his teacher._
##
- **Content Creator Account** - An account that is responsible for adding content to the system. Can upload files to create and organize lessons, chapters, and lesson tabs.
    - **Scenario**: _The school would like to offer another language which students can practice the pronunciation of, so they tasked Mohayemin, one of the school's content creators, with creating lessons for this newly offered language. Mohayemin compiles text (or image) and audio files for each lesson in this language, then logs in to his account and **creates a new lesson tab** - which he titles by the name of the language. He then **uploads** the files he compiled and sees that the lessons have been uploaded successfully, in the order he structured his files in. He also sees that the lesson texts correctly correspond with the lesson audios. He publishes the new lesson tab, and now teachers can view this tab as well as assign students some of the lessons Mohayemin just uploaded._


## User Stories
### Epic 1 - Admin
##### US 1.01 - Add Users
> As an admin, I would like to add users to my service, so that they can use my service.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Admin can add users
> 2. New user can log in to their account
> 3. New user has the correct information displayed on their account

##### US 1.02 - Assign Roles to Users 
> As an admin, I would like to assign a user a role from “student”, “parent”, “teacher”, “content creator”, so that they can only use the service according to their assigned role.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Admin can assign a role to user
> 2. Role is one of "student", “parent”, “teacher”, “content creator”.
> 3. User roles stored in database

##### US 1.04 - Add Admin
> As an admin, I would like to add another admin to my service, so that they can manage my service.

> **Story Points**: 0

> **Acceptance Tests**

> 1. Admin 1 can add another admin account, Admin 2
> 2. Admin 2 can log in to the admin panel
> 3. Admin 2 has all the privileges of Admin 1

##### US 1.05 - Remove Users
> As an admin, I would like to remove users from my database, so that they can no longer use my service.

> **Story Points**: 0

> **Acceptance Tests**

> 1. Admin can delete users
> 2. Deleted user can not log in to their account

##### US 1.06 - Manage User Accounts
> As an admin, I would like to manage each user’s account, so that I can update their information if needed.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Admin can select a user’s account to manage
> 2. Admin can update information of user’s account
> 3. Updated information displayed when user logs in to their account

##### US 1.07 - Change User Roles
> As an admin, I would like to change the assigned roles of users of my service, so that they can use my service according to different roles.

> **Story Points**: 3

> **Acceptance Tests**

> 1. Admin can change the roles of existing users
> 2. New roles are updated in the database
> 3. User can see the layout(s) associated with the different role(s) assigned to them

##### US 1.08 - Filter Users by Role
> As an admin, I would like to filter out users of my service according to their assigned roles, so that I can manage groups of users at once.

> **Story Points**: 0

> **Acceptance Tests**

> 1. Admin can filter users according to one or more roles
> 2. All users with the selected role(s) are returned
> 3. No users with different roles are returned

##### US 1.09 - Link Students to Parents
> As an admin, I would like to link student accounts to parent accounts, so that I know who a student’s parents are.

> **Story Points**: 0

> **Acceptance Tests**

> 1. Admin can link parent accounts to student accounts
> 2. Parents of student are displayed when managing student accounts

##### US 1.10 - Link Parents to Students
> As an admin, I would like to link parent sccounts to student accounts, so that I know who a parent’s children (students in the database) are.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Admin can link student accounts to parent accounts
> 2. Parents can have multiple student accounts linked to their account
> 3. Parent’s children are displayed when managing parent accounts

### Epic 2 - Content Creator
##### US 2.01 - Create Lesson Tabs
> As a content creator, I would like to create new lesson tabs, so that I can add lessons to them.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Content creator can create new lesson tabs
> 2. New lesson tabs are displayed when content creators or teachers log in to their account

##### US 2.02 - Naming/Renaming Lesson Tabs
> As a content creator, I would like to be able to name and rename lesson tabs, so that they can be differentiated.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lesson tabs can be named
> 2. Lesson tabs can be renamed
> 3. Make sure new/updated names of lesson tabs are displayed correctly when a user (that can see the lesson tab) logs in to their account

##### US 2.03 - Upload Lessons
> As a content creator, I would like to upload one or more lessons to each lesson tab, so that lessons can be assigned by teachers.

> **Story Points**: 5

> **Acceptance Tests**

> 1. Content creator can upload one lesson to a lesson tab
> 2. Content creator can upload multiple lessons to a lesson tab at once
> 3. All lessons that content creator has uploaded are displayed under the corresponding lesson tab
> 4. All lessons that content creator has uploaded are displayed correctly
> 5. Teachers can see newly uploaded lessons
> 6. Teachers can assign newly uploaded lessons to students

##### US 2.04 - Group Lessons into Chapters
> As a content creator, I would like to group lessons in each lesson tab into chapters, so that similar lessons are displayed together.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Content creator can select one or more lesson and join them into a chapter
> 2. Content creator can add lessons to the chapter
> 3. Content creator can remove lessons from a chapter
> 4. Chapters and their lessons are displayed correctly when a user (that can see the lesson tab) logs in to their account

##### US 2.05 - Naming/Renaming Chapters
> As a content creator, I would like to name and rename chapters in a lesson tab, so that I can differentiate different chapters within a lesson tab.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Content creator can name new chapters
> 2. Content creator can rename existing chapters
> 3. New/updated chapter names are correctly displayed when a user (that can see the lesson tab) logs in to their account

##### US 2.06 - Textual and Audible Components in Lessons
> As a content creator, I would like each lesson to have both a textual and an audible component.

> **Story Points**: 3

> **Acceptance Tests**

> 1. Content creator can upload 2 files for each lesson, one representing the textual part and one representing the audible part
> 2. Textual component displayed correctly
> 3. Audible component plays the correct audio file
> 4. Textual and audible components correspond to the same lesson
> 5. Content creator can only upload 2 files per lesson, one of them being an audio file

##### US 2.07 - Textual Component Format
> As a content creator, I would like the textual aspect of each lesson to be represented by either an image or a plain text file, so that I can upload a lesson in multiple formats.

> **Story Points**: 3

> **Acceptance Tests**

> 1. Content creator can select .txt files (along with audio files) when uploading new lessons
> 2. Content creator can select image (.jpg, .png) files when u uploading new lessons
> 3. Content creator can select only 1 file of either tab when uploading a lesson
> 4. Image is displayed correctly if textual part of lesson is an image
> 5. Text is displayed correctly if textual part of lesson is a plain text file

##### US 2.08 - Reorder Chapters
> As a content creator, I would like to reorder chapters within a lesson tab, so that I can make the chapters chronologically coherent.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Content creator can change the order of chapters in a lesson tab
> 2. New order of chapters is preserved when a user (that can see the lesson tab) logs in to their account

##### US 2.09 - Reorder Lessons
> As a content creator, I would like to reorder lessons within a chapter, so that I can make the lessons chronologically coherent.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Content creator can change the order of lessons in a chapter
> 2. New order of lessons is preserved when a user (that can see the chapter) logs in to their account

##### US 2.10 - Upload Arabic Lessons
> As a content creator, I would like to upload lessons in Arabic, so that I can create Arabic lessons.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Content creator can upload lessons with Arabic text
> 2. Arabic text is displayed correctly and appropriately (in the correct position)

##### US 2.11 - Content Creator
> As a content creator, I want to be able to remove lessons from the system, in case there are issues with the lessons.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Lesson data is no longer stored in the system
> 2. Lesson is no longer displayed to any user

### Epic 3 - Student
##### US 3.01 - View Lesson Tabs
> As a student, I want to be able to view lesson tabs that have assigned lessons for me, so that I can access my lessons.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Can see lesson tabs
> 2. Can only see lesson tabs that have lessons assigned to me

##### US 3.02 - Students Get Assigned Lessons
> As a student, I want to be able to have lessons assigned to me, so that I can know what to complete.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Student can have a number of lessons assigned to them in a lesson tab
> 2. Visual indicator of being assigned
> 3. Non assigned lessons are not indicated

##### US 3.03 - See Lesson Text
> As a student, I want to be able to see the text associated with a lesson, so I can know what I am learning to pronounce.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lesson has text displayed
> 2. Text is displayed correctly, in english and arabic

##### US 3.04 - Lesson Audio Available
> As a student, I want to be able to listen to the pronunciation of some lesson text, so I can learn how to pronounce it correctly.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Lesson has associated audio included
> 2. Audio plays when selected
> 3. Audio is correct for the given lesson
> 4. Audio is audible and at reasonable volume

##### US 3.05 - Pause Lesson Audio
> As a student, I want to be able to have my lesson pause, so I can learn practice my pronunciation.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lesson audio pauses after being played
> 2. Audio pauses for at least as long as the audio played for
> 3. Audio resumes after pause

##### US 3.06 - Repeat Lesson Audio
> As a student, I want to be able to have my lesson repeat for the given duration or number of times, so I can be able to practice.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lesson audio repeats for at least the given duration, including pauses
> 2. Lesson audio repeats for the given amount of times
> 3. Lesson audio does not overlap itself
> 4. Lesson audio pauses to allow practice, following audio pausing story guidelines

##### US 3.07 - See Lesson Status
> As a student, I want to be able to see the status of my lessons, so I can view my progress.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lessons are marked assigned after being assigned
> 2. Lessons are marked completed after being finished by student
> 3. Lessons are only marked completed after finishing an assignment including them
> 4. Lessons are marked as confirmed after a teacher condoms the progress
> 5. Lessons are marked for redo if a teacher marks them

##### US 3.08 - Redo Assignments
> As a student, I want to be able to redo assignments, so that I can properly practice.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Lessons marked for being redone may be reattempted
> 2. Redone lessons conform to previous lesson story requirements
> 3. Redone lessons will be marked completed upon completion

##### US 3.09 - See Chapters
> As a student, I want to be able to see how assignments are sorted into chapters within a lesson tab, so I know what I am practicing.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Lessons are visually divided into tabs
> 2. Lessons tabs have a header to indicate type and content of the lesson tab

##### US 3.10 - Student Accounts
> As a student, I want to have an account associated with me, so that I can have my progress tracked and have assignments.

> **Story Points**: 5

> **Acceptance Tests**

> 1. Student can have an account with their information
> 2. Progress is tracked based on account

##### US 3.11 - Log in to Account
> As a student, I want to be able to log into my account, so that I may access things associated with my account.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Interface to log into account
> 2. Correctly authenticates account information
> 3. Denies access with incorrect account information

### Epic 4 - Parent
##### US 4.01 - Associate Parents & Students
> As a parent, I want to be able to have children associated with me, so I can monitor their progress.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Parent account may have any number of associated children account
> 2. Parent account is only associated with there accounts

##### US 4.02 - Seee Children's Assigned Tabs
> As a parent, I want to be able to see what lesson tabs my children have assigned to them, so I can see what they are learning.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Lesson tabs are displayed correctly
> 2. Lesson tabs only display if an associated child account has been assigned content from them
> 3. Lesson tabs will display if any child account has been assigned to them


##### US 4.03 - See Children's Assigned Lessons
> As a parent, I want to be able to see what lessons my children have assigned to them (past and present), so i can monitor their progress.

> **Story Points**: 0

> **Acceptance Tests**

> 1. Any lessons assigned to associated children accounts are displayed and noted
> 2. Lessons not assigned to an associated child account are not displayed
> 3. Visual indicator is given to indicate assignment

### Epic 5 - Teacher
##### US 5.01 - Associate Teachers with Students
> As a teacher, I want to have students associated with me, so that I can teach these students.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Only specifically assigned students are associated with the teacher

##### US 5.02 - Assigning Lessons to Students
> As a teacher, I want to assign lessons to students, so they can practice these lessons.

> **Story Points**: 3

> **Acceptance Tests**

> 1. Individual lessons can be assigned
> 2. Groups of lessons can be assigned
> 3. Assignments can be per student or groups of students

##### US 5.03 - Add Repetitions Per Assigned Lesson
> As a teacher, I want to assign lessons to students based on duration or number of repetitions, so they will practice the lesson for the given duration.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Lessons repeat for the given duration
> 2. Lessons repeat for the given number of repetitions
> 3. Lessons are only marked complete after the duration elapses

##### US 5.04 - See Students' Progress
> As a teacher, I want to see my students progress on assigned lessons, so that I can monitor their learning progress.

> **Story Points**: 2

> **Acceptance Tests**

> 1. Progress is displayed for each students assignments
> 2. Visually indicates the students progress (assigned, completed, confirmed, marked for redo)

##### US 5.05 - Mark Assignments for Redo
> As a teacher, I want to mark assignments for redoing, so that my students can get more practice on problem lessons.

> **Story Points**: 1

> **Acceptance Tests**

> 1. Completed assignments can be set to be redone
> 2. Visual indication that lessons have been set for recompletion
> 3. Visual indication when a lesson has be re completed

##### US 5.06 - See Content
> As a teacher, I want to see all content, so I can know what material is out there.

> **Story Points**: 2

> **Acceptance Tests**

> 1. All tabs are visible to the teacher
> 2. All content of lesson tabs are visible to the teacher

## MoSCoW
### Must Have
* US 1.01 - Add Users
* US 1.02 - Assign Roles to Users
* US 1.06 - Manage User Accounts
* US 2.01 - Create Lesson Tabs
* US 2.03 - Upload Lessons
* US 2.06 - Textual and Audible Components in Lessons
* US 2.07 - Textual Component Format
* US 2.10 - Upload Arabic Lessons
* US 3.01 - View Lesson Tabs
* US 3.02 - Students Get Assigned Lessons
* US 3.03 - See Lesson Text
* US 3.04 - Lesson Audio Avaialable
* US 3.07 - See Lesson Status
* US 3.10 - Student Accounts
* US 3.11 - Log In to Account
* US 5.02 - Assigning Lessons to Students
* US 5.04 - See Student's Progress

### Should Have
* US 1.05 - Remove Users
* US 1.10 - Link Parents to Students
* US 2.02 = Naming/Renaming Lesson Tabs
* US 2.04 - Group Lessons into Chapters
* US 3.05 - Pause Lesson Audio
* US 3.06 - Repeat Lesson Audio
* US 3.08 - Redo Assignments
* US 3.09 - See Chapters
* US 4.01 - Associate Parents and Students
* US 4.02 - See Children's Assigned Tabs
* US 4.03 - See Children's Assigned Lessons
* US 5.03 - Add Repititions for Assigned Lessons
* US 5.05 - Mark Assignments for Redo
* US 5.06 - See Content

### Could Have
* US 1.04 - Add Admin
* US 1.08 - Filter Users by Role
* US 2.08 - Reorder Chapters
* US 2.09 - Reorder Lessons
* US 2.11 - Remove Lessons
* US 5.01 - Associate Teachers with Students

### Would Like But Won't Get
* US 1.07 - Change User Roles
* US 1.09 - Link Students to Parents

## Similar Products
* [Duolingo](https://www.duolingo.com/)
    - Online language-learning software
    - Language learning completed in the form of 'lessons' can be applied to current project
    - Capable of displaying Arabic script, so is a useful reference for displaying Arabic properly
    - Simple UI that is widely-accessible, so should take insipration on design since it will work well for young students
* [TarteeleQuran](https://www.tarteelequran.com/)
    - Online Quran education
    - No self-directed learning, students have lessons with teachers, helping us see what elements of the Arabic Quran can't easily be taught in a self-directed manner
    - Teaches Arabic outside of the Quran as well, providing insights into how we can expand the project in future to grow the user-base
* [ArabAcademy](https://www.arabacademy.com/)
    - Site for learning Arabic and not just the Quran
    - Provides Arabic lessons in a self-learning environment, similar to what this project intends to accomplish
    - Integrated teacher support that connects students with teachers, providing inspiration for expanding student-teacher interactions in this project

## Open-source Projects
* [Quran.com API](https://quran.api-docs.io/v4/getting-started/introduction)
    - Open-source API of Quranic verses
    - Allows us to query the API when we want to the text for specific verses
    - Provides audio files containing the pronunciation of each verse, allowing us to easily access all audio needed for the project
    - We can scrape the data from the API and add it to our own database, allowing us to add lessons outside the Quran without having to worry about unnecessary API calls
* [Tanzil Quran](https://tanzil.net/download/)
    - Open-source database of Quranic verses in Arabic
    - Allows us to download the complete text of the Quran in multiple styles and formats, allowing us to configure the data to fit our requirements
    - No audio files, so we would still have to incorporate the Quran.com API as well

## Techincal Resources
### Backend: Django + PostgreSQL
  * [Django Documentation](https://docs.djangoproject.com/en/4.1/)
  * [Setting up Postgres, SQLAlchemy, and Alembic](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
### Deployment: Docker + CyberaRAC
  * [Using Docker with CyberaRAC](https://wiki.cybera.ca/display/RAC/Using+Docker+Machine)
  * [Docker Documentation](https://docs.docker.com/)
  * [Cybera Rapid Access Cloud Guide](https://wiki.cybera.ca/display/RAC/Rapid+Access+Cloud+Guide%3A+Part+1)
### Frontend: React.js
  * [React.js Documentation](https://reactjs.org/docs/getting-started.html)

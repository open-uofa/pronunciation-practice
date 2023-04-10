
import '../css/Help.css';
// render the help page for parents
export const ParentHelp = () => {
    return (
        <div className='text'>
            <p>Welcome to the IlmHub pronunciation practice app! This app is designed to help your children practice their pronunciation
            of the Quran outside of their normal class time. When your child's teacher assigns them a lesson, the chapter the lesson is in 
            will appear as a <span style={{color: '#b09e02'}}>yellow</span> box on your home page. Click on any of these boxes to view the lessons for that chapter.
            </p>
            <p>This app splits the Quran into "chapters," where each chapter is a Surah of the Quran, that contain "lessons," 
            where each lesson is a verse from the Surah. You can see only the chapters and lessons that have been assigned to your child.
            </p>
            <p>If a lesson is coloured <span style={{color: '#b09e02'}}>yellow</span>, your child will have to practice it for the amount
            of times shown in the 'repetitions' box to the left of the lesson text.
            </p>
            <p>If a lesson is coloured <span style={{color: 'blue'}}>blue</span>, your child has completed practicing the lesson, and their teacher will be
            notified that they completed the lesson and will test them on it in their next class. Your child can still practice the lesson as much as they want.
            </p>
            <p>If a lesson is coloured <span style={{color: 'green'}}>green</span>, they have completed the lesson and can move on to another one.</p>
            <p>Press the "Child" button on the menu bar to view all the children associated with your account. Click on the name of a child to view the
            number of lessons they have completed and the number of lessons they have left to complete.
            </p>
            <p>When you are finished, press the user icon in the top right of your screen and press "Log out" to log out of your account</p>
            <p>If you have any other questions, please contact your child's teacher!</p>
        </div>
    )
};

 // render the help page for students
 export const StudentHelp = () => {
    return (
        <div className='text'>
            <p>Welcome to the IlmHub pronunciation practice app! This app is designed to help you practice your pronunciation of the Quran outside of class. 
                When your teacher assigns a lesson to you, it will appear as a <span style={{color: '#b09e02'}}>yellow</span> box on your home page. 
                Click on any box to view the lessons for that chapter.
            </p>
            <p>If a lesson is coloured <span style={{color: '#b09e02'}}>yellow</span>, you will have to practice it for the amount
            of times shown in the 'repetitions' box next to the triangle 'play' button.
            </p>
            <p>If a lesson is coloured <span style={{color: 'blue'}}>blue</span>, you have completed practicing the lesson, and your teacher will be
            notified that you completed the lesson and will test you on it in your next class. You can still practice the lesson as much as you want
            if you want to improve your pronunciation more.
            </p>
            <p>If a lesson is coloured <span style={{color: 'green'}}>green</span>, you have completed the lesson and can move on to another one.</p>
            <p>Click on the triangle 'play' button on the left of the lesson text to listen to the lesson. 
            You can click on the 'play' button again to pause the audio. Once the lesson audio has played through, the 'repetitions' counter will decrease by 1.
            </p>
            <p>When the 'repetitions' counter reaches 0, the lesson will be marked <span style={{color: 'blue'}}>completed</span> and you can move onto
            the next lesson. Make sure you are prepared to be tested on this lesson by your teacher next class!
            </p>
            <p>When you are finished practicing, press the user icon in the top right of your screen and press "Log out" to log out of your account</p>
            <p>If you have any other questions, please contact your teacher!</p>
        </div>
    )
};


/**
 * Renders the help page for students and parents, allowing them to view instructions on how to use the app.
 * 
 * @returns the help page for students and parents
 */
export default function HelpPage(props) {

    return (
            <div className="help">
                <h1 className='helptitle'>Help</h1>
                {props.role === 'Student' ? <StudentHelp /> : <ParentHelp />}
            </div>
    )
}

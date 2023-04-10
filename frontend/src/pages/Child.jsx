import * as React from 'react';
import '../css/Sidebar.css';
import Lesson from '../components/StudentParent/Lesson';

function Child(props) {

        return(
        <div className="App" style={{ height: "100%" , backgroundColor: "lightblue"}}>
          <h1>{props.childName}'s Lessons:</h1>
          <div className="lessons" width="100%" style={{backgroundColor: "white"}}>
           {props.lessons.map((lesson, index) => {
              return (
                <Lesson lesson={lesson} status={lesson.status} parent={true} key={index}/>
              )})}
         </div>
        </div>
        )
}

export default Child;
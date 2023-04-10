import React from 'react';
import Lesson from './Lesson';


/**
 * This component generates a list of lessons for a given chapter.
 * 
 * @param {Array} props.lessons - array of lessons for the current chapter represented as JSON objects
 * @param {string} props.student - student ID for the current student 
 * @returns {div} a div containing a list of lessons
 */
export default function Chapter(props) {
    const lessonMenu = props.lessons.map((lesson) =>
        // Generate a lesson component for each lesson
        <Lesson key={lesson.id} lesson={lesson} student={props.student}/> // pass the lesson and student id to the lesson component
    );
    
    

    // Render the list of lessons
    return (
        <div>
            {lessonMenu}          
        </div>
    );
    
}
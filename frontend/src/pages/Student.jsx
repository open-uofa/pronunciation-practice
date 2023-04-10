import * as React from 'react';
import axiosInstance from '../utlities/axiosInstance';
import { useState, useEffect } from 'react';
import Lesson from '../components/StudentParent/Lesson';
import Stack from '@mui/material/Stack';



function SideBarStudentLesson(props) {
  const [student, setStudent] = useState([]);

  useEffect(()=>{
    axiosInstance.get(`students/${localStorage.getItem('id')}/`)
    .then((response)=>{
      setStudent(response.data);
    })
    .catch(err => {
      console.error(err);
    }) 
  }, [])

  const lessonComponents = props.chapter.lessons.map(lesson => (
    <Lesson lesson={lesson} status={lesson.status} student={student}/>
  ));

  return (
      <div className="App" style={{ height: "100%" , backgroundColor: "lightblue"}}>
         <h1>Lessons for {props.chapter.name}:</h1>
         <div className="lessons" width="100%" style={{backgroundColor: "white"}}>
            <Stack spacing={2} alignItems='center' justifyContent='center' p='16px' gap='16px' width="100%">{lessonComponents}</Stack>
          </div>
      </div>
    );
}

export default SideBarStudentLesson;
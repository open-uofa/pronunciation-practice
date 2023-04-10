import * as React from 'react';
import Stack from '@mui/material/Stack';
import { useState, useEffect } from 'react';
import axiosInstance from '../../utlities/axiosInstance';
import Lesson from './LessonComponent/Lesson';


/**
 * A collection of all lesson tabs visible to the user.
 * 
 * @returns {JSX.Element} - The JSX for displaying all the lesson tabs
 */
function LessonTab() {
  const [lesson, setLesson] = useState([]);
  useEffect(() => {
    axiosInstance.get(`lessontabs/`)
      .then((response) => {
        console.log(response.data);
        console.log(response.data["tabs"][0]["name"]);
        setLesson(response.data);
      })
      .catch(err => {
        console.error(err);
      })
  }, []);

  return (
    <Stack spacing={2} alignItems='center' justifyContent='center' p='16px' gap='16px'>
      {lesson?.tabs?.map((tab, index) => {
        return (
          <div key={index}>
            <h2>{tab.name}</h2>
            {tab?.chapters?.map((chapter) => {
              return (
                <div key={chapter.id}>
                  <h3>{chapter.name}</h3>
                  {chapter?.lessons?.map((lesson, index) => (
                    <Lesson lesson={lesson} />
                  ))}
                </div>
              )
            })
            }
          </div>
        )
      })}
    </Stack>
  );
}
export default LessonTab;
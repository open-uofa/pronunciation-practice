import React from 'react';
import HomeChapter from './homeChapter';
import { Grid } from '@mui/material';


/**
 * Configures the layout of the lesson tab for the home page.
 * 
 * @param {JSON} props.tab - The tab object
 * @param {String} props.role - The role of the user
 * @param {String} props.childName - The name of the student
 * @param {String} props.selectedChild - The id of the selected child
 * @param {Function} props.setShowLessons - The function to set the showLessons state
 * @param {Function} props.setChildLessons - The function to set the childLessons state
 * @param {JSON} props.child - The child object
 * 
 * @returns {JSX.Element} - The JSX for the lesson tab
 */
function HomeLessonTab(props) {

    const handleTabClick = (chapter) => {
        if (props.role==="Parent") {
            props.setShowLessons(props.child.id)
            let lessons=[]
            for (let chap of props.tab.chapters) {
                for (let lesson of chap.lessons) {
                    lessons.push(lesson);
                } 
            }
            props.setChildLessons(lessons)
        } else if (props.role==="Student") {
            props.setShowLessons(chapter)
        }
    }

    function renderTab() {
        if (props.role==="Student" || props.selectedChild === '' || props.selectedChild===props.child.id) {
            return (
                <div key={props.tab.id} className="lesson-tab">
                <div className="module-text">{props.tab.name} {props.role === "Parent" && "- "+props.child.first_name} </div>
                <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
                    {props.tab.chapters?.map((chapter) => (
                        <Grid item xs={2} sm={4} md={3} key={chapter.id}>
                            <HomeChapter
                            key = {chapter.id}
                            chapter = {chapter}
                            onClick={() =>{handleTabClick(chapter)}}
                            />
                        </Grid>
                    ))}
                </Grid>
            </div>
            );
        } return null;
    }

    return (
        <>
        {renderTab()}
        </>
    );
}

export default HomeLessonTab;

import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import { Typography } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import React, { useCallback } from 'react';
import Chapter from './Chapter';
import axiosInstance from '../../utlities/axiosInstance';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useState, useEffect } from 'react';
import { Button } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

/** 
 * This component generates a list of chapters for a student.
 * 
 * @param {Array} props.chapters - array of all chapters in the DB, each chapter contains a collection of lessons
 * @param {string} props.student - student ID for the current student
 * @return {div} a div containing a list of chapters
*/
export default function Student(props) {
    // get the array of chapters from the prop and generate the array of lessons
    const time = 500;

    const id = props.student;
    const [repetitions, setRepetitions] = useState(1); //for setting number of repetitions
    const [status, setStatus] = useState('Assigned'); //for setting status of lesson
    
    const [chapters, setChapters] = useState([]);
    const [tabsName, setTabsName] = useState([]); 

    let getTabs = useCallback(() => {
      if (id) {
        axiosInstance.get(`lessons/${id}/`)
        .then((res) => {
          console.log("student changed")
          console.log("")
            let tabs = res.data.tabs;
            let newTabsName = [];
            let newChapters = [];
            // Add each chapter ID to the chapters array
            for(let i = 0; i < tabs.length; i++) {
                newTabsName.push(tabs[i]);
                for(let j = 0; j < tabs[i].chapters.length; j++) {
                    newChapters.push(tabs[i].chapters[j]);
                }
            }
            setTabsName(newTabsName);
            setChapters(newChapters);
        });
      }
    }, [id]);

    // Get the list of chapters from all lesson tabs from the backend endpoint
    useEffect(() => {
        getTabs();
    }, [getTabs]);
    
    const handleAssign = (id) => {//assigns chapter to student
        axiosInstance.post(`studentchapter/add/${id}/${props.student}`, {
          'num_repetitions': repetitions,
          'status': status,
        }, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        .then(response => {
          toast.success('Student chapter added successfully!', {autoClose: time}); //success message
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
          toast.error('chapter already assigned to student!', {autoClose: time}); //error message;
        });
      }
      const handleRepetitionsChange = (event) => {
        setRepetitions(event.target.value);
      };
    const handleStatusChange = (event) => {
        setStatus(event.target.value);
      };
       
    

    const tabMenu = tabsName.map((tab) =>
        <Accordion style={{backgroundColor: "#6699CC"}}>
            <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
            >
                <Typography>{tab.name}</Typography>
           </AccordionSummary>
      {chapters.map((chapter) =>
        // Accordian menu for each chapter and their lessons
        chapter.tab === tab.id &&
        <Accordion style={{backgroundColor: "powderblue"}}>
            <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
            >
                <Typography sx={{paddingLeft:"0.75%"}}>{chapter.name}</Typography>
            </AccordionSummary>
            <AccordionDetails  style={{backgroundColor: "#D4BCA6"}}>
              <input type="number" id="repetitions" name="repetitions" value={repetitions} onChange={handleRepetitionsChange} style={{ width: '70px' }}/>
                  <select id="status" name="status" value={status} onChange={handleStatusChange}>
                    <option value="Assigned">Assigned</option>
                  <option value="Marked For Redo">Redo</option>
                </select>
                <Button onClick={() => handleAssign(chapter.id)}><AddIcon></AddIcon></Button>
                <Chapter lessons={chapter.lessons} student={props.student} />
            </AccordionDetails>
            <Typography align='left' padding="5px">
                </Typography>
        </Accordion>
      )}
        </Accordion>
    );

    return (
        <div>
            {tabMenu}
        </div>
    );

}
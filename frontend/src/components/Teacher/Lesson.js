import React from 'react';
import { Typography, Grid, CardMedia } from '@mui/material';
import { Box } from '@mui/system';
import axiosInstance from '../../utlities/axiosInstance';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { useState } from 'react';
import Button from '@mui/material/Button';
import { TextField } from '@mui/material';
import { Card } from '@mui/material';
import DoneAllIcon from '@mui/icons-material/DoneAll';
import ReplayIcon from '@mui/icons-material/Replay';
import AddIcon from '@mui/icons-material/Add';
import CloseIcon from '@mui/icons-material/Close';



/**
 * This component generates a lesson card with options to assign or unassign a lesson to a student and to set
 * the number of repetitions for the lesson before it can be marked as completed.
 * 
 * @param {string} props.student - student ID for the current student
 * @param {JSON} props.lesson - lesson JSON object 
 * @returns {div} a div containing the generated lesson
 */
export default function Lesson(props) {
  const time = 500;
  const [repetitions, setRepetitions] = useState(1); //for setting number of repetitions
  let [lessonText, setLessonText] = React.useState("");
  let [colour, setColour] = React.useState("");
  let [status, setStatus] = React.useState(props.lesson.status);
  React.useEffect(() => { //fetches lesson text if the lesson does not have an image
    if (!props.lesson.has_image) {
      axiosInstance.get(props.lesson.text)
        .then((response) => {
          setLessonText(response.data);
        })
        .catch((error) => {
          console.log(error);
        })
    }
    setColour(getButtonColour(props.lesson.status)); //sets colour of button based on lesson status
  }, [props.lesson.status, props.lesson.text, props.lesson.has_image])

  const handleAssign = (lessonId) => {//assigns per lesson to student
    axiosInstance.post(`studentlesson/add/${lessonId}/${props.student}`, {
      'num_repetitions': repetitions,
      'status': "Assigned",
    }, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        toast.success('Student lesson added successfully!', { autoClose: time }); //success message
        console.log(response.data);
        setStatus("assigned");
        setColour('#FFEC02')
      })
      .catch(error => {
        console.error(error);
        toast.error('Lesson already assigned to student!', { autoClose: time });
      });
  }
  const handleDelete = (lessonId) => {//deletes assigned lesson to student
    axiosInstance.delete(`studentlesson/add/${lessonId}/${props.student}`, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        toast.success('Student lesson deleted successfully!', { autoClose: time });
        console.log(response.data);
        setStatus("unassigned");
        setColour("papayawhip");
      })
      .catch(error => {
        console.error(error);
        toast.error('Lesson not assigned to student yet!', { autoClose: time });
      });
  }
  const handleConfirm = (lessonId) => {//updates assigned lesson to student to confirmed
    axiosInstance.put(`studentlesson/add/${lessonId}/${props.student}`, {
      'num_repetitions': repetitions,
      'status': "Confirmed",
    }, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        toast.success('Student lesson updated successfully!', { autoClose: time });
        console.log(response.data);
        setStatus("confirmed");
        setColour('#00a693'); // green
      })
      .catch(error => {
        console.error(error);
        toast.error('Lesson not assigned to student yet!', { autoClose: time });
      });
  }
  const handleRedo = (lessonId) => {//updates assigned lesson to student to marked for redo
    axiosInstance.put(`studentlesson/add/${lessonId}/${props.student}`, {
      'num_repetitions': repetitions,
      'status': "Marked For Redo",
    }, {
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then(response => {
        toast.success('Student lesson updated successfully!', { autoClose: time });
        console.log(response.data);
        setColour('#FF7C60'); // red
        setStatus("marked_for_redo");
      })
      .catch(error => {
        console.error(error);
        toast.error('Lesson not assigned to student yet!', { autoClose: time });
      });
  }


  const handleRepetitionsChange = (event) => {
    setRepetitions(event.target.value);
  };

  let getButtonColour = (status) => {
    if (status === "completed") {
      return "#7DDAFF"; // light blue
    } else if (status === "assigned") {
      return "#FFEC02"; // yellow
    } else if (status === "confirmed") {
      return "#00a693"; // green
    } else if (status === "marked_for_redo") {
      return "#FF7C60"; // red
    } else if (status === "unassigned") {
      return "papayawhip";
    }
  };
  return (
    <Card sx={{ marginTop: 2, display: "flex", backgroundColor: colour, width: "100%" }}>
      <Box sx={{ display: "flex", alignItems: "center", flexDirection: "row", width: "100%" }}>


        {
          props.lesson.has_image
            ?
            <CardMedia
              component="img"
              sx={{ width: "75%", height: "100%" }}
              image={axiosInstance.getUri() + props.lesson.text}
              alt="Lesson Text for Quran"
            />
            :

            <TextField fullWidth variant="filled" label="Lesson Text" type="text"
              value={lessonText} InputProps={{ readOnly: true, disableUnderline: true }} />
        }
        <Grid item xs={4}>
          <Typography align='right' paddingRight="20px">


          </Typography>
          <ToastContainer />

        </Grid>
        <div>

          {status === "unassigned" && (
            <>
              <input type="number" id="repetitions" name="repetitions" value={repetitions} onChange={handleRepetitionsChange} style={{ width: '60px' }} />
              <Button onClick={() => handleAssign(props.lesson.id)}><AddIcon></AddIcon></Button>
            </>
          )}
          {status === "assigned" && (
            <Button onClick={() => handleDelete(props.lesson.id)}><CloseIcon></CloseIcon></Button>
          )}

          {status === "completed" && (
            <>
              <input type="number" id="repetitions" name="repetitions" value={repetitions} onChange={handleRepetitionsChange} style={{ width: '60px' }} />
              <Button onClick={() => handleConfirm(props.lesson.id)}><DoneAllIcon></DoneAllIcon></Button>
              <Button onClick={() => handleRedo(props.lesson.id)}><ReplayIcon></ReplayIcon></Button>
            </>
          )}
          {status === "marked_for_redo" && (
            <Button onClick={() => handleDelete(props.lesson.id)}><CloseIcon></CloseIcon></Button>
          )}
        </div>
      </Box>
    </Card>
  );

}
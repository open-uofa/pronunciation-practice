import * as React from 'react';
import { Box, TextField, IconButton, Button } from '@mui/material';
import CardMedia from '@mui/material/CardMedia';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';
import Card from '@mui/material/Card';
import axiosInstance from '../../utlities/axiosInstance';
import DoneIcon from '@mui/icons-material/Done';
import ReplayIcon from '@mui/icons-material/Replay';
import DoneAllIcon from '@mui/icons-material/DoneAll';

/**
 * Renders a lesson component that allows a student to listen to a lesson, practice it, and mark it as completed.
 * 
 * @param {JSON} props.lesson - lesson object
 * @param {JSON} props.student - student object
 * @param {String} props.status - status of the lesson
 * @param {Boolean} props.teacher - whether the user is a teacher
 * @param {Boolean} props.content_creator - whether the user is a content creator
 * @param {Boolean} props.parent - whether the user is a parent
 * @param {Function} props.onClickStudent - function to call when the student is clicked
 * 
 * @returns {JSX.Element} - Lesson component 
 */
export default function Lesson(props) {

    let [currentRepetition, setCurrentRepetition] = React.useState(0);
    let lesson = props.lesson;
    let student = props.student;
    let [lessonText, setLessonText] = React.useState("");
    let status = props.status;
    let teacher = props.teacher || false;
    let parent = props.parent || false;
    let content_creator = props.content_creator || false;
    let [size, setSize] = React.useState([0, 0]);


    console.log(lesson.audio);
    let [audio] = React.useState(new Audio(axiosInstance.getUri() + lesson.audio));
    let [isPlaying, setIsPlaying] = React.useState(false);

    let [colour, setColour] = React.useState("");

    React.useEffect(() => { //fetches lesson text if the lesson does not have an image
        if (!lesson.has_image) {
            axiosInstance.get(lesson.text)
                .then((response) => {
                    setLessonText(response.data);
                })
                .catch((error) => {
                    console.log(error);
                })
        }
        setColour(getButtonColour(status));
    }, [status, lesson.text, lesson.has_image, size])

    React.useLayoutEffect(() => {
        function updateSize() {
        setSize([window.innerWidth, window.innerHeight]);
        }
        window.addEventListener('resize', updateSize);
        updateSize();
        return () => window.removeEventListener('resize', updateSize);
    }, []);

    audio.oncanplay = () => {
        audio.addEventListener('play', () => {
            setIsPlaying(true);
        });
        audio.addEventListener('pause', () => {
            setIsPlaying(false);
        });
    };

    audio.onended = () => {

        console.log(currentRepetition);
        setCurrentRepetition(currentRepetition + 1);
        if (content_creator) {
            audio.pause();
        }
        else if (currentRepetition >= lesson.num_repetitions - 1) {
            setCurrentRepetition(0);
            toggleButtonStatus();
        }
        else {
            setTimeout(() => { audio.play(); }, audio.duration * 1000);
        }

    };

    let playAudio = () => {

        if (isPlaying) {
            audio.pause();
        } else {
            audio.play();
        }
    };

    let toggleButtonStatus = () => { //toggles the status of the lesson
        if (lesson.status !== "Completed") {
            lesson.status = "Completed";
            setColour(getButtonColour(lesson.status));
        }
        axiosInstance.put(`students/${student.id}/lessons/${lesson.id}`, lesson)
    };
    let ConfirmButtonStatus = () => { //confirms the status of the lesson
        console.log(student);
        if (status !== "Confirmed") {
            status = "Confirmed";
        }
        axiosInstance.put(`studentlesson/add/${lesson.id}/${student.id}`, { //updates the status of the lesson
            'status': "Confirmed",
        }, {
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                console.log(response.data);
                props.onClickStudent(student.id);
            })
            .catch(error => {
                console.error(error);
            }
            );
    }
    let RedoButtonStatus = () => {
        console.log(student);
        if (status !== "Marked For Redo") {
            status = "Marked For Redo";
        }
        axiosInstance.put(`studentlesson/add/${lesson.id}/${student.id}`, {
            'status': "Marked For Redo",
        }, {
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                console.log(response.data);
                props.onClickStudent(student.id);
            })
            .catch(error => {
                console.error(error);
            }
            );
    }

    let getButtonColour = (status) => {
        if (status === "Completed") {
            return "#7DDAFF"; // light blue
        } else if (status === "Assigned") {
            return "#FFEC02"; // yellow
        } else if (status === "Confirmed") {
            return "#00a693"; // green
        } else if (status === "Marked For Redo") {
            return "#FF7C60"; // red
        }
    };


    return (
        <Card sx={{ display: "flex", backgroundColor: colour, width: 0.9*size[0] }}>
            <Box sx={{ display: "flex", alignItems: "center", flexDirection: "row", width: "100%" }}>

                {!content_creator ? (
                    <>
                    <TextField sx={{ display: "flex", minWidth:"60px", maxidth: "7.5%", width: "7.5%" }} defaultValue={1} variant="filled" label="Repetitions" type="number"
                    value={lesson.num_repetitions} InputProps={{ readOnly: true, disableUnderline: true }} />
                    </>
                ) : null}
                
                <IconButton onClick={playAudio}>
                    {isPlaying ? <PauseIcon /> : <PlayArrowIcon />}
                </IconButton>

                {
                    (lesson.status !== "Confirmed" && lesson.status !== "Completed" && !teacher && !parent && !content_creator) &&
                    <Button variant="text" sx={{ color: "green", height: "75%" }} onClick={toggleButtonStatus}><DoneIcon></DoneIcon></Button>
                }
                {
                    (status === "Completed" && status !== "Confirmed" && teacher) &&
                    <Button variant="text" sx={{ color: "blue", height: "75%" }} onClick={ConfirmButtonStatus}><DoneAllIcon></DoneAllIcon></Button>
                }
                {
                    (status === "Completed" && status !== "Confirmed" && teacher) &&
                    <Button variant="text" sx={{ color: "red", height: "75%" }} onClick={RedoButtonStatus}><ReplayIcon></ReplayIcon></Button>
                }
                {
                    lesson.has_image
                        ?
                        <CardMedia
                            component="img"
                            sx={{ width: "100%", height: "100%", objectFit:"cover", objectPosition:"100% 0" }}
                            image={axiosInstance.getUri() + lesson.text}
                            alt="Lesson Text for Quran"
                        />
                        :

                        <TextField fullWidth variant="filled" multiline label="Lesson Text" type="text" inputProps={{ style: {whiteSpace: "initial", fontSize: 64, fontFamily: "cursive", textAlign: "center", textAlignVertical: "center", lineHeight: 1.2} }}   
                            value={lessonText} InputProps={{ readOnly: true, disableUnderline: true }} />
                }
            </Box>
        </Card>
    );
}
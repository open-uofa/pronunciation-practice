import { useEffect, useState } from 'react';
import "../../css/homePage.css";
import HomeLessonTab from './HomeLessonTab';
import SidebarStudent from './Sidebar_student';
import SidebarParent from '../../pages/Parent';
import axiosInstance from '../../utlities/axiosInstance';
import {useLocation} from 'react-router-dom';
import Child from '../../pages/Child';
import SideBarStudentLesson from '../../pages/Student';
import HelpPage from '../../pages/Help';

/**
 * Renders the home page of the student or parent
  @param props: 
    - role: student or parent
    - username: username of the user
    - items: list of lesson tabs
    @returns: JSX.Element
    
*/
function HomePage() {
  const uuid = localStorage.getItem("id");
  const [username, setUsername] = useState("");
  const [firstName, setFirstName] = useState("");
  const [items, setItems] = useState([]);
  const [role, setRole] = useState('');
  const location = useLocation(); 
  const [parentStudent, setParentStudent] = useState([]);
  const [showLessons, setShowLessons] = useState('');
  const [childLessons, setChildLessons] = useState([]);
  const [selectedChild, setSelectedChild] = useState('')
  const [goToHelp, setGoToHelp] = useState(false)


  // When the component mounts, fetch the JSON data from the API endpoint
  useEffect(() => {
    // Check if user is a student
    axiosInstance.get(`users/${localStorage.getItem("id")}/`)
      .then((res) => {
            //console.log(student.id);
            setRole(res.data.role);
            setFirstName(res.data.first_name);
            // Get lesson tab of student
              axiosInstance.get(`lessontabs/student/${uuid}/`)
                .then((res) => {
                  console.log(res.data);
                  setItems(res.data.tabs);
                });
         
      });

      axiosInstance.get(`parentstudent/${localStorage.getItem('id')}`)
      .then((response)=>{
          setParentStudent(response.data);
      }) 


    // Check if user is a parent
    axiosInstance.get('parents/')
      .then((res) => {
        let parents = res.data
        for (let parent of parents) {
          if (parent.id === uuid) {
            setRole('Parent');
            setFirstName(parent.first_name);
            setUsername(parent.first_name);
            // Get children
            axiosInstance.get(`lessontabs/parentchildren/${uuid}/`)
              .then((res) => {
                setItems(res.data);
              });
            break;
          }
        }
      });
  }, [uuid]);


  // Render tabs of student or children of parent
  function renderTabs() {
    if (role === "Student") {
      return (items?.map((tab) => (
        <HomeLessonTab key={tab.id} tab={tab} role={role} childName={null} setShowLessons={setShowLessons}/>
      )));
    } else if (role === "Parent") {
      console.log("student",items)
      return (items.students?.map((student) => (
        student.tabs?.map((tab) => (
          <HomeLessonTab 
            key={tab.id} 
            tab={tab} 
            role={role} 
            child={student} 
            setShowLessons={setShowLessons} 
            setChildLessons={setChildLessons}
            selectedChild={selectedChild}/>
        ))
      )));
    }
  }

  // Display parent or student sidebar based on role
  function displaySidebar() {
    if (role === "Parent") {
      return (
      <SidebarParent 
        username={username} 
        role={role} 
        chapters={location?.state?.chapters} 
        setShowLessons={setShowLessons}
        setChild={setSelectedChild}
        setGoToHelp={setGoToHelp}/>);
    } else if (role === "Student") {
      return <SidebarStudent onTabChange={setItems} setShowLessons={setShowLessons} setGoToHelp={setGoToHelp}/>;
    }
  }

  function displayHomePage() {

    if (showLessons!=='') {
      if (role==="Parent") {
        return(
          parentStudent.map((item)=>{
            if (item.student.id === showLessons) {
              return(
              <Child 
                lessons={childLessons}
                childName = {item.student.first_name}>
              </Child>)
            } return null
          }))
        } else if (role==="Student"){
            return(<SideBarStudentLesson chapter={showLessons}></SideBarStudentLesson>)
        }
    } else if (goToHelp === true) {
        return <HelpPage role={role}></HelpPage>
    }
    return(
      <div className='bg'>
        <div className="title">IlmHub Pronunciation Practice for {role}s</div>
        <div className="welcome-msg">Welcome back, {firstName}! To get started, select a chapter below:</div>
        {renderTabs()}
      </div>)
  }

  return (
    <>
      {displaySidebar()}
      {displayHomePage()}
    </>
  );
}

export default HomePage;
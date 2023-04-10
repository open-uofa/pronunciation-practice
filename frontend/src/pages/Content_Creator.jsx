import * as React from 'react';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Divider from '@mui/material/Divider';
import Tooltip from '@mui/material/Tooltip';
import axiosInstance from '../utlities/axiosInstance';
import { useState, useEffect } from 'react';
import { styled, useTheme } from '@mui/material/styles';
import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItemButton from '@mui/material/ListItemButton';
import Lesson from '../components/StudentParent/Lesson';
import Stack from '@mui/material/Stack';
import logout from '../utlities/Logout';

const drawerWidth = 240;

const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));

function Sidebar4() {
  const [anchorEl, setAnchorEl] = useState(null);
  const [tabIdx, setTabIdx] = useState(0);
  const [tabs, setTabs] = useState([]);
  const [lessons, setLessons] = useState([]);
  const [chapters, setChapters] = useState([]);
  const [chapName, setChapName] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [fileName, setFileName] = useState(null);
  const [upload, setUpload] = useState(false);
  const theme = useTheme();
  const [open2, setOpen] = React.useState(false);
  const [tabId, setTabID] = useState(null);

  const handleDrawerOpen = (tab, index) => {
    setChapters(tab.chapters);
    setTabIdx(index);
    setOpen(true);
    setUpload(false);
  };

  const handleDrawerClose = () => {
    setOpen(false);
  };
  

  const open = Boolean(anchorEl);

  useEffect(()=>{

    axiosInstance.get(`lessontabs/`)
    .then((response) => {
      setTabs(response.data.tabs);
      setLessons(response.data.tabs[0].chapters[0].lessons);
      setChapters(response.data.tabs[0].chapters);
      setChapName(response.data.tabs[0].chapters[0].name);
    })
    .catch((err) => {
      console.error(err);
    })
  }, [])

  const lessonComponents = lessons.map(lesson => (
    <Lesson lesson={lesson} content_creator={true}/>
  ));

  const onClickChapter = (chapter) => {
    setUpload(false);
    setChapName(chapter.name);
    setLessons(chapter.lessons);
  }

  const onClickUpload = () => {
    setUpload(true);
  }

  const onClickUploadChapter = (tabId) => {
    setUpload(true);
    setTabID(tabId);
  }

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const onFileChange = (event) => {
    setFileName(event.target.files[0].name);
    setSelectedFile(event.target.files[0]);
  };
  
  const onFileUpload = (event) => {

    if(tabId != null){
      event.preventDefault();
      const formData = new FormData();
      formData.append('filename', fileName);
      formData.append('file', selectedFile);
      //formData.append('tabId', tabId);
      setTabID(null);
      const config = {
          headers: { 'content-type': 'multipart/form-data' }
      }

      axiosInstance.post(`lessontabs/${tabId}/`, formData, config)
      .then((response) => {
          alert(fileName.slice(0,-4) + " chapter is successfully uploaded!");
          axiosInstance.get(`lessontabs/`)
          .then((response) => {
            setTabs(response.data.tabs);
            setLessons(response.data.tabs[tabIdx].chapters[0].lessons);
            setChapters(response.data.tabs[tabIdx].chapters);
          })
          .catch((err) => {
            console.error(err);
          })
      })
      .catch((error) => {
        alert("ERROR: " + fileName.slice(0,-4) + " chapter could not be uploaded, please check the file format/structure and try again");
            
      });
    }

    else {
      event.preventDefault();
      const formData = new FormData();
      formData.append('filename', fileName);
      formData.append('file', selectedFile);

      const config = {
          headers: { 'content-type': 'multipart/form-data' }
      }

      axiosInstance.post(`lessontabs/`, formData, config)
      .then((response) => {
          alert(fileName.slice(0,-4) + " tab is successfully uploaded!");
          axiosInstance.get(`lessontabs/`)
          .then((response) => {
            setTabs(response.data.tabs);
            setLessons(response.data.tabs[0].chapters[0].lessons);
            setChapters(response.data.tabs[0].chapters);
          })
          .catch((err) => {
            
            console.error(err);
          })
      })
      .catch((error) => {
        alert("ERROR: " + fileName.slice(0,-4) + " tab could not be uploaded, please check the file format/structure and try again");
      }); 
    }  
  }; 
  

  return (
    <React.Fragment>
      <Box sx={{ display: 'flex', alignItems: 'center', textAlign: 'center', backgroundColor: "green" }}>
      <Toolbar>
        {tabs.map((item, index)=>{
          return (
            <IconButton
            color="inherit"
            aria-label="open drawer"
            onClick={()=>handleDrawerOpen(item, index)}
            edge="start"
            sx={{ mr: 2, ...(open && { display: 'none' }) }}
          >
            {item.name}
          </IconButton>
          )
        })}
            <IconButton
                aria-label="tab upload"
                onClick={()=>onClickUpload()}
                edge="start"
                sx={{ color: "white", fontWeight: "bold", mr: 2, ...(open && { display: 'none' }) }}
            >
                Upload +
            </IconButton>
        </Toolbar>
        <Box sx={{ display: 'flex', width: '100%', justifyContent: "flex-end"}}>
        <Tooltip title="Account settings">
          <IconButton
            onClick={handleClick}
            size="small"
            sx={{ ml: 2 }}
            aria-controls={open ? 'account-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
          >
            <Avatar sx={{ width: 32, height: 32 }}>CC</Avatar>
          </IconButton>
        </Tooltip>
      </Box>
      </Box>
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
          },
        }}
        variant="persistent"
        anchor="left"
        open={open2}
      >
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
          </IconButton>
        </DrawerHeader>
        <Divider />
        <List style={{backgroundColor: "palegreen"}}>
          {chapters.map((item, index)=>{
        return (
          <ListItemButton onClick={()=>onClickChapter(item)} key={index}> {item.name} </ListItemButton>
        )
      })}
        <ListItemButton sx={{ fontWeight: "bold" }}onClick={()=>onClickUploadChapter(chapters[0].tab)}> Upload Chapter + </ListItemButton>
        </List>
      </Drawer>
        <DrawerHeader />

    <Menu
        anchorEl={anchorEl}
        id="account-menu"
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        PaperProps={{
            elevation: 0,
            sx: {
            overflow: 'visible',
            filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
            mt: 1.5,
            '& .MuiAvatar-root': {
                width: 32,
                height: 32,
                ml: -0.5,
                mr: 1,
            },
            '&:before': {
                content: '""',
                display: 'block',
                position: 'absolute',
                top: 0,
                right: 14,
                width: 10,
                height: 10,
                bgcolor: 'background.paper',
                transform: 'translateY(-50%) rotate(45deg)',
                zIndex: 0,
            },
            },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
        >
        <MenuItem  >
            <Avatar /> Content Creator
        </MenuItem>
        {/* <MenuItem onClick={handleClose}>
            <Avatar /> My account
        </MenuItem> */}
        <Divider />
        <MenuItem  >
        <button onClick={logout}>Log Out</button>
        </MenuItem>
    </Menu>
    {upload ? 
        <div className="App" style={{height:"100%"}}>
        <h1>Lesson Upload</h1>
        <h4>Upload lessons and chapters manually by adding .zip files containing lesson text and audio:</h4>
        <div>
            <form encType='multipart/form-data' method='POST'>
                <input type="file" id="file" name="file" onChange={onFileChange} accept=".zip"/>
                <button type="submit" onClick={onFileUpload}>Upload Tab/Chapter</button>
            </form>
        </div>
    </div>   
    : 
    <div className="App" style={{height:"100%", backgroundColor: "powderblue"}} >
        <h1 style={{fontWeight:"normal"}}>Lessons for {chapName}:</h1>
        <div className="lessons" width="100%" >
        <Stack spacing={2} alignItems='center' justifyContent='center' p='16px' gap='16px' width="100%" >{lessonComponents}</Stack>
        </div>
    </div>     
    }
    </React.Fragment>
  );
}

export default Sidebar4;
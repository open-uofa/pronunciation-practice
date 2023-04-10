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
import logout from '../utlities/Logout';
import '../css/Sidebar.css';
import HomeIcon from '@mui/icons-material/Home';
import ListItemIcon from '@mui/material/ListItemIcon';
import Logout from '@mui/icons-material/Logout';
import HelpIcon from '@mui/icons-material/Help';
import { useNavigate } from 'react-router-dom';

const drawerWidth = 240;




const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));

function Sidebar2(props) {
  const [parent, setParent] = useState([])
  const [ps, setPs] = useState([]);
  const [undone, setUndone] = useState([]);
  const [done, setDone] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);
  let navigate = useNavigate();

  const [anchorEl, setAnchorEl] = useState(null);

  const theme = useTheme();
  const [open2, setOpen] = React.useState(false);
  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  const open = Boolean(anchorEl);

  useEffect(() => {
    axiosInstance.get(`parents/${localStorage.getItem('id')}/`)
      .then((response) => {
        setParent(response.data);
      })
      .catch(err => {
        console.error(err);
      })
    axiosInstance.get(`parentstudent/${localStorage.getItem('id')}`)
      .then((response) => {
        setPs(response.data);
      })


  }, [])
  const onClickStudent = (id) => { // This function is called when a student is clicked
    console.log(`Clicked on item with id ${id}`);
    axiosInstance.get(`unfinished/${id}/lessons/`)

      .then((resp) => {
        console.log(resp.data);
        setUndone(resp.data); // Update the component's state with the fetched data
        setShowDropdown(id); // Show the dropdown
      })
      .catch((error) => {
        console.error(error); // Log any errors
        // Handle the error
      });
    axiosInstance.get(`finished/${id}/lessons/`)
      .then((resp) => {
        console.log(resp.data);
        setDone(resp.data); // Update the component's state with the fetched data
        setShowDropdown(id); // Show the dropdown
      })
      .catch((error) => {
        console.error(error); // Log any errors
      });
  };


  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };
  return (
    <React.Fragment>
      <Box sx={{ display: 'flex', alignItems: 'center', textAlign: 'center', backgroundColor: "green" }}>
      <Toolbar>
      <IconButton style={{ color: 'white', marginRight: '50px', fontSize: 'medium'}} onClick={() => {props.setShowLessons(""); props.setChild('');}}>
      <HomeIcon sx={{ fontSize: 30 }} />
        </IconButton>
          <IconButton style={{ color: 'white', marginRight: '50px', fontSize: 'medium'}}
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{ mr: 2, ...(open && { display: 'none' }) }}
          >
            Child
          </IconButton>
          <IconButton style={{ color: 'white', marginRight: '50px', fontSize: 'medium' }} onClick={() => {
              navigate("/help");
            }}>
            <HelpIcon sx={{ fontSize: 30 }} />
          </IconButton>

        </Toolbar>
        <Box sx={{ display: 'flex', width: '100%', justifyContent: "flex-end" }}>
          <Tooltip title="Account settings">
            <IconButton
              onClick={handleClick}
              size="small"
              sx={{ ml: 2 }}
              aria-controls={open ? 'account-menu' : undefined}
              aria-haspopup="true"
              aria-expanded={open ? 'true' : undefined}
            >
              <Avatar sx={{ width: 32, height: 32 }}>P</Avatar>
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
        {ps.map((item, index)=>{
      return (
        <ListItemButton className='lesson-finish-unfinsh' onClick={()=>{onClickStudent(item.student.id);props.setChild(item.student.id)}} key={index}> <strong>{item.student.username}</strong>
        {showDropdown === item.student.id && (
          <div  > 
          <p>Unfinished: {undone.length}</p>  
          <p>Finished: {done.length}</p> 
        </div>
      )}
        </ListItemButton>
      )
      })}
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
          <Avatar /> <strong>{parent["username"]}</strong>
        </MenuItem>
        <Divider />
        <MenuItem  >
          <ListItemIcon>
            <Logout fontSize="small" />
          </ListItemIcon>
          <button onClick={logout}>Log Out</button>
        </MenuItem>
      </Menu>
    </React.Fragment>
  );
}

export default Sidebar2;
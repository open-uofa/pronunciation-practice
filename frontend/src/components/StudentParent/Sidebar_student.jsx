import * as React from 'react';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Divider from '@mui/material/Divider';
import Tooltip from '@mui/material/Tooltip';
import Logout from '@mui/icons-material/Logout';
import axiosInstance from '../../utlities/axiosInstance';
import { useState, useEffect, useCallback } from 'react';
import { styled, useTheme } from '@mui/material/styles';
import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import logout from '../../utlities/Logout';
import { FormControl, Select, InputLabel } from '@mui/material';
import DoneIcon from '@mui/icons-material/Done';
import HourglassTopIcon from '@mui/icons-material/HourglassTop';
import HomeIcon from '@mui/icons-material/Home';
import HelpIcon from '@mui/icons-material/Help';
import { useNavigate } from 'react-router-dom';

const drawerWidth = 240;

const DrawerHeader = styled("div")(({ theme }) => ({
  display: "flex",
  alignItems: "center",
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: "flex-end",
}));

function Sidebar(props) {
  const [anchorEl, setAnchorEl] = useState(null);
  const [student, setStudent] = useState([]);
  const [chapters, setChapters] = useState([]);
  const [lessontabs, setLessontabs] = useState([]);
  const [tabName, setTabName] = useState(0);
  const [undone, setUndone] = useState([]);
  const [done, setDone] = useState([]);
  let navigate = useNavigate();
  

  const theme = useTheme();
  const [open2, setOpen] = React.useState(false);
  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  const open = Boolean(anchorEl);

  const onTabChange=props.onTabChange

  useEffect(() => {
    axiosInstance
      .get(`students/${localStorage.getItem("id")}/`)
      .then((response) => {
        setStudent(response.data);
      })
      .catch((err) => {
        console.error(err);
      });

    axiosInstance
      .get(`lessontabs/student/${localStorage.getItem("id")}/`)
      .then((response) => {
        console.log("dataaaa: ", response.data);
        setLessontabs(response.data["tabs"]); 
        var chapters = []
        for (let tab of response.data.tabs) {
          chapters = chapters.concat(tab.chapters)
        }
        setChapters(chapters);
      })
      .catch((err) => {
        console.error(err);
      });
    axiosInstance
      .get(`unfinished/${localStorage.getItem("id")}/lessons/`)
      .then((response) => {
        setUndone(response.data);
      })
      .catch((err) => {
        console.error(err);
      });

    axiosInstance
      .get(`finished/${localStorage.getItem("id")}/lessons/`)
      .then((response) => {
        setDone(response.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  const onClickChapter = (chapter) => {
    props.setShowLessons(chapter)
  }

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleInputChange = useCallback(event => {
    setTabName(event.target.value);
    setChapters(event.target.value.chapters);
    const tabs = [event.target.value]
    onTabChange(tabs)
  }, [onTabChange])

  return (
    <React.Fragment>
      <Box
        sx={{
          display: "flex",
          alignItems: "center",
          textAlign: "center",
          backgroundColor: "green",
          fontSize: "small",
        }}
      >
        <Toolbar>
          <IconButton
            style={{ color: "white", marginRight: "50px", fontSize: "medium" }}
            onClick={() => {props.setShowLessons("");}}
          >
            <HomeIcon sx={{ fontSize: 30 }} />
          </IconButton>
          <IconButton
            style={{ color: "white", marginRight: "10px", fontSize: "medium" }}
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            edge="start"
            sx={{ mr: 2 }}
          >
            Chapter
          </IconButton>
          <IconButton
            style={{ color: "white", marginRight: "50px", fontSize: "medium" }}
            onClick={() => {
              navigate("/help");
            }}
          >
            <HelpIcon sx={{ fontSize: 30 }} />
          </IconButton>
          <Box sx={{ minWidth: 120 }}>
            <FormControl fullWidth>
              <InputLabel id="demo-simple-select-label">Tab</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={tabName}
                label="Tab"
                onChange={handleInputChange}
              >
                {lessontabs.map((tab) => (
                  <MenuItem value={tab}>{tab.name}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
        </Toolbar>
        <Box
          sx={{ display: "flex", width: "100%", justifyContent: "flex-end" }}
        >
          <Tooltip title="Account settings">
            <IconButton
              onClick={handleClick}
              size="small"
              sx={{ ml: 2 }}
              aria-controls={open ? "account-menu" : undefined}
              aria-haspopup="true"
              aria-expanded={open ? "true" : undefined}
            >
              <Avatar sx={{ width: 32, height: 32 }}>S</Avatar>
            </IconButton>
          </Tooltip>
        </Box>
      </Box>
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
          },
        }}
        variant="persistent"
        anchor="left"
        open={open2}
      >
        <DrawerHeader>
          <IconButton onClick={handleDrawerClose}>
            {theme.direction === "ltr" ? (
              <ChevronLeftIcon />
            ) : (
              <ChevronRightIcon />
            )}
          </IconButton>
        </DrawerHeader>
        <Divider />
        <List style={{ backgroundColor: "palegreen" }}>
          {chapters.map((item, index) => {
            return (
              <ListItemButton onClick={() => onClickChapter(item)} key={index}>
                {" "}
                {item.name}{" "}
              </ListItemButton>
            );
          })}
        </List>
        <List></List>
      </Drawer>
      <DrawerHeader />



      <Menu
        anchorEl={anchorEl}
        id="account-menu"
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        disableEnforceFocus={true}
        PaperProps={{
          elevation: 0,
          sx: {
            overflow: "visible",
            filter: "drop-shadow(0px 2px 8px rgba(0,0,0,0.32))",
            mt: 1.5,
            "& .MuiAvatar-root": {
              width: 32,
              height: 32,
              ml: -0.5,
              mr: 1,
            },
            "&:before": {
              content: '""',
              display: "block",
              position: "absolute",
              top: 0,
              right: 14,
              width: 10,
              height: 10,
              bgcolor: "background.paper",
              transform: "translateY(-50%) rotate(45deg)",
              zIndex: 0,
            },
          },
        }}
        transformOrigin={{ horizontal: "right", vertical: "top" }}
        anchorOrigin={{ horizontal: "right", vertical: "bottom" }}
      >
        <MenuItem>
          <Avatar /> <strong>{student["username"]}</strong>
        </MenuItem>
        <Divider />
        <MenuItem sx={{ pointerEvents: "none" }}>
          <ListItemIcon>
            <DoneIcon fontSize="small" />
          </ListItemIcon>
          <strong>Finished Lessons:</strong> {done?.length}
        </MenuItem>
        <MenuItem sx={{ pointerEvents: "none" }}>
          <ListItemIcon>
            <HourglassTopIcon fontSize="small" />
          </ListItemIcon>
          <strong>Unfinished Lessons:</strong> {undone?.length}
        </MenuItem>
        <MenuItem>
          <ListItemIcon>
            <Logout fontSize="small" />
          </ListItemIcon>
          <button onClick={logout}>Log Out</button>
        </MenuItem>
      </Menu>
    </React.Fragment>
  );
}

export default Sidebar;

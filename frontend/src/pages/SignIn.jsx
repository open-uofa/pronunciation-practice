import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useState } from 'react';
import axiosInstance from '../utlities/axiosInstance';
import { useNavigate } from 'react-router-dom';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import logo from '../logo/ilmhub-halal-logo.png';
const theme = createTheme();

/**
 * Renders the login page.
 * 
 * @returns {JSX.Element} - The JSX for the login page
 */
export default function SignIn({ onRoleChange }) {
  const time = 500;
  const navigate = useNavigate()
  const [username, setUsername] = useState(null);
  const [password, setPassword] = useState(null);

  const onClickLogin = () => {
    return;
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData();
    data.append('username', username);
    data.append('password', password);
    axiosInstance.postForm('login/', data)
    .then((response)=>{
      console.log(response.data)
      localStorage.setItem('access_token', response.data["access"]);
      localStorage.setItem('refresh_token', response.data["refresh"]);
      localStorage.setItem('id', response.data["id"]);
      localStorage.setItem('role', response.data["role"]);
      onRoleChange(response.data["role"]); // Call onRoleChange to update the role
      if(response.data["role"].toLowerCase() === "student"){
        navigate('/student/home')
      }else if(response.data["role"].toLowerCase() === "teacher"){
        navigate('/teacher')
      } else if(response.data["role"].toLowerCase() === "parent"){
        navigate('/parent/home')
      }
      else if(response.data["role"].toLowerCase() === "content creator"){
        navigate('/content_creator')
      }
    })
    .catch((error) => {
      console.log(error);
      toast.error('Invalid username or password', {autoClose: time});
    });
  };


  return (
    <div style={{ 
      backgroundImage: `url(ilmhub.jpg)`,
      backgroundSize: 'cover',
      height: '100vh',
      width: '100vw',
    }}>
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ width: 90, height: 90 }} variant="rounded" alt="IlmHub" src={logo} />
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="Username"
              name="Username"
              autoComplete="Username"
              autoFocus
              onChange={(e)=>{setUsername(e.target.value)}}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              onChange={(e)=>{setPassword(e.target.value)}}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2}}
              onClick={()=>onClickLogin()}
            >
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
              </Grid>
            </Grid>
            <ToastContainer position="top-right" />
        </Box>
      </Box>
    </Container>
  </ThemeProvider>
  </div>
);
}

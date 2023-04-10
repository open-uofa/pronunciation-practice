import React, { useState } from "react";
import './css/App.css';
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar3 from "./pages/Teacher";
import Sidebar4 from "./pages/Content_Creator";
import ProtectedRoute from "./utlities/ProtectedRoute";
import HomePage from "./components/StudentParent/homePage";
import HelpPage from "./pages/Help";

function App() {
  const [role, setRole] = useState(localStorage.getItem('role'));

  
  const handleRoleChange = (newRole) => {
    setRole(newRole);
  };
  // console.log('role', role);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/login" replace={true}/>}/>
        <Route element={<SignIn onRoleChange={handleRoleChange}/>} path="/login" />
        {role === 'Student' && <Route element={<ProtectedRoute> <HomePage/></ProtectedRoute>} path="/" />}
        {role === 'Student' && <Route element={<ProtectedRoute> <HomePage/></ProtectedRoute>} path="/student/home" />}
        <Route element={<SignUp/>} path="/register" />
        {role === 'Teacher' && <Route element={<ProtectedRoute> <Sidebar3/></ProtectedRoute>} path="/teacher" />}
        {role === 'Parent' && <Route element={<ProtectedRoute> <HomePage/></ProtectedRoute>} path="/parent" />}
        {role === 'Parent' && <Route element={<ProtectedRoute> <HomePage/></ProtectedRoute>} path="/parent/home" />}
        {role === 'Content Creator' && <Route element={<ProtectedRoute> <Sidebar4/></ProtectedRoute>} path="/content_creator" />}
        <Route element={<HelpPage />} path="/help"/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;

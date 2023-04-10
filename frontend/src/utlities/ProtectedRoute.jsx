import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";


/**
 * A protected route that redirects the user to the login page if they are not logged in, and displays the page if they are logged in.
 * 
 * @param {String[]} props.children - The children of the parent user
 * @returns {JSX.Element} - The list of children of the parent user or the login page
 */
const ProtectedRoute = (props) => {

    const navigate = useNavigate();
    const [isLoggedIn, setIsLoggedIn] = useState(false);

     

    useEffect(() => {
        const checkLoggedIn = () => {
            const token = localStorage.getItem('access_token');
            if (!token || token === 'undefined') {
                setIsLoggedIn(false);
                return navigate('/login');
            }
    
            setIsLoggedIn(true);
        }
        checkLoggedIn();
    }, [isLoggedIn, navigate]);


    return (
        <React.Fragment>
            {
                isLoggedIn ? props.children : null
            }
        </React.Fragment>
    );
}

export default ProtectedRoute;
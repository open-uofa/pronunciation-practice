import * as React from 'react';
import axiosInstance from '../../utlities/axiosInstance';
import { useState, useEffect } from 'react';


/**
 * Renders a complete list of all the parent's children.
 * 
 * @returns {JSX.Element} - The JSX to display a list of all the parent's children
 */
function Parents() {
    const [id, setId] = useState(null);
    const [parent, setParent] = useState([])
    const [ps, setPs] = useState([]);

useEffect(()=>{
    axiosInstance.get(`parents/${localStorage.getItem('id')}/`)
    .then((response)=>{
        console.log(response.data);
      setParent(response.data);
    })
    .catch(err => {
      console.error(err);
    })
    axiosInstance.get(`parentstudent/${localStorage.getItem('id')}`)
    .then((response)=>{
        console.log(response.data);
        setPs(response.data);
    }) 


  }, [])

  return(
    <h1>{ps.map((item, index)=>{
      return (
        <h1 key={index}>{item.student.username}</h1>
      )
    })}</h1>
  );  
}
export default Parents;
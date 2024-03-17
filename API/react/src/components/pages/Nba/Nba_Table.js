import React from "react";
import { useState,useEffect } from "react";

function Nba_Table() {
    //need to fetch my nba_match_up data here
  
    //useEffect to prevent multi fetches
    //below will fetch data twice if we invoke fetchData()

    //introduce useEffect will only fetch once component is mounted
    // useEffect -> code to run after every render
    // TODO: could add cache file to prevent multiple renderings get requests
    // to get jsondata outside of fetch scope
    const [jsonData,setJsonData] = useState(null);
    const [count , setCount] = useState(0);
    useEffect(()=>{
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:5000/nba_data');
                const jsonData = await response.json();
                setJsonData(jsonData);
                setCount(prevCount => prevCount + 1);
            }catch (error) {
                console.error("woops",error);
            }
        }
        fetchData();
    },[]);

    return (
        <div>
            <h1>{count}</h1>
            <p>{jsonData}</p>
        </div>
    );
}

export default Nba_Table;
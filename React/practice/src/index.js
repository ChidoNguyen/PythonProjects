import React from "react";
import App from './App';
import ReactDOM from 'react-dom/client';
//import './Table.css';

const root = ReactDOM.createRoot(document.getElementById("root"));
// root variable is essentially our react component "starting" point we find a specific element in our html doc and then render our stuff under "root" element 
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
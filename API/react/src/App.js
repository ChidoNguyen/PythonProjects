import React from "react";  
import {BrowserRouter as Router , Routes , Route } from 'react-router-dom';
import  Home from './components/pages/Home/Home';
import Nba from './components/pages/Nba/Nba';
function App() {
    return (
        <div>
            <Routes>
                <Route path="/"  element = {<Home/>} />
                <Route path="/nba" element = {<Nba/>}/>
            </Routes>
        </div>
    );
}

export default App;
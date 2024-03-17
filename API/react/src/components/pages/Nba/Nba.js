import React , {useState,useEffect} from "react";
import { Link } from "react-router-dom";
import Nba_Table from "./Nba_Table";

/**
 * 
 *  NBA home page -> div -> table -> table data formatting 
 */
function Nba() {
    return(
        <div id = "nba">
            <h1>Today's Game</h1>
            <div id = "game_table">
                GameTableCompCalledInSource
                <Nba_Table />
                <Link to="/">Homepage</Link>
            </div>
        </div>
    );
}

export default Nba;
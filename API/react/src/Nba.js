import React from "react";
import { Link } from "react-router-dom";
function Nba() {
    return(
        <div id = "nba">
            <h1>Today's Game</h1>
            <div id = "game_table">
                GameTableGoesHereLater
                <Link to="/">Homepage</Link>
            </div>
        </div>
    );
}

export default Nba;
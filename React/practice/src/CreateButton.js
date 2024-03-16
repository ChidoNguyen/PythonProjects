import React , {useState} from "react";
import './Button.css'
//props here will be 2 int values to create our button key

const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey
    const [playerText , setDisplayText] = useState(''); //useState takes starting arg in this case empty string

    // on click we check 
    const handleClick = () =>{
        
        //playable square check
        //winner or loser(?)
        let sq = props.key;

        if (playerText === ''){ //check the useState of the button to see if its empty 
            console.log("playable");
            props.move(sq);
            setDisplayText('X');
        }else{
            console.log("unplayble");
            alert("no play");
        }
    };

    return (
        <button className = 'empty-button' key = {buttKey} onClick = {handleClick}>
            <p>{playerText}</p>
        </button>
    );
}
export default CreateButton;
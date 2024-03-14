import React , {useState} from "react";
import './Button.css'
//props here will be 2 int values to create our button key
const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey
    const [playerText , setDisplayText] = useState(' '); //useState takes starting arg in this case empty string
    const [playerTurn , setPlayerTurn] = useState(0);

    // on click we check 
    const handleClick = () =>{
        if( playerTurn === 0){
            setDisplayText('X');
        } else {
            setDisplayText('O');
        }
        setPlayerTurn(1)
        console.log(playerTurn)
    };

    return (
        <button className = 'empty-button'key = {buttKey} onClick = {handleClick}>
            <p>{playerText}</p>
        </button>
    );
}
export default CreateButton;
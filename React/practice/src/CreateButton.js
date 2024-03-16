import React , {useState} from "react";
import './Button.css'
//props here will be 2 int values to create our button key

const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey
    const [playerText , setDisplayText] = useState(''); //useState takes starting arg in this case empty string

    // on click we check 
    const handleClick = () =>{
        if(playerText === ''){
            if (props.count === 0){
                setDisplayText('X');
            }else{
                setDisplayText('O');
            }
            props.move(buttKey);
            
            //let pC = props.count === 0 ? props.p1: props.p2;
            //console.log(props.p1);
            //console.log(props.p2);
            if (props.win(pC)) {
                window.location.reload()
                //winner_restart();
            }
            props.turn();
        } else{
            alert("Can't make a play here!");
        }
    };

    return (
        <button className = 'empty-button' key = {buttKey} onClick = {handleClick}>
            <p>{playerText}</p>
        </button>
    );
}
export default CreateButton;
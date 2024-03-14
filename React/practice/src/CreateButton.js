import React from "react";
import './Button.css'
//props here will be 2 int values to create our button key
const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey

    const handleClick = () =>{
        alert('woah!');
    };

    return (
        <button className = 'empty-button'key = {buttKey} onClick = {handleClick}></button>
    );
}
export default CreateButton;
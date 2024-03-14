import React from "react";
//props here will be 2 int values to create our button key
const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey

    return (
        <button key = {buttKey}>XO</button>
    );
}
export default CreateButton;
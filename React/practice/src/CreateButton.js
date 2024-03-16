import React , {useState} from "react";
import './Button.css'
//props here will be 2 int values to create our button key
/* 
Parent Properties being passed down:
p1 - an arr of already made "plays"
p2-  same as above
buttonKey - "keygen" to give each square/button a distinct key/id
count -> 0/1 for which player is playing
change_turn => function to swap turns after each play might even nest this into makeMove
make -> function to assign square/id/key to p1 or p2's plays arr
win -> check for winner
*/
async function winnerRender(player){
    let pText = player === 0 ? 'Player 1' : 'Player 2';
    //js doesnt let you stall directly ; patch job possible
    function myAlert(pText){
        return new Promise(resolve => { // to be used with await/async
            alert(`${pText} has won! Close alert to restart game.`);
            ;resolve();
        });
    }
    await myAlert(player);
};
const CreateButton = (props) => {
    // make my button
    const buttKey = props.buttonKey
    const [playerText , setDisplayText] = useState(''); //useState takes starting arg in this case empty string

    // on click we check 
    const handleClick = () =>{
        
        //playable square check
        // who gets to play
        //winner or loser(?)
        let sq = props.buttonKey;
        console.log(sq);
        let pTurn = props.count;
        if (playerText === ''){ //check the useState of the button to see if its empty 
            console.log("playable");
            let newM = props.move(sq);
            if(pTurn){
                setDisplayText('O');
            }else{
                setDisplayText('X');
            }
            setTimeout(() => {
                if(props.win(newM)){ 
                    winnerRender(pTurn);
                }
            },500);
        props.change_turn();
        }else{
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
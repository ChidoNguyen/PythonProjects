import React , {useState} from "react";
import config from  './config';
import './Table.css'
import CreateButton from './CreateButton';
/* could prolly pass in X_Y grid size*/
/*could be considered our "game" controller too */

const WinCon = (playerChoice) => {
    // 00 / 01 // 02
    // 10 / 11 // 12
    // 20 / 21 // 22
    // 3x3 square ids
    const winDex = [["00","01","02"],
                    ["10","11","12"],
                    ["20","21","22"],

                    ["00","10","20"],
                    ["01","11","22"],
                    ["02","12","20"],

                    ["00","11","22"],
                    ["02","11","20"]];
    const arr = playerChoice;
    for (let i = 0; i < winDex.length; i++){
        for (let j = 0; j < 3; j++){
            if (!arr.includes(winDex[i][j])) {break;}
            if (j == 2) {return true}
        }
    }
    return false;

}
const CreateTable = () =>{
    const { numRows , numCols } = config; // import our row/col size from ocnfig file
    const rows = Array.from({length:numRows},(unusedvariable_equivalent_to_cur_index,rowIndex)=>rowIndex);
    const cols = Array.from ({length:numCols},(_,rowIndex) => rowIndex); 
    //Array.from creates an array from argument given "foo" beomces ['f', 'o', 'o']
    // length : x ; telling our array.from what size our array is
    // () => arrow function the ( unused , what_we_want) // unused reps the value of current element we dont care for it so _ , what_we_want rep the current index
    // TLDR : (_,r) idc what value is gimme the index (r)
    const keygen = (a,b) => {return `${a}${b}`}; // create our function to do a job ( in this case make a key) , call this inside our <html> identifier and pass in args see <button>
    const [pOne, setPOne] = useState([]);
    const [pTwo,setPTwo] = useState([])
    const [turnCount , setTurnCount ] = useState(0);
    const [winner, setWiner] = useState(0); // 0 no win / 1 is p1 , 2 is p2
    const [pString , setPString ] = useState('X');
    
    const changeTurns = () =>{
        if (turnCount === 0){
            setTurnCount(1);
        } else {
            setTurnCount(0);
        }
        // game winning logic check here
    };
    const makeMove = (boxKey) =>{
        let playerArr = turnCount === 0 ? pOne : pTwo;
        let setFunc = turnCount === 0? setPOne : setPTwo;
        const newMoves = [...playerArr,boxKey];
        setFunc(newMoves);
        return newMoves;

    };
    const updatePlayerTextHeader = () =>{

        let pOneTwo = turnCount === 0 ?  'O' : 'X';
        setPString(pOneTwo);
    }
    return(
        <div className = "tableDiv">
            <h1>Player {pString} turn.</h1>
            <table className = "board">
                <tbody>
                    {rows.map( rowIndex =>(
                        <tr key = {rowIndex}>
                            {cols.map( colIndex =>(
                                <td key = {colIndex}>
                                    <CreateButton p1 = {pOne}  p2 = {pTwo} buttonKey = {keygen(rowIndex,colIndex)} count = {turnCount} change_turn = {changeTurns} move = {makeMove} win = {WinCon} updateParent = {updatePlayerTextHeader}/>
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
    // we create a " double for loop" inside tbody to create our rows with (y) number of cols
    // tr = row , td = cols (td = table data)
    // code flow table/tbody , we map each element/index in our rows array to rowIndex => () function
    // for each element in our rows array the rowIndex creates <tr> component within tr we map cols similarly to create <td> components (y) amount of times == cols
}

export default CreateTable;
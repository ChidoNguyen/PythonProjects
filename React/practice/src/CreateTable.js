import React from "react";
import config from  './config';
import './Table.css'
import CreateButton from './CreateButton';
/* could prolly pass in X_Y grid size*/

const CreateTable = () =>{
    const { numRows , numCols } = config; // import our row/col size from ocnfig file
    const rows = Array.from({length:numRows},(unusedvariable_equivalent_to_cur_index,rowIndex)=>rowIndex);
    const cols = Array.from ({length:numCols},(_,rowIndex) => rowIndex); 
    //Array.from creates an array from argument given "foo" beomces ['f', 'o', 'o']
    // length : x ; telling our array.from what size our array is
    // () => arrow function the ( unused , what_we_want) // unused reps the value of current element we dont care for it so _ , what_we_want rep the current index
    // TLDR : (_,r) idc what value is gimme the index (r)
    const keygen = (a,b) => {return `${a}${b}`}; // create our function to do a job ( in this case make a key) , call this inside our <html> identifier and pass in args see <button>
    return(
        <table className = "board">
            <tbody>
                {rows.map( rowIndex =>(
                    <tr key = {rowIndex}>
                        {cols.map( colIndex =>(
                            <td key = {colIndex}>
                                <CreateButton buttonKey = {keygen(rowIndex,colIndex)} />
                            </td>
                        ))}
                    </tr>
                ))}
            </tbody>
        </table>
    );
    // we create a " double for loop" inside tbody to create our rows with (y) number of cols
    // tr = row , td = cols (td = table data)
    // code flow table/tbody , we map each element/index in our rows array to rowIndex => () function
    // for each element in our rows array the rowIndex creates <tr> component within tr we map cols similarly to create <td> components (y) amount of times == cols
}

export default CreateTable;
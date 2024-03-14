/* App opperates like main() function.
    index.js will import "App" and things will build out from there */

import React from 'react';
import CreateTable from './CreateTable';

function App() {
    return(
        <div className ="something else">
                <CreateTable />
        </div>
    );
}

export default App;
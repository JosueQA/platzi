import React from "react";
import './TodoSearch.css'

// class Componente extends React.Component{
//     constructor() {
//         this.state = {
//             patito: 'Juan'
//         }
//     }

//     render() {
//         return (
//             <div onClick={() => this.setState('Enrique')}>{this.state.patito}</div>
//         )
//     }
// }


function TodoSearch({searchvalue, setSearchValue}) {
    const onSearchValueChange = (change) => {
         console.log(change.target.value);
         setSearchValue(change.target.value)
     }
    
    return (
        <input 
            className="TodoSearch"
            placeholder="Cebolla"
            value={searchvalue}
            onChange={onSearchValueChange}    
        />
        );
}

export { TodoSearch };
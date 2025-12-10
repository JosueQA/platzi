import React from 'react';
import { AppUI } from './AppUI';

// const defaultTodos = [
//   { text: 'Cortar cebolla', completed: true },
//   { text: 'Tomar el curso de intro a React', completed: false },
//   { text: 'Llorar con la llorona', completed: false },
// ]


function App() {
  const localStorageTodos = localStorage.getItem('TODOS_V1');
  let todosProjection;

  if(!localStorageTodos){
    localStorage.setItem('TODOS_V1', JSON.stringify([]));
    todosProjection = []
  } else {
    todosProjection = JSON.parse(localStorageTodos)
  }
  

  const [todos, setTodos] = React.useState(todosProjection);
  const [searchValue, setSearchValue] = React.useState('');

  let searchedTodos = [];

  if (!searchValue.length >= 1){
    searchedTodos = todos;
  } else {
    searchedTodos = todos.filter(todo => {
        const todoText = todo.text.toLowerCase();
        const searchText = searchValue.toLowerCase(); 

        return todoText.includes(searchText);
        })
  }

  const savedTodos = (newTodos) => {
    let stringyfiedTodos = localStorage.setItem('TODOS_V1', JSON.stringify(newTodos));
    setTodos(JSON.parse(stringyfiedTodos))
  }

  const completeTodo = (text) => {
    const todoIndex = todos.findIndex(todo => todo.text === text);
    const newTodos = [...todos];
    newTodos[todoIndex].completed = true;
    savedTodos(newTodos)
  }

  const deleteTodo = (text) => {
    const todoIndex = todos.findIndex(todo => todo.text === text);
    const newTodos = [...todos];
    newTodos.splice(todoIndex, 1);
    savedTodos(newTodos)
  }

  const completedTodos = todos.filter( todos => !!todos.completed).length;
  const totalTodos = todos.length;

  return (
    <AppUI 
    totalTodos = {totalTodos}
    completedTodos = {completedTodos}
    searchValue={searchValue}
    setSearchValue={setSearchValue}
    searchedTodos = {searchedTodos}
    completeTodo = {completeTodo}
    deleteTodo = {deleteTodo}
    />
  );
}

export default App;
 
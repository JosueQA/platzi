import React from 'react';
import { TodoCounter } from '../TodoCounter/index.';
import { TodoItem } from '../TodoItem/index.';
import { TodoList } from '../TodoList';
import { TodoSearch } from '../TodoSearch'; 
import { CreateTodoButton } from '../CreateTodoButton';
import './App.css';

function AppUI({
  totalTodos,
  completedTodos,
  searchValue,
  setSearchValue,
  searchedTodos,
  completeTodo,
  deleteTodo
}) {
return (
    <React.Fragment>
      <TodoCounter
        total = {totalTodos}
        completed = {completedTodos}
      />,
      <TodoSearch
        searchvalue={searchValue}
        setSearchValue={setSearchValue}
      />,
      <TodoList>
        {searchedTodos.map(todos => (
          <TodoItem 
          key={todos.text} 
          text={todos.text}
          completed={todos.completed}
          onComplete= {() => completeTodo(todos.text)}
          onDelete= {() => deleteTodo(todos.text)}
          />
        ))},
      </TodoList>,
      <CreateTodoButton/>
    </React.Fragment>
  )
}

export {AppUI}
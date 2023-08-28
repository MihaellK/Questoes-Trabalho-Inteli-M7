'use client'

import { useState } from 'react';

const TodoApp = () => {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');

  // GET NOTES FROM DATABASE
  const [notes, setNotes] = useState([])
  const [note, setNote] = useState('');

  const fetchNotes = async () => {
    const response = await fetch("/api/todos")
    const data = await response.json()
    setNotes(data)
  }
  // END GET NOTES

  // POST NOTES
  const submitNote = async () => {
    const response = await fetch("/api/new-todo", {
      method: 'POST',
      body: JSON.stringify({ note }),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    const data = await response.json()
    console.log(data)
  }
  // END POST NOTES

  const addTodo = (e) => {
    e.preventDefault();
    if (!input) return;
    setTodos([...todos, { id: Date.now(), text: input, done: false }]);
    setInput('');
  };
  
  const deleteTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };
  
  const markTodo = (id) => {
    setTodos(
      todos.map((todo) => (todo.id === id ? { ...todo, done: !todo.done } : todo))
    );
  };
  
  return (
    <div className="container">
      <h1>Todo App</h1>
      <form onSubmit={addTodo}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Add a new todo"
        />
        <button type="submit">Add Todo</button>
      </form>

      {/* FETCH NOTES */}
      <button onClick={fetchNotes}>Load Notes</button>
      {notes.map((note) => {
        return(
          <div key={note.id}>
            {note.id} {note.description}
          </div>
        )
      })}
      {/* POST NOTE */}
      <button onClick={submitNote}>Submit note</button>

      <ul>
        {todos.map((todo) => (
          <li key={todo.id} className={`todo-item ${todo.done ? "done" : ""}`}>
            <span onClick={() => markTodo(todo.id)}>{todo.text}</span>
            <button className="delete" onClick={() => deleteTodo(todo.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoApp;


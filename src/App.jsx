import React, { useState } from 'react';

function TodoList() {
    const [todos, setTodos] = useState([]);
    const [newTodo, setNewTodo] = useState('');

    const handleAddTodo = () => {
        if (newTodo.trim() !== '') {
            setTodos([...todos, newTodo]);
            setNewTodo('');
        }
    };

    const handleDeleteTodo = (indexToDelete) => {
        const updatedTodos = todos.filter((_, index) => index !== indexToDelete);
        setTodos(updatedTodos);
    };

    return (
        <div>
            <h1>TodoList</h1>

            <input
                type="text"
                value={newTodo}
                onChange={(e) => setNewTodo(e.target.value)}
                placeholder="Enter a new todo"
            />

            <button onClick={handleAddTodo}>Add Todo</button>

            <ul>
                {todos.map((todo, index) => (
                    <li key={index}>
                        {todo}
                        <button onClick={() => handleDeleteTodo(index)}>
                            Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TodoList;


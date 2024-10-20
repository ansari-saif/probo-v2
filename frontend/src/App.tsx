import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import TodoList from './pages/TodoList';
import AddTodoForm from './components/AddTodoForm';
const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<TodoList />} />
        <Route path="/add" element={<AddTodoForm onAdd={() => {}} />} />
      </Routes>
    </Router>
  );
};


export default App

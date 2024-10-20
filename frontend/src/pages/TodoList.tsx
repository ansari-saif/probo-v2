import React, { useEffect, useState } from 'react';
import TodoItem from '../components/TodoItem';
import { DefaultService, TodoRead } from '../client';
import AddTodoForm from '@/components/AddTodoForm';
import { motion } from 'framer-motion';

const TodoList: React.FC = () => {
  const [todos, setTodos] = useState<TodoRead[]>([]);
  const getTodos = ()=>{
    DefaultService.listAllTodosApiV1TodosGet()
      .then(setTodos)
      .catch(console.error);
  }
  useEffect(() => {
    getTodos()
  }, []);

  const handleToggle = (id: number) => {
    const todo = todos.find((t) => t.id === id);
    if (!todo) return;

    const updatedTodo = {
      ...todo,
      is_completed: !todo.is_completed,
    };

    DefaultService.updateTodoApiV1TodosTodoIdPut({
      todoId: id,
      requestBody: updatedTodo,
    })
      .then((updated) => {
        setTodos((prev) =>
          prev.map((t) => (t.id === id ? updated : t))
        );
      })
      .catch(console.error);
  };

  const handleDelete = (id: number) => {
    DefaultService.deleteTodoApiV1TodosTodoIdDelete({ todoId: id })
      .then(() => {
        setTodos((prev) => prev.filter((t) => t.id !== id));
      })
      .catch(console.error);
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-100 to-purple-100 p-8">
      <motion.div
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="max-w-md mx-auto bg-white rounded-lg shadow-lg overflow-hidden"
      >
        <div className="p-6">
          <h1 className="text-3xl font-bold mb-6 text-center text-gray-800">To-Do List</h1>
          <AddTodoForm onAdd={getTodos} />
          <div className="mt-6 space-y-4">
            {todos.map((todo) => (
              <motion.div
                key={todo.id}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.3 }}
              >
                <TodoItem
                  todo={todo}
                  onToggle={handleToggle}
                  onDelete={handleDelete}
                />
              </motion.div>
            ))}
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default TodoList;

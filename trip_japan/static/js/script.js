document.addEventListener('DOMContentLoaded', () => {
    const addBtn = document.getElementById('add-todo-btn');
    const inputField = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    // Add Todo
    addBtn.addEventListener('click', () => {
        const title = inputField.value.trim();
        if (title) {
            fetch('/api/add/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ title: title }),
            })
            .then(response => response.json())
            .then(data => {
                const newTodo = document.createElement('li');
                newTodo.setAttribute('data-id', data.id);
                newTodo.innerHTML = `
                    <input type="checkbox" class="todo-checkbox">
                    <span class="todo-title">${data.title}</span>
                    <button class="delete-btn">Delete</button>
                `;
                todoList.prepend(newTodo);
                inputField.value = '';
            });
        }
    });

    // Toggle Todo
    todoList.addEventListener('change', (e) => {
        if (e.target.classList.contains('todo-checkbox')) {
            const todoId = e.target.closest('li').dataset.id;
            fetch(`/api/toggle/${todoId}/`, { method: 'POST' })
            .then(response => response.json())
            .then(data => {
                const titleElem = e.target.nextElementSibling;
                if (data.is_completed) {
                    titleElem.classList.add('completed');
                } else {
                    titleElem.classList.remove('completed');
                }
            });
        }
    });

    // Delete Todo
    todoList.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            const todoId = e.target.closest('li').dataset.id;
            fetch(`/api/delete/${todoId}/`, { method: 'DELETE' })
            .then(response => {
                if (response.status === 200) {
                    e.target.closest('li').remove();
                }
            });
        }
    });
});
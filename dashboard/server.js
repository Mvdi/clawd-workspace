const express = require('express');
const path = require('path');
const fs = require('fs').promises;
const { exec } = require('child_process');
const { promisify } = require('util');

const execAsync = promisify(exec);
const app = express();
const PORT = 3000;

const DATA_DIR = path.join(__dirname, 'data');

app.use(express.json());

// Serve static files
app.use(express.static(__dirname));

// API endpoints
app.get('/api/tasks', async (req, res) => {
    try {
        const data = await fs.readFile(path.join(DATA_DIR, 'tasks.json'), 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.json({ todo: [], 'in-progress': [], done: [] });
    }
});

app.get('/api/activity', async (req, res) => {
    try {
        const data = await fs.readFile(path.join(DATA_DIR, 'activity-log.json'), 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.json([]);
    }
});

app.get('/api/info', async (req, res) => {
    try {
        const data = await fs.readFile(path.join(DATA_DIR, 'dashboard-info.json'), 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.json({ title: 'Jue & Mathias Dashboard', lastUpdated: null });
    }
});

// Personal Todos API
app.get('/api/personal-todos', async (req, res) => {
    try {
        const data = await fs.readFile(path.join(DATA_DIR, 'personal-todos.json'), 'utf8');
        res.json(JSON.parse(data));
    } catch (error) {
        res.json({ mathias: [], jue: [] });
    }
});

app.post('/api/personal-todos', async (req, res) => {
    try {
        const { person, text, priority = 'medium' } = req.body;
        
        const data = await fs.readFile(path.join(DATA_DIR, 'personal-todos.json'), 'utf8');
        const todos = JSON.parse(data);
        
        if (!todos[person]) todos[person] = [];
        
        const newTodo = {
            id: Date.now(),
            text,
            priority,
            completed: false,
            created: new Date().toISOString(),
            completedAt: null
        };
        
        todos[person].push(newTodo);
        
        await fs.writeFile(path.join(DATA_DIR, 'personal-todos.json'), JSON.stringify(todos, null, 2));
        
        // Update dashboard info
        await updateDashboardInfo();
        
        res.json(newTodo);
    } catch (error) {
        res.status(500).json({ error: 'Failed to create todo' });
    }
});

app.put('/api/personal-todos/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const { completed, text, priority } = req.body;
        
        const data = await fs.readFile(path.join(DATA_DIR, 'personal-todos.json'), 'utf8');
        const todos = JSON.parse(data);
        
        for (const person in todos) {
            const todo = todos[person].find(t => t.id === parseInt(id));
            if (todo) {
                if (completed !== undefined) {
                    todo.completed = completed;
                    todo.completedAt = completed ? new Date().toISOString() : null;
                }
                if (text !== undefined) todo.text = text;
                if (priority !== undefined) todo.priority = priority;
                
                await fs.writeFile(path.join(DATA_DIR, 'personal-todos.json'), JSON.stringify(todos, null, 2));
                await updateDashboardInfo();
                return res.json(todo);
            }
        }
        
        res.status(404).json({ error: 'Todo not found' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to update todo' });
    }
});

app.delete('/api/personal-todos/:id', async (req, res) => {
    try {
        const { id } = req.params;
        
        const data = await fs.readFile(path.join(DATA_DIR, 'personal-todos.json'), 'utf8');
        const todos = JSON.parse(data);
        
        for (const person in todos) {
            const index = todos[person].findIndex(t => t.id === parseInt(id));
            if (index !== -1) {
                todos[person].splice(index, 1);
                await fs.writeFile(path.join(DATA_DIR, 'personal-todos.json'), JSON.stringify(todos, null, 2));
                await updateDashboardInfo();
                return res.json({ success: true });
            }
        }
        
        res.status(404).json({ error: 'Todo not found' });
    } catch (error) {
        res.status(500).json({ error: 'Failed to delete todo' });
    }
});

async function updateDashboardInfo() {
    try {
        const data = await fs.readFile(path.join(DATA_DIR, 'dashboard-info.json'), 'utf8');
        const info = JSON.parse(data);
        info.lastUpdated = new Date().toISOString();
        await fs.writeFile(path.join(DATA_DIR, 'dashboard-info.json'), JSON.stringify(info, null, 2));
    } catch (error) {
        console.error('Failed to update dashboard info:', error);
    }
}

// Codex API endpoints
app.post('/api/code/generate-component', async (req, res) => {
    try {
        const { componentName, description, componentType = 'react' } = req.body;

        if (!componentName || !description) {
            return res.status(400).json({ error: 'componentName and description are required' });
        }

        const prompt = `Create a modern ${componentType} component named ${componentName} with this functionality: ${description}.
Use TypeScript with proper types.
If React, use functional components with hooks.
Use Tailwind CSS for styling.
Include error handling and loading states.
Write clean, well-documented code.
Return only the component code.`;

        const result = await execAsync(`codex exec "${prompt}"`, {
            cwd: path.join(__dirname, '..'),
            timeout: 60000
        });

        // Extract code from output
        const codeMatch = result.stdout.match(/```(?:typescript|tsx|jsx|js)?\n([\s\S]*?)\n```/);
        const code = codeMatch ? codeMatch[1] : result.stdout;

        res.json({
            success: true,
            code,
            componentName,
            componentType
        });
    } catch (error) {
        console.error('Code generation failed:', error);
        res.status(500).json({ error: 'Failed to generate code with Codex CLI' });
    }
});

app.post('/api/code/fix-code', async (req, res) => {
    try {
        const { filePath, issue } = req.body;

        if (!filePath || !issue) {
            return res.status(400).json({ error: 'filePath and issue are required' });
        }

        const prompt = `Fix this issue in ${filePath}: ${issue}.
Keep the same structure and imports.
Only modify what's necessary to fix the bug.
Add comments explaining the fix.
Return the complete corrected file.`;

        const result = await execAsync(`codex exec "${prompt}"`, {
            cwd: path.join(__dirname, '..'),
            timeout: 60000
        });

        const codeMatch = result.stdout.match(/```(?:typescript|tsx|jsx|js)?\n([\s\S]*?)\n```/);
        const code = codeMatch ? codeMatch[1] : result.stdout;

        res.json({
            success: true,
            code,
            filePath
        });
    } catch (error) {
        console.error('Code fix failed:', error);
        res.status(500).json({ error: 'Failed to fix code with Codex CLI' });
    }
});

app.post('/api/code/generate-workflow-ui', async (req, res) => {
    try {
        const { workflowName, workflowType, customFields = [] } = req.body;

        if (!workflowName || !workflowType) {
            return res.status(400).json({ error: 'workflowName and workflowType are required' });
        }

        const prompt = `Create a modern React TypeScript component for a ${workflowType} workflow UI.
Workflow name: ${workflowName}
Custom fields: ${customFields.join(', ')}

The UI should include:
- Clean, modern design with Tailwind CSS
- Form inputs for all custom fields with validation
- Responsive layout
- Loading states and error handling
- Submit and cancel buttons
- Use existing UI components from project (Card, Input, Button, etc.)
Write production-ready, well-documented code.
Return only the component code.`;

        const result = await execAsync(`codex exec "${prompt}"`, {
            cwd: path.join(__dirname, '..'),
            timeout: 90000
        });

        const codeMatch = result.stdout.match(/```(?:typescript|tsx|jsx|js)?\n([\s\S]*?)\n```/);
        const code = codeMatch ? codeMatch[1] : result.stdout;

        res.json({
            success: true,
            code,
            workflowName,
            workflowType
        });
    } catch (error) {
        console.error('Workflow UI generation failed:', error);
        res.status(500).json({ error: 'Failed to generate workflow UI with Codex CLI' });
    }
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Dashboard kører på port ${PORT}`);
    console.log(`📱 Tilgå fra telefonen: http://<din-IP>:${PORT}`);
});

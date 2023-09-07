const express = require('express')
const router = express.Router()
const tasks = require('../data.js')

router.get('/',(req,res) => {
    res.json(tasks)
});

router.post('/',(req,res) => {
    const newtask = {
        id: tasks.length + 1,
        task : req.body.task
    }
tasks.push(newtask)
res.status(201).json(newtask)
});

router.put('/:taskID',(req,res) => {
    const id = Number(req.params.taskID)
    const index = tasks.findIndex(task => task.id === id)
    const updateTask = {
        id: tasks[index].id,
        task: req.body.task
    }
    tasks[index] = updateTask
    res.status(200).json('Task updated')
});

router.delete('/:taskID',(req,res) => {
    const id = Number(req.params.taskID)
    const index = tasks.findIndex(task => task.id === id)
    tasks.splice(index, 1)
    res.status(200).json('Task deleted')
});

module.exports = router
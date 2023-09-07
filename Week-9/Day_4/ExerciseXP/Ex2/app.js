const express = require('express')
const app = express()
const app_routes = require('./routes/todos.js')

app.listen(2000, () => {
    console.log('server is listening on port 2000')
})

app.use(express.json())
app.use('/', app_routes)
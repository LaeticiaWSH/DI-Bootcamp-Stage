const express = require('express')
const app = express()
const app_routes = require('./routes/book.js')

app.listen(1000, () => {
    console.log('server is listening on port 1000')
})


app.use(express.json())
app.use('/', app_routes)
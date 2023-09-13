const express = require('express');
const app = express();
const app_routes = require('./routes/routes.js')


app.listen(3000, () => {
    console.log('server is listening on port 3000')
})
app.use(express.json())
app.use('/', app_routes)
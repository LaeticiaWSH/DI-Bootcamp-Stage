const express = require('express')
const router = express.Router()

router.get('/',(req,res) =>{
    res.send('You are on the app.')
});
router.get('/home',(req,res) => {
    res.send('Welcome Home sweetheart !')
});
router.get('/about',(req,res) =>{
    res.send('Currently in the APP ABOUT.')
});
module.exports = router
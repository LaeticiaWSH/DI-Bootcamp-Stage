const express = require('express')
const router = express.Router()
const books = [
    {id: 1, "title": "The Song of Achilles", "author": "Madeleine Miller"},
    { id: 2, "title": "A seperate peace", "author": "John Knowles" },
    { id: 3, "title": "Romeo and Juliet", "author": "William Shakespeare" },
    { id: 4, "title": "The Tempest", "author": "Willaim Shakespeare" }
]
// Get all books
router.get('/', (req, res) => {
    res.json(books)
});

// Add a new book
router.post('/',(req,res) =>{
    const newbook ={
        id: books.length + 1,
        title : req.body.title,
        author : req.body.author
    }
    books.push(newbook)
    res.status(201).json(newbook)
});

module.exports = router

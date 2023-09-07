//Exercise 1: Building A RESTful API

const express = require('express')
const blog = express()

const data = [
    {id: 1,title: "Walking on sunshine",content:"A romance film."},
    { id: 2, title: "The water so bottle", content:"A documentary about water ... so fresh."},
    { id: 3, title: "Learn to code", content:"A course about learning how to code."}
]
blog.listen(5000, () => {
    console.log("server is listening on port 5000");
});

blog.get("/blog", (req, res) => {
    res.json(data);
});
blog.get("/blog/:blogID", (req, res) => {
    const id = Number(req.params.blogID);
    const dat = data.find((dat) => dat.id === id );

    if(!dat){
        return res.status(404).send("Data not found");
    }
    res.json(dat)
});
blog.use(express.json()); // parse json body content

blog.post("/blog", (req, res) => {
    const newData = {
        id: data.length + 1,
        title: req.body.title,
        content: req.body.content,
    };
    data.push(newData);
    res.status(201).json(newData);
});
blog.use(express.json()); // parse json body content

blog.delete("/blog/:blogID", (req, res) => {
  const id = Number(req.params.blogID);
  const index = data.findIndex((dat) => dat.id === id);
  if (index === -1) {
    return res.status(404).send("Data not found");
  }
  data.splice(index, 1);
  res.status(200).json("Data deleted");
});
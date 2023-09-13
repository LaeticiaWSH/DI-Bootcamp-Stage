const knex = require('../config/config.js')

const getAllpost = (req,res) => {
    try{
        knex("posts")
            .select()
            .then((posts) => res.status(200).json(posts))
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
}

const getPostId = (req, res) => {
    const postId = req.params.id;
    try{
        knex("posts")
        .where({id : postId })
        if(!post){
            return res.status(404).json({error : 'No post found'})
        }
        res.json(post)
    }catch(error){
        console.log(error)
        console.log("An error occurred")
    }
}

const createPost = (req, res) => {
    const { title, content } = req.body;
    try{
        knex("post")
        .insert()
    }
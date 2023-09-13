const knex = require("knex")({
    client: "pg",
    version: "7.3",
    connection: {
        host: "127.0.0.1",
        user: "laeticiaoceane",
        password: "12345678",
        database: "exercise",
        port: 5432,
    },
});

const createTable = (req, res) => {
    knex.schema
        .createTable("posts", function (table) {
            table.increments();
            table.string("title");
            table.integer("content");
        })
        .then(() => console.log("Table created"));
    res.sendStatus(200);
};

module.exports = createTable
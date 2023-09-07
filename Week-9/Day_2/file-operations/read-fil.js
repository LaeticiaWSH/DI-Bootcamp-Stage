const fs = require("fs").promises;

const start = async () => {
    const data = await fs.readFile("output.txt", "utf8");
    console.log(data);
};

start();
const gameInfo = [
    {
        username: "john",
        team: "red",
        score: 5,
        items: ["ball", "book", "pen"]
    },
    {
        username: "becky",
        team: "blue",
        score: 10,
        items: ["tape", "backpack", "pen"]
    },
    {
        username: "susy",
        team: "red",
        score: 55,
        items: ["ball", "eraser", "pen"]
    },
    {
        username: "tyson",
        team: "green",
        score: 1,
        items: ["book", "pen"]
    },
];
let user = "";
const usernames = [];
gameInfo.forEach((player) => {
    user = player.username + "!";
    usernames.push(user);
})

let winners = [];
gameInfo.forEach((player)=>{
    if (player.score > 5){
        winners.push(player.username);
    }
}
);

gameInfo.reduce((acc, score) => { return acc + score.score }, 0);


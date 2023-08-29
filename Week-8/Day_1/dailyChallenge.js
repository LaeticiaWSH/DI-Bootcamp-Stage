class Video{
    constructor(title,uploader,time){
        this.title = title;
        this.uploader = uploader;
        this.time = time ;
    }
    watch(){
        console.log(`${this.uploader} watched all ${this.time} of ${this.title}!`)
    }

}
const video = new Video('Lord of the rings','Piper',120)
video.watch()
const film = new Video('Hobbits', 'Katherine', 180)
film.watch()

let movies = [
    ['Venom','Angel',120],
    ['Jurassic Park',''],
    [],
    [],
    []
]
import logo from './logo.svg';
import './App.css';
import Vote from './vote';
import { useState } from "react"


// const [languages, setLanguages] = useState([
//   { name: "Php", votes: 0 },
//   { name: "Python", votes: 0 },
//   { name: "JavaSript", votes: 0 },
//   { name: "Java", votes: 0 }
// ])

// const languages = [
//   { name: "Php", votes: 0 },
//   { name: "Python", votes: 0 },
//   { name: "JavaSript", votes: 0 },
//   { name: "Java", votes: 0 }
// ]

function App() {

  return (

    <div>
      {/* <p>{languages.votes} Php </p><button onClick ={() => setLanguages(languages.votes + 1)}>
        Click Here
      </button> */}
      <Vote />
    </div>
  );
}

export default App;

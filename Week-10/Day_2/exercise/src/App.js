// import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from './UserFavoriteAnimals'
import Exercise from './Exercise3';
// Create a constant variable with JSX const myelement = <h1>I Love JSX!</h1>;, and render it on the page.
const myelement = <h1>I love JSX!</h1>
const sum = 5 + 5

function App() {
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
  };
  return (
    <div >
      {/* display a “Hello World!” message in a paragraph. */}
      <p>Hello World!</p>
      {myelement}
      <p>React is {sum} times better with JSX</p>
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <UserFavoriteAnimals favAnimals = {user.favAnimals}/>
      <Exercise />
      
    </div>
  );
}

export default App;

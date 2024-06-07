import logo from './logo.svg';
import './App.css';
import axios from 'axios';


function App() {
  const handleClick = async () => {
    console.log("clciked");
    try{
      const response = await axios.get('http://127.0.0.1:5000');
      console.log(response);
    }catch(error){
      console.log("There was an error" + error);
    }
  }

  const handleCreateTable = async () => {
    console.log("createtable");
    try{
      const response = await axios.get('http://127.0.0.1:5000/create_table');
      console.log(response);
    }catch(error){
      console.log("There was an error" + error);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <button onClick={handleClick}>Click me!</button>
        <button onClick={handleCreateTable}>create table button</button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

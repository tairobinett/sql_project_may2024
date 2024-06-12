import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useState } from 'react';


function App() {
  const [tableName, setTableName] = useState('');

  const handleCreateTable = async () => {
    console.log("createtable, tableName = " + tableName);
    try{
      //const response = await axios.get('http://127.0.0.1:5000/create_table?', { params: { tableName: tableName } });
      // const response = await axios.post('http://127.0.0.1:5000/create_table', { params: { tableName: tableName } });
      const response = await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/create_table',
        data: {
          tableName: tableName,
        }
      });
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
        <input type="text" value={tableName} onChange={(e) => setTableName(e.target.value)} placeholder="Enter table name" />

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

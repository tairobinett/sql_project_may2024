import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import React, { useState } from 'react';


function App() {
  const [tableNameToCreate, setTableNameToCreate] = useState('');
  const [tableNameToDelete, setTableNameToDelete] = useState('');

  const [tableNameToAddStudent, setTableNameToAddStudent] = useState('');
  const [studentName, setStudentName] = useState('');
  const [studentMajor, setStudentMajor] = useState('');

  const handleCreateTable = async () => {
    console.log("createtable, tableName = " + tableNameToCreate);
    try{
      //const response = await axios.get('http://127.0.0.1:5000/create_table?', { params: { tableName: tableName } });
      // const response = await axios.post('http://127.0.0.1:5000/create_table', { params: { tableName: tableName } });
      const response = await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/create_table',
        data: {
          tableName: tableNameToCreate,
        }
      });
      console.log(response);
    }catch(error){
      console.log("There was an error" + error);
    }
  }

  const handleDeleteTable = async () => {
    console.log("deletetable, tableName = " + tableNameToDelete);
    try{
      const response = await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/delete_table',
        data: {
          tableName: tableNameToDelete,
        }
      });
      console.log(response);
    }catch(error){
      console.log("There was an error" + error);
    }
  }

  const handleAddStudent = async () => {
    console.log("addstudent, tableName = " + tableNameToAddStudent);
    try{
      const response = await axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/add_student',
        data: {
          tableName: tableNameToAddStudent,
          studentName: studentName, 
          studentMajor: studentMajor,
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
        <input 
          type="text" 
          value={tableNameToCreate} 
          onChange={(e) => 
          setTableNameToCreate(e.target.value)} 
          placeholder="Enter table name to create" />
        <button onClick={handleCreateTable}>create table button</button>

        <input 
          type="text" 
          value={tableNameToDelete} 
          onChange={(e) => 
          setTableNameToDelete(e.target.value)} 
          placeholder="Enter table name to delete" />
        <button onClick={handleDeleteTable}>delete table button</button>

        <input 
          type="text" 
          value={tableNameToAddStudent} 
          onChange={(e) => 
          setTableNameToAddStudent(e.target.value)} 
          placeholder="Enter name of table to add student to" />
        <input 
          type="text" 
          value={studentName} 
          onChange={(e) => 
          setStudentName(e.target.value)} 
          placeholder="Enter student name" />
        <input 
          type="text" 
          value={studentMajor} 
          onChange={(e) => 
          setStudentMajor(e.target.value)} 
          placeholder="Enter student major" />
        <button onClick={handleAddStudent}>add student button</button>

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

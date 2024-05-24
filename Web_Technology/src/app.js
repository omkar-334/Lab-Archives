// App.js
import React, { useState } from 'react';

// Function to get a greeting message based on the time of day
const getGreeting = () => {
  const hour = new Date().getHours();
  if (hour < 12) {
    return 'Good morning';
  } else if (hour < 18) {
    return 'Good afternoon';
  } else {
    return 'Good evening';
  }
};

// Functional component that accepts props
const Greeting = (props) => {
  return (
    <div>
      <h1>{getGreeting()}, {props.name}!</h1>
      <p>{props.message}</p>
    </div>
  );
};

// Parent component where Greeting component is used
const App = () => {
  const [name, setName] = useState("Mahes");

  const handleChange = (event) => {
    setName(event.target.value);
  };

  return (
    <div>
      <input 
        type="text" 
        value={name} 
        onChange={handleChange} 
        placeholder="Enter your name" 
      />
      <Greeting name={name} message="Welcome to our website!. Hope you have a great day!" />
    </div>
  );
};

export default App;

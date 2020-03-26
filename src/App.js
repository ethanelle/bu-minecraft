import React from 'react';
// import logo from './logo.svg';
import './App.scss';
import Mobile from './Components/Mobile.jsx';
import Desktop from './Components/Desktop.jsx';

function App() {
  const mobile = window.innerWidth <= 500;
  if (true) {
    return (
      <div className="App">
        <Mobile />
      </div>
    );
  } else {
    return (
      <div className="App">
        <Desktop />
      </div>
    );
  }
}

export default App;

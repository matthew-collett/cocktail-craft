import { useState, useEffect } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';

function App() {
  const [count, setCount] = useState(0);
  const [cocktail, setCocktail] = useState(null);

  useEffect(() => {
    // Call the API on component mount
    fetch('http://localhost:5000/cocktail')
      .then(response => response.json())
      .then(data => setCocktail(data))
      .catch(error => console.error('Error fetching data: ', error));
  }, []); // Empty dependency array means this effect will only run once on mount

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR updates.
        </p>
        {/* Display cocktail data here */}
        {cocktail && (
          <div>
            <h2>Cocktail Info:</h2>
            <pre>{JSON.stringify(cocktail, null, 2)}</pre>
          </div>
        )}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  );
}

export default App;

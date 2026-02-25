import React, { useState } from 'react';
import './App.css';

function App() {
  const [input, setInput] = useState('');
  const [sortedArray, setSortedArray] = useState([]);
  const [error, setError] = useState('');

  const handleSort = async () => {
    setError('');
    try {
      const inputArray = input.split(',').map(num => parseInt(num.trim()));

      if (inputArray.some(isNaN)) {
        setError('Invalid input: Please enter a comma-separated list of integers.');
        return;
      }

      const response = await fetch('http://localhost:5000/sort', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ arr: inputArray }),
      });

      const data = await response.json();

      if (response.ok) {
        setSortedArray(data.sorted_arr);
      } else {
        setError(data.error);
      }
    } catch (err) {
      setError('An error occurred while sorting the array.');
    }
  };

  return (
    <div className="App">
      <h1>Sort Integers by Number of 1s</h1>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter comma-separated integers"
      />
      <button onClick={handleSort}>Sort</button>
      {error && <p className="error">{error}</p>}
      {sortedArray.length > 0 && (
        <p>Sorted Array: [{sortedArray.join(', ')}]</p>
      )}
    </div>
  );
}

export default App;

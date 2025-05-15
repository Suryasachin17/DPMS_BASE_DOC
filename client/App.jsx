import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [name, setName] = useState('');
  const [age, setAge] = useState('');

const handleSubmit = async () => {
  try {
    const res = await axios.post('/api/submit', {
      name,
      age
    });
    alert('Saved! ID: ' + res.data.id);
  } catch (err) {
    console.error(err.response || err);
    alert('Error saving');
  }
};



  return (
    <div style={{ padding: 20 }}>
      <h2>DPMS Form</h2>
      <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} /><br />
      <input placeholder="Age" value={age} type="number" onChange={(e) => setAge(e.target.value)} /><br />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
}

export default App;
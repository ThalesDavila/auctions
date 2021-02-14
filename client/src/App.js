import './App.css';
import { useState } from 'react';

function App() {
  let [counter, setData] = useState()  
  
  let eventSource = new EventSource("http://localhost:5000/auctions_counter_stream")

  eventSource.onerror = (e) => {
    console.log("An error occurred while attempting to connect.");
  };

  eventSource.onmessage = function(event) {
    if(!(event || event.data || typeof event.data == 'number')) {
      console.log('Warning: invalid type for auctions_counter')
    } else {
      setData(event.data)
    }
  };

  if(counter) {
    return (
      <div className="App">
        <h1>Auction data received: {counter}</h1>
      </div>
    )
  } else {
    return(
      <div className="App">
        <h1>Connecting</h1>
      </div>
    )
  }
  
}

export default App;

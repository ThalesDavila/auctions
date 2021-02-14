import { useState, React } from 'react';
import './Counter.css';

function Counter() {
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
            <div className="Counter">
                <div>
                    <h1>{counter}</h1>
                    <h5 className="Description">auctions data counter</h5>
                </div>
            </div>
        )
    } else {
        return(
        <div className="Connecting">
            <h3>... connecting</h3>
        </div>
        )
    }
}

export default Counter;
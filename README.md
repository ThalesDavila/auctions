Adds auction data received from a javascript call to a persistent queue.
Shows a counter of auction data.

<video width="320" height="240" controls>
  <source src="screencast.mov" type="video/mp4">
</video>

Built With
Python
React
EventSource

### Built With

* [Python](https://getbootstrap.com)
* [React](https://jquery.com)
* [EventSource](https://laravel.com)
* [Flask](https://laravel.com)

### Prerequisites

* [python 3.7](https://www.python.org/downloads/)
* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Install NPM packages
   ```sh
   npm install
3. [Install Python pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-pip)
4. [Install Python virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-pip)
5. [Create a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
6. Install the requests package
   ```sh
   python3 -m pip install requests
7. Build
   ```sh
   docker build -t compose-flask .
  
### Run

1. Run the react frontend counter
   ```sh
   npm start
2. Run the API that runs with Event Stream
   ```sh
   docker-compose up
3. [Activate the virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#activating-a-virtual-environment)
4. Run the auctions data requests mock
   ```sh
   python python mock_auction.py

## License

Distributed under the MIT License. See `LICENSE` for more information.

  
   




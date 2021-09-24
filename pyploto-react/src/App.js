import './App.css';
import { Route } from 'react-router-dom'
import Feed from './components/Feed.jsx'

function App() {
  return (

    <div className="App">
      
      <div className="App-header">
        <h1>PyPloto</h1>
      </div>

      <div className="App-main">
        <Route path='/' component={Feed}/>
      </div>

      <div className="App-footer">
        <h1>Footer</h1>
      </div>

    </div>
  );
}

export default App;

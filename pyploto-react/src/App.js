import './App.css';
import { Route, Switch } from 'react-router-dom'

import Nav      from './components/Nav.jsx'
import Feed     from './components/Feed.jsx'
import Search   from './components/Search.jsx'
import Profile  from './components/Profile.jsx'
import Login    from './components/Login.jsx'
import Signup   from './components/Signup.jsx'
import axiosInstance from './axios.js';

function App() {

  async function handleLogout() {
    const response = await axiosInstance.post('/blacklist/', {
      'refresh_token': localStorage.getItem('refresh_token')
    })
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('username')
    axiosInstance.defaults.headers['Authorization'] = null;
    return response
  }
  
  return (

    <div className="App">
      
      <div className="App-header">
          <Nav/>          
          <button onClick={handleLogout}>Logout</button>
      </div>

      <div className="App-main">
        <Switch>
          <Route exact path="/feed" component={Feed}/>
          <Route exact path='/search' component={Search}/>
          <Route exact path='/profile' component={Profile}/>
          <Route exact path="/login" component={Login}/>
          <Route exact path="/signup" component={Signup}/>
        </Switch>
      </div>

      <div className="App-footer">
        <h1>Footer</h1>
      </div>

    </div>
  );
}

export default App;

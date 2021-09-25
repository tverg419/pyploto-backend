import './App.css';
import { Route, Switch } from 'react-router-dom'
import Nav from './components/Nav.jsx'
import Login from './components/Login.jsx'
import Signup from './components/Signup.jsx'
import Feed from './components/Feed.jsx'

function App() {
  return (

    <div className="container mx-auto">
      
      <div className="block">
        <h1 className=''>PyPloto</h1>
        <Nav/>
      </div>

      <div className="App-main">
        <Switch>
          <Route exact path="/login" component={Login}/>
          <Route exact path="/signup" component={Signup}/>
          <Route exact path="/feed" component={Feed}/>
          <Route path={"/"} render={() => <div>Home again</div>}/>
        </Switch>
      </div>

      <div className="App-footer">
        <h1>Footer</h1>
      </div>

    </div>
  );
}

export default App;

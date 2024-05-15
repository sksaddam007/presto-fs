import React from 'react';
import { useSelector } from 'react-redux';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import Login from './components/Login';
import TaskList from './components/TaskList';

const App = () => {
  const { token } = useSelector(state => state.auth);

  return (
    <Router>
      <div>
        <Switch>
          <Route path="/login">
            {token ? <Redirect to="/" /> : <Login />}
          </Route>
          <Route path="/">
            {token ? <TaskList /> : <Redirect to="/login" />}
          </Route>
        </Switch>
      </div>
    </Router>
  );
};

export default App;

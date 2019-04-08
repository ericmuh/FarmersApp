import React, { Component, Fragment } from "react";
import PropTypes from "prop-types";
import { HashRouter as Router, Route, Link, Switch } from "react-router-dom";
import LoginPage from "./Components/LoginPage";

class App extends Component {
  static propTypes = {
    prop: PropTypes
  };

  render() {
    return (
      <Router>
        <Fragment>
          <Switch>
            <Route path="/" exact component={LoginPage} />
          </Switch>
        </Fragment>
      </Router>
    );
  }
}
export default App;

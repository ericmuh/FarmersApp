import React, { Component, Fragment } from "react";
import PropTypes from "prop-types";
import { HashRouter as Router, Route, Link, Switch } from "react-router-dom";
import LoginPage from "./Pages/LoginPage";

import { Provider } from "react-redux";
import Store from "./Store";
import { loadUser } from "./Actions/Auth";
class App extends Component {
  static propTypes = {
    prop: PropTypes
  };

  render() {
    return (

        <Provider store={Store}>
      <Router>
        <Fragment>
          <Switch>
            <Route path="/" exact component={LoginPage} />
          </Switch>
        </Fragment>
            </Router>
            </Provider>
    );
  }
}
export default App;

import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap";
import "./LoginPage.css";
import logo from "../assets/images/logo.png";

class LoginPage extends Component {
  render() {
    return (
      <div className="text-center form">
        <form className="form-signin">
          <img className="mb-4" src={logo} alt="" width="70%" height="70%" />
          <h1 className="h3 mb-3 font-weight-normal">Please sign in</h1>
          <label for="inputEmail" className="sr-only">
            Email address
          </label>
          <input
            type="email"
            id="inputEmail"
            className="form-control"
            placeholder="Email address"
            required
            autofocus
          />
          <label for="inputPassword" className="sr-only">
            Password
          </label>
          <input
            type="password"
            id="inputPassword"
            className="form-control"
            placeholder="Password"
            required
          />
          <div className="checkbox mb-3">
            <label>
              <input type="checkbox" value="remember-me" /> Remember me
            </label>
          </div>
          <button className="btn btn-lg btn-success outline-info btn-block" type="submit">
            Sign in
          </button>
          <p className="mt-5 mb-3 text-muted">&copy; 2019-2021</p>
        </form>
      </div>
    );
  }
}
export default LoginPage;

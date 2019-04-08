import { combineReducers } from "redux";
import Errors from "./Errors";
import Messages from "./Messages";
import Auth from "./Auth";

export default combineReducers({
  Errors,
  Messages,
  Auth
});
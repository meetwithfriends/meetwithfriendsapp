import React from "react";
import { Switch, Route } from 'react-router-dom'

import "./App.css";

import MainPage from "./components/Mainpage/MainPage";
import Signup from "./components/signup/signup";
import Login from "./components/login/Login";



const App = () => (
  <>
    <Switch>
      <Route exact path='/' component={MainPage}/>
      <Route path='/signup' component={Signup}/>
      <Route path='/login' component={Login}/>
    </Switch>
  </>
)

export default App;
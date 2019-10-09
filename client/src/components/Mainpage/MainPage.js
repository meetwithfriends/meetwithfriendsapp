import React from "react";

import Login from "../login/Login";
import Home from "../Home/Home";
import {loginReducer, initialState} from "../../reducers/login";
import { AuthContext } from "../../context/Context";



function MainPage() {  
  const [state, dispatch] = React.useReducer(loginReducer, initialState);
return (
    <AuthContext.Provider
      value={{
        state,
        dispatch
      }}
    >
      <div className="App">{!state.isAuthenticated ? <Login /> : <Home />}</div>
    </AuthContext.Provider>

  );
}

export default MainPage;
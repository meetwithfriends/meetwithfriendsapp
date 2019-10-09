import React from "react";

import "./App.css";

import Login from "./components/login/Login";
import Home from "./components/Home/Home";

export const AuthContext = React.createContext();

const initialState = {
  isAuthenticated: false,
  user: null,
  token: null,
};

const reducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      localStorage.setItem("user", JSON.stringify(action.payload.email));
      localStorage.setItem("token", JSON.stringify(action.payload.token));
      return {
        ...state,
        isAuthenticated: true,
        user: action.payload.user,
        token: action.payload.token
      };
    case "LOGOUT":
      localStorage.clear();
      return {
        ...state,
        isAuthenticated: false,
        user: null
      };
    default:
      return state;
  }
};

function App() {
  const [state, dispatch] = React.useReducer(reducer, initialState);
return (
    <AuthContext.Provider
      value={{
        state,
        dispatch
      }}
    >
      <div className="App">{!state.isAuthenticated ? <Login /> : <Home />}</div>
      {/* <div className="App">{!state.isAuthenticated ? <Login /> : <Login />}</div> */}

    </AuthContext.Provider>
  );
}

export default App;
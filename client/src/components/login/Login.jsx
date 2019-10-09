import React from "react";
import { AuthContext } from "../../context/Context";
import { Link } from 'react-router-dom';

import "./Login.css";

import { URL, PORT } from '../../Constants'

export const Login = () => {
  const { dispatch } = React.useContext(AuthContext);
  const initialState = {
    email: "",
    password: "",
    isSubmitting: false,
    errorMessage: null
  };
const [data, setData] = React.useState(initialState);

const handleInputChange = event => {
    setData({
      ...data,
      [event.target.name]: event.target.value
    });
  };

const handleFormSubmit = event => {
    event.preventDefault();
    setData({
      ...data,
      isSubmitting: true,
      errorMessage: null
    });
    fetch(`${URL}:${PORT}/signin`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        email: data.email,
        pass: data.password
      })
    })
      .then(res => {
        console.log(res)
        if (res.ok) {
          return res.json();
        }
        throw res;
      })
      .then(resJson => {
        console.log(resJson)
        dispatch({
            type: "LOGIN",
            payload: resJson
        })
      })
      .catch(error => {
        setData({
          ...data,
          isSubmitting: false,
          errorMessage: error.message || error.statusText
        });
      });
  };

return (
    <div className="login-container"> 
      <div className="card">
          <form className="form-content" onSubmit={handleFormSubmit}>
          <h1 className="title">MEET WITH <span className="br">FRIENDS</span></h1>
              <input
                className="form-styling" 
                type="text"
                value={data.email}
                onChange={handleInputChange}
                name="email"
                placeholder="Email"
                id="email"
                required
              />
              <input
                className="form-styling" 
                type="password"
                value={data.password}
                onChange={handleInputChange}
                name="password"
                id="password"
                placeholder="Password"
                required
              />
      
			{data.errorMessage && (
              <span className="form-error">{data.errorMessage}</span>
            )}
            <Link to='/restore' className='recovery-link'>Forgot your password?</Link>
           <button className='btn btn-login' disabled={data.isSubmitting}>
              {data.isSubmitting ? (
                "Loading..."
              ) : (
                "Login"
              )}
            </button>
            <p className="btn-title">Don't have an account?</p>
            <Link to='/signup' className='btn btn-signup'>SIGN UP</Link>
          </form>
        </div>
    </div>
  );
};

export default Login;
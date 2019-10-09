import React from "react";
import { Redirect, Link } from 'react-router-dom';

import "./signup.css";

import { URL, PORT } from '../../Constants'

export const Signup = () => {
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
    fetch(`${URL}:${PORT}/signup`, {
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
        if (!res.ok) {
            throw res;
        }
        return <Redirect to="/"/>;
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
    <div className="signup-container"> 
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
                "Sign up"
              )}
            </button>
            <p className="btn-title">Already have an account?</p>
            <Link to='/' className='btn btn-signup'>Back to login</Link>
          </form>
        </div>
    </div>
  );
};

export default Signup;
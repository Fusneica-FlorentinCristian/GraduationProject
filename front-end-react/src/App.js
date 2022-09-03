import './App.css';
import './theme.css'
import {Route, BrowserRouter as Router, Routes, useLocation} from "react-router-dom";
import Login from "./Pages/Login";
import Page from "./components/page";
import {useEffect, useState} from "react";
import {getProperty} from "./requests";
import Register from "./Pages/Register";

export default function App() {

    const location = useLocation()

    useEffect(() => {
        // console.log(location)
    }, [location])
    return (
      <div className="App">
          <Routes>
                <Route exact path="/login" element={
                    <Page title="Login">
                        <Login/>
                    </Page>
                }/>
              <Route exact path="/register" element={
                  <Page title="Register">
                      <Register/>
                  </Page>
              }/>
                <Route exact path="/*"  element={
                    <Page title="Page unknown"/>
                }/>
          </Routes>
      </div>
  );
}

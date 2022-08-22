import React from 'react';
import axios from 'axios';
import { useLocation, BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "../components/Login";
import Register from "../components/Register";
import Reset from "../components/Reset";
import Dashboard from "../components/Dashboard";
import Main from "../components/Main";

export default function App() {
    return (
        <div className="App">
            <Router>
                <Routes>
                    <Route exact path="/login" element={<Login />} />
                    <Route exact path="/register" element={<Register />} />
                    <Route exact path="/reset" element={<Reset />} />
                    <Route exact path="/dashboard" element={<Dashboard />} />
                    <Route exact path="/*"  element={<Main/>} />
                </Routes>
            </Router>
        </div>
    )
}
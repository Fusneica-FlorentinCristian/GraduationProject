import './App.css';
import './theme.css'
import {Route, Routes, useLocation} from "react-router-dom";
import Login from "./Pages/Login";
import Page from "./components/Page";
import {useEffect} from "react";
import Register from "./Pages/Register";
import Home from "./Pages/Home";


export default function App() {

    const location = useLocation()

    useEffect(() => {
        // console.log(location)
    }, [location])
    return (
      <div className="App">
          <Routes>
              <Route exact path="/login" element={<Login/>}/>
              <Route exact path="/register" element={<Register/>}/>
              <Route exact path="/home" element={<Home/>}/>
              <Route path="/*"  element={<Page title="Page unknown"/>}/>
          </Routes>
      </div>
  );
}

import React from "react";
import {useLocation} from "react-router-dom";
import Header from "./Header"
import Meme from "./Meme"
import "../styles/Login.css";

export default function Main() {
    const location = useLocation();
    
    return(
      <div>
          <Header linkPath = {location.pathname}/>
          <Meme/>
      </div>
  )
}
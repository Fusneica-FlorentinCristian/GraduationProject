import './App.css';
import './theme.css'
import {Route, Routes, useLocation, useNavigate} from "react-router-dom";
import {createContext, useContext, useEffect, useState} from "react";
import Home from "./Pages/Home";
import {getCookie} from "./utilities/apiUtilities";
import {useAuth, UserProvider} from "./components/AuthProvider";
import Login from "./Pages/Login";
import Register from "./Pages/Register";
import Page from "./components/Page";
import UtilityTypes from "./Pages/UtilityTypes";
import Properties from "./Pages/Properties";
import Users from "./Pages/Users";





export default function App() {

    const location = useLocation()
    const navigate = useNavigate()
    const [role, setRole] = useState(null)
    // const [user, setUser] = useState(null)

    return (
            <div className="App">
                <UserProvider>
                  <Routes>
                      {/*{*/}
                      {/*    Object.keys(navigationItems).map(pathname =>*/}
                      {/*        <PrivateRoute settings={{exact: true, path: pathname, element: navigationItems[pathname]}}*/}
                      {/*                      role={role}*/}
                      {/*        />)*/}
                      {/*}*/}
                      <Route exact path="/home" element={<Home/>}/>
                      <Route exact path="/property" element={<Properties/>}/>
                      <Route exact path="/user" element={<Users/>}/>
                      <Route exact path="/login" element={<Login/>}/>
                      <Route exact path="/register" element={<Register/>}/>
                      {/*<Route exact path="/" element={<Home usedRoutes={usedRoutes}/>}/>*/}
                      <Route exact path="/" element={<Home />}/>
                      <Route path="/*"  element={<Page title="Page unknown"/>}/>
                      {/*{usedRoutes && usedRoutes.map(pageName => navigationItems[pageName])}*/}
                  </Routes>
                </UserProvider>
            </div>

    );
}

import './App.css';
import './theme.css'
import {Route, Routes, useLocation, useNavigate} from "react-router-dom";
import {createContext, useContext, useEffect, useState} from "react";
import Home from "./Pages/Home";
import {getCookie} from "./utilities/apiUtilities";
import {useAuth, UserProvider} from "./components/AuthProvider";
import Login from "./Pages/Login";





export default function App() {

    const location = useLocation()
    const navigate = useNavigate()
    const [role, setRole] = useState(null)
    // const [user, setUser] = useState(null)

    return (
        <UserProvider>
            <div className="App">
                  <Routes>
                      {/*{*/}
                      {/*    Object.keys(navigationItems).map(pathname =>*/}
                      {/*        <PrivateRoute settings={{exact: true, path: pathname, element: navigationItems[pathname]}}*/}
                      {/*                      role={role}*/}
                      {/*        />)*/}
                      {/*}*/}
                      <Route exact path="/something" element={<Home/>}/>
                      <Route exact path="/login" element={<Login/>}/>
                      {/*<Route exact path="/register" element={<Register/>}/>*/}
                      {/*<Route exact path="/" element={<Home usedRoutes={usedRoutes}/>}/>*/}
                      {/*<Route path="/*"  element={<Page title="Page unknown"/>}/>*/}
                      {/*{usedRoutes && usedRoutes.map(pageName => navigationItems[pageName])}*/}
                  </Routes>
            </div>
        </UserProvider>

    );
}

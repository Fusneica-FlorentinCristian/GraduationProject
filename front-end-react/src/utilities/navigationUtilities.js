import {Route} from "react-router-dom";
import Login from "../Pages/Login";
import Register from "../Pages/Register";
import Home from "../Pages/Home";
import UtilityTypes from "../Pages/UtilityTypes";

export const navigationItems = {
    "login": <Login/>,
    "register": <Register/>,
    // TODO create dashboard elements of users and properties based
    //  on the role of the user (not logged in -> properties without renters, some platform users,
    //  logged in -> profile, friends/networks - connect button)
    "payments": <Home/>,
    "property": <Home/>,
    "utility":<UtilityTypes/>,
}

export const navigationSystem = {
    isAdministrator: ["payments", "property"],
    isTenant: ["payments", "property", "home", "utility"],
    anonymous: ["login", "register",]
}


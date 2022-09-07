import {createContext, useContext, useState} from "react";
import {getCookie} from "../utilities/apiUtilities";
import {useLocation, useNavigate} from "react-router-dom";


const UserContext = createContext(null)
export const useAuth = () => {
    return useContext(UserContext)
};

export const UserProvider = (props) => {
    const [user, setUser] = useState(null);
    const navigate = useNavigate()
    const location = useLocation()

    const handleLogin = async () => {
        if(!user)
        {
            let userInfo = getCookie('user')
            console.log('Here are the user info', userInfo)

            if(userInfo !== '')
                setUser(JSON.parse(userInfo))
            else
            if(location.pathname !== "login")
                navigate("/login")
        }
    };

    const handleLogout = () => {
        setUser(null)};

    const value = {
        user: user,
        onLogin: handleLogin,
        onLogout: handleLogout,
    };

    return (
        <UserContext.Provider value={value}>
            {props.children}
        </UserContext.Provider>
    );
};
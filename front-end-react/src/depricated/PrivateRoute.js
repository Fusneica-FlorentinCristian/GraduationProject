import {Route} from "react-router-dom";
import NotFound from "../Pages/Not found";
import {navigationSystem} from "../utilities/navigationUtilities";

const PrivateRoute = (props) => {
    return (
        <>
            {navigationSystem[props.role ?? "anonymous"].includes(props.settings.path) ?
                <Route {...props.settings}/> :
                <Route path="not-found" element={<NotFound/>}/>
            }
        </>
    );
}

export default PrivateRoute;
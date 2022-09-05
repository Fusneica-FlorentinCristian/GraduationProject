import React, {useState} from "react";
import {getUser} from "../requests";
import {setCookie} from "../utilities/apiUtilities";
import {useLocation, useNavigate} from "react-router-dom";
import {Alert, Button, Grid, Paper} from "@mui/material";
import {Link} from "react-router-dom";
import TextFieldExtended from "../components/TextFieldExtended";
import Page from "../components/Page";


export default function Login(){
    const [error, setError] = useState(null)
    const location = useLocation()
    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        username: "",
        password: ""
    })

    const handleSubmit = (event) =>
    {
        event.preventDefault()
        // console.log()
        getUser(formData).then(response => {
            if(response?.status) {
                //    this means that we have received a valid response
                setCookie("token", response.data.token, 48)
                location.state = response.data
                console.log('This is the global state', location.state)
                navigate("/home")
            }
            else {
                setError(response.response.data)
            }
        })

    }

    const handleInputChange = (event) => {
        console.log(event.target.id, event.target.value)
        setError(null)
        setFormData((pastFormData) => {
            pastFormData[event.target.id] = event.target.value
            return {...pastFormData}
        })
    }

    return (
        <Page title="Login">
            <Grid container item justifyContent="center" p={2}>
                <Paper elevation={3}>
                    <form onSubmit={handleSubmit}>
                        <Grid item container xs={12} p={3} gap={2} flexDirection="column" alignItems="flex-start">
                            <Grid container item flexDirection="column" gap={2}>
                                {!!error && !!error['detail'] && <Alert color="error">{error['detail']}</Alert>}
                                {
                                    Object.keys(formData).map(key =>
                                        <TextFieldExtended key={key}
                                                           name={key}
                                                           fieldType={key === "password" ? "password" : "text"}
                                                           hasError={error && !!error[key]}
                                                           defaultValue={formData[key]}
                                                           helperText={error && !!error[key] && error[key][0]}
                                                           handleChange={handleInputChange}
                                        />
                                    )
                                }
                                <Button variant="contained" color="primary" type="submit">
                                    Submit
                                </Button>
                                <Grid container item alignItems="baseline" gap={1}>
                                    <h6 style={{margin: 0}}>New around here?</h6>
                                    <Link to="/register">Register</Link>
                                </Grid>
                            </Grid>
                        </Grid>
                    </form>
                </Paper>
            </Grid>
        </Page>
    )
}
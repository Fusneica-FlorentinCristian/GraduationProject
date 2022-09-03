import React, {useEffect, useState} from "react";
import {setUser} from "../requests";
import {setCookie} from "../utilities/apiUtilities";
import {useLocation, useNavigate} from "react-router-dom";
import {Button, Grid, Paper, TextField} from "@mui/material";
import {Link} from "react-router-dom";
import TextFieldExtended from "../components/TextFieldExtended";

export default function Register(){

    const [isLoading, setIsLoading] = useState(true)
    const [data, setData] = useState(null)
    const [error, setError] = useState(null)
    const location = useLocation()
    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        username: "",
    })


    const handleSubmit = (event) =>
    {
        event.preventDefault()
        setUser(formData).then(response => {
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
        setFormData((pastFormData) => {
            pastFormData[event.target.id] = event.target.value
            return {...pastFormData}
        })
    }

    return (
        <Grid container item justifyContent="center" p={2}>
            <Paper elevation={3}>
                <form onSubmit={handleSubmit}>
                    <Grid item container xs={12} p={3} gap={2} flexDirection="column" alignItems="flex-start">
                            <Grid container item flexDirection="column" gap={2}>
                                {
                                    Object.keys(formData).map(key =>
                                        <TextFieldExtended key={key}
                                                           name={key}
                                                           fieldType={key === "password" && key}
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
                                    <h6 style={{margin: 0}}>Already have an account?</h6>
                                    <Link to="/login">Log in</Link>
                                </Grid>
                            </Grid>
                    </Grid>
                </form>
            </Paper>
        </Grid>

        // <div>
        //     <p>Errors: {error && JSON.stringify(error)}</p>
        //     <p>Data: {data && JSON.stringify(data)}</p>
        //     {/*{property ? JSON.stringify(property) : 'Still loading'}*/}
        // </div>

)
}
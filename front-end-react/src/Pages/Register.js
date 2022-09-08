import React, {useState} from "react";
import {setUser} from "../requests";
import {setCookie} from "../utilities/apiUtilities";
import {useLocation, useNavigate} from "react-router-dom";
import {Alert, Button, FormControl, FormControlLabel, Grid, Paper, Radio, RadioGroup} from "@mui/material";
import {Link} from "react-router-dom";
import TextFieldExtended from "../components/TextFieldExtended";
import FormLabel from "@mui/material/FormLabel";
import Page from "../components/Page";

export default function Register(){
    const [error, setError] = useState(null)
    const location = useLocation()
    const navigate = useNavigate()
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        username: "",
        role: "tenant"
    })


    const handleSubmit = (event) =>
    {
        event.preventDefault()
        console.log(formData)

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
        console.log(event.target)
        const {name, value, type, checked} = event.target
        console.log(name, value, type, checked, event.target.id)
        setError(null)
        setFormData(prevFormData => {
            prevFormData[event.target.id ? event.target.id: name] = type === "checkbox" ? checked : value
            console.log(prevFormData)
            return {
                ...prevFormData,
            }
        })
    }

    return (
        <Page title="Register">
            <Grid container item justifyContent="center" p={2}>
                <Paper elevation={3}>
                    <form onSubmit={handleSubmit}>
                        <Grid item container xs={12} p={3} gap={2} flexDirection="column" alignItems="flex-start">
                            {!!error && !!error['detail'] && <Alert color="error">{error['detail']}</Alert>}

                            <Grid container item flexDirection="column" gap={2}>
                                {
                                    Object.keys(formData).map(key =>
                                        key !== "role" &&
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
                                <FormControl>
                                    <FormLabel id="demo-radio-buttons-group-label">Are you a landlord or a tenant?</FormLabel>
                                    <RadioGroup
                                        aria-labelledby="demo-radio-buttons-group-label"
                                        defaultValue={"tenant"}
                                        // name="role"
                                        // id="role"
                                        onChange={handleInputChange}
                                    >
                                        <FormControlLabel id="role" value="tenant" name="role" control={<Radio />} label="Tenant" />
                                        <FormControlLabel id="role" value="owner" name="role" control={<Radio />} label="Landlord" />
                                    </RadioGroup>
                                </FormControl>
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
        </Page>);
}
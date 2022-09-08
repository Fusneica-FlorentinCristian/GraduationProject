import React, {useEffect, useState} from "react";
import {getProperties, getUsers, getUtilityTypes} from "../requests";
import {Card, CircularProgress, Grid} from "@mui/material";
import Page from "../components/Page";
import "../theme.css"

export default function Users(){

    const [data, setData] = useState(null)
    const [isLoading, setIsLoading] = useState(true)
    const [currentPage, setCurrentPage] = useState(1)

    useEffect(() => {
        if(isLoading)
        {
            getUsers("", currentPage).then(response => {
                if(response.data)
                {
                    console.log(response.data)
                    setData(response.data.results)
                    setIsLoading(false)
                }
                else
                    setData({error: 'There was an error in loading the requested resource'})

            })
        }
    }, [isLoading])

    return (
        <Page title="Users">
            <Grid container item gap={2}>
                {isLoading &&
                    <Grid item xs={12} p={2} justifyContent="center">
                        <CircularProgress color="primary"/>
                    </Grid>
                }
                {!isLoading && <>
                        <Grid item xs={12} mt={2} mb={2}>
                            <h3 style={{margin: 0, textAlign: "left"}}>Here are some users you can connect with!</h3>
                        </Grid>
                        {data.map(element =>
                        <Grid container item xs>
                            <Card sx={{minWidth: {lg: "300px", md: "250px", sm: "200px", xs: "150px"}, height: "100%", width: "100%"}}>
                                <Grid item container p={2} gap={0.5} xs={12} height="100%">
                                    <Grid item container p={0.5} alignItems="center">
                                        <h4 style={{margin: 0, textAlign: "left"}}>Hey, I am {element.username}!</h4>
                                    </Grid>
                                    <Grid item container p={0.5} alignItems="center">
                                        <p style={{margin: 0, textAlign: "left"}}>My email is {element.email}</p>
                                    </Grid>
                                    <Grid item container p={0.5} alignItems="center">
                                        {element.isTenant ?
                                            <p style={{margin: 0, textAlign: "left"}}>Role: <span style={{color: "#38ce00"}}>tenant</span></p> :
                                            <p style={{margin: 0, textAlign: "left"}}>Role: <span style={{color: "#ce0037"}}>administrator</span></p>
                                        }
                                    </Grid>
                                </Grid>
                            </Card>
                        </Grid>)}
                </>}
                {/*{data ? JSON.stringify(data) : 'Still loading'}*/}
            </Grid>
        </Page>
    )
}
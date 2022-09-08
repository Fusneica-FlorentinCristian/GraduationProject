import React, {useEffect, useState} from "react";
import {getProperties, getUtilityTypes} from "../requests";
import {Card, CircularProgress, Grid} from "@mui/material";
import Page from "../components/Page";

export default function Properties(){

    const [data, setData] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        if(isLoading)
        {
            getProperties().then(response => {
                if(response.data)
                {
                    setData(response.data.results)
                    setIsLoading(false)
                }
                else
                    setData({error: 'There was an error'})

            })
        }
    }, [isLoading])

    return (
        <Page title="Properties">
            <Grid container item gap={2}>
                {isLoading &&
                    <Grid item xs={12} p={2} justifyContent="center">
                        <CircularProgress color="primary"/>
                    </Grid>
                }
                {!isLoading && <>
                    {data.map((element, index) =>
                        <Grid container item xs>
                            <Card sx={{minWidth: {lg: "300px", md: "250px", sm: "200px", xs: "150px"}, height: "100%", width: "100%"}}>
                                <Grid item container p={2} gap={0.5} xs={12} height="100%">
                                    <Grid item container p={0.5} alignItems="center">
                                        <h4 style={{margin: 0, textAlign: "left"}}>Property #{index}</h4>
                                    </Grid>
                                    <Grid item container p={0.5} alignItems="center" gap={1} justifyContent="space-between">
                                        <p style={{margin: 0, textAlign: "left"}}>Rent price: {element.rent_price ?? "negotiable"}</p>
                                        <p style={{margin: 0, textAlign: "left"}}>Sell price: {element.selling_price ?? "negotiable"}</p>
                                    </Grid>
                                    <Grid item container p={0.5} alignItems="center" gap={1} justifyContent="space-between">
                                        {element.currency_type &&
                                            <p style={{margin: 0, textAlign: "left"}}>Currency: {element.currency_type}</p>
                                        }
                                        {element.year &&
                                            <p style={{margin: 0, textAlign: "left"}}>Year of construction: {element.year}</p>
                                        }

                                    </Grid>
                                </Grid>
                            </Card>
                        </Grid>)}
                </>}
            </Grid>
        </Page>
    )
}
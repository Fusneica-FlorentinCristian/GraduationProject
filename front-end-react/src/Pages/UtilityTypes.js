import React, {useEffect, useState} from "react";
import {getUtilityTypes} from "../requests";
import {Grid} from "@mui/material";
import Page from "../components/Page";

export default function UtilityTypes(){

    const [data, setData] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        if(isLoading)
        {
            getUtilityTypes(0).then(response => {
                if(response.data)
                {
                    setData(response.data)
                    setIsLoading(false)
                }
                else
                    setData({error: 'There was an error'})

            })
        }
    }, [isLoading])

return (
        <Page title="UtilityType">
            <Grid container item>
                {data ? JSON.stringify(data) : 'Still loading'}
            </Grid>
        </Page>
    )
}
import React, {useEffect, useState} from "react";
import {getUtilityTypes} from "../requests";

export default function Login(){

    const [property, setProperty] = useState(null)
    const [isLoading, setIsLoading] = useState(true)

    useEffect(() => {
        if(isLoading)
        {
            getUtilityTypes(0).then(response => {
                if(response.data)
                {
                    setProperty(response.data)
                    setIsLoading(false)
                }
                else
                    setProperty({error: 'There was an error'})

            })
        }
    }, [isLoading])

return (
    <div>
        <h3>Login page</h3>
        {property ? JSON.stringify(property) : 'Still loading'}
    </div>)
}
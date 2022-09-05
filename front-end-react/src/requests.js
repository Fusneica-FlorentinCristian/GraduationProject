import axios from "axios";
import {baseUrl} from "../src/utilities/apiUtilities";

export const apiController = (url, method, data, authorization) => {
    const config = {
        method: method,
        url: url,
        withCredentials: true,
        headers: {
            // 'X-CSRFToken': getCookie('csrftoken'),
        }
    };

    if(authorization)
        config['headers']['authorization'] = "Token " + authorization

    if(data){
        if(method === 'GET')
            config['params'] = data;
        else
            config['data'] = data;
    }

    return axios.request(config)
        .then(response => {
            console.log("response is given", response)
            return response;
        }).catch(error => {
            console.log("======= service error ========");
            console.log(error);
            return error;
        });
};

export const getUtilityTypes = (utilityTypeDepth) => {
    const GET_UTILITY_TYPE_ENDPOINT= baseUrl('api/utility_types/' + utilityTypeDepth + '/');
    return apiController(GET_UTILITY_TYPE_ENDPOINT, 'GET')
};

export const getUser = (userData) => {
    const GET_USER_ENDPOINT= baseUrl('api/auth/login/');
    return apiController(GET_USER_ENDPOINT, 'POST', userData)
};

export const setUser = (userData) => {
    const SET_USER_ENDPOINT= baseUrl('api/auth/register/');
    return apiController(SET_USER_ENDPOINT, 'POST', userData)

}
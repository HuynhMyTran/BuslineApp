import axios, { Axios } from "axios";

const HOST = "https://tranhuynh.pythonanywhere.com"

export const endpoints = {
    'buses' : "/buses/",
    'categories': "/categories/",
    'login': '/o/token/',
    'current_user': '/users/'
}

export const authApi = (accessToken) => axios.create({
    baseURL: HOST,
    headers:{
        "Authorization": `Bearer ${accessToken}`
    }
})

export default axios.create({
    baseURL: HOST
})
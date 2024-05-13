import axios from "axios";

const HOST = "https://datvexeapp.com"

export const endpoints = {
    'route' : "h/route/",
    'category' : "/category/"
}

export default axios.create({
    baseURL: HOST
})
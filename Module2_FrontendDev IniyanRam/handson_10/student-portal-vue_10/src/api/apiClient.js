import axios from "axios";

/*
Task 138 - Centralized API Client

A centralized Axios instance has been created so that every API request
uses the same base URL, timeout, headers and interceptors.
Changing the base URL in this file automatically updates all API calls
throughout the application.

Task 140 - Response Interceptor

The response interceptor returns response.data directly so that
components only receive the required data.

Errors are standardized by throwing an object containing
both the error message and HTTP status code.

Task 141 - Request Interceptor

A request interceptor adds a mock Authorization token to every
outgoing request.
*/

const apiClient = axios.create({
    baseURL: "https://jsonplaceholder.typicode.com",
    timeout: 5000,
    headers: {
        "Content-Type": "application/json"
    }
});

apiClient.interceptors.request.use(
    (config) => {

        config.headers.Authorization =
            "Bearer mock-token-12345";

        return config;
    },

    (error) => Promise.reject(error)
);

apiClient.interceptors.response.use(

    response => response.data,

    error => {

        throw {
            message:
                error.response?.data?.message ||
                error.message ||
                "Something went wrong",

            statusCode:
                error.response?.status || 500
        };

    }

);

export default apiClient;
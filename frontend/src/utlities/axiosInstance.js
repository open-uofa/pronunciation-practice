import axios from "axios";
import jwt_decode from "jwt-decode";

const baseURL = "http://localhost:8000";

const axiosInstance = axios.create({
	baseURL: baseURL,
	timeout: 5000,
	headers: {
		Authorization: localStorage.getItem('access_token')
			? `Bearer ${localStorage.getItem('access_token')}`
			: null,
		 
	}
})

axiosInstance.interceptors.response.use(

	(response) => {
		return response;
	},
	async (error) => {

		const originalRequest = error.config;

		// refresh request fails
		if (error.response.status === 401 && error.config.url === 'refresh/') {
			window.location.href = 'login/';
			return Promise.reject(error);
		}
		if (error.response.status === 401 && error.response.data.code ===
			"token_not_valid") {

			const refreshToken = localStorage.getItem('refresh_token')
			if (refreshToken) {
				if (jwt_decode(refreshToken).exp * 1000 > Date.now()) {

					return axiosInstance.post(
						'refresh/',
						{ refresh: refreshToken }
					).then((response) => {
						 
						localStorage.setItem('access_token', response.data.access);
						axiosInstance.defaults.headers['Authorization'] =
							'Bearer ' + response.data.access;
						originalRequest.headers['Authorization'] =
							'Bearer ' + response.data.access; 
							// console.log(originalRequest)
							return axiosInstance(originalRequest);
					}).catch((error) => {
						console.log(error);
					})
					//refresh token expired
				} else {
					window.location.href = 'login/';
					return Promise.reject(error);
				}
				//undefine value in refresh token
			} else {
				window.location.href = 'login/';
				return Promise.reject(error);
			}
		}
		return Promise.reject(error);
	}
);


export default axiosInstance;
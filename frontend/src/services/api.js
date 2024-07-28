import axios from 'axios';

const API = axios.create({

	baseURL: 'http://127.0.0.1:8000/', // Django's base URL
});


export const fetchSailors = () => API.get('/sailors/');
export const fetchProfiles = () => API.get('/profiles/');
export const fetchPosts = () => API.get('/posts/');
// Similarly, create functions for other endpoints

/**
 * @file src/request/index.ts
 * @desc request
 * @since 2024-02-27
 */

import axios from 'axios';

// todo 这边得写个返回类型，与 flask 交互的时候，需要用到
const request = axios.create({
    // baseURL: 'http://localhost:6553',
    baseURL: '/',
});

export default request;

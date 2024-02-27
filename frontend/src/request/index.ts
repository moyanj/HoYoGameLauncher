/**
 * @file src/request/index.ts
 * @desc request
 * @since 2023-10-13
 */

import axios from 'axios';

// 判断是否是生产环境
// const isProduction = import.meta.env.MODE === 'production';

// todo 这边得写个返回类型，与 flask 交互的时候，需要用到
const request = axios.create({
    baseURL: 'http://127.0.0.1:6553',
    // baseURL: '/',
});

export default request;

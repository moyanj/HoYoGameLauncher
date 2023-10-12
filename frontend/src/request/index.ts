/**
 * @file src/request/index.ts
 * @desc request
 * @since 2023-10-13
 */

import axios from 'axios';

// todo 这边得写个返回类型，与 flask 交互的时候，需要用到
const request = axios.create({
    baseURL: 'http://localhost:6553', // todo: 解决动态端口问题
});

export default request;

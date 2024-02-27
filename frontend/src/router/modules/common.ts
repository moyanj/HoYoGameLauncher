/**
 * @file router/modules/common.ts
 * @desc Vue Router common module
 * @since 2021-10-06
 */

import {RouteRecordRaw} from 'vue-router'
import Launcher from "../../pages/Launcher.vue";

const commonRoutes: Array<RouteRecordRaw> = [{
    path: '/',
    redirect: '/launcher/ys',
}, {
    path: '/launcher/:game',
    name: 'Launcher',
    component: Launcher,
}]

export default commonRoutes
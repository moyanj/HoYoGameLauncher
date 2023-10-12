/**
 * @file router/modules/common.ts
 * @desc Vue Router common module
 * @since 2021-10-06
 */

import {RouteRecordRaw} from 'vue-router'
import Home from "../../pages/common/Home.vue";
import Launcher from "../../pages/common/Launcher.vue";
import Setting from "../../pages/common/Setting.vue";
import NotFound from "../../pages/common/NotFound.vue";

const commonRoutes: Array<RouteRecordRaw> = [{
    path: '/',
    name: 'Home',
    component: Home
}, {
    path: '/launcher/:game',
    name: 'Launcher',
    component: Launcher,
}, {
    path: '/config',
    name: 'Setting',
    component: Setting
}, {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: NotFound
}]

export default commonRoutes
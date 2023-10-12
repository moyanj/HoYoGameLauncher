/**
 * @file src/router/modules/user.ts
 * @desc Vue Router user module
 * @since 2023-10-06
 */

import { RouteRecordRaw } from 'vue-router'
import Abyss from "../../pages/User/Abyss.vue";
import Avatar from "../../pages/User/Avatar.vue";
import Gacha from "../../pages/User/Gacha.vue";

const userRoutes: Array<RouteRecordRaw> = [{
    path: '/user/abyss',
    name: 'Abyss',
    component: Abyss
},{
    path: '/user/avatar',
    name: 'Avatar',
    component: Avatar
},{
    path: '/user/gacha',
    name: 'Gacha',
    component: Gacha
}]

export default userRoutes

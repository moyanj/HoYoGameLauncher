/**
 * @file src/router/routes.ts
 * @desc Vue Router routes
 * @since 2023-10-06
 */

import {RouteRecordRaw} from 'vue-router';
import commonRoutes from "./modules/common.ts";

const routes: Array<RouteRecordRaw> = [
    ...commonRoutes,
];

export default routes

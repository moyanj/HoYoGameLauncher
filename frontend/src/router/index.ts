/**
 * @file src/router/index.ts
 * @desc Vue Router configuration
 * @since 2023-10-06
 */

import { createRouter, createWebHistory } from 'vue-router'
import routes from './routes'

const router = createRouter({
    history: createWebHistory('/web/'),
    routes,
});

// 参数变化时，刷新页面
router.afterEach((to, from) => {
    if (from.name === to.name && from.fullPath !== to.fullPath) {
        window.location.reload();
    }
});

export default router

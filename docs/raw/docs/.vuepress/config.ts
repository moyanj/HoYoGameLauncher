import { defineUserConfig } from 'vuepress'
import { defaultTheme } from '@vuepress/theme-default'
import { backToTopPlugin } from '@vuepress/plugin-back-to-top'

export default defineUserConfig({
  lang: 'zh-CN',
  title: 'HoYoGameLauncher',
  description: '这是我的第一个 VuePress 站点',
  theme: defaultTheme({
    navbar: [
      // NavbarItem
      {
        text: '开发文档',
        link: '/dev',
      }
      // 字符串 - 页面文件路径
    ],
    repo: 'moyanj/HoYoGameLauncher',
    docsDir: 'docs',
  }),
  plugins: [
    backToTopPlugin(),
  ],
  dest:"docs/dist"
})
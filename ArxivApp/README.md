# Arxiv 小程序

## Taro 使用

创建 Taro 小程序

``` bash
taro init ArxivApp
```

编译为微信小程序 

```bash
taro build --type weapp --watch
```



## 项目结构

```bash
├── config                 配置目录
|   ├── dev.js             开发时配置
|   ├── index.js           默认配置
|   └── prod.js            打包时配置
├── src                    源码目录
|   ├── actions            Redux Action
|   ├── assets             媒体文件目录
|   ├── constants          常量文件目录
|   ├── components         公共组件目录
|   ├── pages              页面文件目录
|   |   ├── index          index 页面目录
|   |   |   ├── banner     页面 index 私有组件
|   |   |   ├── index.js   index 页面逻辑
|   |   |   └── index.css  index 页面样式
|   ├── reducers           Redux Reducer
|   ├── service            Request API
|   ├── store              Redux Store
|   ├── styles             样式文件目录
|   ├── utils              公共方法库
|   ├── app.css            项目总通用样式
|   └── app.js             项目入口文件
└── package.json
```



## 开发历程

* 2020/02/02
  * 添加 Home，User 页面。
  * 添加封装 api 脚手架：service/，utils/common.js，utils/validator.js，constants/status.js
  * 添加搜索栏组件：components/fake-search-bar/，styles/
  * 使用 URL 控制页面路由：constants/urls.js
  * 添加类别分页*AtTabBar*：最新，热门，推荐。
  
* 2020/02/03
  * 解决 async 不可用问题，[参考文章](https://blog.csdn.net/xubaifu1997/article/details/90605683)
  * 完成 Redux 集成，可以从 mock 中读取数据并显示。
  * 添加 AtList 组件，使用伪数据显示。
  
* 2020/02/05
  * 添加 loading 组件：components/loading
  * 抽离 PaperList 组件：components/paper-list
  
* 2020/02/06
  * 添加正在加载文字
  * 修改 PaperList 实现方式：去除AtList。以便可以实现上拉加载功能。
  
* 2020/02/07
  * 修改 Item 样式，可以使文本显示两行，[参考文章](https://blog.csdn.net/Beamon__/article/details/82757172)
  * 绑定 Item 点击事件。
  
* 2020/02/08

  * 重构 Home 页面数据 fetch 方式，以便后续实现上拉加载，下拉刷新。

  * 完成上拉加载，后续需要重构。

    注：onScrollToLower 的响应函数需要.bind去绑定，否则无限调用。

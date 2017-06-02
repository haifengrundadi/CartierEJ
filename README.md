# CartierEJ 开源框架框架

## CartierEJ是什么？

	CartierEJ是基于小红书Cartier开发的一个适合各种APP移动UI开源自动化框架，包括NATIVE和Hybird H5。

## CariterEJ可以做哪些？

	CariterEJ可以让你在几分钟之内实现单个设备上的UI移动化运行，包括常见的NATIVE和Hybird。

	结合另外一个开源项目DisCartierEJ（后续会并到一起),可以在一台物理机上根据用户需要生产多个不同要求的
	Docker镜像，进而可以Run Cases。

	例如，需要运行 3 台 5.0 以上的三星手机，那么当用户配置完以后就可以将自己的case跑在了这 3 台设备上了。

	结合Jenkins可以完成日常App的主流程的巡检，并将结果生产可视化报告。


## 你需要什么？

	所有的Case都是Python写的，需要了解基本的Python语法。所需要的相关包，都可以通过“pip install -r
	requirements.txt" 进行安装。

	另外，需要安装相关的软件，Appium，并将手机和电脑通过USB或者相关的管理工具连接，保证能跟设备进行交互。

## 目标是什么？

	实现一个模板式的移动自动化开发框架，开发者只需要花很少的时间，既可以实现一个Case的编写，并可以和DisCartierEJ
	结合形成多设备同时run tests的局面，并能和Jenkins结合完成日常化的巡检。
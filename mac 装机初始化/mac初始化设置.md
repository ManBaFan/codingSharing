1. mac提效设置  
（1）系统设置，触控板，打开“单指轻点”；  
（2）系统设置，触控板，查询与数据监测器，选择“三指轻点”；  
（3）系统设置，触控板，更多手势，轻扫切换全屏幕显示的应用程序，选择“四指左右轻扫”；  
（4）系统设置，辅助功能，指针控制，触控板选项，打开“使用触控板进行拖移”，拖移样式选择“三指拖移”。  
2. 安装软件  
（1）chrome  
（2）vscode  
（3）iterm2  
（4）homebrew  
mac电脑安装homebrew，选择最新版的包。  
    [https://github.com/Homebrew/brew/releases/download/4.2.6/Homebrew-4.2.6.pkg]  
    安装完成后，设置环境变量。`vim ～/.zshrc` ，加入如下两行内容，保存退出。  
    `export HOMEBREW_PATH="/opt/homebrew/bin/"`
    `export PATH=".$PATH:$HOMEBREW_PATH"`
（5）git  
    使用brew来安装  
    `brew install git && source .zshrc`  
（6）python  
    使用brew来安装  
    `brew install python && source .zshrc`  

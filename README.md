# alien_invasion
 
## 2020年2月10日
看完13章，按照书上代码，写完发现有个问题，
当飞船用完的时候，并没有停止不动。
可能是我哪里和书上写的不一样，或者代码本身存在着bug。

bug已经解决
````
 stats.game_active=False 误写成ship.game_active
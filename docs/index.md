---
title: 知识花园
template: home.html
---

<center><font  color= #518FC1 size=6 class="ml3">用科学解释世界 用理性破除愚昧</font></center>
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/2.0.2/anime.min.js"></script>


本知识库基于 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 进行部署，在于收藏和分享感兴趣的话题和信息。

<div id="rcorners">
    <body>
      <font color="#4351AF">
        <p class="p1"></p>
<script defer>
    //格式：2020年04月12日 10:20:00 星期二
    function format(newDate) {
        var day = newDate.getDay();
        var y = newDate.getFullYear();
        var m =
            newDate.getMonth() + 1 < 10
                ? "0" + (newDate.getMonth() + 1)
                : newDate.getMonth() + 1;
        var d =
            newDate.getDate() < 10 ? "0" + newDate.getDate() : newDate.getDate();
        var h =
            newDate.getHours() < 10 ? "0" + newDate.getHours() : newDate.getHours();
        var min =
            newDate.getMinutes() < 10
                ? "0" + newDate.getMinutes()
                : newDate.getMinutes();
        var s =
            newDate.getSeconds() < 10
                ? "0" + newDate.getSeconds()
                : newDate.getSeconds();
        var dict = {
            1: "一",
            2: "二",
            3: "三",
            4: "四",
            5: "五",
            6: "六",
            0: "天",
        };
        //var week=["日","一","二","三","四","五","六"]
        return (
            y +
            "年" +
            m +
            "月" +
            d +
            "日" +
            " " +
            h +
            ":" +
            min +
            ":" +
            s +
            " 星期" +
            dict[day]
        );
    }
    var timerId = setInterval(function () {
        var newDate = new Date();
        var p1 = document.querySelector(".p1");
        if (p1) {
            p1.textContent = format(newDate);
        }
    }, 1000);
</script>
      </font>
    </body>
  </div>

以下两个地址都可以访问本站点：     

- [info.ccsyue.com](https://info.ccsyue.com)：基于 [Netlify](https://app.netlify.com/)，国内访问相对快一些；     
- [doc.ccsyue.com](https://doc.ccsyue.com)：基于 [GitHub Pages](https://pages.github.com/)，国内访问可能有一定延迟。

<p align="center">
    <img src="https://cdn.ccsyue.com/picx-images-hosting/master/kg-readme-cover.4xucvdmtbp.gif" alt><br>
</p>

!!! abstract "方氏三定律"

    一、只允许你听的一面之辞，十之八九是谎言。
    
    二、在不清楚鸡蛋与高墙孰是孰非时，不妨先站在鸡蛋一边。站鸡蛋站错了没有什么危害、站高墙站错了就成了帮凶。
    
    三、翻身外的墙容易，翻心中的墙难。
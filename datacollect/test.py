# -*- coding: utf-8 -*-

import xlwt
from datetime import datetime
import json
import HTMLParser
s = "&#xf189;&#xe890;"
h = HTMLParser.HTMLParser()
print h.unescape(s)
import json


result = u'{"data":{"tag":"73409061","end":true,"nextPageIndex":1,"spuList":[{"spuName":"[太极]一清颗粒7.5g*12袋","unit":"盒","spuId":1341423606,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/1e8c51ae9e679ce59477d40054636310239816.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/1e8c51ae9e679ce59477d40054636310239816.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":32.0,"currentPrice":32.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1510115898,"spec":"7.5g*12袋","soldStatus":0,"realStock":5,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":32.0,"currentPrice":32.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[同仁堂]京制牛黄解毒片","unit":"","spuId":1010141902,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/8721282491551e37ed33d0a5206b0eba196340.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/8721282491551e37ed33d0a5206b0eba196340.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;&#xeb2d;","originPrice":33.0,"currentPrice":33.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111175378,"spec":"0.6gx8片x10瓶","soldStatus":0,"realStock":17,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":33.0,"currentPrice":33.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[可可康]复方金银花颗粒10g*18袋","unit":"","spuId":1188030190,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/scproduct/150d110e39a9839fe353a3e3c7785207173335.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/scproduct/150d110e39a9839fe353a3e3c7785207173335.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe6fc;&#xeb2d;","originPrice":28.0,"currentPrice":28.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1319748542,"spec":"10g*18袋","soldStatus":0,"realStock":6,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":28.0,"currentPrice":28.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[可可康]蒲地蓝消炎片0.3g*10片*5板","unit":"","spuId":1188106255,"tag":"73409061","activityTag":"discount","littleImageUrl":"http://p1.meituan.net/scproduct/6e226fca86cc9aaa4975e83e7b2b2b2d230907.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/scproduct/6e226fca86cc9aaa4975e83e7b2b2b2d230907.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe422;&#xeb2d;","originPrice":27.5,"currentPrice":19.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":1,"skuList":[{"skuId":1319674003,"spec":"0.3g*10片*5板","soldStatus":0,"realStock":32,"activityStock":32,"minPurchaseNum":-1,"restrict":1,"originPrice":27.5,"currentPrice":19.0,"boxFee":0.0,"skuPromotionInfo":"6.91折 限1份","count":0}],"spuAttrList":[],"spuPromotionInfo":"6.91折 限1份","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[金太子]清热解毒口服液 10ml*10支","unit":"","spuId":1573502542,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/38322add77264381255587cbadaf8847460337.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/38322add77264381255587cbadaf8847460337.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf4f0;&#xeb2d;","originPrice":8.8,"currentPrice":8.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793268798,"spec":"10ml*10支","soldStatus":0,"realStock":8,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":8.8,"currentPrice":8.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[香雪]广东凉茶颗粒10g*20袋","unit":"包","spuId":1573502678,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/2ee1eee6a7fdccb8fb3d3c772282f102167819.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/2ee1eee6a7fdccb8fb3d3c772282f102167819.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":19.8,"currentPrice":19.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793196314,"spec":"10g*20袋","soldStatus":0,"realStock":5,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":19.8,"currentPrice":19.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[999]板蓝根颗粒10g*20袋","unit":"","spuId":1573503060,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/wmproduct/4ab8d08e1ddd7a4a1b970f73093ac79f79975.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/wmproduct/4ab8d08e1ddd7a4a1b970f73093ac79f79975.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":23.5,"currentPrice":23.5,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793196700,"spec":"10g*20袋盒装","soldStatus":0,"realStock":17,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":23.5,"currentPrice":23.5,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[欧意]银黄软胶囊0.49g*12粒*2板","unit":"","spuId":1573541844,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/30312f9f2731135d841139a46e28302c214854.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/30312f9f2731135d841139a46e28302c214854.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":32.8,"currentPrice":32.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793230790,"spec":"0.49g*12粒*2板","soldStatus":0,"realStock":4,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":32.8,"currentPrice":32.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[国金]复方金银花颗粒 10g*12袋","unit":"","spuId":1573580471,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/6b33b01ad0e5647eb0c11d22f26211c7280594.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/6b33b01ad0e5647eb0c11d22f26211c7280594.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":19.8,"currentPrice":19.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793196207,"spec":"10g*12袋","soldStatus":0,"realStock":6,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":19.8,"currentPrice":19.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[午时]金银花露(含糖型)340ml","unit":"","spuId":1034392400,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/be5c2ee5d8b089f5e12a3b2318c699b4132571.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/be5c2ee5d8b089f5e12a3b2318c699b4132571.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe703;&#xeb2d;","originPrice":8.0,"currentPrice":8.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139193380,"spec":"340ml","soldStatus":0,"realStock":9,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":8.0,"currentPrice":8.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[白云山]复方板蓝根颗粒15g*20袋","unit":"包","spuId":1573541582,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/cbb08c4559919d97ffe89c21a10a79d4201809.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/cbb08c4559919d97ffe89c21a10a79d4201809.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf4f0;&#xeb2d;","originPrice":26.0,"currentPrice":26.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793230522,"spec":"15g*20袋","soldStatus":0,"realStock":13,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":26.0,"currentPrice":26.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[白云山]板蓝根颗粒10g*20袋","unit":"","spuId":1010246736,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/08f146baf934be093783602a8d205fba180734.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/08f146baf934be093783602a8d205fba180734.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf808;&#xeb2d;","originPrice":23.0,"currentPrice":23.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1110967122,"spec":"10g*20袋","soldStatus":0,"realStock":14,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":23.0,"currentPrice":23.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[白云山]板蓝根颗粒10g*30袋","unit":"包","spuId":1010063558,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/69041ffe766edec43891109e246037b1178083.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/69041ffe766edec43891109e246037b1178083.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf4f0;&#xeb2d;","originPrice":21.0,"currentPrice":21.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xf3ca;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111175377,"spec":"10g*30袋","soldStatus":0,"realStock":11,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":21.0,"currentPrice":21.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[王老吉]广东凉茶颗粒10g*20袋","unit":"包","spuId":1573541576,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/4576207bd1f7f32cde0f038699d6ada4282407.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/4576207bd1f7f32cde0f038699d6ada4282407.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf4f0;&#xeb2d;","originPrice":19.8,"currentPrice":19.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xf3ca;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793268701,"spec":"10g*20袋","soldStatus":0,"realStock":37,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":19.8,"currentPrice":19.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[仁悦]三黄片0.26g*16片*2板","unit":"","spuId":1010141893,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/scproduct/d799beb5d8795cad326b49ab5ae6fac2196303.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/scproduct/d799beb5d8795cad326b49ab5ae6fac2196303.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":8.5,"currentPrice":8.5,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1110967121,"spec":"0.26g*16片*2板","soldStatus":0,"realStock":9,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":8.5,"currentPrice":8.5,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[诺金]复方金银花颗粒10g*10袋","unit":"","spuId":1010024515,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/cbdd03615d2b638f41c53641a499ad39168280.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/cbdd03615d2b638f41c53641a499ad39168280.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":25.0,"currentPrice":25.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111099679,"spec":"10g*10袋","soldStatus":0,"realStock":2,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":25.0,"currentPrice":25.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[葵花]金银花露250ml","unit":"","spuId":1573502454,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/14e443a2c23b9b6001460be17b0808c8170800.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/14e443a2c23b9b6001460be17b0808c8170800.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":12.0,"currentPrice":12.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793268699,"spec":"250ml","soldStatus":0,"realStock":86,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":12.0,"currentPrice":12.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[星群]夏桑菊颗粒3g*10袋","unit":"","spuId":1573502505,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/fd5fea8135f1c5d7060b4d25f25cbe9d216408.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/fd5fea8135f1c5d7060b4d25f25cbe9d216408.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe6fc;&#xeb2d;","originPrice":18.0,"currentPrice":18.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793230597,"spec":"3g*10袋","soldStatus":0,"realStock":13,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":18.0,"currentPrice":18.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[三精]双黄连口服液10ml*10支","unit":"盒","spuId":1107678654,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/scproduct/9df11d643fbeffa2da55fd4a3ff0c8de204604.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/scproduct/9df11d643fbeffa2da55fd4a3ff0c8de204604.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":25.0,"currentPrice":25.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1222736785,"spec":"10ml*10支","soldStatus":0,"realStock":4,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":25.0,"currentPrice":25.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[邦琪]复方鱼腥草颗粒6g*12袋","unit":"","spuId":1010024546,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/621128a6f03bf643bdc9b541eae5dcc5182589.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/621128a6f03bf643bdc9b541eae5dcc5182589.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe6fc;&#xeb2d;","originPrice":24.6,"currentPrice":24.6,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1110967166,"spec":"6g*12袋","soldStatus":0,"realStock":9,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":24.6,"currentPrice":24.6,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[仲景]黄连上清丸","unit":"","spuId":1010325744,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/16c1071ec4eea70bbd680958419df2c9156075.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/16c1071ec4eea70bbd680958419df2c9156075.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":12.0,"currentPrice":12.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111175371,"spec":"6gx10袋","soldStatus":0,"realStock":3,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":12.0,"currentPrice":12.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[腾药]银翘解毒片0.5g*12片*2板","unit":"","spuId":1573580351,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/941118ece14b1717bfb6fc48762fd0a6166180.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/941118ece14b1717bfb6fc48762fd0a6166180.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":7.8,"currentPrice":7.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793268692,"spec":"0.5g*12片*2板","soldStatus":0,"realStock":12,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":7.8,"currentPrice":7.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[惠海希康]金莲花软胶囊0.55g*10粒*3板","unit":"","spuId":1573502455,"tag":"73409061","activityTag":"discount","littleImageUrl":"http://p1.meituan.net/xianfu/6f6bc0f990657d7c07481cef12deaa62139481.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/6f6bc0f990657d7c07481cef12deaa62139481.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":41.3,"currentPrice":25.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":1,"skuList":[{"skuId":1793196096,"spec":"0.55g*10粒*3板","soldStatus":0,"realStock":10,"activityStock":10,"minPurchaseNum":-1,"restrict":1,"originPrice":41.3,"currentPrice":25.0,"boxFee":0.0,"skuPromotionInfo":"6.05折 限1份","count":0}],"spuAttrList":[],"spuPromotionInfo":"6.05折 限1份","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[太极]板蓝根颗粒(儿童装)5g*20袋","unit":"包","spuId":1034740067,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/c6e8e48c0fc8a02c75a53f14e70828dc152302.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/c6e8e48c0fc8a02c75a53f14e70828dc152302.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":22.5,"currentPrice":22.5,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1138997016,"spec":"5g*20袋","soldStatus":0,"realStock":2,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":22.5,"currentPrice":22.5,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[陈李济]上清丸42g","unit":"","spuId":1010024512,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/8765328a23684daf99580aef405675d2176975.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/8765328a23684daf99580aef405675d2176975.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":12.0,"currentPrice":12.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111099672,"spec":"42g","soldStatus":0,"realStock":7,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":12.0,"currentPrice":12.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[修正]二丁颗粒20g*10袋","unit":"盒","spuId":1034847861,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/b3f115e3517f022128290dd0d455de57188983.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/b3f115e3517f022128290dd0d455de57188983.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":48.3,"currentPrice":48.3,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139034367,"spec":"20g*10袋","soldStatus":0,"realStock":1,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":48.3,"currentPrice":48.3,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[邦琪]复方鱼腥草颗粒6g*10袋","unit":"","spuId":1010141927,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/c74def3032706d32d7997a90b48dd880207308.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/c74def3032706d32d7997a90b48dd880207308.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe6fc;&#xeb2d;","originPrice":25.8,"currentPrice":25.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111006880,"spec":"6g*10袋","soldStatus":0,"realStock":12,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":25.8,"currentPrice":25.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[白云山]复方穿心莲片100片","unit":"盒","spuId":1034353211,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/50d650a4697dbab751e3cdbd88fb8b5a134761.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/50d650a4697dbab751e3cdbd88fb8b5a134761.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":18.9,"currentPrice":18.9,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139193379,"spec":"100片","soldStatus":0,"realStock":7,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":18.9,"currentPrice":18.9,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[今辰]牛黄上清片24片*2板","unit":"","spuId":1010141900,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/47dd4f95739dae02ff24e5843eb45148164596.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/47dd4f95739dae02ff24e5843eb45148164596.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xe6fc;&#xeb2d;","originPrice":4.0,"currentPrice":4.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111099678,"spec":"24片*2板","soldStatus":0,"realStock":7,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":4.0,"currentPrice":4.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[星湖]复方黄芩片60片","unit":"","spuId":1010024511,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/1cde1d4a03d967d59cee7ea1269581d1149036.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/1cde1d4a03d967d59cee7ea1269581d1149036.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":10.8,"currentPrice":10.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111099671,"spec":"60片","soldStatus":0,"realStock":7,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":10.8,"currentPrice":10.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[陈李济]上清丸9g*10丸","unit":"","spuId":1010141898,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/f66c789ad0c20f5ceb00332464121399119962.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/f66c789ad0c20f5ceb00332464121399119962.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":13.2,"currentPrice":13.2,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1111099673,"spec":"9g*10丸","soldStatus":0,"realStock":9,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":13.2,"currentPrice":13.2,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[神威]清开灵软胶囊0.4g*12粒","unit":"","spuId":1573541611,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/ab084599cd54082bafc65b4b70fa142d762695.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/ab084599cd54082bafc65b4b70fa142d762695.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xf3ca;&#xeb2d;","originPrice":22.1,"currentPrice":22.1,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1793230549,"spec":"0.4g*12粒","soldStatus":0,"realStock":1,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":22.1,"currentPrice":22.1,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[白鹤]复方南板蓝根片100片","unit":"盒","spuId":1034588575,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/f42e204abf1195f4c6b98ddf348bb913108150.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/f42e204abf1195f4c6b98ddf348bb913108150.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":4.6,"currentPrice":4.6,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139294346,"spec":"100片","soldStatus":0,"realStock":1,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":4.6,"currentPrice":4.6,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[德众]三黄片0.26g*24片","unit":"盒","spuId":1034548525,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/db9fc3bc998cb127665facc232a4a487147374.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/db9fc3bc998cb127665facc232a4a487147374.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":6.0,"currentPrice":6.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139116214,"spec":"0.26g*24片","soldStatus":0,"realStock":14,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":6.0,"currentPrice":6.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[百利]柴黄颗粒","unit":"盒","spuId":1034314252,"tag":"73409061","activityTag":"","littleImageUrl":"http://p1.meituan.net/xianfu/2cbecc0b08cb339d79d3721d85c1652a172577.jpg@100w_100h_1e_1c","bigImageUrl":"http://p1.meituan.net/xianfu/2cbecc0b08cb339d79d3721d85c1652a172577.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":36.8,"currentPrice":36.8,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139034334,"spec":"3gx12袋","soldStatus":0,"realStock":2,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":36.8,"currentPrice":36.8,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[冯了性]羚翘解毒丸9g*10丸","unit":"","spuId":1010063555,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/b1a423da114c92cd6c46747e05e4e8f2147781.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/b1a423da114c92cd6c46747e05e4e8f2147781.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":14.5,"currentPrice":14.5,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1110967123,"spec":"9g*10丸","soldStatus":0,"realStock":4,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":14.5,"currentPrice":14.5,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""},{"spuName":"[同仁堂]防风通圣丸","unit":"盒","spuId":1034548549,"tag":"73409061","activityTag":"","littleImageUrl":"http://p0.meituan.net/xianfu/750c082061fe5e88f4d285650f1fc14d271592.jpg@100w_100h_1e_1c","bigImageUrl":"http://p0.meituan.net/xianfu/750c082061fe5e88f4d285650f1fc14d271592.jpg@800w_600h_1e_1c","saleVolume":0,"saleVolumeDecoded":"&#xeb2d;","originPrice":30.0,"currentPrice":30.0,"spuDesc":"","praiseNum":0,"praiseNumDecoded":"&#xeb2d;","sellStatus":0,"activityType":0,"skuList":[{"skuId":1139334092,"spec":"6gx10袋","soldStatus":0,"realStock":5,"activityStock":0,"minPurchaseNum":-1,"restrict":-1,"originPrice":30.0,"currentPrice":30.0,"boxFee":0.0,"skuPromotionInfo":"","count":0}],"spuAttrList":[],"spuPromotionInfo":"","activityPolicy":{"discountByCount":{"count":0,"discount":1.0}},"statusDesc":""}]},"code":0,"msg":"成功"}'

print  1111
result = json.loads(result,"utf-8")

result = result['data']['spuList']
print result


wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
today = datetime.today()
today_date = datetime.date(today)

for i in xrange(len(result)):
    # 对result的每个子元素作遍历，
    for j in xrange(len(result[i])):
        # 将每一行的每个元素按行号i,列号j,写入到excel中。
        print result[i].values().__getitem__(j)
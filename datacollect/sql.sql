CREATE TABLE `t_spider_collect` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(500) DEFAULT NULL COMMENT '问题',
  `url` varchar(1000) DEFAULT NULL,
  `answer` text COMMENT '答案',
  `source` varchar(200) DEFAULT NULL COMMENT '来源',
  `praise_num` int(10) DEFAULT NULL COMMENT '点赞数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

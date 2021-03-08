-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: solo
-- ------------------------------------------------------
-- Server version	5.7.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `b3_solo_archivedate`
--

DROP TABLE IF EXISTS `b3_solo_archivedate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_archivedate` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `archiveTime` bigint(20) NOT NULL COMMENT '存档日期时间，该月份第一天的时间戳',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='存档日期表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_archivedate`
--

LOCK TABLES `b3_solo_archivedate` WRITE;
/*!40000 ALTER TABLE `b3_solo_archivedate` DISABLE KEYS */;
INSERT INTO `b3_solo_archivedate` VALUES ('1611663188171',1609430400000);
/*!40000 ALTER TABLE `b3_solo_archivedate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_archivedate_article`
--

DROP TABLE IF EXISTS `b3_solo_archivedate_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_archivedate_article` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `archiveDate_oId` varchar(19) NOT NULL COMMENT '存档日期 id',
  `article_oId` varchar(19) NOT NULL COMMENT '文章 id',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='存档-文章关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_archivedate_article`
--

LOCK TABLES `b3_solo_archivedate_article` WRITE;
/*!40000 ALTER TABLE `b3_solo_archivedate_article` DISABLE KEYS */;
INSERT INTO `b3_solo_archivedate_article` VALUES ('1611663188228','1611663188171','1611663187998');
/*!40000 ALTER TABLE `b3_solo_archivedate_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_article`
--

DROP TABLE IF EXISTS `b3_solo_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_article` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `articleTitle` varchar(255) NOT NULL COMMENT '文章标题',
  `articleAbstract` text NOT NULL COMMENT '文章摘要 Markdown',
  `articleAbstractText` text NOT NULL COMMENT '文章摘要纯文本',
  `articleTags` text NOT NULL COMMENT '文章标签，英文逗号分隔',
  `articleAuthorId` varchar(19) NOT NULL COMMENT '文章作者 id',
  `articleCommentCount` int(11) NOT NULL COMMENT '文章评论计数',
  `articleViewCount` int(11) NOT NULL COMMENT '文章浏览计数',
  `articleContent` mediumtext NOT NULL COMMENT '文章正文内容',
  `articlePermalink` varchar(255) NOT NULL COMMENT '文章访问路径',
  `articlePutTop` char(1) NOT NULL COMMENT '文章是否置顶',
  `articleCreated` bigint(20) NOT NULL COMMENT '文章创建时间戳',
  `articleUpdated` bigint(20) NOT NULL COMMENT '文章更新时间戳',
  `articleRandomDouble` double NOT NULL COMMENT '文章随机数，用于快速查询随机文章列表',
  `articleSignId` varchar(19) NOT NULL COMMENT '文章关联的签名档 id',
  `articleCommentable` char(1) NOT NULL COMMENT '文章是否可以评论',
  `articleViewPwd` varchar(128) NOT NULL COMMENT '文章浏览密码，留空为不设置访问密码',
  `articleImg1URL` varchar(255) NOT NULL COMMENT '文章首图地址',
  `articleStatus` int(11) NOT NULL COMMENT '文章状态，0：已发布，1：草稿',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_article`
--

LOCK TABLES `b3_solo_article` WRITE;
/*!40000 ALTER TABLE `b3_solo_article` DISABLE KEYS */;
INSERT INTO `b3_solo_article` VALUES ('1611663187998','菠萝 Bolo 博客系统已部署成功。','![](https://b3logfile.com/bing/20181120.jpg?imageView2/1/w/1280/h/720/interlace/1/q/100) \n\nBolo 博客系统已经初始化完毕，可在管理后台 - 工具 - 偏好设定中调整更多细节设置。如果需要导入已有博客文章，请参考文档 [Hexo/Jekyll/Markdown 文件导入](https://ld246.com/article/1498490209748)。\n\nBolo 是基于 [Solo](https://github.com/b3log/solo) 的修改版，主打功能：\n\n1. 离线\n\n2. 分类优化\n\n3. 游客化评论\n\n4. 同步与主分支更新\n\n欢迎你的体验！\n\n请在设置-偏好设定中设置黑客派用户名和 B3log Key 以获得完整体验。\n\n最后，如果你觉得 Bolo 很赞，请到[项目主页](https://github.com/adlered/bolo-solo)给颗星鼓励一下 :heart:','Bolo 博客系统已经初始化完毕，可在管理后台 - 工具 - 偏好设定中调整更多细节设置。如果需要导入已有博客文章，请参考文档 Hexo/Jekyll/Markdown 文件导入。 Bolo 是基于 Solo 的修改版，主打功能：   离线   分类优化   游客化评论   同步与主分支更新   欢迎你的体验！ 请在设置-偏好设定中设置黑客派用户名和 B3log Key 以获得完整体验。 最后，如果你觉得 Bolo 很赞，请到项目主页给颗星鼓励一下 ❤️','Bolo','1611663187140',1,13,'![](https://b3logfile.com/bing/20181120.jpg?imageView2/1/w/1280/h/720/interlace/1/q/100) \n\nBolo 博客系统已经初始化完毕，可在管理后台 - 工具 - 偏好设定中调整更多细节设置。如果需要导入已有博客文章，请参考文档 [Hexo/Jekyll/Markdown 文件导入](https://ld246.com/article/1498490209748)。\n\nBolo 是基于 [Solo](https://github.com/b3log/solo) 的修改版，主打功能：\n\n1. 离线\n\n2. 分类优化\n\n3. 游客化评论\n\n4. 同步与主分支更新\n\n欢迎你的体验！\n\n请在设置-偏好设定中设置黑客派用户名和 B3log Key 以获得完整体验。\n\n最后，如果你觉得 Bolo 很赞，请到[项目主页](https://github.com/adlered/bolo-solo)给颗星鼓励一下 :heart:','/hello-bolo','0',1611663187940,1611663187940,0.3437879607903013,'1','1','','https://b3logfile.com/bing/20181120.jpg?imageView2/1/w/1280/h/720/interlace/1/q/100',0);
/*!40000 ALTER TABLE `b3_solo_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_category`
--

DROP TABLE IF EXISTS `b3_solo_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_category` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `categoryTitle` varchar(64) NOT NULL COMMENT '分类标题',
  `categoryURI` varchar(255) NOT NULL COMMENT '分类访问路径',
  `categoryDescription` text NOT NULL COMMENT '分类描述',
  `categoryOrder` int(11) NOT NULL COMMENT '分类展现的排序',
  `categoryTagCnt` int(11) NOT NULL COMMENT '分类下聚合的标签计数',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='分类表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_category`
--

LOCK TABLES `b3_solo_category` WRITE;
/*!40000 ALTER TABLE `b3_solo_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `b3_solo_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_category_tag`
--

DROP TABLE IF EXISTS `b3_solo_category_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_category_tag` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `category_oId` varchar(19) NOT NULL COMMENT '分类 id',
  `tag_oId` varchar(19) NOT NULL COMMENT '标签 id',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='分类-标签关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_category_tag`
--

LOCK TABLES `b3_solo_category_tag` WRITE;
/*!40000 ALTER TABLE `b3_solo_category_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `b3_solo_category_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_comment`
--

DROP TABLE IF EXISTS `b3_solo_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_comment` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `commentContent` text NOT NULL COMMENT '评论内容',
  `commentCreated` bigint(20) NOT NULL COMMENT '评论时间戳',
  `commentName` varchar(50) NOT NULL COMMENT '评论人名称',
  `commentOnId` varchar(19) NOT NULL COMMENT '评论的文章/页面的 id',
  `commentSharpURL` varchar(255) NOT NULL COMMENT '评论访问路径，带 # 锚点',
  `commentThumbnailURL` text NOT NULL COMMENT '评论人头像图片链接地址',
  `commentURL` varchar(255) NOT NULL COMMENT '评论人链接地址',
  `commentOriginalCommentId` varchar(19) DEFAULT NULL COMMENT '评论回复时原始的评论 id，即父评论 id',
  `commentOriginalCommentName` varchar(50) DEFAULT NULL COMMENT '评论回复时原始的评论人名称，即父评论人名称',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='评论表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_comment`
--

LOCK TABLES `b3_solo_comment` WRITE;
/*!40000 ALTER TABLE `b3_solo_comment` DISABLE KEYS */;
INSERT INTO `b3_solo_comment` VALUES ('1611663188303','写博客需要坚持，相信积累后必然会有收获，我们一起努力加油 :smile:',1611663187940,'adlered','1611663187998','/hello-bolo#1611663188303','https://avatars1.githubusercontent.com/u/6754458?s=400&u=a8d4a1321a2f140d66a7c229ecd510c5560f1148&v=4','https://github.com/adlered','','');
/*!40000 ALTER TABLE `b3_solo_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_link`
--

DROP TABLE IF EXISTS `b3_solo_link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_link` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `linkAddress` varchar(255) NOT NULL COMMENT '链接地址',
  `linkDescription` varchar(255) NOT NULL COMMENT '链接描述',
  `linkOrder` int(11) NOT NULL COMMENT '链接展现的排序',
  `linkTitle` varchar(255) NOT NULL COMMENT '链接标题',
  `linkIcon` varchar(255) NOT NULL COMMENT '链接图标链接地址',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='链接表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_link`
--

LOCK TABLES `b3_solo_link` WRITE;
/*!40000 ALTER TABLE `b3_solo_link` DISABLE KEYS */;
/*!40000 ALTER TABLE `b3_solo_link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_option`
--

DROP TABLE IF EXISTS `b3_solo_option`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_option` (
  `oId` varchar(64) NOT NULL COMMENT '主键',
  `optionValue` text NOT NULL COMMENT '配置项值',
  `optionCategory` varchar(128) NOT NULL COMMENT '配置项分类',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='配置项';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_option`
--

LOCK TABLES `b3_solo_option` WRITE;
/*!40000 ALTER TABLE `b3_solo_option` DISABLE KEYS */;
INSERT INTO `b3_solo_option` VALUES ('adminActiveSentToMailbox','on','preference'),('allowVisitDraftViaPermalink','false','preference'),('articleListDisplayCount','20','preference'),('articleListPaginationWindowSize','15','preference'),('articleListStyle','titleAndAbstract','preference'),('b3logKey','','preference'),('blogSubtitle','记录精彩的程序人生','preference'),('blogTitle','jwf 的个人博客','preference'),('commentable','true','preference'),('customVars','key0=val0|key1=list|key2=val2','preference'),('editorMode','sv','preference'),('enableArticleUpdateHint','false','preference'),('externalRelevantArticlesDisplayCount','0','preference'),('faviconURL','https://pic.stackoverflow.wiki/uploadImages/114/246/231/87/2020/06/06/16/41/3e4a3ce8-8882-4258-9860-a337bf859605.png','preference'),('feedOutputCnt','10','preference'),('feedOutputMode','abstract','preference'),('footerContent','','preference'),('githubPAT','e4b067b24ce74408c6835d12c37923a600611323','preference'),('hacpaiUser','','preference'),('hljsTheme','github','preference'),('htmlHead','','preference'),('interactive','on','preference'),('kanbanniangSelector','','preference'),('localeString','zh_CN','preference'),('mailBox','','preference'),('mailPassword','','preference'),('mailUserContext','','preference'),('mailUsername','','preference'),('maxArchive','-1','preference'),('metaDescription','A small and beautiful blogging system. 一款小而美的博客系统。','preference'),('metaKeywords','Solo,Java,博客,开源','preference'),('mobileSkinDirName','bolo-bubble','skin'),('mostCommentArticleDisplayCount','5','preference'),('mostUsedTagDisplayCount','20','preference'),('mostViewArticleDisplayCount','5','preference'),('noticeBoard','Open Source, Open Mind, <br/>Open Sight, Open Future!\n\n<!-- 公告栏可使用 HTML、JavaScript，比如可以在此加入第三方统计 js -->','preference'),('pullGitHub','','preference'),('randomArticlesDisplayCount','5','preference'),('recentArticleDisplayCount','','preference'),('recentCommentDisplayCount','10','preference'),('relevantArticlesDisplayCount','5','preference'),('replyRemind','','preference'),('showCodeBlockLn','false','preference'),('signs','[{\"signHTML\":\"\",\"oId\":0},{\"signHTML\":\"<hr>\\n\\n标题：{title}<br>\\n作者：<a href=\\\"{blog}\\\" target=\\\"_blank\\\">{author}<\\/a><br>\\n地址：<a href=\\\"{url}\\\" target=\\\"_blank\\\">{url}<\\/a><br>\\n\\n<!-- 签名档内可使用 HTML、JavaScript -->\\n<br>\",\"oId\":1},{\"signHTML\":\"<hr>\\n\\n标题：{title}<br>\\n作者：<a href=\\\"{blog}\\\" target=\\\"_blank\\\">{author}<\\/a><br>\\n地址：<a href=\\\"{url}\\\" target=\\\"_blank\\\">{url}<\\/a><br>\\n\\n<!-- 签名档内可使用 HTML、JavaScript -->\\n<br>\",\"oId\":2},{\"signHTML\":\"<hr>\\n\\n标题：{title}<br>\\n作者：<a href=\\\"{blog}\\\" target=\\\"_blank\\\">{author}<\\/a><br>\\n地址：<a href=\\\"{url}\\\" target=\\\"_blank\\\">{url}<\\/a><br>\\n\\n<!-- 签名档内可使用 HTML、JavaScript -->\\n<br>\",\"oId\":3}]','preference'),('skinDirName','bolo-bubble','skin'),('spam','','preference'),('statisticBlogViewCount','168','statistic'),('syncGitHub','true','preference'),('timeZoneId','Asia/Shanghai','preference'),('tuChuangConfig','hacpai','preference'),('version','4.3.1','preference'),('wafCurrentLimitSecond','180','preference'),('wafCurrentLimitTimes','180','preference'),('wafPower','on','preference'),('welfareLuteService','false','preference');
/*!40000 ALTER TABLE `b3_solo_option` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_page`
--

DROP TABLE IF EXISTS `b3_solo_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_page` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `pageOrder` int(11) NOT NULL COMMENT '页面展现排序',
  `pagePermalink` varchar(255) NOT NULL COMMENT '页面访问路径',
  `pageTitle` varchar(255) NOT NULL COMMENT '页面标题',
  `pageOpenTarget` varchar(255) NOT NULL COMMENT '页面打开方式',
  `pageIcon` varchar(255) NOT NULL COMMENT '页面展示用小图标',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='自定义页面表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_page`
--

LOCK TABLES `b3_solo_page` WRITE;
/*!40000 ALTER TABLE `b3_solo_page` DISABLE KEYS */;
/*!40000 ALTER TABLE `b3_solo_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_plugin`
--

DROP TABLE IF EXISTS `b3_solo_plugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_plugin` (
  `oId` varchar(128) NOT NULL COMMENT '主键',
  `author` text NOT NULL COMMENT '插件作者',
  `name` varchar(255) NOT NULL COMMENT '插件名称',
  `status` varchar(10) NOT NULL COMMENT '插件状态，启用：ENABLED，禁用：DISABLED',
  `version` varchar(10) NOT NULL COMMENT '插件版本',
  `setting` text COMMENT '插件配置，JSON 字符串',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='插件表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_plugin`
--

LOCK TABLES `b3_solo_plugin` WRITE;
/*!40000 ALTER TABLE `b3_solo_plugin` DISABLE KEYS */;
INSERT INTO `b3_solo_plugin` VALUES ('目录生成器_1.0.1','<a href=\"http://88250.b3log.org\">88250</a>','目录生成器','ENABLED','1.0.1','{}'),('看板娘 ＋_0.0.2','<a href=\"https://github.com/Vanessa219\">Vanessa</a> Re: <a href=\"https://github.com/csfwff\">csfwff</a>','看板娘 ＋','ENABLED','0.0.2','{}');
/*!40000 ALTER TABLE `b3_solo_plugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_tag`
--

DROP TABLE IF EXISTS `b3_solo_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_tag` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `tagTitle` varchar(255) NOT NULL COMMENT '标签标题',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='标签表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_tag`
--

LOCK TABLES `b3_solo_tag` WRITE;
/*!40000 ALTER TABLE `b3_solo_tag` DISABLE KEYS */;
INSERT INTO `b3_solo_tag` VALUES ('1611663188048','Bolo');
/*!40000 ALTER TABLE `b3_solo_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_tag_article`
--

DROP TABLE IF EXISTS `b3_solo_tag_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_tag_article` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `article_oId` varchar(19) NOT NULL COMMENT '文章 id',
  `tag_oId` varchar(19) NOT NULL COMMENT '标签 id',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='标签-文章关联表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_tag_article`
--

LOCK TABLES `b3_solo_tag_article` WRITE;
/*!40000 ALTER TABLE `b3_solo_tag_article` DISABLE KEYS */;
INSERT INTO `b3_solo_tag_article` VALUES ('1611663188110','1611663187998','1611663188048');
/*!40000 ALTER TABLE `b3_solo_tag_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `b3_solo_user`
--

DROP TABLE IF EXISTS `b3_solo_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `b3_solo_user` (
  `oId` varchar(19) NOT NULL COMMENT '主键',
  `userName` varchar(255) NOT NULL COMMENT '用户名',
  `userURL` varchar(255) NOT NULL COMMENT '用户链接地址',
  `userRole` varchar(255) NOT NULL COMMENT '用户角色，管理员：adminRole，普通用户：defaultRole，访客用户：visitorRole',
  `userAvatar` varchar(255) NOT NULL COMMENT '用户头像图片链接地址',
  `userB3Key` varchar(64) NOT NULL COMMENT 'B3log Key',
  `userGitHubId` varchar(32) NOT NULL COMMENT '用户 GitHub Open Id',
  PRIMARY KEY (`oId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `b3_solo_user`
--

LOCK TABLES `b3_solo_user` WRITE;
/*!40000 ALTER TABLE `b3_solo_user` DISABLE KEYS */;
INSERT INTO `b3_solo_user` VALUES ('1611663187140','jwf','http://sick.pwall.icu:8080','adminRole','https://pic.stackoverflow.wiki/uploadImages/117/136/73/84/2020/08/03/19/59/2c12286b-91a0-478e-ba47-edaa21f19476.png','0a38591e388682690be7429685110e1c','000000');
/*!40000 ALTER TABLE `b3_solo_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-25 12:03:47

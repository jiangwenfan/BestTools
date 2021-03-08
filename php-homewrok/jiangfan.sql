
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin
-- ----------------------------
DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `user` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pass` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin
-- ----------------------------
INSERT INTO `admin` VALUES (1, 'admin', '770c4a912d49bd125d93bd855e035f79');

-- ----------------------------
-- Table structure for class
-- ----------------------------
DROP TABLE IF EXISTS `class`;
CREATE TABLE `class`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `banjihao` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `zhuanye` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ssxi` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `intro` text CHARACTER SET utf8 COLLATE utf8_general_ci,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `banjihao`(`banjihao`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class
-- ----------------------------
INSERT INTO `class` VALUES (1, '21715', '计算机应用技术12', '计算机科学系1', 'web应用软件开发1');
INSERT INTO `class` VALUES (2, '21702', '计算机应用技术', '计算机科学系', 'web应用软件开发');
INSERT INTO `class` VALUES (3, '21703', '计算机网络技术', '计算机科学系', '网络工程、网络管理、网络搭建');
INSERT INTO `class` VALUES (4, '21704', '计算机网络技术', '计算机科学系', '网络工程、网络管理、网络搭建');
INSERT INTO `class` VALUES (5, '21705', '软件技术', '计算机科学系', 'java程序开发、app应用开发');
INSERT INTO `class` VALUES (6, '21706', '软件技术', '计算机科学系', 'java程序开发、app应用开发');
INSERT INTO `class` VALUES (7, '31701', '应用电子技术', '电子信息工程系', '电子电路设计开发');
INSERT INTO `class` VALUES (8, '31702', '应用电子技术', '电子信息工程系', '电子电路设计开发');
INSERT INTO `class` VALUES (9, '41701', '市场营销', '电子商务学院', '产品营销、产品包装售卖');
INSERT INTO `class` VALUES (10, '21711', '旅游管理111', '电子商务学院11', '酒店管理、旅游经营、导游服务11');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `xuehao` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `xm` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `xb` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` tinyint(4) NOT NULL,
  `csrq` date NOT NULL,
  `sfzh` varchar(18) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ssbanji` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `height` float(3, 2) NOT NULL,
  `address` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `xuehao`(`xuehao`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (1, '20170001', '杨华', '男', 24, '1995-08-06', '522601199508061108', '21715', 1.68, '贵州省凯里市华联路1号');
INSERT INTO `student` VALUES (2, '20170002', '赵天翔', '男', 35, '1984-08-06', '522601198408061108', '21715', 1.77, '湖南省长沙市迎宾路2号');
INSERT INTO `student` VALUES (3, '20170003', '李萌', '女', 29, '1990-06-22', '522601199006221298', '21702', 1.86, '贵州省贵阳市大营坡');
INSERT INTO `student` VALUES (4, '20170004', '张扬', '男', 28, '1991-02-17', '522601199102170987', '21702', 1.62, '贵州省六盘水市葫芦娃大道12号');
INSERT INTO `student` VALUES (5, '20170005', '荀彧', '女', 27, '1992-06-16', '522601199206166549', '21703', 1.76, '贵州省凯里市麻江县碧波镇');
INSERT INTO `student` VALUES (6, '20170006', '刘洋', '女', 23, '1996-11-11', '522601199611110438', '21704', 1.81, '河南省郑州市中洲中路121号');
INSERT INTO `student` VALUES (7, '20170007', '梦航', '男', 31, '1988-12-25', '522601198812253872', '21708', 1.45, '湖北省武汉市学府路11号');
INSERT INTO `student` VALUES (10, '20170008', '张子君', '女', 36, '1983-04-28', '522601198304280012', '21711', 1.58, '福建省福州市富通大道980号');

-- ----------------------------
-- View structure for xiaozhu
-- ----------------------------
DROP VIEW IF EXISTS `xiaozhu`;
CREATE  VIEW `xiaozhu` AS select `student`.`id` AS `id`,`student`.`xuehao` AS `xuehao`,`student`.`xm` AS `xm`,`student`.`xb` AS `xb`,`student`.`age` AS `age`,`student`.`csrq` AS `csrq`,`student`.`sfzh` AS `sfzh`,`student`.`ssbanji` AS `ssbanji`,`student`.`height` AS `height`,`student`.`address` AS `address` from `student`;

SET FOREIGN_KEY_CHECKS = 1;

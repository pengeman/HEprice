
DROP TABLE IF EXISTS `t_s_version`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `s_version` (
  `ID` varchar(32) NOT NULL promary key,
  `loginpage` varchar(100) default NULL,
  `versioncode` varchar(50) default NULL,
  `versionname` varchar(30) default NULL,
  `versionnum` varchar(20) default NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `t_s_version`
--

LOCK TABLES `t_s_version` WRITE;
/*!40000 ALTER TABLE `t_s_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_s_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_ditie`
--

-- Table structure for table `u_area`
--

DROP TABLE IF EXISTS `u_area`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_area` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '板型：BP100',
  `area` decimal(5,3) default NULL COMMENT '面积',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COMMENT='单板面积\r\n';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_area`
--

LOCK TABLES `u_area` WRITE;
/*!40000 ALTER TABLE `u_area` DISABLE KEYS */;
INSERT INTO `u_area` VALUES (1,'bp32','0.014'),(2,'bp50','0.140'),(3,'bp100','0.240'),(4,'bp150','0.620'),(5,'bp200','0.850'),(6,'bp250','1.500'),(7,'bs150','0.240'),(8,'bs200','0.620'),(9,'bw300','1.500');
/*!40000 ALTER TABLE `u_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_collet`
--

DROP TABLE IF EXISTS `u_collet`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_collet` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '换热器型号',
  `price` decimal(8,2) default NULL,
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='底托';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_collet`
--

LOCK TABLES `u_collet` WRITE;
/*!40000 ALTER TABLE `u_collet` DISABLE KEYS */;
INSERT INTO `u_collet` VALUES (1,'bp100','85.00',NULL),(2,'BP150','170.00',NULL),(3,'bp50','60.00',NULL),(4,'bp200','200.00',NULL),(5,NULL,NULL,NULL);
/*!40000 ALTER TABLE `u_collet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_customer`
--

DROP TABLE IF EXISTS `u_customer`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_customer` (
  `ID` int(11) NOT NULL auto_increment COMMENT '主键',
  `CREATE_NAME` varchar(50) default NULL COMMENT '创建人名称',
  `CREATE_BY` varchar(50) default NULL COMMENT '创建人登录名称',
  `CREATE_DATE` datetime default NULL COMMENT '创建日期',
  `UPDATE_NAME` varchar(50) default NULL COMMENT '更新人名称',
  `UPDATE_BY` varchar(50) default NULL COMMENT '更新人登录名称',
  `UPDATE_DATE` datetime default NULL COMMENT '更新日期',
  `SYS_ORG_CODE` varchar(50) default NULL COMMENT '所属部门',
  `SYS_COMPANY_CODE` varchar(50) default NULL COMMENT '所属公司',
  `CODE` varchar(32) default NULL COMMENT '客户编码',
  `NAME` varchar(32) default NULL COMMENT '客户名称',
  `TELPHONE` varchar(32) default NULL COMMENT '客户电话',
  `EMPLOYEEID` varchar(32) default NULL COMMENT '业务人员',
  `PROPERTIES` varchar(32) default NULL COMMENT '客户属性',
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_customer`
--

LOCK TABLES `u_customer` WRITE;
/*!40000 ALTER TABLE `u_customer` DISABLE KEYS */;
INSERT INTO `u_customer` VALUES (1,'管理员','admin','2017-04-09 19:19:13','','',NULL,'A02','A02','ggg','ttt','34343','8a8ab0b246dc81120146dc8181950052','新客户'),(2,' 尔哈','sal001','2017-04-28 09:31:10','','',NULL,'B02','B02','1445','就是要','1358476554','402882025b666efa015b667f18a50003','新客户'),(3,' 尔哈','sal001','2017-09-04 19:18:15','','',NULL,'B02','B02','李丽珊','雪山狼破镇','333333333','402882025b666efa015b667f18a50003','新客户'),(4,' 尔哈','sal001','2018-08-05 23:17:35','','',NULL,'B02','B02','拉大','达赖喇嘛','3333','402882025b666efa015b667f18a50003','新客户');
/*!40000 ALTER TABLE `u_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_flange1`
--

DROP TABLE IF EXISTS `u_flange1`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_flange1` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '型号：DN100',
  `texture` varchar(45) default NULL COMMENT '材质：碳钢',
  `class` varchar(45) default NULL COMMENT '规格：pn1.0,PN1.6',
  `price` decimal(9,2) default NULL,
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COMMENT='法兰-HG/T20592-09化工';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_flange1`
--

LOCK TABLES `u_flange1` WRITE;
/*!40000 ALTER TABLE `u_flange1` DISABLE KEYS */;
INSERT INTO `u_flange1` VALUES (1,'DN100','tan','16','46.80',NULL),(2,'DN150','tan','16','76.80',NULL);
/*!40000 ALTER TABLE `u_flange1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_flange2`
--

DROP TABLE IF EXISTS `u_flange2`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_flange2` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '型号：DN100',
  `texture` varchar(45) default NULL COMMENT '材质：碳钢',
  `class` varchar(45) default NULL COMMENT '规格：pn1.0,PN1.6',
  `price` decimal(9,2) default NULL,
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COMMENT='法兰-JB/T81-94国标';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_flange2`
--

LOCK TABLES `u_flange2` WRITE;
/*!40000 ALTER TABLE `u_flange2` DISABLE KEYS */;
INSERT INTO `u_flange2` VALUES (1,'DN100','tan','16','46.80',NULL),(2,'DN100','304','16','146.00',NULL),(3,'dn150','tan','16','96.00',NULL),(4,'dn150','304','16','241.00',NULL),(5,'dn50','tan','16','32.40',NULL),(6,'dn50','304','16','85.20',NULL),(7,'dn200','tan','16','120.00',NULL),(8,'dn200','304','16','367.20',NULL),(9,'dn250','tan','16','210.00',NULL),(10,'dn250','304','16','529.00',NULL),(11,'dn300','tan','16','260.40',NULL),(12,'dn300','304','16','660.00',NULL),(13,'dn350','tan','16','372.00',NULL),(14,'dn350','304','16','906.00',NULL);
/*!40000 ALTER TABLE `u_flange2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_formvalid`
--

--
-- Dumping data for table `u_formvalid`
--


--
-- Table structure for table `u_itemcase`
--

--
-- Dumping data for table `u_itemcase`
--

LOCK TABLES `u_itemcase` WRITE;
/*!40000 ALTER TABLE `u_itemcase` DISABLE KEYS */;
/*!40000 ALTER TABLE `u_itemcase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_items`
--

DROP TABLE IF EXISTS `u_items`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_items` (
  `id` int(20) NOT NULL auto_increment COMMENT '主键',
  `create_name` varchar(50) default NULL COMMENT '创建人名称',
  `create_by` varchar(50) default NULL COMMENT '创建人登录名称',
  `create_date` datetime default NULL COMMENT '创建日期',
  `update_name` varchar(50) default NULL COMMENT '更新人名称',
  `update_by` varchar(50) default NULL COMMENT '更新人登录名称',
  `update_date` datetime default NULL COMMENT '更新日期',
  `sys_org_code` varchar(50) default NULL COMMENT '所属部门',
  `sys_company_code` varchar(50) default NULL COMMENT '所属公司',
  `code` varchar(32) default NULL COMMENT '项目编号',
  `costomerid` int(32) default NULL COMMENT '客户',
  `itemname` varchar(32) default NULL COMMENT '项目名称',
  `employeeid` varchar(32) default NULL COMMENT '业务员',
  `itemcase` varchar(128) default NULL COMMENT '项目工况',
  `heatload` double(32,0) default NULL COMMENT '热负荷量',
  `area` double(32,0) default NULL COMMENT '采暖面积',
  `media1` varchar(32) default NULL COMMENT '一次测介质',
  `tempin1` double(32,0) default NULL COMMENT '一次测进温度',
  `tempout1` double(32,0) default NULL COMMENT '一次侧出温度',
  `media2` varchar(32) default NULL COMMENT '二次侧介质',
  `tempin2` double(32,0) default NULL COMMENT '二次侧进温度',
  `tempout2` double(32,0) default NULL COMMENT '二次侧出温度',
  `thetime` datetime default NULL COMMENT '询价时间',
  `itempro` int(32) default NULL COMMENT '项目进展',
  `teglock` varchar(8) default NULL COMMENT '技术锁',
  `flow1` double(32,0) default NULL COMMENT '一次侧流量',
  `flow2` double(32,0) default NULL COMMENT '二次侧流量',
  `tech` varchar(32) default NULL COMMENT '选型技术人员',
  `gaspressure` char(36) default NULL COMMENT '蒸汽压力',
  `notes` char(128) default '' COMMENT '备注',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_items`
--

LOCK TABLES `u_items` WRITE;
/*!40000 ALTER TABLE `u_items` DISABLE KEYS */;
INSERT INTO `u_items` VALUES (1,'管理员','admin','2016-11-21 19:31:35','','',NULL,'A03','A0','001',NULL,'大峡谷',NULL,'氟利昂,',3999,3000,'氟利昂',8,12,'水',30,20,NULL,NULL,'0',NULL,NULL,NULL,NULL,'2'),(2,'彭微涛','peng','2016-11-22 12:15:57','管理员','admin','2016-11-24 14:53:32','A02','A0','002',NULL,'天上人间',NULL,'10000平米采暖，水水，风机盘管,',2000,10000,'水',70,50,'水',40,50,NULL,NULL,'1',NULL,NULL,NULL,NULL,'2'),(5,'管理员','admin','2016-12-01 14:41:21','管理员','admin','2017-01-20 23:38:19','A03','A0','003',NULL,'马戏团','8a8ab0b246dc81120146dc8181950052','马槽加热',300,100,'水',50,30,'水',10,20,'2016-12-01 14:41:21',NULL,'2',NULL,NULL,'8a8ab0b246dc81120146dc8181950052',NULL,'2'),(7,'管理员','admin','2016-12-02 11:36:04','管理员','admin','2016-12-02 11:38:34','A03','A0','004',NULL,'恒基伟业换热机组','8a8ab0b246dc81120146dc8181950052','水水',2000,200,'水',70,50,'水',50,60,'2016-12-02 11:36:04',NULL,'1',NULL,NULL,NULL,NULL,'2'),(8,'管理员','admin','2016-12-10 00:16:42','','',NULL,'A03','A0','005',NULL,'马戏团','8a8ab0b246dc81120146dc8181950052','5555',55,55,'55',55,55,'55',55,55,'2016-12-10 00:16:16',NULL,'1',NULL,NULL,NULL,NULL,'2'),(9,'管理员','admin','2017-01-02 23:36:31','','',NULL,'A0001','A0','008',4,'7777','8a8ab0b246dc81120146dc8181950052','7777',777,77,'77',77,77,'77',77,77,'2017-01-02 23:35:08',NULL,'0',NULL,NULL,NULL,NULL,'2'),(10,'管理员','admin','2017-01-05 17:50:27','管理员','admin','2017-01-24 19:18:56','A0001','A0','005',5,'雾霾天气冰块出门','8a8ab0b246dc81120146dc8181950052','33232',32332,333,'3232',3232,3232,'3232',3232,3232,'2017-01-05 17:50:27',NULL,'2',3232,3232,'8a8ab0b246dc81120146dc8181950052',NULL,'2'),(11,'管理员','admin','2017-02-07 18:28:25','','',NULL,'A0001','A0','007',4,' 新年快乐了','8a8ab0b246dc81120146dc8181950052','为新年家装换热器',33,33,'33',33,33,'33',33,33,'2017-02-07 18:28:25',NULL,'0',33,33,NULL,NULL,'2'),(12,'彭微涛','peng','2017-02-20 23:06:52','','',NULL,'A0003','A0','333',7,'3333','4028838a5865a97b015865ba09500019','444',44,444,'44',44,44,'44',44,44,'2017-02-20 23:06:04',NULL,'0',44,44,NULL,NULL,'2'),(13,'管理员','admin','2017-04-09 22:38:36','','',NULL,'A02','A02','球球',1,'qqqq','8a8ab0b246dc81120146dc8181950052','qqqq',22,2222,'222',22,22,'22',22,22,'2017-04-09 22:31:29',NULL,'0',22,22,NULL,NULL,'2'),(14,'管理员','admin','2017-04-09 22:46:11','','',NULL,'A02','A02','娃娃娃娃',1,'wwww','8a8ab0b246dc81120146dc8181950052','wwww',4444,4444,'4444',4444,4444,'4444',4444,4444,'2017-04-09 22:46:03',NULL,'0',4444,4444,NULL,NULL,'2'),(15,' 尔哈','sal001','2017-04-28 09:35:42','刘霞穿','tec001','2017-05-12 23:07:38','B02','B02','002',2,'苏州服务器文房','402882025b666efa015b667f18a50003','a11',345,1111,'3',3,3,'3',3,3,'2017-04-28 09:35:42',NULL,'1',3,3,'402882025bb1eb80015bb211fbb90003',NULL,'2'),(16,'管理员','admin','2017-04-28 11:01:08','','',NULL,'A02','A02','',1,'','8a8ab0b246dc81120146dc8181950052','',NULL,NULL,'',4,5,'',4,5,'2017-04-28 11:01:08',NULL,'0',NULL,NULL,NULL,NULL,'2'),(17,' 尔哈','sal001','2017-05-12 23:15:11','刘霞穿','tec001','2017-05-13 00:32:00','B02','B02','33',2,'rr','402882025b666efa015b667f18a50003','ff',552,333,'s',32,56,'s',32,78,'2017-05-12 23:15:11',NULL,'2',23,23,'402882025bb1eb80015bb211fbb90003',NULL,'2'),(18,' 尔哈','sal001','2017-05-15 22:25:33',' 尔哈','sal001','2017-05-15 23:07:27','B02','B02','222r',2,'馒头太硬了','402882025b666efa015b667f18a50003','dd得到',43,343,'44',44,44,'44',44,444,'2017-05-15 22:25:33',NULL,'1',44,44,'402882025b666efa015b667f18a50003',NULL,'2'),(19,' 尔哈','sal001','2017-06-21 19:26:49','','',NULL,'B02','B02','33',2,'西红柿熟了','402882025b666efa015b667f18a50003','得到3等候',45,43,'9',23,34,'8',56,45,'2017-06-21 19:26:49',NULL,'0',12,67,NULL,'67','2'),(20,' 尔哈','sal001','2017-07-21 22:10:42','','',NULL,'B02','B02','112',2,'112','402882025b666efa015b667f18a50003','112',12,12,'12',12,12,'12',12,122,'2017-07-21 22:10:42',NULL,'0',122,212,NULL,'121212','2'),(21,' 尔哈','sal001','2017-07-21 22:43:48','','',NULL,'B02','B02','444',2,'44','402882025b666efa015b667f18a50003','444',44,44,'444',34,43,'44',44,443,'2017-07-21 22:43:48',NULL,'0',443,44,NULL,'44','4444');
/*!40000 ALTER TABLE `u_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_message`
--

DROP TABLE IF EXISTS `u_message`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_message` (
  `id` bigint(20) NOT NULL auto_increment,
  `create_name` varchar(50) default NULL COMMENT '创建人名称',
  `create_by` varchar(50) default NULL COMMENT '创建人登录名称',
  `create_date` datetime default NULL COMMENT '创建日期',
  `update_name` varchar(50) default NULL COMMENT '更新人名称',
  `update_by` varchar(50) default NULL COMMENT '更新人登录名称',
  `update_date` datetime default NULL COMMENT '更新日期',
  `sys_org_code` varchar(50) default NULL COMMENT '所属部门',
  `sys_company_code` varchar(50) default NULL COMMENT '所属公司',
  `msgtext` varchar(64) default NULL COMMENT '消息文本',
  `thedate` datetime default NULL COMMENT '消息时间',
  `msgmaster` varchar(32) default NULL COMMENT '消息主动人',
  `msgslave` varchar(32) default NULL COMMENT '消息从动人',
  `itemid` int(11) default NULL COMMENT '项目id',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_message`
--

-- Table structure for table `u_package`
--

DROP TABLE IF EXISTS `u_package`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_package` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '包装型号',
  `area` decimal(5,3) default NULL COMMENT '换热器面积',
  `price` decimal(8,2) default NULL,
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='包装箱\r\n';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_package`
--

LOCK TABLES `u_package` WRITE;
/*!40000 ALTER TABLE `u_package` DISABLE KEYS */;
/*!40000 ALTER TABLE `u_package` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_price`
--

DROP TABLE IF EXISTS `u_price`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_price` (
  `sheet_id` int(11) NOT NULL,
  `texture_id` int(11) NOT NULL,
  `thinkness_id` int(11) NOT NULL,
  `price` decimal(9,2) default NULL,
  PRIMARY KEY  (`sheet_id`,`texture_id`,`thinkness_id`),
  KEY `fk_price_sheet_idx` (`sheet_id`),
  KEY `fk_price_texture1_idx` (`texture_id`),
  KEY `fk_price_thinkness1_idx` (`thinkness_id`),
  CONSTRAINT `fk_price_sheet` FOREIGN KEY (`sheet_id`) REFERENCES `u_sheet` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_price_texture1` FOREIGN KEY (`texture_id`) REFERENCES `u_texture` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_price_thinkness1` FOREIGN KEY (`thinkness_id`) REFERENCES `u_thinkness` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='报价';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_price`
--

LOCK TABLES `u_price` WRITE;
/*!40000 ALTER TABLE `u_price` DISABLE KEYS */;
INSERT INTO `u_price` VALUES (1,1,1,'488.75'),(2,1,1,'437.00'),(3,1,1,'460.00'),(4,1,1,'391.00'),(5,1,1,'425.50'),(6,1,1,'368.00');
/*!40000 ALTER TABLE `u_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_sheet`
--

DROP TABLE IF EXISTS `u_sheet`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_sheet` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(45) default NULL COMMENT '板型',
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `type_UNIQUE` (`type`),
  KEY `index2` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='板片';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_sheet`
--

LOCK TABLES `u_sheet` WRITE;
/*!40000 ALTER TABLE `u_sheet` DISABLE KEYS */;
INSERT INTO `u_sheet` VALUES (1,'BP32',NULL),(2,'BP50B',NULL),(3,'BP50M',NULL),(4,'BP100B',NULL),(5,'BP100M',NULL),(6,'BP150B',NULL),(7,'BP150M',NULL),(8,'BP200B',NULL),(9,'BP200M',NULL),(10,'BP250B',NULL),(11,'BP350B',NULL),(12,'BS150M',NULL),(13,'BS150',NULL),(14,'BS200M',NULL),(15,'BS200',NULL),(16,'BT65',NULL),(17,'BT200',NULL);
/*!40000 ALTER TABLE `u_sheet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_sheetarear`
--

DROP TABLE IF EXISTS `u_sheetarear`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_sheetarear` (
  `id` int(11) NOT NULL auto_increment COMMENT '单板面积',
  `sheet` char(16) default NULL COMMENT '板片型号',
  `arear` double(16,4) default NULL COMMENT '面积',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_sheetarear`
--

LOCK TABLES `u_sheetarear` WRITE;
/*!40000 ALTER TABLE `u_sheetarear` DISABLE KEYS */;
INSERT INTO `u_sheetarear` VALUES (1,'BP50',0.1400),(2,'BP100',0.2400),(3,'BP32',0.0140),(4,'BP150',0.6200),(5,'BP200',0.8500);
/*!40000 ALTER TABLE `u_sheetarear` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_splint`
--

DROP TABLE IF EXISTS `u_splint`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_splint` (
  `id` int(11) NOT NULL auto_increment,
  `type` varchar(16) default NULL COMMENT '类型：BP150',
  `pressure` varchar(45) default NULL COMMENT '承压：16,25',
  `classmin` smallint(8) default NULL COMMENT '规格：最少板片数',
  `classmax` smallint(8) default NULL COMMENT '最大板片数',
  `price` decimal(8,2) default NULL,
  `pic` varchar(128) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8 COMMENT='夹板';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_splint`
--

LOCK TABLES `u_splint` WRITE;
/*!40000 ALTER TABLE `u_splint` DISABLE KEYS */;
INSERT INTO `u_splint` VALUES (1,'BP32','16',1,50,'650.00',NULL),(2,'BP50','16',1,50,'1800.00',NULL),(3,'BP50','16',50,100,'1950.00',NULL),(4,'BP50','16',100,150,'2100.00',NULL),(5,'BP50','16',150,200,'2250.00',NULL),(6,'BP100','16',100,150,'3600.00',NULL),(7,'BP150','16',1,50,'7000.00',NULL),(8,'BP150','16',50,100,'7500.00',NULL),(9,'BP100','16',1,50,'3000.00',NULL),(10,'BP100','16',50,100,'3300.00',NULL),(11,'BP100','16',150,200,'4000.00',NULL),(12,'BP100','16',200,300,'4500.00',NULL),(13,'BP150','16',100,150,'8000.00',NULL),(14,'BP150','16',150,200,'8500.00',NULL),(15,'BP150','16',200,300,'9000.00',NULL),(16,'BP200','16',50,100,'13500.00',NULL),(17,'BP200','16',100,150,'14500.00',NULL),(18,'BP200','16',150,200,'15500.00',NULL),(19,'BP200','16',200,300,'16500.00',NULL),(20,'BP200','16',300,1000,'17500.00',NULL),(21,'BP250','10',50,100,'26000.00',NULL),(22,'BP250','10',100,150,'27000.00',NULL),(23,'BP250','10',150,200,'28000.00',NULL),(24,'BP250','10',200,300,'30000.00',NULL),(25,'BP250','10',300,9999,'32000.00',NULL),(26,'BP250','16',50,100,'29000.00',NULL),(27,'BP250','16',100,150,'30000.00',NULL),(28,'BP250','16',150,200,'31000.00',NULL),(29,'BP250','16',200,300,'33000.00',NULL),(30,'BP250','16',300,9999,'35000.00',NULL),(31,'BP350','10',50,100,'41000.00',NULL),(32,'BP350','10',100,150,'42000.00',NULL),(33,'BP350','10',150,200,'43000.00',NULL),(34,'BP350','10',200,300,'45000.00',NULL),(35,'BP350','10',300,9999,'47000.00',NULL),(36,'BP350','16',50,100,'45000.00',NULL),(37,'BP350','16',100,150,'46000.00',NULL),(38,'BP350','16',150,200,'47000.00',NULL),(39,'BP350','16',200,300,'49000.00',NULL),(40,'BP350','16',300,9999,'51000.00',NULL),(41,'BS150','16',1,50,'6000.00',NULL),(42,'BS150','16',50,100,'65000.00',NULL),(43,'BS150','16',100,150,'7000.00',NULL),(44,'BS150','16',150,200,'7500.00',NULL),(45,'BS150','16',200,300,'8000.00',NULL),(46,'BS200','16',1,50,'8000.00',NULL),(47,'BS200','16',50,100,'8500.00',NULL),(48,'BS200','16',100,150,'9000.00',NULL),(49,'BS200','16',150,200,'9500.00',NULL),(50,'BS200','16',200,300,'10000.00',NULL),(51,'BT65','16',1,50,'1600.00',NULL),(52,'BT65','16',50,100,'1800.00',NULL),(53,'BT65','16',100,150,'2000.00',NULL),(54,'BT65','16',150,200,'2200.00',NULL),(55,'BT65','16',200,300,'2500.00',NULL),(56,'BT300','16',1,50,'6000.00',NULL),(57,'BT300','16',50,100,'6500.00',NULL),(58,'BT300','16',100,150,'7000.00',NULL),(59,'BT300','16',150,200,'7500.00',NULL),(60,'BT300','16',200,300,'8000.00',NULL),(61,'BL80','5',1,50,'17000.00',NULL),(62,'BL80','5',50,100,'17500.00',NULL),(63,'BL80','5',100,150,'18000.00',NULL),(64,'BL80','5',150,200,'18500.00',NULL);
/*!40000 ALTER TABLE `u_splint` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_texture`
--

DROP TABLE IF EXISTS `u_texture`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_texture` (
  `id` int(11) NOT NULL auto_increment,
  `texture` varchar(45) default NULL COMMENT '材质',
  `about` varchar(256) default NULL COMMENT '材质简介',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `texture_UNIQUE` (`texture`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='材质';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_texture`
--

LOCK TABLES `u_texture` WRITE;
/*!40000 ALTER TABLE `u_texture` DISABLE KEYS */;
INSERT INTO `u_texture` VALUES (1,'304',NULL),(2,'316',NULL),(3,'ni','镍材'),(4,'tai','钛材'),(5,'316L',NULL);
/*!40000 ALTER TABLE `u_texture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `u_thinkness`
--

DROP TABLE IF EXISTS `u_thinkness`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
CREATE TABLE `u_thinkness` (
  `id` int(11) NOT NULL auto_increment,
  `thinkness` decimal(4,2) default NULL COMMENT '板片厚度',
  `about` varchar(128) default NULL COMMENT '简介',
  PRIMARY KEY  (`id`),
  UNIQUE KEY `thinkness_UNIQUE` (`thinkness`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='板片厚度';
SET character_set_client = @saved_cs_client;

--
-- Dumping data for table `u_thinkness`
--

LOCK TABLES `u_thinkness` WRITE;
/*!40000 ALTER TABLE `u_thinkness` DISABLE KEYS */;
INSERT INTO `u_thinkness` VALUES (1,'0.50',NULL),(2,'0.60',NULL),(3,'0.70',NULL);
/*!40000 ALTER TABLE `u_thinkness` ENABLE KEYS */;
UNLOCK TABLES;

 
DROP TABLE IF EXISTS `u_pipeline`;
CREATE TABLE `u_pipeline` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(16) DEFAULT NULL COMMENT '板型',
  `texture` varchar(16) DEFAULT NULL COMMENT '接管材质，碳钢304316',
  `about` varchar(128) DEFAULT NULL COMMENT '简介',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `u_pipeline` WRITE;
/*!40000 ALTER TABLE `u_pipeline` DISABLE KEYS */;
/*!40000 ALTER TABLE `u_pipeline` ENABLE KEYS */;
UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-07 16:12:10

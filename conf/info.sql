-- MySQL dump 10.13  Distrib 5.6.46, for Linux (x86_64)
--
-- Host: localhost    Database: windit_test
-- ------------------------------------------------------
-- Server version	5.6.46

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
-- Current Database: `windit_test`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `windit_test` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `windit_test`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add content type',3,'add_contenttype'),(10,'Can change content type',3,'change_contenttype'),(11,'Can delete content type',3,'delete_contenttype'),(12,'Can view content type',3,'view_contenttype'),(13,'Can add session',4,'add_session'),(14,'Can change session',4,'change_session'),(15,'Can delete session',4,'delete_session'),(16,'Can view session',4,'view_session'),(17,'Can add User Widget',5,'add_userwidget'),(18,'Can change User Widget',5,'change_userwidget'),(19,'Can delete User Widget',5,'delete_userwidget'),(20,'Can view User Widget',5,'view_userwidget'),(21,'Can add User Setting',6,'add_usersettings'),(22,'Can change User Setting',6,'change_usersettings'),(23,'Can delete User Setting',6,'delete_usersettings'),(24,'Can view User Setting',6,'view_usersettings'),(25,'Can add log entry',7,'add_log'),(26,'Can change log entry',7,'change_log'),(27,'Can delete log entry',7,'delete_log'),(28,'Can view log entry',7,'view_log'),(29,'Can add Bookmark',8,'add_bookmark'),(30,'Can change Bookmark',8,'change_bookmark'),(31,'Can delete Bookmark',8,'delete_bookmark'),(32,'Can view Bookmark',8,'view_bookmark'),(33,'Can add 系统设置',9,'add_systemsetup'),(34,'Can change 系统设置',9,'change_systemsetup'),(35,'Can delete 系统设置',9,'delete_systemsetup'),(36,'Can view 系统设置',9,'view_systemsetup'),(37,'Can add 发件邮箱设置',10,'add_emailsetup'),(38,'Can change 发件邮箱设置',10,'change_emailsetup'),(39,'Can delete 发件邮箱设置',10,'delete_emailsetup'),(40,'Can view 发件邮箱设置',10,'view_emailsetup'),(41,'Can add 组织架构',11,'add_structure'),(42,'Can change 组织架构',11,'change_structure'),(43,'Can delete 组织架构',11,'delete_structure'),(44,'Can view 组织架构',11,'view_structure'),(45,'Can add 用户信息',12,'add_userprofile'),(46,'Can change 用户信息',12,'change_userprofile'),(47,'Can delete 用户信息',12,'delete_userprofile'),(48,'Can view 用户信息',12,'view_userprofile'),(49,'Can add 工单信息',13,'add_workorder'),(50,'Can change 工单信息',13,'change_workorder'),(51,'Can delete 工单信息',13,'delete_workorder'),(52,'Can view 工单信息',13,'view_workorder'),(53,'Can add 执行记录',14,'add_workorderrecord'),(54,'Can change 执行记录',14,'change_workorderrecord'),(55,'Can delete 执行记录',14,'delete_workorderrecord'),(56,'Can view 执行记录',14,'view_workorderrecord'),(57,'Can add 菜单',15,'add_menu'),(58,'Can change 菜单',15,'change_menu'),(59,'Can delete 菜单',15,'delete_menu'),(60,'Can view 菜单',15,'view_menu'),(61,'Can add 角色',16,'add_role'),(62,'Can change 角色',16,'change_role'),(63,'Can delete 角色',16,'delete_role'),(64,'Can view 角色',16,'view_role'),(65,'Can add 项目信息',17,'add_items'),(66,'Can change 项目信息',17,'change_items'),(67,'Can delete 项目信息',17,'delete_items'),(68,'Can view 项目信息',17,'view_items'),(69,'Can add 项目管理公司',18,'add_managerfirm'),(70,'Can change 项目管理公司',18,'change_managerfirm'),(71,'Can delete 项目管理公司',18,'delete_managerfirm'),(72,'Can view 项目管理公司',18,'view_managerfirm'),(73,'Can add 项目联系人',19,'add_itemlinkman'),(74,'Can change 项目联系人',19,'change_itemlinkman'),(75,'Can delete 项目联系人',19,'delete_itemlinkman'),(76,'Can view 项目联系人',19,'view_itemlinkman'),(77,'Can add 风场主机厂信息',20,'add_itemmanufacturer'),(78,'Can change 风场主机厂信息',20,'change_itemmanufacturer'),(79,'Can delete 风场主机厂信息',20,'delete_itemmanufacturer'),(80,'Can view 风场主机厂信息',20,'view_itemmanufacturer'),(81,'Can add 厂商',21,'add_manufacturer'),(82,'Can change 厂商',21,'change_manufacturer'),(83,'Can delete 厂商',21,'delete_manufacturer'),(84,'Can view 厂商',21,'view_manufacturer'),(85,'Can add 风电主机',22,'add_windpower'),(86,'Can change 风电主机',22,'change_windpower'),(87,'Can delete 风电主机',22,'delete_windpower'),(88,'Can view 风电主机',22,'view_windpower'),(89,'Can add 项目文件',23,'add_itemsfiles'),(90,'Can change 项目文件',23,'change_itemsfiles'),(91,'Can delete 项目文件',23,'delete_itemsfiles'),(92,'Can view 项目文件',23,'view_itemsfiles'),(93,'Can add 项目图片',24,'add_itemsimage'),(94,'Can change 项目图片',24,'change_itemsimage'),(95,'Can delete 项目图片',24,'delete_itemsimage'),(96,'Can view 项目图片',24,'view_itemsimage'),(97,'Can add 出行表',25,'add_itemtrip'),(98,'Can change 出行表',25,'change_itemtrip'),(99,'Can delete 出行表',25,'delete_itemtrip'),(100,'Can view 出行表',25,'view_itemtrip'),(101,'Can add 住宿表',26,'add_itemstay'),(102,'Can change 住宿表',26,'change_itemstay'),(103,'Can delete 住宿表',26,'delete_itemstay'),(104,'Can view 住宿表',26,'view_itemstay'),(105,'Can add 租车表',27,'add_itemcar'),(106,'Can change 租车表',27,'change_itemcar'),(107,'Can delete 租车表',27,'delete_itemcar'),(108,'Can view 租车表',27,'view_itemcar'),(109,'Can add 施工人员表',28,'add_itemexecutr'),(110,'Can change 施工人员表',28,'change_itemexecutr'),(111,'Can delete 施工人员表',28,'delete_itemexecutr'),(112,'Can view 施工人员表',28,'view_itemexecutr'),(113,'Can add 服务器信息',29,'add_itemserver'),(114,'Can change 服务器信息',29,'change_itemserver'),(115,'Can delete 服务器信息',29,'delete_itemserver'),(116,'Can view 服务器信息',29,'view_itemserver'),(117,'Can add CPU',30,'add_cpu'),(118,'Can change CPU',30,'change_cpu'),(119,'Can delete CPU',30,'delete_cpu'),(120,'Can view CPU',30,'view_cpu'),(121,'Can add 服务器图片',31,'add_serverimage'),(122,'Can change 服务器图片',31,'change_serverimage'),(123,'Can delete 服务器图片',31,'delete_serverimage'),(124,'Can view 服务器图片',31,'view_serverimage'),(125,'Can add 采集器信息',32,'add_itemfacility'),(126,'Can change 采集器信息',32,'change_itemfacility'),(127,'Can delete 采集器信息',32,'delete_itemfacility'),(128,'Can view 采集器信息',32,'view_itemfacility'),(129,'Can add 采集器类型',33,'add_facilitytype'),(130,'Can change 采集器类型',33,'change_facilitytype'),(131,'Can delete 采集器类型',33,'delete_facilitytype'),(132,'Can view 采集器类型',33,'view_facilitytype'),(133,'Can add 传感器信息',34,'add_itemsensor'),(134,'Can change 传感器信息',34,'change_itemsensor'),(135,'Can delete 传感器信息',34,'delete_itemsensor'),(136,'Can view 传感器信息',34,'view_itemsensor'),(137,'Can add 传感器类型',35,'add_sensortype'),(138,'Can change 传感器类型',35,'change_sensortype'),(139,'Can delete 传感器类型',35,'delete_sensortype'),(140,'Can view 传感器类型',35,'view_sensortype'),(141,'Can add item goods',36,'add_itemgoods'),(142,'Can change item goods',36,'change_itemgoods'),(143,'Can delete item goods',36,'delete_itemgoods'),(144,'Can view item goods',36,'view_itemgoods'),(145,'Can add goods image',37,'add_goodsimage'),(146,'Can change goods image',37,'change_goodsimage'),(147,'Can delete goods image',37,'delete_goodsimage'),(148,'Can view goods image',37,'view_goodsimage'),(149,'Can add 人员情况',38,'add_personnel'),(150,'Can change 人员情况',38,'change_personnel'),(151,'Can delete 人员情况',38,'delete_personnel'),(152,'Can view 人员情况',38,'view_personnel'),(153,'Can add 工作日志',39,'add_worklog'),(154,'Can change 工作日志',39,'change_worklog'),(155,'Can delete 工作日志',39,'delete_worklog'),(156,'Can view 工作日志',39,'view_worklog');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'auth','group'),(1,'auth','permission'),(3,'contenttypes','contenttype'),(13,'personal','workorder'),(14,'personal','workorderrecord'),(30,'PMsys','cpu'),(33,'PMsys','facilitytype'),(37,'PMsys','goodsimage'),(27,'PMsys','itemcar'),(28,'PMsys','itemexecutr'),(32,'PMsys','itemfacility'),(36,'PMsys','itemgoods'),(19,'PMsys','itemlinkman'),(20,'PMsys','itemmanufacturer'),(17,'PMsys','items'),(34,'PMsys','itemsensor'),(29,'PMsys','itemserver'),(23,'PMsys','itemsfiles'),(24,'PMsys','itemsimage'),(26,'PMsys','itemstay'),(25,'PMsys','itemtrip'),(18,'PMsys','managerfirm'),(21,'PMsys','manufacturer'),(38,'PMsys','personnel'),(35,'PMsys','sensortype'),(31,'PMsys','serverimage'),(22,'PMsys','windpower'),(39,'PMsys','worklog'),(15,'rbac','menu'),(16,'rbac','role'),(4,'sessions','session'),(10,'system','emailsetup'),(9,'system','systemsetup'),(11,'users','structure'),(12,'users','userprofile'),(8,'xadmin','bookmark'),(7,'xadmin','log'),(6,'xadmin','usersettings'),(5,'xadmin','userwidget');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-06 02:18:04.496218'),(2,'contenttypes','0002_remove_content_type_name','2020-03-06 02:18:04.549359'),(3,'auth','0001_initial','2020-03-06 02:18:04.592914'),(4,'auth','0002_alter_permission_name_max_length','2020-03-06 02:18:04.670164'),(5,'auth','0003_alter_user_email_max_length','2020-03-06 02:18:04.677172'),(6,'auth','0004_alter_user_username_opts','2020-03-06 02:18:04.685193'),(7,'auth','0005_alter_user_last_login_null','2020-03-06 02:18:04.693251'),(8,'auth','0006_require_contenttypes_0002','2020-03-06 02:18:04.695251'),(9,'auth','0007_alter_validators_add_error_messages','2020-03-06 02:18:04.702239'),(10,'auth','0008_alter_user_username_max_length','2020-03-06 02:18:04.708309'),(11,'auth','0009_alter_user_last_name_max_length','2020-03-06 02:18:04.715302'),(12,'auth','0010_alter_group_name_max_length','2020-03-06 02:18:04.734325'),(13,'auth','0011_update_proxy_permissions','2020-03-06 02:18:04.759392'),(14,'rbac','0001_initial','2020-03-06 02:18:04.798032'),(15,'rbac','0002_remove_role_permissions','2020-03-06 02:18:04.858660'),(16,'rbac','0003_role_permissions','2020-03-06 02:18:04.873620'),(17,'sessions','0001_initial','2020-03-06 02:18:04.921966'),(18,'system','0001_initial','2020-03-06 02:18:04.944025'),(19,'system','0002_emailsetup','2020-03-06 02:18:04.959572'),(20,'system','0003_auto_20200206_0945','2020-03-06 02:18:04.968198'),(21,'users','0001_initial','2020-03-06 02:18:05.027344'),(22,'users','0002_userprofile_roles','2020-03-06 02:18:05.225848'),(23,'users','0003_auto_20200206_0931','2020-03-06 02:18:05.273242'),(24,'xadmin','0001_initial','2020-03-06 02:18:05.360354');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('86gwjxvzv1p0lz5dz3w8mp7ngv4y3s2g','OTEyZjY5N2QwNzlmNjJhNDU5Yzc2NWJhY2FhZWIyYmM0ZWIyOGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgifQ==','2020-04-29 09:38:49.767456'),('9r0i4nkomw9hzpx1wuxrxyuc19esv4vi','OTEyZjY5N2QwNzlmNjJhNDU5Yzc2NWJhY2FhZWIyYmM0ZWIyOGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgifQ==','2020-03-26 07:21:11.249415'),('axj2rcpc00vevkbnnrtpa9l4n4jkuvil','OTEyZjY5N2QwNzlmNjJhNDU5Yzc2NWJhY2FhZWIyYmM0ZWIyOGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgifQ==','2020-04-29 09:40:14.068228'),('dev9oavtx8ckq9di4co6ix5kjgv8cf15','OTEyZjY5N2QwNzlmNjJhNDU5Yzc2NWJhY2FhZWIyYmM0ZWIyOGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgifQ==','2020-03-26 07:16:26.677025'),('g09jc54caaqlf4hnab7jp53m10mfvlx6','YTU4MDcwMDBlNTY2NTM2YjAwNjg1OGY1MGY0NzU4NzA0ZGIxYmIxMDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgiLCJMSVNUX1FVRVJZIjpbWyJyYmFjIiwicm9sZSJdLCIiXX0=','2020-03-26 07:23:14.433303'),('gpaww0778gv0s7hw4xs7zwlxs2okthxh','OTEyZjY5N2QwNzlmNjJhNDU5Yzc2NWJhY2FhZWIyYmM0ZWIyOGQ3MDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgifQ==','2020-04-29 09:41:50.133758'),('hybkb2dxoprq2xgpu44in53ksshcgc3e','MTlhNmU5OTAyYWE5YTM0MGRhYzJmYzhiMzg4OTE1MzU5MmNkNzg2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgiLCJMSVNUX1FVRVJZIjpbWyJyYmFjIiwibWVudSJdLCIiXX0=','2020-03-20 02:24:01.810947'),('pp86u2uo2hx1ny8ey96h8lwwfok5s4mm','YjFkYjkxNGEzMDAyMWY5NjE1NWM0OTU4OWNlM2MxNDgzNDkyY2Q1Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoidXNlcnMudmlld3NfdXNlci5Vc2VyQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjMyOTk1ZTU2OTI2YjFiYTVmNGQ3ZTM3YWU2YzIzZmQyNTZmZWRlNzgiLCJzdGF0dXMiOm51bGx9','2020-03-20 02:24:14.529786');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_menu`
--

DROP TABLE IF EXISTS `rbac_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `icon` varchar(50) DEFAULT NULL,
  `code` varchar(50) DEFAULT NULL,
  `url` varchar(128) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  KEY `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` (`parent_id`),
  CONSTRAINT `rbac_menu_parent_id_60a5b178_fk_rbac_menu_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_menu`
--

LOCK TABLES `rbac_menu` WRITE;
/*!40000 ALTER TABLE `rbac_menu` DISABLE KEYS */;
INSERT INTO `rbac_menu` VALUES (1,'系统',1,NULL,'SYSTEM','/system/',NULL),(2,'我的工作台',0,NULL,'PERSONAL','/personal/',NULL),(3,'基本设置',0,'fas fa-clone','SYSTEM-BASIC',NULL,1),(4,'权限管理',0,'fas fa-clone','SYSTEM-RBAC',NULL,1),(5,'系统工具',0,'fas fa-clone','SYSTEM-TOOLS',NULL,1),(6,'菜单管理',0,NULL,'SYSTEM-RBAC-MENU','/system/rbac/menu/',4),(7,'角色管理',0,NULL,'SYSTEM-RBAC-ROLE','/system/rbac/role/',4),(8,'菜单管理：列表',0,NULL,'SYSTEM-RBAC-MENU-LIST','/system/rbac/menu/list',6),(9,'菜单管理：详情修改',0,NULL,'SYSTEM-RBAC-MENU-DETAIL','/system/rbac/menu/detail',6),(10,'工程信息平台',1,NULL,'PROJECT','/project/',NULL),(11,'项目总览',0,'icon-zonglan','PROJECT-OVER','/project/pro_over/',10),(12,'项目列表',0,'fas icon-liebiao','PROJECT-LIST','/project/pro_list/',10),(13,'新项目录入',0,'fas icon-jia','PROJECT-NEW','/project/new_pro/',10),(14,'用户管理',0,NULL,'SYSTEM-BASIC-USER','/system/basic/user/',3),(15,'组织构架',0,NULL,'SYSTEM-BASIC-STRUCTURE','/syste/basic/structure/',3),(16,'工作日志',0,'icon-wodegongzuorizhi','PROJECT-WORKLOG','/project/work_log/',10),(17,'项目列表：服务器信息',0,NULL,NULL,'/project/pro_list/show/server/',12),(18,'资源管理',0,'icon-lianxiren','PROJECT-FACILITIES','/project/facilities/',10);
/*!40000 ALTER TABLE `rbac_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role`
--

DROP TABLE IF EXISTS `rbac_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role`
--

LOCK TABLES `rbac_role` WRITE;
/*!40000 ALTER TABLE `rbac_role` DISABLE KEYS */;
INSERT INTO `rbac_role` VALUES (1,'系统'),(2,'测试用户');
/*!40000 ALTER TABLE `rbac_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rbac_role_permissions`
--

DROP TABLE IF EXISTS `rbac_role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rbac_role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rbac_role_permissions_role_id_menu_id_8ba9f835_uniq` (`role_id`,`menu_id`),
  KEY `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` (`menu_id`),
  CONSTRAINT `rbac_role_permissions_menu_id_bb73fb9a_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`),
  CONSTRAINT `rbac_role_permissions_role_id_d10416cb_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rbac_role_permissions`
--

LOCK TABLES `rbac_role_permissions` WRITE;
/*!40000 ALTER TABLE `rbac_role_permissions` DISABLE KEYS */;
INSERT INTO `rbac_role_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(14,1,10),(15,1,11),(12,1,12),(13,1,13),(21,1,14),(22,1,15),(23,1,16),(24,1,17),(25,1,18),(20,2,10),(17,2,11),(18,2,12),(19,2,13);
/*!40000 ALTER TABLE `rbac_role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_emailsetup`
--

DROP TABLE IF EXISTS `system_emailsetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_emailsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emailHost` varchar(30) NOT NULL,
  `emailPort` int(11) NOT NULL,
  `emailUser` varchar(100) NOT NULL,
  `emailPassword` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_emailsetup`
--

LOCK TABLES `system_emailsetup` WRITE;
/*!40000 ALTER TABLE `system_emailsetup` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_emailsetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_systemsetup`
--

DROP TABLE IF EXISTS `system_systemsetup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `system_systemsetup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `loginTitle` varchar(20) DEFAULT NULL,
  `mainTitle` varchar(20) DEFAULT NULL,
  `headTitle` varchar(20) DEFAULT NULL,
  `copyright` varchar(100) DEFAULT NULL,
  `url` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_systemsetup`
--

LOCK TABLES `system_systemsetup` WRITE;
/*!40000 ALTER TABLE `system_systemsetup` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_systemsetup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_structure`
--

DROP TABLE IF EXISTS `users_structure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_structure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(60) NOT NULL,
  `type` varchar(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `users_structure_parent_id_e73fd647_fk_users_structure_id` (`parent_id`),
  CONSTRAINT `users_structure_parent_id_e73fd647_fk_users_structure_id` FOREIGN KEY (`parent_id`) REFERENCES `users_structure` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_structure`
--

LOCK TABLES `users_structure` WRITE;
/*!40000 ALTER TABLE `users_structure` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_structure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile`
--

DROP TABLE IF EXISTS `users_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  `birthday` date DEFAULT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `joined_date` date DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL,
  `superior_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `users_userprofile_department_id_b060d851_fk_users_structure_id` (`department_id`),
  KEY `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` (`superior_id`),
  CONSTRAINT `users_userprofile_department_id_b060d851_fk_users_structure_id` FOREIGN KEY (`department_id`) REFERENCES `users_structure` (`id`),
  CONSTRAINT `users_userprofile_superior_id_3869391f_fk_users_userprofile_id` FOREIGN KEY (`superior_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile`
--

LOCK TABLES `users_userprofile` WRITE;
/*!40000 ALTER TABLE `users_userprofile` DISABLE KEYS */;
INSERT INTO `users_userprofile` VALUES (1,'pbkdf2_sha256$150000$Wm448xCs9H7N$bfvHZbtz0rMaOp4GUKmCa6qs4imrm/zkPoGWWrIhRmQ=','2020-04-15 09:41:50.130697',1,'admin','','','zhouwx@windit.com.cn',1,1,'2020-02-21 05:58:00.000000','周凡',NULL,'male','18167000916','image/default.jpg',NULL,NULL,NULL,NULL),(2,'pbkdf2_sha256$150000$V5AqCmOG0zGS$db/749O0HJ9WIOcxAwl+ocFx+0noGgLcw4NAOBm4iJQ=','2020-02-28 03:57:00.000000',0,'test1','','','',1,1,'2020-02-28 03:50:00.000000','测试用户1',NULL,'male','12345678912','image/default.jpg',NULL,NULL,NULL,NULL),(3,'pbkdf2_sha256$150000$UHG5ER1JmgG3$l4rS9Mu89mz5oL0u+yxYCRYCk1nAChdD0+8cBo/wLAI=',NULL,0,'test2','','','',1,1,'2020-03-02 05:28:00.000000','测试用户2',NULL,'male','12345678912','image/default.jpg',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_groups`
--

DROP TABLE IF EXISTS `users_userprofile_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_group_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_gr_userprofile_id_a4496a80_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_groups`
--

LOCK TABLES `users_userprofile_groups` WRITE;
/*!40000 ALTER TABLE `users_userprofile_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_roles`
--

DROP TABLE IF EXISTS `users_userprofile_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_roles_userprofile_id_role_id_81c255df_uniq` (`userprofile_id`,`role_id`),
  KEY `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` (`role_id`),
  CONSTRAINT `users_userprofile_ro_userprofile_id_ae49de2a_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `users_userprofile_roles_role_id_740e5521_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_roles`
--

LOCK TABLES `users_userprofile_roles` WRITE;
/*!40000 ALTER TABLE `users_userprofile_roles` DISABLE KEYS */;
INSERT INTO `users_userprofile_roles` VALUES (1,1,1),(3,2,2),(4,3,2);
/*!40000 ALTER TABLE `users_userprofile_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_userprofile_user_permissions`
--

DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_p_userprofile_id_permissio_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_us_permission_id_393136b6_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_userprofile_us_permission_id_393136b6_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofile_us_userprofile_id_34544737_fk_users_use` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_userprofile_user_permissions`
--

LOCK TABLES `users_userprofile_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_userprofile_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_bookmark`
--

DROP TABLE IF EXISTS `xadmin_bookmark`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookmark_content_type_id_60941679_fk_django_co` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_content_type_id_60941679_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_bookmark`
--

LOCK TABLES `xadmin_bookmark` WRITE;
/*!40000 ALTER TABLE `xadmin_bookmark` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_bookmark` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_log`
--

DROP TABLE IF EXISTS `xadmin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_log`
--

LOCK TABLES `xadmin_log` WRITE;
/*!40000 ALTER TABLE `xadmin_log` DISABLE KEYS */;
INSERT INTO `xadmin_log` VALUES (1,'2020-03-12 07:23:14.315726','127.0.0.1','1','系统','change','修改 permissions',16,1);
/*!40000 ALTER TABLE `xadmin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_usersettings`
--

DROP TABLE IF EXISTS `xadmin_usersettings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_usersettings`
--

LOCK TABLES `xadmin_usersettings` WRITE;
/*!40000 ALTER TABLE `xadmin_usersettings` DISABLE KEYS */;
INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1);
/*!40000 ALTER TABLE `xadmin_usersettings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xadmin_userwidget`
--

DROP TABLE IF EXISTS `xadmin_userwidget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xadmin_userwidget`
--

LOCK TABLES `xadmin_userwidget` WRITE;
/*!40000 ALTER TABLE `xadmin_userwidget` DISABLE KEYS */;
/*!40000 ALTER TABLE `xadmin_userwidget` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-15  9:46:07

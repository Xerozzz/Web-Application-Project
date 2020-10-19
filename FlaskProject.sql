CREATE DATABASE  IF NOT EXISTS `flask` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `flask`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: project-database.cokyaqjxq7d8.ap-southeast-1.rds.amazonaws.com    Database: flask
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `adminid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `hash` varchar(255) NOT NULL,
  PRIMARY KEY (`adminid`),
  UNIQUE KEY `adminid_UNIQUE` (`adminid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','pbkdf2:sha256:150000$hNlZ3u5a$e805c965f2f3db6d2fa7d7f22e5861db39361be137ff83f093785eaca66eae88');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `productid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `price` float(10,2) NOT NULL,
  `description` varchar(200) NOT NULL DEFAULT 'no description',
  `category` varchar(45) NOT NULL DEFAULT 'miscellaneous',
  PRIMARY KEY (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'A4 Paper 200pc',200.00,'it is just paperz','miscellaneous'),(2,'Stone 500g',200.00,'it is just some rocks','miscellaneous'),(3,'Printer Ink 100ml',999.00,'it is just ink','miscellaneous'),(4,'Water Bottle 1L',5.10,'it is just a bottle',''),(5,'Another test item',200.00,'II NEEEE','miscellaneous'),(7,'Test Item',200.12,'I LOVE YEET','Food'),(8,'III NEEEEEEEEEEEEEE',200.00,'GAY','Food');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `hash` varchar(255) NOT NULL,
  `email` varchar(45) NOT NULL,
  `about` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `userid_UNIQUE` (`userid`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (18,'chloe','pbkdf2:sha256:150000$CCgax1No$706b3cd01eaa607a42cb23b0f1b20b4d38a268de6177979c0542e075bee72344','chloe@gmail.com','hello chloe here','2020-10-12 07:57:48'),(19,'Xeroz','pbkdf2:sha256:150000$ThyIVt9h$f21971e4a7918ec0fd9b3761f464ea281a2891cced497bd15e7a8cc9488593ce','xeroz@gmail.com','heheheaaaa','2020-10-12 07:58:14'),(22,'testing','pbkdf2:sha256:150000$Zii9SJFz$38e4872354660ca20c4ecf31cbbd25955dddf1c83e4262eff71b2183f76ddf4f','testing@gmail.com','just a test','2020-10-12 09:34:40'),(25,'ethan','pbkdf2:sha256:150000$iflGkSeK$4f4beef5f36ca8080279dc82957986b065b9f3c8b7856ec29ba02bb8a947fa01','whats up ethana','yo ethan','2020-10-12 14:42:16'),(29,'test','pbkdf2:sha256:150000$MfhLCMQ9$03b948a90e6c9398e62795afb48001dba5f9634eb6fb2430b4ea64071f1d1478','TESSSSSS',NULL,'2020-10-18 03:52:33');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variations`
--

DROP TABLE IF EXISTS `variations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variations` (
  `idvariations` int NOT NULL AUTO_INCREMENT,
  `productid` int NOT NULL,
  `color` varchar(45) DEFAULT NULL,
  `size` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idvariations`),
  KEY `productid_idx` (`productid`),
  CONSTRAINT `productid` FOREIGN KEY (`productid`) REFERENCES `products` (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variations`
--

LOCK TABLES `variations` WRITE;
/*!40000 ALTER TABLE `variations` DISABLE KEYS */;
INSERT INTO `variations` VALUES (1,1,'blue','a'),(2,1,'red','b'),(5,1,'yellow','c');
/*!40000 ALTER TABLE `variations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'flask'
--

--
-- Dumping routines for database 'flask'
--
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-19 22:36:52

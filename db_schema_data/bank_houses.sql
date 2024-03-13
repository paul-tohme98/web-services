-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: bank
-- ------------------------------------------------------
-- Server version	8.0.33

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

--
-- Table structure for table `houses`
--

DROP TABLE IF EXISTS `houses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `houses` (
  `house_id` tinyint DEFAULT NULL,
  `address` varchar(17) DEFAULT NULL,
  `estimated_value` decimal(7,1) DEFAULT NULL,
  `area` decimal(5,1) DEFAULT NULL,
  `num_of_chambers` tinyint DEFAULT NULL,
  `inspected` tinyint DEFAULT NULL,
  `land_dispute` tinyint DEFAULT NULL,
  `complies_with_regulations` tinyint DEFAULT NULL,
  `eligible_for_loan` tinyint DEFAULT NULL,
  `region` varchar(5) DEFAULT NULL,
  `code_postal` mediumint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `houses`
--

LOCK TABLES `houses` WRITE;
/*!40000 ALTER TABLE `houses` DISABLE KEYS */;
INSERT INTO `houses` VALUES (1,'123 Elm Street',250000.0,2000.0,3,1,0,1,1,'North',12345),(2,'456 Oak Avenue',320000.0,2200.0,4,1,0,1,1,'South',54321),(3,'789 Maple Lane',280000.0,1800.0,3,1,0,1,1,'East',67890),(4,'101 Pine Avenue',210000.0,1600.0,2,1,0,1,1,'West',98765),(5,'222 Cedar Road',300000.0,2400.0,4,1,0,1,1,'North',11111),(6,'555 Birch Street',270000.0,2200.0,3,1,0,0,0,'South',22222),(7,'777 Willow Avenue',350000.0,2800.0,4,1,0,1,1,'East',33333),(8,'333 Spruce Lane',260000.0,1900.0,3,0,0,0,0,'West',44444),(9,'999 Redwood Road',400000.0,3200.0,5,1,0,1,1,'North',55555),(10,'444 Elm Street',295000.0,2500.0,4,1,0,1,1,'South',66666),(11,'123 Pine Avenue',180000.0,1500.0,2,1,1,0,0,'East',77777),(12,'555 Cedar Road',290000.0,2300.0,4,1,1,1,1,'West',88888),(13,'999 Birch Street',320000.0,2700.0,4,1,0,1,1,'North',99999),(14,'123 Willow Avenue',350000.0,2900.0,5,1,0,1,1,'South',0),(15,'456 Spruce Lane',265000.0,2000.0,3,0,0,0,0,'East',12345),(16,'789 Redwood Road',410000.0,3400.0,6,1,0,1,1,'North',54321),(17,'101 Elm Street',270000.0,2200.0,3,1,0,1,1,'South',67890),(18,'222 Oak Avenue',330000.0,2600.0,4,1,0,1,1,'East',98765),(19,'555 Maple Lane',290000.0,2300.0,4,1,0,1,1,'West',11111),(20,'777 Pine Avenue',220000.0,1900.0,3,0,0,0,0,'North',22222),(21,'223 Cedar Road',500000.0,2450.0,4,1,0,0,0,'North',11111);
/*!40000 ALTER TABLE `houses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-13  9:43:02

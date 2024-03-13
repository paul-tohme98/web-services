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
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clients` (
  `client_id` tinyint DEFAULT NULL,
  `name` varchar(16) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `telephone` varchar(15) DEFAULT NULL,
  `address` varchar(33) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
INSERT INTO `clients` VALUES (1,'John Doe','john@example.com','+1 123-456-7890','123 Main St, Anytown, USA'),(2,'Alice Johnson','alice@example.com','+1 987-654-3210','456 Elm Ave, Othercity, USA'),(3,'Bob Smith','bob@example.com','+1 555-123-4567','789 Oak Ln, Anothercity, USA'),(4,'Jane Wilson','jane@example.com','+1 777-888-9999','321 Maple Rd, Somewhere, USA'),(5,'Eva Brown','eva@example.com','+1 222-333-4444','555 Pine Dr, Anotherplace, USA'),(6,'David Lee','david@example.com','+1 666-777-8888','789 Cedar Rd, Yetanothercity, USA'),(7,'Olivia Taylor','olivia@example.com','+1 111-222-3333','432 Birch Ave, Townsville, USA'),(8,'Michael Miller','michael@example.com','+1 777-111-3333','987 Willow St, Outskirts, USA'),(9,'Sophia Davis','sophia@example.com','+1 333-555-7777','654 Spruce Ave, Countryside, USA'),(10,'William Anderson','william@example.com','+1 222-444-6666','123 Fir Rd, Hometown, USA'),(11,'Ava Wilson','ava@example.com','+1 444-555-6666','567 Redwood Dr, Suburbia, USA'),(12,'James Harris','james@example.com','+1 111-222-3333','890 Cherry Ln, Village, USA'),(13,'Emma White','emma@example.com','+1 888-777-6666','123 Elm St, Urbanville, USA'),(14,'Benjamin Turner','benjamin@example.com','+1 777-555-3333','555 Oak Ave, Cityville, USA'),(15,'Mia Moore','mia@example.com','+1 666-333-1111','333 Pine Rd, Metropolis, USA'),(16,'Logan Hall','logan@example.com','+1 555-333-1111','654 Birch Ln, Megacity, USA'),(17,'Emily Scott','emily@example.com','+1 444-222-1111','789 Cedar Dr, Gigatown, USA'),(18,'Daniel Parker','daniel@example.com','+1 333-222-1111','123 Maple Rd, Highriseville, USA'),(19,'Sofia Phillips','sofia@example.com','+1 222-111-4444','456 Oak Ave, Supercity, USA');
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
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

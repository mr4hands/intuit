/*
SQLyog Trial v13.1.5  (64 bit)
MySQL - 5.7.27 : Database - intuitest
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`intuitest` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `intuitest`;

/*Table structure for table `channels` */

DROP TABLE IF EXISTS `channels`;

CREATE TABLE `channels` (
  `id` int(255) NOT NULL AUTO_INCREMENT,
  `channel` varchar(200) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`,`channel`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `channels` */

insert  into `channels`(`id`,`channel`,`type`) values 
(1,'https://dratler.github.io/fake-bank/','website'),
(2,'https://qndxqxuz35.execute-api.us-west-2.amazonaws.com/senior-test','api');

/*Table structure for table `user_channel_transactions` */

DROP TABLE IF EXISTS `user_channel_transactions`;

CREATE TABLE `user_channel_transactions` (
  `user_id` bigint(20) NOT NULL,
  `channel` varchar(200) NOT NULL,
  `last_aggregation_date` datetime NOT NULL,
  `transactions_list` text NOT NULL,
  `balance` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`user_id`,`channel`),
  KEY `channel_id` (`channel`),
  CONSTRAINT `user_channel_transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_channel_transactions` */

/*Table structure for table `user_channels` */

DROP TABLE IF EXISTS `user_channels`;

CREATE TABLE `user_channels` (
  `user_id` bigint(20) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `balance` decimal(10,0) DEFAULT NULL,
  `currency` text,
  PRIMARY KEY (`user_id`,`channel_id`),
  KEY `user_id` (`user_id`),
  KEY `bank_id` (`channel_id`),
  CONSTRAINT `user_channels_ibfk_5` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_channels` */

insert  into `user_channels`(`user_id`,`channel_id`,`balance`,`currency`) values 
(61509949,1,NULL,NULL),
(61509949,2,NULL,NULL);

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`id`,`name`) values 
(61509949,'erez gilron');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

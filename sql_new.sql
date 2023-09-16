/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - canine
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`canine` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `canine`;

/*Table structure for table `accessories` */

DROP TABLE IF EXISTS `accessories`;

CREATE TABLE `accessories` (
  `A_id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `Photo` varchar(200) DEFAULT NULL,
  `Price` varchar(20) DEFAULT NULL,
  `Qty` int(11) DEFAULT NULL,
  `SHOP_ID` int(20) DEFAULT NULL,
  PRIMARY KEY (`A_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `accessories` */

insert  into `accessories`(`A_id`,`Name`,`Photo`,`Price`,`Qty`,`SHOP_ID`) values (1,'nest','/static/img/230119-230718.jpg','600',2,3);

/*Table structure for table `accessories booking` */

DROP TABLE IF EXISTS `accessories booking`;

CREATE TABLE `accessories booking` (
  `AB_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Shop_id` int(11) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Payment_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`AB_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `accessories booking` */

/*Table structure for table `add_to_cart` */

DROP TABLE IF EXISTS `add_to_cart`;

CREATE TABLE `add_to_cart` (
  `C_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `A_id` int(11) DEFAULT NULL,
  `Qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`C_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `add_to_cart` */

insert  into `add_to_cart`(`C_id`,`User_id`,`A_id`,`Qty`) values (1,4,1,1),(2,4,1,2),(3,4,1,2);

/*Table structure for table `breed` */

DROP TABLE IF EXISTS `breed`;

CREATE TABLE `breed` (
  `Breed_id` int(11) NOT NULL AUTO_INCREMENT,
  `Breed_name` varchar(20) DEFAULT NULL,
  `Breed_photo` varchar(200) DEFAULT NULL,
  `Breed_rate_from` varchar(20) DEFAULT NULL,
  `Breed_rate_to` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`Breed_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `breed` */

insert  into `breed`(`Breed_id`,`Breed_name`,`Breed_photo`,`Breed_rate_from`,`Breed_rate_to`) values (2,'germen shepherd','/static/img/230119-220721.jpg','2','2');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `Complaint` varchar(20) DEFAULT NULL,
  `Cdate` date DEFAULT NULL,
  `Reply` varchar(20) DEFAULT NULL,
  `Reply_date` date DEFAULT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Complaint_id`,`userid`,`Complaint`,`Cdate`,`Reply`,`Reply_date`) values (1,1,'rtdtgrx',NULL,'asdasf','2023-01-04');

/*Table structure for table `diseases` */

DROP TABLE IF EXISTS `diseases`;

CREATE TABLE `diseases` (
  `D_id` int(11) NOT NULL AUTO_INCREMENT,
  `Breed_id` int(11) DEFAULT NULL,
  `D_name` varchar(20) DEFAULT NULL,
  `Symptoms` varchar(20) DEFAULT NULL,
  `Solutions` varchar(20) DEFAULT NULL,
  `D_photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`D_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `diseases` */

insert  into `diseases`(`D_id`,`Breed_id`,`D_name`,`Symptoms`,`Solutions`,`D_photo`) values (1,1,'nn',NULL,NULL,NULL),(2,1,'','','','/static/img/230105-022618.jpg'),(3,1,'admin','admin','fv','/static/img/230105-022635.jpg'),(4,1,'vishnu','fur lose','asas','/static/img/230105-022808.jpg'),(5,1,'admin','iyg','tfh','/static/img/230105-022922.jpg'),(6,1,'d','dsf','sfdf','/static/img/230105-023005.jpg');

/*Table structure for table `food` */

DROP TABLE IF EXISTS `food`;

CREATE TABLE `food` (
  `Food_id` int(11) NOT NULL AUTO_INCREMENT,
  `Breed_id` int(11) DEFAULT NULL,
  `Food_name` varchar(20) DEFAULT NULL,
  `Food_photo` varchar(200) DEFAULT NULL,
  `Food_details` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `food` */

insert  into `food`(`Food_id`,`Breed_id`,`Food_name`,`Food_photo`,`Food_details`) values (1,1,'royal',NULL,NULL);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`loginid`,`username`,`password`,`usertype`) values (1,'admin','admin1 ','admin'),(3,'shop','admin ','shop'),(4,'x@gmail.com','12345','user');

/*Table structure for table `ordered accessories` */

DROP TABLE IF EXISTS `ordered accessories`;

CREATE TABLE `ordered accessories` (
  `OA_id` int(11) NOT NULL AUTO_INCREMENT,
  `OAB_id` int(11) DEFAULT NULL,
  `AC_id` int(11) DEFAULT NULL,
  `Qty` int(11) DEFAULT NULL,
  PRIMARY KEY (`OA_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `ordered accessories` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `Holder_id` int(11) DEFAULT NULL,
  `Bank_name` varchar(20) DEFAULT NULL,
  `Acc_no` int(11) DEFAULT NULL,
  `IFSC_code` varchar(20) DEFAULT NULL,
  `Ammount` int(11) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `pets` */

DROP TABLE IF EXISTS `pets`;

CREATE TABLE `pets` (
  `P_id` int(11) NOT NULL AUTO_INCREMENT,
  `Breed_id` int(11) DEFAULT NULL,
  `P_photo` varchar(200) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  `Details` varchar(200) DEFAULT NULL,
  `User_id` int(11) DEFAULT NULL,
  `User_type` varchar(20) DEFAULT NULL,
  `Status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`P_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `pets` */

insert  into `pets`(`P_id`,`Breed_id`,`P_photo`,`Price`,`Details`,`User_id`,`User_type`,`Status`) values (1,2,'/static/img/230120-062234.jpg',4000,'1234567',4,'user',NULL);

/*Table structure for table `pets_booking` */

DROP TABLE IF EXISTS `pets_booking`;

CREATE TABLE `pets_booking` (
  `PB_id` int(11) NOT NULL AUTO_INCREMENT,
  `PB_user_id` int(11) DEFAULT NULL,
  `PB_pet_id` int(11) DEFAULT NULL,
  `PB_date` date DEFAULT NULL,
  `PB_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`PB_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `pets_booking` */

insert  into `pets_booking`(`PB_id`,`PB_user_id`,`PB_pet_id`,`PB_date`,`PB_status`) values (1,4,1,'2023-01-20','pending');

/*Table structure for table `rating` */

DROP TABLE IF EXISTS `rating`;

CREATE TABLE `rating` (
  `Rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `User_id` int(11) DEFAULT NULL,
  `Shop_id` int(11) DEFAULT NULL,
  `Rating` varchar(20) DEFAULT NULL,
  `Comment` varchar(10) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  PRIMARY KEY (`Rating_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `rating` */

insert  into `rating`(`Rating_id`,`User_id`,`Shop_id`,`Rating`,`Comment`,`Date`) values (1,1,3,'gbuygi',NULL,NULL);

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(20) DEFAULT NULL,
  `shop_email` varchar(20) DEFAULT NULL,
  `shop_phonenumber` bigint(20) DEFAULT NULL,
  `shop_lattitude` varchar(20) DEFAULT NULL,
  `shop_longitude` varchar(20) DEFAULT NULL,
  `shop_photo` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `shop` */

insert  into `shop`(`shop_id`,`shop_name`,`shop_email`,`shop_phonenumber`,`shop_lattitude`,`shop_longitude`,`shop_photo`) values (3,'hhh','ddd',NULL,NULL,NULL,NULL);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) DEFAULT NULL,
  `user_email` varchar(20) DEFAULT NULL,
  `user_housename` varchar(20) DEFAULT NULL,
  `user_place` varchar(20) DEFAULT NULL,
  `user_post` varchar(20) DEFAULT NULL,
  `user_pin` int(11) DEFAULT NULL,
  `user_latitude` varchar(20) DEFAULT NULL,
  `user_longitude` varchar(20) DEFAULT NULL,
  `user_phonenumber` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_name`,`user_email`,`user_housename`,`user_place`,`user_post`,`user_pin`,`user_latitude`,`user_longitude`,`user_phonenumber`) values (1,'amal',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,'qwerty','x@gmail.com','sdfgh','xcvbn','xcvbnmm',670646,'10.02','76.4026',9562142249);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

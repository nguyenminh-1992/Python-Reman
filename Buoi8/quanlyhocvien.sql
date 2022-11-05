-- create database
DROP DATABASE IF EXISTS Quan_ly_hoc_vien;
CREATE DATABASE Quan_ly_hoc_vien;
USE Quan_ly_hoc_vien;


DROP TABLE IF EXISTS `Hocvien`;
CREATE TABLE `Hocvien`(
	Id						TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `Name`					VARCHAR(50) NOT NULL UNIQUE KEY,
    Age						INT UNSIGNED NOT NULL,
    Country					NVARCHAR(50) NOT NULL,
    English 				INT UNSIGNED NOT NULL,
    Information				INT UNSIGNED NOT NULL
);

INSERT INTO `Hocvien`(Id		,  `Name`			, Age	, Country	, English, Information)
VALUES 				 (1	        , 'Nguyen Van A'    , 20    , 'Ha Noi'  ,  3     , 4     ),
					 (2	        , 'Nguyen Van B'    , 21    , 'Sai Gon'  ,  6     , 8     ),
					 (3	        , 'Nguyen Van C'    , 22    , 'Hue'     ,  3     , 7   )

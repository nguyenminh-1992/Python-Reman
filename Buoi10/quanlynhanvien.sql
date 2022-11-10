-- create database
DROP DATABASE IF EXISTS Quan_ly_nhan_vien;
CREATE DATABASE Quan_ly_nhan_vien;
USE Quan_ly_nhan_vien;


DROP TABLE IF EXISTS `Hocvien`;
CREATE TABLE `Hocvien`(
	Id						TINYINT UNSIGNED PRIMARY KEY,
    `Name`					VARCHAR(50) NOT NULL,
    Age						INT UNSIGNED NOT NULL,
    Country					NVARCHAR(50) NOT NULL,
    Sex 					TINYINT UNSIGNED NOT NULL,
    Chucvu					NVARCHAR(50) NOT NULL,
    Chamcong				TINYINT UNSIGNED NOT NULL
);

INSERT INTO `Hocvien`(Id	,  `Name`			, Age	, Country	, Sex	 , Chucvu , Chamcong)
VALUES 				 (1	    , 'Nguyen Van A'    , 20    , 'Ha Noi'  ,  0     , 'GD'   , 20 		),
					 (2	    , 'Nguyen Van B'    , 21    , 'Sai Gon' ,  1     , 'TP'   ,  21		),
					 (3	    , 'Nguyen Van C'    , 22    , 'Hue'     ,  2     , 'CB'   ,	22		)

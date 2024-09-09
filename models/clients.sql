-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema clients
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema clients
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `clients` DEFAULT CHARACTER SET utf8 ;
USE `clients` ;

-- -----------------------------------------------------
-- Table `clients`.`registered`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `clients`.`registered` ;

CREATE TABLE IF NOT EXISTS `clients`.`registered` (
  `id` INT AUTO_INCREMENT,
  `instituteName` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `contactNumber` VARCHAR(11) NOT NULL,
  `principalName` VARCHAR(45) NOT NULL,
  `schoolType` VARCHAR(45) NOT NULL,
  -- `logo` VARCHAR(255) NOT NULL,
  `date` DATETIME NOT NULL,
  UNIQUE INDEX `instituteName_UNIQUE` (`instituteName` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `contactNumber_UNIQUE` (`contactNumber` ASC) VISIBLE,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `clients`.`auth`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `clients`.`auth` ;

CREATE TABLE IF NOT EXISTS `clients`.`auth` (
  `sno` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NOT NULL,
  `passwords` VARCHAR(255) NOT NULL,
  UNIQUE INDEX `sno_UNIQUE` (`sno` ASC) VISIBLE,
  PRIMARY KEY (`email`),
  CONSTRAINT `authEmail`
    FOREIGN KEY (`email`)
    REFERENCES `clients`.`registered` (`email`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

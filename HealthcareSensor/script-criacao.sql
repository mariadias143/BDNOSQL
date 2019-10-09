-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema HealthcareSensors
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema HealthcareSensors
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `HealthcareSensors` DEFAULT CHARACTER SET utf8 ;
USE `HealthcareSensors` ;

-- -----------------------------------------------------
-- Table `HealthcareSensors`.`Sensor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HealthcareSensors`.`Sensor` (
  `sensorid` INT NOT NULL,
  `sensornum` INT NULL,
  `type` VARCHAR(32) NULL,
  PRIMARY KEY (`sensorid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `HealthcareSensors`.`Patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HealthcareSensors`.`Patient` (
  `patientid` INT NOT NULL,
  `name` VARCHAR(128) NOT NULL,
  `birthdate` DATE NOT NULL,
  `age` INT NOT NULL,
  `sensorid` INT NOT NULL,
  PRIMARY KEY (`patientid`, `sensorid`),
  INDEX `fk_Patient_Sensor_idx` (`sensorid` ASC) VISIBLE,
  CONSTRAINT `fk_Patient_Sensor`
    FOREIGN KEY (`sensorid`)
    REFERENCES `HealthcareSensors`.`Sensor` (`sensorid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `HealthcareSensors`.`Biometrics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HealthcareSensors`.`Biometrics` (
  `biometricsid` INT NOT NULL,
  `bodytemp` INT NOT NULL,
  `systolic` INT NOT NULL,
  `diastolic` INT NOT NULL,
  `bpm` INT NOT NULL,
  `timestamp` DATETIME NOT NULL,
  `sensorid` INT NOT NULL,
  PRIMARY KEY (`biometricsid`, `sensorid`),
  INDEX `fk_Biometrics_Sensor1_idx` (`sensorid` ASC) VISIBLE,
  CONSTRAINT `fk_Biometrics_Sensor1`
    FOREIGN KEY (`sensorid`)
    REFERENCES `HealthcareSensors`.`Sensor` (`sensorid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

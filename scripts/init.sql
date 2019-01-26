CREATE DATABASE `meetwithfriends`;


CREATE TABLE `meetwithfriends`.`Users` (
  `Id` VARCHAR(50) NOT NULL,
  `Email` VARCHAR(50) NOT NULL,
  `FirstName` VARCHAR(50) NULL,
  `LastName` VARCHAR(50) NULL,
  `PassHash` VARCHAR(128) NOT NULL,
  `IsAdmin` TINYINT NULL,
  `Avatar` BLOB NULL,
  PRIMARY KEY (`Id`),
  UNIQUE INDEX `Email_UNIQUE` (`Email` ASC));

CREATE TABLE `meetwithfriends`.`Sessions` (
  `Id` INT NOT NULL,
  `UserId` VARCHAR(50) NOT NULL,
  `Token` VARCHAR(50) NOT NULL,
  `StartDate` DATETIME NOT NULL,
  `DueDate` DATETIME NOT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Sessions_1_idx` (`UserId` ASC),
  CONSTRAINT `fk_Sessions_1`
    FOREIGN KEY (`UserId`)
    REFERENCES `meetwithfriends`.`Users` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`Groups` (
  `Id` VARCHAR(50) NOT NULL,
  `CreatorId` VARCHAR(50) NULL,
  `Note` VARCHAR(255) NULL,
  `Avatar` BLOB NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_GroupCreatorId_idx` (`CreatorId` ASC),
  CONSTRAINT `fk_GroupCreatorId`
    FOREIGN KEY (`CreatorId`)
    REFERENCES `meetwithfriends`.`Users` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`Meetings` (
  `Id` varchar(50) NOT NULL,
  `MeetingDate` datetime DEFAULT NULL,
  `CreatorId` varchar(50) DEFAULT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `GroupId` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  KEY `fk_CreatorId_idx` (`CreatorId`),
  KEY `fk_MeetingGroupId_idx` (`GroupId`),
  CONSTRAINT `fk_CreatorId` FOREIGN KEY (`CreatorId`) REFERENCES `Users` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_MeetingGroupId` FOREIGN KEY (`GroupId`) REFERENCES `Groups` (`Id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE `meetwithfriends`.`MealProviders` (
  `Id` VARCHAR(50) NOT NULL,
  `Name` VARCHAR(50) NULL,
  `Note` VARCHAR(50) NULL,
  `Address` VARCHAR(50) NULL,
  `Site` VARCHAR(50) NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `meetwithfriends`.`Meals` (
  `Id` VARCHAR(50)  NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `ProviderId` VARCHAR(50) NULL,
  `Image` BLOB NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_Mealprovider_idx` (`ProviderId` ASC),
  CONSTRAINT `fk_Mealprovider`
    FOREIGN KEY (`ProviderId`)
    REFERENCES `meetwithfriends`.`MealProviders` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
CREATE TABLE `meetwithfriends`.`Places` (
  `Id` VARCHAR(50) NOT NULL,
  `Name` VARCHAR(50) NOT NULL,
  `Address` VARCHAR(50) NULL,
  `Site` VARCHAR(50) NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `meetwithfriends`.`MealsInMeetings` (
  `Id` VARCHAR(50) NOT NULL,
  `MealId` VARCHAR(50) NOT NULL,
  `MeetingId` VARCHAR(50) NOT NULL,
  `VotesNum` INT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_MealsInMeetings1_idx` (`MealId` ASC),
  INDEX `fk_MealsInMeetings2_idx` (`MeetingId` ASC),
  CONSTRAINT `fk_MealsInMeetings1`
    FOREIGN KEY (`MealId`)
    REFERENCES `meetwithfriends`.`Meals` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MealsInMeetings2`
    FOREIGN KEY (`MeetingId`)
    REFERENCES `meetwithfriends`.`Meetings` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`PlacesInMeetings` (
  `Id` VARCHAR(50) NOT NULL,
  `PlaceId` VARCHAR(50) NOT NULL,
  `MeetingId` VARCHAR(50) NOT NULL,
  `VotesNum` INT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_PlacesInMeetings1_idx` (`PlaceId` ASC),
  INDEX `fk_PlacesInMeetings2_idx` (`MeetingId` ASC),
  CONSTRAINT `fk_PlacesInMeetings1`
    FOREIGN KEY (`PlaceId`)
    REFERENCES `meetwithfriends`.`Places` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PlacesInMeetings2`
    FOREIGN KEY (`MeetingId`)
    REFERENCES `meetwithfriends`.`Meetings` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`UsersInGroups` (
  `Id` VARCHAR(50) NOT NULL,
  `UserId` VARCHAR(50) NOT NULL,
  `GroupId` VARCHAR(50) NOT NULL,
  `IsAdmin` TINYINT NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_UsersInGroups1_idx` (`UserId` ASC),
  INDEX `fk_UsersInGroups2_idx` (`GroupId` ASC),
  CONSTRAINT `fk_UsersInGroups1`
    FOREIGN KEY (`UserId`)
    REFERENCES `meetwithfriends`.`Users` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UsersInGroups2`
    FOREIGN KEY (`GroupId`)
    REFERENCES `meetwithfriends`.`Groups` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

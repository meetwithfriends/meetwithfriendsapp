CREATE DATABASE `meetwithfriends`;


CREATE TABLE `meetwithfriends`.`users` (
  `id` VARCHAR(50) NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `first_name` VARCHAR(50) NULL,
  `last_name` VARCHAR(50) NULL,
  `pass_hash` VARCHAR(128) NOT NULL,
  `is_admin` TINYINT NULL,
  `avatar` BLOB NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC));

CREATE TABLE `meetwithfriends`.`sessions` (
  `id` VARCHAR(50) NOT NULL,
  `user_id` VARCHAR(50) NOT NULL,
  `token` VARCHAR(255) NOT NULL,
  `start_date` DATETIME NOT NULL,
  `due_date` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Sessions_1_idx` (`user_id` ASC),
  CONSTRAINT `fk_Sessions_1`
    FOREIGN KEY (`user_id`)
    REFERENCES `meetwithfriends`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`groups` (
  `id` VARCHAR(50) NOT NULL,
  `creator_id` VARCHAR(50) NULL,
  `name` VARCHAR(50) NULL,
  `note` VARCHAR(255) NULL,
  `avatar` BLOB NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_GroupCreatorid_idx` (`creator_id` ASC),
  CONSTRAINT `fk_group_creator_id`
    FOREIGN KEY (`creator_id`)
    REFERENCES `meetwithfriends`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`users_in_groups` (
  `id` VARCHAR(50) NOT NULL,
  `user_id` VARCHAR(50) NOT NULL,
  `group_id` VARCHAR(50) NOT NULL,
  `is_admin` TINYINT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_UsersInGroups1_idx` (`user_id` ASC),
  INDEX `fk_UsersInGroups2_idx` (`group_id` ASC),
  CONSTRAINT `fk_UsersInGroups1`
    FOREIGN KEY (`user_id`)
    REFERENCES `meetwithfriends`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UsersInGroups2`
    FOREIGN KEY (`group_id`)
    REFERENCES `meetwithfriends`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `meetwithfriends`.`places` (
  `id` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `address` VARCHAR(50) NULL,
  `site` VARCHAR(50) NULL,
  `group_id` VARCHAR(50) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_PlacesGroupid_idx` (`group_id` ASC),
  CONSTRAINT `fk_places_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `meetwithfriends`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


CREATE TABLE `meetwithfriends`.`meal_providers` (
  `id` VARCHAR(50) NOT NULL,
  `name` VARCHAR(50) NULL,
  `note` VARCHAR(50) NULL,
  `address` VARCHAR(50) NULL,
  `site` VARCHAR(50) NULL,
  `group_id` VARCHAR(50) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_ProvidersGroupid_idx` (`group_id` ASC),
  CONSTRAINT `fk_places_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `meetwithfriends`.`groups` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION));

CREATE TABLE `meetwithfriends`.`meals` (
  `id` VARCHAR(50)  NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `provider_id` VARCHAR(50) NULL,
  `image` BLOB NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Mealprovider_idx` (`provider_id` ASC),
  CONSTRAINT `fk_Mealprovider`
    FOREIGN KEY (`provider_id`)
    REFERENCES `meetwithfriends`.`meal_providers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`meetings` (
  `id` varchar(50) NOT NULL,
  `meeting_date` datetime DEFAULT NULL,
  `creator_id` varchar(50) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `group_id` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_Creatorid_idx` (`creator_id`),
  KEY `fk_MeetingGroupid_idx` (`group_id`),
  CONSTRAINT `fk_Creatorid` FOREIGN KEY (`creator_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_MeetingGroupid` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
);
    

CREATE TABLE `meetwithfriends`.`meals_in_meetings` (
  `id` VARCHAR(50) NOT NULL,
  `meal_id` VARCHAR(50) NOT NULL,
  `meeting_id` VARCHAR(50) NOT NULL,
  `votes_num` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_MealsInMeetings1_idx` (`meal_id` ASC),
  INDEX `fk_MealsInMeetings2_idx` (`meeting_id` ASC),
  CONSTRAINT `fk_MealsInMeetings1`
    FOREIGN KEY (`meal_id`)
    REFERENCES `meetwithfriends`.`meals` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MealsInMeetings2`
    FOREIGN KEY (`meeting_id`)
    REFERENCES `meetwithfriends`.`meetings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

CREATE TABLE `meetwithfriends`.`places_in_meetings` (
  `id` VARCHAR(50) NOT NULL,
  `place_id` VARCHAR(50) NOT NULL,
  `meeting_id` VARCHAR(50) NOT NULL,
  `votes_num` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_PlacesInMeetings1_idx` (`place_id` ASC),
  INDEX `fk_PlacesInMeetings2_idx` (`meeting_id` ASC),
  CONSTRAINT `fk_PlacesInMeetings1`
    FOREIGN KEY (`place_id`)
    REFERENCES `meetwithfriends`.`places` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_PlacesInMeetings2`
    FOREIGN KEY (`meeting_id`)
    REFERENCES `meetwithfriends`.`meetings` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

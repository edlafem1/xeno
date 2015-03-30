CREATE TABLE `xeno`.`users` (
`id` int NOT NULL AUTO_INCREMENT,
`first_name` tinytext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`last_name` tinytext CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
`date_joined` datetime NOT NULL,
`credits` int NOT NULL DEFAULT 100,
`suspended_until` datetime NOT NULL,
`acct_type` tinyint NOT NULL DEFAULT 1,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`acct_types` (
`id` tinyint NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`make` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`model` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`cars` (
`id` int NOT NULL,
`make` int NOT NULL,
`model` int NOT NULL,
`year` int NOT NULL,
`exotic` int NULL DEFAULT 0,
`primary_exterior_color` id NOT NULL,
`secondary_exterior_color` int NULL DEFAULT NULL,
`interior_color` int NOT NULL,
`type` int NOT NULL,
`hp` int NOT NULL,
`torque` int NOT NULL,
`miles_driven` int NOT NULL,
`status` tinyint NOT NULL DEFAULT 0,
UNIQUE INDEX `id` (`id`)
);

CREATE TABLE `xeno`.`car_status` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`type_exotic` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`maintenance_log` (
`id` int NOT NULL,
`description` text NOT NULL,
`date_entered` datetime NOT NULL DEFAULT DATETIME(NOW),
`date_resolved` datetime NULL DEFAULT NULL,
`car` int NOT NULL,
`maintenance_worker` int NOT NULL,
`last_driver` int NOT NULL,
UNIQUE INDEX `id` (`id`)
);

CREATE TABLE `xeno`.`car_colors` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `xeno`.`car_type` (
`id` int NOT NULL,
`description` tinytext NOT NULL,
UNIQUE INDEX `id` (`id`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_unicode_ci;


ALTER TABLE `xeno`.`users` ADD CONSTRAINT `acct_type` FOREIGN KEY (`acct_type`) REFERENCES `xeno`.`acct_types` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `car_make` FOREIGN KEY (`make`) REFERENCES `xeno`.`make` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `car_model` FOREIGN KEY (`model`) REFERENCES `xeno`.`model` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `car_status` FOREIGN KEY (`status`) REFERENCES `xeno`.`car_status` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `car_exotic` FOREIGN KEY (`exotic`) REFERENCES `xeno`.`type_exotic` (`id`);
ALTER TABLE `xeno`.`maintenance_log` ADD CONSTRAINT `car` FOREIGN KEY (`car`) REFERENCES `xeno`.`cars` (`id`);
ALTER TABLE `xeno`.`maintenance_log` ADD CONSTRAINT `maintenance_worker` FOREIGN KEY (`maintenance_worker`) REFERENCES `xeno`.`users` (`id`);
ALTER TABLE `xeno`.`maintenance_log` ADD CONSTRAINT `last_driver` FOREIGN KEY (`last_driver`) REFERENCES `xeno`.`users` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `primary_ext_color` FOREIGN KEY (`primary_exterior_color`) REFERENCES `xeno`.`car_colors` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `secondary_ext_color` FOREIGN KEY (`secondary_exterior_color`) REFERENCES `xeno`.`car_colors` (`id`);
ALTER TABLE `xeno`.`cars` ADD CONSTRAINT `interior_color` FOREIGN KEY (`interior_color`) REFERENCES `xeno`.`car_colors` (`id`);


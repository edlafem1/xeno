DELETE FROM `xeno`.`acct_types`;

INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("admin");

INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("maintenance");

INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("regular");




INSERT INTO `xeno`.`car_status` (`description`) VALUES ("available");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("out");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("maintenance");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("hidden");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("removed");



INSERT INTO `xeno`.`users` (`first_name`, `last_name`, `credits`, `suspended_until`, `acct_type`, `userid`, `hpass`) VALUES
    ('super', 'admin', 0, 0, 1, 'admin', 'admin');
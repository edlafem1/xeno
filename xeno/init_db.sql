USE `xeno`


INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("admin");

INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("maintenance");

INSERT INTO `xeno`.`acct_types` (`description`) VALUES ("regular");




INSERT INTO `xeno`.`car_status` (`description`) VALUES ("available");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("out");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("maintenance");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("hidden");

INSERT INTO `xeno`.`car_status` (`description`) VALUES ("removed");



INSERT INTO `xeno`.`users` (`first_name`, `last_name`, `credits`, `suspended_until`, `acct_type`, `userid`, `hpass`) VALUES
    ('super', 'admin', 0, 0, 1, 'admin', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw=='); # admin password is 'password'


INSERT INTO `car_type` (`id`, `description`) VALUES
(1, 'Convertible'),
(2, 'Coupe'),
(3, 'Sedan'),
(4, 'SUV');

INSERT INTO `country` (`id`, `description`) VALUES
(1, 'Italy'),
(2, 'Germany');

INSERT INTO `make` (`id`, `description`) VALUES
(1, 'Bugatti'),
(2, 'Ferrari'),
(3, 'Audi'),
(4, 'Bentley'),
(5, 'Porsche'),
(6, 'Rolls-Royce'),
(7, 'Jaguar'),
(8, 'Lamborghini');

INSERT INTO `model` (`id`, `description`) VALUES
(1, '911 Turbo S'),
(2, '918 Spyder'),
(3, 'Aventador LP 75-4 Superveloce'),
(4, 'SuperSport'),
(5, 'R8 V12');

INSERT INTO `cars` (`id`, `make`, `model`, `year`, `country`, `type`, `hp`, `torque`, `miles_driven`, `status`, `added_by`, `acceleration`, `max_speed`) VALUES
(3, 1, 4, 2014, 2, 2, 1200, 1001, 10, 1, 1, 2.31, 272),
(4, 5, 1, 2015, 2, 2, 650, 600, 900, 1, 1, 2.7, 240),
(5, 5, 2, 2015, 2, 4, 970, 1200, 5, 1, 1, 2.21, 220),
(6, 3, 5, 2013, 2, 1, 800, 750, 500, 1, 1, 3, 220);

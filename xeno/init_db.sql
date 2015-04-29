--
-- Database: `xeno`
--

--
-- Dumping data for table `acct_types`
--

USE `xeno`;

INSERT INTO `acct_types` (`id`, `description`) VALUES
(1, 'admin'),
(2, 'maintenance'),
(3, 'regular');

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `first_name`, `last_name`, `date_joined`, `credits`, `suspended_until`, `acct_type`, `userid`, `hpass`) VALUES
(1, 'super', 'admin', '2015-04-29 15:34:04', 0, '0000-00-00 00:00:00', 1, 'admin', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw=='),
(2, 'Bruce', 'Wayne', '2015-04-29 15:47:30', 100, '0000-00-00 00:00:00', 3, 'batman', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw=='),
(4, 'Bill', 'Nye', '2015-04-29 15:48:30', 100, '0000-00-00 00:00:00', 2, 'billnye', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw=='),
(5, 'Clark', 'Wayne', '2015-04-29 15:49:14', 100, '0000-00-00 00:00:00', 3, 'superman', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw=='),
(6, 'Diana', 'Prince', '2015-04-29 15:49:42', 100, '0000-00-00 00:00:00', 3, 'wonderwoman', 'fEcdUl1QSEy13L_okEmnCA==w81WBGW1lM8z1CIWfO0ikQrPD-q-UKw9yGgvV7cEWWJlY9at57IEMITPeFW0yWHomGcThDetjFddAqRhfjO4jw==');

--
-- Dumping data for table `car_status`
--

INSERT INTO `car_status` (`id`, `description`) VALUES
(1, 'available'),
(2, 'out'),
(3, 'maintenance'),
(4, 'hidden'),
(5, 'removed');

--
-- Dumping data for table `car_type`
--

INSERT INTO `car_type` (`id`, `description`) VALUES
(1, 'Convertible'),
(2, 'Coupe'),
(3, 'Sedan'),
(4, 'SUV');

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`id`, `description`) VALUES
(1, 'Italy'),
(2, 'Germany');

--
-- Dumping data for table `make`
--

INSERT INTO `make` (`id`, `description`) VALUES
(1, 'Bugatti'),
(2, 'Ferrari'),
(3, 'Audi'),
(4, 'Bentley'),
(5, 'Porsche'),
(6, 'Rolls-Royce'),
(7, 'Jaguar'),
(8, 'Lamborghini');

--
-- Dumping data for table `model`
--

INSERT INTO `model` (`id`, `description`) VALUES
(1, '911 Turbo S'),
(2, '918 Spyder'),
(3, 'Aventador LP 75-4 Superveloce'),
(4, 'SuperSport'),
(5, 'R8 V12');

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`id`, `make`, `model`, `year`, `country`, `type`, `hp`, `torque`, `miles_driven`, `status`, `added_by`, `acceleration`, `max_speed`, `is_featured`, `date_added`) VALUES
(1, 1, 4, 2014, 2, 2, 1200, 1001, 10, 1, 1, 2.31, 272, 0, '2015-04-29 15:34:04'),
(2, 5, 1, 2015, 2, 2, 650, 600, 900, 1, 1, 2.7, 240, 0, '2015-04-29 15:34:04'),
(3, 5, 2, 2015, 2, 4, 970, 1200, 5, 1, 1, 2.21, 217, 0, '2015-04-29 15:34:04'),
(4, 3, 5, 2013, 2, 1, 800, 750, 500, 1, 1, 3, 220, 0, '2015-04-29 15:34:04');

--
-- Dumping data for table `reservations`
--

INSERT INTO `reservations` (`id`, `made_by`, `for_car`, `for_date`, `car_returned`, `return_time`) VALUES
(1, 2, 1, '2015-04-14', 0, '0000-00-00'),
(2, 4, 3, '2015-04-22', 0, '0000-00-00'),
(3, 6, 1, '2015-02-11', 1, '2015-04-15'),
(4, 5, 3, '2015-04-08', 1, '2015-04-08');

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`id`, `date_created`, `num_stars`, `text`, `reviewer`, `car`) VALUES
(1, '2015-04-22 04:18:13', 4, 'This car was exceptional. Would rent again!', 6, 1),
(2, '2015-03-03 07:22:16', 2, 'My stable has more horses than this!', 4, 2),
(3, '2015-01-27 14:30:16', 5, 'WHOA, I no longer need to use gel. I get out of bed, step into this beauty, roll down the windows, and VROOOOM.', 2, 3),
(4, '2015-04-22 06:29:16', 5, 'WARNING! Objects in rearview are LOSING!', 5, 4);
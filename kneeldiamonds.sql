CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` VARCHAR(160) NOT NULL,
    `price` NUMERIC(6,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC (3,2) NOT NULL,
    `price` NUMERIC (6,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` VARCHAR(50) NOT NULL,
    `price` NUMERIC (6,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `time_stamp` VARCHAR(50) NOT NULL,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

--Metals data
INSERT INTO `Metals` VALUES (null, "Sterling Silver", 122.22);
INSERT INTO `Metals` VALUES (null, "Bronze", 122.22);
INSERT INTO `Metals` VALUES (null, "14K Gold", 736.40);
INSERT INTO `Metals` VALUES (null, "24K Gold", 911.10);
INSERT INTO `Metals` VALUES (null, "Rose Gold", 833.30);

--Sizes Data
INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 783);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

--Styles Data
INSERT INTO `Styles` VALUES (null, "Classic", 500);
INSERT INTO `Styles` VALUES (null, "Modern", 710);
INSERT INTO `Styles` VALUES (null, "Vintage", 965);

--Orders Data
INSERT INTO `Orders` VALUES (null, "2023-05-01", 3, 2, 2);
INSERT INTO `Orders` VALUES (null, "2023-06-05", 5, 3, 1);
INSERT INTO `Orders` VALUES (null, "2023-06-22", 4, 1, 3);
INSERT INTO `Orders` VALUES (null, "2023-07-20", 2, 4, 2);
INSERT INTO `Orders` VALUES (null, "2023-07-20", 1, 2, 3);


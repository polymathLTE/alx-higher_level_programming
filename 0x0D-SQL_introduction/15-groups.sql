-- counts and lists the number of rows with the same score
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score`;

-- displays the top 3 cities of avg temp. in july and august
SELECT `city`, AVG(`value`) as avg_temp FROM `temperatures` WHERE `month` IN (7,8) GROUP BY `city` ORDER BY avg_temp DESC LIMIT 3;

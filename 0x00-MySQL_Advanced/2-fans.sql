-- SQL script to rank country origins of bands by the number of (non-unique) fans
-- The results will be ordered by the number of fans in descending order

-- Select the country of origin and the sum of fans grouped by origin
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;

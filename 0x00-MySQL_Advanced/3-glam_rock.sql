-- SQL script to list all bands with Glam rock as their main style
-- The results are ranked by the lifespan of the bands in descending order

-- Select the band name and compute their lifespan in years
SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;

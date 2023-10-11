-- list all bands with Glam rock as main style
-- ranked by longevity

SELECT band_name AS band_name, IFNULL(split, 2020) - IFNULL(formed, 0) AS lifespan 
 FROM metal_bands 
 WHERE style LIKE '%Glam rock%' 
 ORDER BY lifespan DESC;

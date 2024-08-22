-- SQL script to create a stored procedure ComputeAverageWeightedScoreForUsers
-- This procedure computes and stores the average weighted score for all students

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE avg_weighted_score DECIMAL(10, 2);

   
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_scores (
        user_id INT,
        total_score DECIMAL(10, 2),
        total_weight DECIMAL(10, 2)
    );

   
    TRUNCATE TABLE temp_scores;

    
    INSERT INTO temp_scores (user_id, total_score, total_weight)
    SELECT 
        user_id,
        SUM(score * weight) AS total_score,
        SUM(weight) AS total_weight
    FROM 
        scores
    GROUP BY 
        user_id;

    
    UPDATE users u
    JOIN temp_scores t ON u.id = t.user_id
    SET u.average_weighted_score = 
        CASE 
            WHEN t.total_weight = 0 THEN 0
            ELSE t.total_score / t.total_weight
        END;

    
    DROP TEMPORARY TABLE temp_scores;
END$$

DELIMITER ;

-- SQL script to create a stored procedure ComputeAverageWeightedScoreForUser
-- This procedure computes and stores the average weighted score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE avg_weighted_score DECIMAL(10, 2);

   
    SET total_score = 0;
    SET total_weight = 0;

   
    SELECT 
        SUM(score * weight) INTO total_score,
        SUM(weight) INTO total_weight
    FROM 
        scores
    WHERE 
        user_id = user_id;

    
    IF total_weight = 0 THEN
        SET avg_weighted_score = 0; 
    ELSE
        SET avg_weighted_score = total_score / total_weight;
    END IF;

   
    UPDATE users
    SET average_weighted_score = avg_weighted_score
    WHERE id = user_id;
END$$

DELIMITER ;

-- SQL script to create a stored procedure ComputeAverageScoreForUser
-- This procedure computes and stores the average score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT    -- The ID of the user (linked to users.id)
)
BEGIN
    DECLARE avg_score DECIMAL(5,2);  -- Declare a variable to store the average score

    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END$$

DELIMITER ;

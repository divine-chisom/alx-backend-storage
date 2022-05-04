-- creates a stored procedure ComputeAverageWeightedScoreForUser that
-- computes and store the average weighted score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INT)
BEGIN
    DECLARE weighted_score_sum INT DEFAULT 0;
    DECLARE weight_sum INT DEFAULT 0;

    SELECT SUM(corrections.score * projects.weight)
        INTO weighted_score_sum
        FROM corrections
            JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

    SELECT SUM(projects.weight)
        INTO weight_sum
        FROM corrections
            JOIN projects
                ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;
        
        UPDATE users
            SET users.average_score = weighted_score_sum / weight_sum
            WHERE users.id = user_id;
    END IF;
END $$
DELIMITER ;

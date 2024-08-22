-- SQL script to create a view named need_meeting
-- This view lists all students with a score under 80 and either no last meeting or more than 1 month since last meeting

CREATE VIEW need_meeting AS
SELECT 
    s.name AS student_name
FROM 
    students s
LEFT JOIN 
    meetings m ON s.id = m.student_id
WHERE 
    s.score < 80
    AND (m.last_meeting IS NULL OR m.last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));


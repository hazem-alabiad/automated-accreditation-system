CALL usp_insert_department('BBM', 'Computer Engineering');
CALL usp_insert_curriculum(1, 'BBM');
CALL usp_insert_keylearningoutcome('keylearningoutcome', 'BBM');
CALL usp_insert_semester('fall', '2019');
CALL usp_insert_semester('fall', '2019');
CALL usp_insert_instructor('fuat', 'akal', 'BBM');

CALL usp_insert_course('BBM471', 'Intro to DBMS', 10::smallint);
CALL usp_insert_course('BBM495', 'Intro to NLP', 10::smallint);
CALL usp_insert_course('BBM451', 'Networking', 10::smallint);
CALL usp_insert_course('EMU475', 'Intro to PM', 10::smallint);
CALL usp_insert_course('EMU446', 'Supply Chain', 6::smallint);
CALL usp_insert_course('EMU443', 'Revenue Management', 6::smallint);
CALL usp_insert_course('ELE110', 'Intro to ELE', 5::smallint);

CALL usp_insert_curriculum_course(1, 'BBM471');

CALL usp_insert_courseLearningObjective('BBM471', 'courseLearningObjective');

CALL usp_insert_courseoffering(1, 'BBM471', NULL);
CALL usp_insert_courseoffering(1, 'BBM495', NULL);
CALL usp_insert_courseoffering(1, 'BBM451', NULL);
CALL usp_insert_courseoffering(1, 'EMU475', NULL);
CALL usp_insert_courseoffering(1, 'EMU446', NULL);
CALL usp_insert_courseoffering(1, 'EMU443', NULL);
CALL usp_insert_courseoffering(1, 'ELE110', NULL);


CALL usp_insert_assessment(1, 0.3, NULL);
CALL usp_insert_question('question_body', 0.2, 1);
CALL usp_insert_question_courselearningobjective(1, 1, 2::smallint);
CALL usp_insert_question_keyLearningOutcome(1, 1, 5::smallint);
CALL usp_insert_section(1, 3);
CALL usp_insert_section_instructor(1, 1);
CALL usp_insert_student(2140, 'Hazem', 'White');
CALL usp_insert_section_student(1, 2140);
CALL usp_insert_assessment_student(2140, 1, 91.0);
CALL usp_insert_quiz(1, NULL, 0.2, 50::smallint, '2019-08-01');
CALL usp_insert_assignment(1, NULL, 0.1, '2019-03-02', '2019-03-10');
CALL usp_insert_midterm(1, NULL, 0.4, 1::smallint, '2019-04-15', 120::smallint);
CALL usp_insert_final(1, NULL, 0.5, 2::SMALLINT, '2019-05-03', 150::smallint);

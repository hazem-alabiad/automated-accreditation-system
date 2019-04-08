CALL usp_insert_department('BBM', 'Computer Engineering');
CALL usp_insert_department('ELE', 'Electrical Engineering');
CALL usp_insert_department('EMU', 'Industrial Engineering');

CALL usp_insert_curriculum(1, 'BBM');
CALL usp_insert_curriculum(1, 'ELE');
CALL usp_insert_curriculum(1, 'EMU');
CALL usp_insert_curriculum(2, 'EMU');
CALL usp_insert_curriculum(2, 'BBM');

CALL usp_insert_keylearningoutcome('keylearningoutcome', 'BBM');
CALL usp_insert_keylearningoutcome('keylearningoutcome', 'ELE');
CALL usp_insert_keylearningoutcome('keylearningoutcome', 'EMU');


CALL usp_insert_semester('fall', '2019');
CALL usp_insert_semester('spring', '2019');
CALL usp_insert_semester('spring', '2020');

CALL usp_insert_instructor('fuat', 'akal', 'BBM');
CALL usp_insert_instructor('Adnan', 'Ozsoy', 'BBM');
CALL usp_insert_instructor('Engin', 'Demir', 'BBM');
CALL usp_insert_instructor('Umut', 'ahmet', 'EMU');

CALL usp_insert_course('BBM471', 'Intro to DBMS', 10::smallint);
CALL usp_insert_course('BBM495', 'Intro to NLP', 10::smallint);
CALL usp_insert_course('BBM451', 'Networking', 10::smallint);
CALL usp_insert_course('EMU475', 'Intro to PM', 10::smallint);
CALL usp_insert_course('EMU446', 'Supply Chain', 6::smallint);
CALL usp_insert_course('EMU443', 'Revenue Management', 6::smallint);
CALL usp_insert_course('ELE110', 'Intro to ELE', 5::smallint);

CALL usp_insert_curriculum_course(1, 'BBM471');
CALL usp_insert_curriculum_course(1, 'BBM495');
CALL usp_insert_curriculum_course(1, 'BBM451');
CALL usp_insert_curriculum_course(2, 'ELE110');
CALL usp_insert_curriculum_course(3, 'EMU475');
CALL usp_insert_curriculum_course(3, 'EMU446');

CALL usp_insert_courseLearningObjective('BBM471', 'courseLearningObjective');
CALL usp_insert_courseLearningObjective('BBM451', 'courseLearningObjective');
CALL usp_insert_courseLearningObjective('BBM495', 'courseLearningObjective');
CALL usp_insert_courseLearningObjective('ELE110', 'courseLearningObjective');
CALL usp_insert_courseLearningObjective('EMU446', 'courseLearningObjective');
CALL usp_insert_courseLearningObjective('EMU475', 'courseLearningObjective');

CALL usp_insert_courseoffering(1, 'BBM471', NULL);
CALL usp_insert_courseoffering(1, 'BBM495', NULL);
CALL usp_insert_courseoffering(1, 'BBM451', NULL);
CALL usp_insert_courseoffering(1, 'EMU475', NULL);
CALL usp_insert_courseoffering(1, 'EMU446', NULL);
CALL usp_insert_courseoffering(1, 'EMU443', NULL);
CALL usp_insert_courseoffering(1, 'ELE110', NULL);


CALL usp_insert_assessment(1, 0.3, NULL);
CALL usp_insert_assessment(2, 0.5, NULL);
CALL usp_insert_assessment(3, 0.2, NULL);
CALL usp_insert_assessment(3, 0.1, NULL);
CALL usp_insert_assessment(1, 0.3, NULL);

CALL usp_insert_question('question_body', 0.2, 1);
CALL usp_insert_question('question_body', 0.3, 2);
CALL usp_insert_question('question_body', 0.2, 3);

CALL usp_insert_question_courselearningobjective(1, 1, 2::smallint);

CALL usp_insert_question_keyLearningOutcome(1, 1, 5::smallint);

CALL usp_insert_section(1, 3);
CALL usp_insert_section(2, 2);
CALL usp_insert_section(1, 1);

CALL usp_insert_section_instructor(1, 1);
CALL usp_insert_section_instructor(2, 1);

CALL usp_insert_student(2140, 'Hazem', 'White', 'BBM');
CALL usp_insert_student(2150, 'George', 'Gerogenazi', 'BBM');
CALL usp_insert_student(2130, 'Ahmad', 'Miri', 'EMU');
CALL usp_insert_student(2131, 'omer', 'yekta', 'EMU');
CALL usp_insert_student(2141, 'Abueljod', 'Albadin', 'ELE');

CALL usp_insert_section_student(1, 2140);
CALL usp_insert_section_student(2, 2150);
CALL usp_insert_section_student(2, 2131);
CALL usp_insert_section_student(2, 2150);

CALL usp_insert_assessment_student(2140, 1, 91.0);
CALL usp_insert_assessment_student(2150, 2, 61.0);
CALL usp_insert_assessment_student(2131, 3, 41.0);
CALL usp_insert_assessment_student(2141, 1, 41.0);

CALL usp_insert_quiz(1, NULL, 0.2, 50::smallint, '2019-08-01');
CALL usp_insert_quiz(2, NULL, 0.1, 40::smallint, '2019-08-04');

CALL usp_insert_assignment(1, NULL, 0.1, '2019-03-02', '2019-03-10');
CALL usp_insert_midterm(1, NULL, 0.4, 1::smallint, '2019-04-15', 120::smallint);
CALL usp_insert_final(1, NULL, 0.5, 2::SMALLINT, '2019-05-03', 150::smallint);

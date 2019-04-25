CALL usp_insert_department('BBM', 'Computer Engineering');
CALL usp_insert_department('ELE', 'Electrical Engineering');
CALL usp_insert_department('EMU', 'Industrial Engineering');

CALL usp_insert_curriculum(1, 'BBM');
CALL usp_insert_curriculum(1, 'ELE');
CALL usp_insert_curriculum(1, 'EMU');
CALL usp_insert_curriculum(2, 'EMU');
CALL usp_insert_curriculum(2, 'BBM');

CALL usp_insert_keylearningoutcome('keylearningoutcome_BBM', 'BBM');
CALL usp_insert_keylearningoutcome('keylearningoutcome_ELE', 'ELE');
CALL usp_insert_keylearningoutcome('keylearningoutcome_EMU', 'EMU');

CALL usp_insert_semester('fall', '2019');
CALL usp_insert_semester('spring', '2017');
CALL usp_insert_semester('summer', '2018');

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
CALL usp_insert_courseoffering(2, 'BBM451', NULL);
CALL usp_insert_courseoffering(2, 'EMU475', NULL);
CALL usp_insert_courseoffering(3, 'EMU446', NULL);
CALL usp_insert_courseoffering(3, 'EMU443', NULL);
CALL usp_insert_courseoffering(1, 'ELE110', NULL);



CALL usp_insert_section(1, 1);
CALL usp_insert_section(1, 2);
CALL usp_insert_section(2, 1);
CALL usp_insert_section(3, 1);
CALL usp_insert_section(4, 1);
CALL usp_insert_section(4, 2);
CALL usp_insert_section(4, 3);
CALL usp_insert_section(4, 4);
CALL usp_insert_section(5, 1);
CALL usp_insert_section(6, 1);
CALL usp_insert_section(7, 1);

CALL usp_insert_section_instructor(1, 1);
CALL usp_insert_section_instructor(2, 2);
CALL usp_insert_section_instructor(3, 1);
CALL usp_insert_section_instructor(4, 1);
CALL usp_insert_section_instructor(5, 1);
CALL usp_insert_section_instructor(6, 2);
CALL usp_insert_section_instructor(7, 3);
CALL usp_insert_section_instructor(8, 4);
CALL usp_insert_section_instructor(9, 4);
CALL usp_insert_section_instructor(10, 4);

CALL usp_insert_student(2140, 'Hazem', 'White', 'BBM');
CALL usp_insert_student(2150, 'George', 'Gerogenazi', 'BBM');
CALL usp_insert_student(2130, 'Ahmad', 'Miri', 'EMU');
CALL usp_insert_student(2131, 'omer', 'yekta', 'EMU');
CALL usp_insert_student(2141, 'Abueljod', 'Albadin', 'ELE');

CALL usp_insert_section_student(1, 2140);
CALL usp_insert_section_student(2, 2150);
CALL usp_insert_section_student(2, 2131);
CALL usp_insert_section_student(2, 2141);

-- to insert child assessments we first insert a parent assessment and then insert its corresponding child assessmemt (midterm, quiz, ..)
CALL usp_insert_assessment(1, 0.3, NULL);
CALL usp_insert_quiz(50::smallint, '2019-08-01');

CALL usp_insert_assessment(2, 0.5, NULL);
CALL usp_insert_quiz(40::smallint, '2019-08-04');

CALL usp_insert_assessment(3, 0.2, NULL);
CALL usp_insert_assignment('2019-03-02', '2019-03-10');

CALL usp_insert_assessment(3, 0.1, NULL);
CALL usp_insert_assignment('2019-05-01', '2019-05-15');

CALL usp_insert_assessment(1, 0.3, NULL);
CALL usp_insert_assignment('2019-01-16', '2019-01-16');

CALL usp_insert_assessment(1, 0.3, NULL);
CALL usp_insert_midterm('d2', '2019-04-15', 120::smallint);

CALL usp_insert_assessment(2, 0.3, NULL);
CALL usp_insert_final('d1', '2019-05-03', 150::smallint);

CALL usp_insert_assessment(3, 0.3, NULL);
CALL usp_insert_final('e2', '2018-01-07', 180::smallint);


CALL usp_insert_question('question_body_1', 0.2, 1);
CALL usp_insert_question('question_body_2', 0.3, 1);
CALL usp_insert_question('question_body_3', 0.2, 1);
CALL usp_insert_question('q_1', 0.4, 2);
CALL usp_insert_question('q_2', 0.1, 2);

CALL usp_insert_question_courselearningobjective(1, 1, 2::smallint);

CALL usp_insert_question_keyLearningOutcome(1, 1, 5::smallint);


CALL usp_insert_assessment_student(2140, 1, 91.0);
CALL usp_insert_assessment_student(2150, 2, 61.0);
CALL usp_insert_assessment_student(2131, 3, 41.0);
CALL usp_insert_assessment_student(2141, 1, 41.0);



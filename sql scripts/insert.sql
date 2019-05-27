CALL usp_insert_department('BBM', 'Computer Engineering');
CALL usp_insert_department('ELE', 'Electrical Engineering');
CALL usp_insert_department('EMU', 'Industrial Engineering');
CALL usp_insert_department('IMU', 'Civil Engineering');

CALL usp_insert_curriculum(1, 'BBM');
CALL usp_insert_curriculum(1, 'ELE');
CALL usp_insert_curriculum(1, 'EMU');
CALL usp_insert_curriculum(1, 'IMU');
CALL usp_insert_curriculum(2, 'BBM');
CALL usp_insert_curriculum(2, 'ELE');
CALL usp_insert_curriculum(2, 'EMU');
CALL usp_insert_curriculum(2, 'IMU');

CALL usp_insert_instructor('Fuat', 'Akal', 'BBM');
CALL usp_insert_instructor('Adnan', 'Ozsoy', 'BBM');
CALL usp_insert_instructor('Engin', 'Demir', 'BBM');
CALL usp_insert_instructor('Burcu', 'Can', 'BBM');
CALL usp_insert_instructor('Umut', 'Aslan', 'EMU');
CALL usp_insert_instructor('Yusuf', 'Oglu', 'ELE');
CALL usp_insert_instructor('Mehmet', 'Beyaz', 'IMU');

CALL usp_insert_course('BBM471', 'Intro to DBMS', 10::smallint);
CALL usp_insert_course('BBM495', 'Intro to NLP', 10::smallint);
CALL usp_insert_course('BBM451', 'Intro Networking', 10::smallint);
CALL usp_insert_course('BBM441', 'Intro Parallel Processing', 6::smallint);
CALL usp_insert_course('EMU475', 'Intro to PM', 10::smallint);
CALL usp_insert_course('EMU446', 'Supply Chain', 6::smallint);
CALL usp_insert_course('EMU443', 'Revenue Management', 6::smallint);
CALL usp_insert_course('ELE110', 'Intro to ELE', 5::smallint);
CALL usp_insert_course('ELE290', 'Intro to Quantum Electric', 5::smallint);
CALL usp_insert_course('IMU102', 'Intro to Civil Egineering', 4::smallint);
CALL usp_insert_course('IMU348', 'Intro to Interior Design', 5::smallint);

CALL usp_insert_curriculum_course(1, 'BBM471');
CALL usp_insert_curriculum_course(1, 'BBM495');
CALL usp_insert_curriculum_course(1, 'BBM451');
CALL usp_insert_curriculum_course(1, 'BBM451');
CALL usp_insert_curriculum_course(1, 'EMU475'); 
CALL usp_insert_curriculum_course(2, 'EMU446');
CALL usp_insert_curriculum_course(2, 'EMU443');
CALL usp_insert_curriculum_course(1, 'ELE110');
CALL usp_insert_curriculum_course(1, 'ELE290');
CALL usp_insert_curriculum_course(1, 'IMU102');
CALL usp_insert_curriculum_course(1, 'IMU348');

CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_1', 'BBM');
CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_2', 'BBM');
CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_3', 'BBM');
CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_4', 'BBM');
CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_5', 'BBM');
CALL usp_insert_keylearningoutcome('BBM_keylearningoutcome_6', 'BBM');
CALL usp_insert_keylearningoutcome('ELE_keylearningoutcome', 'ELE');
CALL usp_insert_keylearningoutcome('EMU_keylearningoutcome', 'EMU');
CALL usp_insert_keylearningoutcome('IMU_keylearningoutcome', 'IMU');

CALL usp_insert_semester('fall', '2019');
CALL usp_insert_semester('spring', '2019');
CALL usp_insert_semester('spring', '2017');
CALL usp_insert_semester('summer', '2018');

CALL usp_insert_courseLearningObjective('BBM471', 'BBM471_courseLearningObjective_1');
CALL usp_insert_courseLearningObjective('BBM471', 'BBM471_courseLearningObjective_2');
CALL usp_insert_courseLearningObjective('BBM451', 'BBM451_courseLearningObjective');
CALL usp_insert_courseLearningObjective('BBM495', 'BBM495_courseLearningObjective');
CALL usp_insert_courseLearningObjective('ELE110', 'ELE110_courseLearningObjective');
CALL usp_insert_courseLearningObjective('EMU446', 'EMU446_courseLearningObjective');
CALL usp_insert_courseLearningObjective('EMU475', 'EMU475_courseLearningObjective');

CALL usp_insert_courseoffering(1, 'BBM471', NULL);
CALL usp_insert_courseoffering(1, 'BBM495', NULL);
CALL usp_insert_courseoffering(1, 'BBM451', NULL);
CALL usp_insert_courseoffering(2, 'BBM441', NULL);
CALL usp_insert_courseoffering(2, 'EMU475', NULL);
CALL usp_insert_courseoffering(2, 'EMU446', NULL);
CALL usp_insert_courseoffering(2, 'EMU443', NULL);
CALL usp_insert_courseoffering(3, 'ELE110', NULL);
CALL usp_insert_courseoffering(3, 'ELE290', NULL);
CALL usp_insert_courseoffering(4, 'ELE110', NULL);

CALL usp_insert_section(1, 1);  --1
CALL usp_insert_section(1, 2);  --2 
CALL usp_insert_section(2, 1);  --3
CALL usp_insert_section(3, 1);  --4
CALL usp_insert_section(4, 1);  --5
CALL usp_insert_section(4, 2);  --6
CALL usp_insert_section(4, 3);  --7
CALL usp_insert_section(4, 4);  --8
CALL usp_insert_section(5, 1);  --9
CALL usp_insert_section(6, 1);  --10
CALL usp_insert_section(7, 1);  --11

CALL usp_insert_section_instructor(1, 1);
CALL usp_insert_section_instructor(2, 2);
CALL usp_insert_section_instructor(3, 2);
CALL usp_insert_section_instructor(4, 2);
CALL usp_insert_section_instructor(5, 1);
CALL usp_insert_section_instructor(6, 2);
CALL usp_insert_section_instructor(7, 3);
CALL usp_insert_section_instructor(8, 4);
CALL usp_insert_section_instructor(9, 5);
CALL usp_insert_section_instructor(10, 5);

CALL usp_insert_student(2140, 'Hazem', 'White', 'BBM');         --1
CALL usp_insert_student(2150, 'George', 'Gerogenazi', 'BBM');   --2
CALL usp_insert_student(2141, 'Bilal', 'Oglu', 'BBM');          --3 
CALL usp_insert_student(2145, 'Ali', 'Yapistirici', 'BBM');     --4
CALL usp_insert_student(2156, 'Mahmut', 'Birinci', 'BBM');      --5
CALL usp_insert_student(2147, 'Hayat', 'Ekinci', 'BBM');        --6
CALL usp_insert_student(2164, 'Donald', 'Trumpa', 'BBM');       --7
CALL usp_insert_student(2165, 'Ibrahim', 'Tatlises', 'BBM');    --8 
CALL usp_insert_student(2130, 'Ahmad', 'Miri', 'EMU');          --9
CALL usp_insert_student(2131, 'Defne', 'Yekta', 'EMU');         --10
CALL usp_insert_student(2141, 'Ahmet', 'Gorkem', 'ELE');        --11
CALL usp_insert_student(2144, 'Murat', 'Boz', 'IMU');           --12

CALL usp_insert_section_student(1, 2140);
CALL usp_insert_section_student(1, 2150);
CALL usp_insert_section_student(1, 2141);
CALL usp_insert_section_student(1, 2145);
CALL usp_insert_section_student(1, 2156);
CALL usp_insert_section_student(1, 2147);
CALL usp_insert_section_student(1, 2164);

-- to insert child assessments we first insert a parent assessment and then insert its corresponding child assessmemt (midterm, quiz, ..)
CALL usp_insert_assessment(1, 0.25, NULL);   --1
CALL usp_insert_examination('D1', '2019-08-01' ,100::smallint, 'midterm');

CALL usp_insert_assessment(1, 0.25, NULL);   --2
CALL usp_insert_examination('D10', '2019-09-03' ,110::smallint, 'midterm');

CALL usp_insert_assessment(1, 0.1, NULL);   --4
CALL usp_insert_assignment('2019-09-07', '2019-09-10');

CALL usp_insert_assessment(1, 0.1, NULL);   --5
CALL usp_insert_assignment('2019-10-06', '2019-10-16');

CALL usp_insert_assessment(1, 0.3, NULL);   --2
CALL usp_insert_examination('D10', '2019-11-13' ,150::smallint, 'final');




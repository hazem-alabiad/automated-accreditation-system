--1 Return learning outcomes of CS department
CREATE VIEW cs_key_learning_outcomes AS
    SELECT *
    FROM keylearningoutcome klo
    WHERE klo.dept_code LIKE 'BBM';

--2 Return All courses recently "last semester" offered by CS department
CREATE VIEW all_cs_course_recently_offering AS
    SELECT co.*, s.year, s.type
    FROM courseoffering co, semester s
    WHERE co.course_code LIKE 'BBM%' AND co.semester_id=s.id AND co.semester_id
        IN (SELECT max(sem.id)-1 as recent_semester FROM semester sem);

--3 Return All courses  offered by CS department
CREATE VIEW all_cs_course_offering AS
    SELECT co.*, s.year, s.type
    FROM courseoffering co, semester s
    WHERE co.course_code LIKE 'BBM%' AND co.semester_id=s.id;

--4 Return All questions of all courses offered by CS department
CREATE VIEW all_cs_questions_courses AS
    SELECT s.year, s.type, co.course_code, a.files, a.weight as assesment_weight, q.body, q.weight as question_weight
    FROM courseoffering co, assessment a, question q, semester s
    WHERE co.course_code LIKE 'BBM%' AND co.id=a.courseoffering_id
      AND a.id=q.assessment_id AND co.semester_id=s.id;

--5 Return All instructors of CS
CREATE VIEW all_cs_instructor AS
    SELECT *
    FROM instructor i
    WHERE i.dept_code='BBM';

--6 Return all sections of courses taught by all instructors in CS
CREATE VIEW all_cs_courses_section AS
    SELECT i.id, i.name, i.surname, co.course_code, s.number AS section_number, sem.year, sem.type
    FROM section_instructor si, section s, instructor i, courseoffering co, semester sem
    WHERE si.section_id=s.id AND si.instructor_id=i.id AND s.courseoffering_id=co.id
      AND sem.id=co.semester_id AND co.course_code LIKE 'BBM%'
    GROUP BY sem.year, sem.type, i.id, i.name, i.surname, co.course_code, section_number
    ORDER BY sem.year DESC;

--7 Return feedback 'key and course learning outcome' of all CS offered courses
CREATE VIEW feedback_all_cs_courses AS
    SELECT s.year, s.type, co.course_code, q.weight, q.id, q.body
    FROM question q, assessment a, courseoffering co, semester s
    WHERE q.assessment_id=a.id AND a.courseoffering_id=co.id
      AND co.course_code LIKE 'BBM%' AND s.id=co.semester_id
    GROUP BY s.year, s.type, q.id, co.course_code, q.weight, q.body
    ORDER BY s.year DESC;
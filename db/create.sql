DROP schema if exists public cascade;
create schema public;

CREATE TABLE Department(
    Code    Varchar(10),
    Name varchar(25),
    PRIMARY KEY (code)
);

Create procedure usp_insert_department(dep_code Varchar(10), dep_name varchar(25))
Language sql
As $$ INSERT INTO department VALUES(dep_code, dep_name)$$;

Create procedure usp_update_department(dep_code Varchar(10), new_name varchar(25) )
Language sql
As $$ update Department set Name = new_name  where Code = dep_code$$;

Create procedure usp_delete_department (dep_code Varchar(10))
Language sql
As $$ delete from Department where Code = dep_code  $$;

--------------------------------------------------------------
create sequence curriculum_id_seq;

CREATE TABLE Curriculum (
    id int default nextval('curriculum_id_seq') not null,
    version int,
    dept_code Varchar(10),
    PRIMARY KEY (id),
    FOREIGN KEY (dept_code) REFERENCES Department(code)
);

Create procedure usp_insert_curriculum  (c_version int, c_dept_code Varchar(10))
Language sql
As $$ INSERT INTO Curriculum VALUES (default ,c_version, c_dept_code)$$;

Create procedure usp_update_curriculum  (c_id int ,new_version int, new_dept_code Varchar(10))
Language sql
As $$ update Curriculum set  version = new_version, dept_code = new_dept_code where id = c_id$$;

Create procedure usp_delete_curriculum (c_id int)
    Language sql
As $$ delete from Curriculum where id = c_id  $$;

------------------------------------------------------
CREATE sequence key_learning_outcome_id_seq;

CREATE TABLE keyLearningOutcome(
    id int default nextval('key_learning_outcome_id_seq') not null,
    body varchar(1000),
    dept_code varchar(10),
    PRIMARY KEY (id),
    FOREIGN KEY (dept_code) REFERENCES Department(code)
);

Create procedure usp_insert_keyLearningOutcome  (o_body varchar(1000) , o_dept_code varchar(10))
Language sql
As $$ INSERT INTO keyLearningOutcome VALUES(default, o_body, o_dept_code)  $$;

Create procedure usp_update_keyLearningOutcome  (o_id int ,new_body varchar(1000) , new_dept_code varchar(10))
Language sql
As $$ update keyLearningOutcome set body = new_body, dept_code = new_dept_code where id = o_id$$;

Create procedure usp_delete_keyLearningOutcome (o_id int)
    Language sql
As $$ delete from keyLearningOutcome where id = o_id $$;

-----------------------------------------------------
create sequence semester_id_seq;

CREATE TABLE semester (
    id int default nextval('semester_id_seq') not null,
    type varchar(10),
    year char(4),
    PRIMARY KEY(id)
);
Create procedure usp_insert_semester (s_type varchar(10), s_year char(4))
    Language sql
As $$ INSERT INTO semester VALUES(default, s_type, s_year)$$;

Create procedure usp_update_semester (s_id int ,new_type varchar(10), new_year char(4))
    Language sql
As $$ update semester set type = new_type, year = new_year where id = s_id$$;

Create procedure usp_delete_semester (s_id int)
    Language sql
As $$ delete from semester where id = s_id $$;

-----------------------------------------------------
create sequence instructor_id_seq;

CREATE TABLE instructor(
    id int default nextval('instructor_id_seq') not null,
    name varchar(255),
    Surname varchar(255),
    dept_code Varchar(10),
    PRIMARY KEY(id),
    FOREIGN KEY(dept_code) REFERENCES Department (code)
);
Create procedure usp_insert_instructor (i_name varchar(255), i_surname varchar(255), i_dept_code varchar(10))
    Language sql
As $$ insert into instructor values(default, i_name, i_surname, i_dept_code) $$;

Create procedure usp_update_instructor ( i_id int, new_name varchar(255), new_surname varchar(255), new_dept_code varchar(10))
    Language sql
As $$ update instructor set name = new_name, Surname = new_surname, dept_code = new_dept_code where id = i_id$$;

Create procedure usp_delete_instructor (i_id int)
    Language sql
As $$ delete from instructor where id = i_id$$;
-------------------------------------------------
CREATE TABLE course (
    code varchar(10),
    name varchar(255),
    credit smallint,
    PRIMARY KEY(code)
);

Create procedure usp_insert_course(c_code varchar(10), c_name varchar(255), c_credit smallint)
    Language sql
As $$ insert into course values(c_code, c_name, c_credit)$$;

Create procedure usp_update_course(c_code varchar(10), new_name varchar(255), new_credit smallint)
    Language sql
As $$ update course set name = new_name, credit = new_credit where code = c_code$$;

Create procedure usp_delete_course (c_code varchar(10))
    Language sql
As $$ delete from course where code = c_code$$;
-------------------------------------------------
CREATE TABLE curriculum_course(
    curriculum_id int,
    course_code varchar(10),
    PRIMARY KEY(curriculum_id , course_code),
    FOREIGN KEY(curriculum_id) REFERENCES Curriculum (id),
    FOREIGN KEY(course_code) REFERENCES course (Code)
);
Create procedure usp_insert_curriculum_course(c_curriculum_id int, c_course_code varchar(10))
    Language sql
As $$ insert into curriculum_course values(c_curriculum_id, c_course_code)$$;


Create procedure usp_delete_curriculum_course (c_curriculum_id int, c_course_code varchar(10))
    Language sql
As $$ delete from curriculum_course where curriculum_id = c_curriculum_id and course_code = c_course_code $$;

-----------------------------------------------
create sequence course_learning_objective_id_seq;

CREATE TABLE courseLearningObjective(
    id int default nextval('course_learning_objective_id_seq') not null,
    course_code varchar(10),
    Body varchar(1000) ,
    PRIMARY KEY(Id),
    FOREIGN KEY(course_code) REFERENCES course (code)
);
Create procedure usp_insert_courseLearningObjective(c_course_code varchar(10), c_body varchar(1000))
    Language sql
As $$ insert into courseLearningObjective values(default, c_course_code, c_body) $$;

Create procedure usp_update_courseLearningObjective(c_id int ,new_course_code varchar(10), new_body varchar(1000))
    Language sql
As $$ update courseLearningObjective set course_code = new_course_code, Body = new_body where id = c_id$$;

Create procedure usp_delete_courseLearningObjective (c_id int)
    Language sql
As $$ delete from courseLearningObjective where id = c_id $$;
---------------------------------------
create sequence course_offering_id_seq;

CREATE TABLE courseOffering (
    id int default nextval('course_offering_id_seq') not null,
    semester_id int,
    course_code varchar(10),
    letter_grades bytea,
    PRIMARY KEY(id),
    FOREIGN KEY(semester_id) REFERENCES semester(id),
    FOREIGN KEY(course_code) REFERENCES course (code)
);

Create procedure usp_insert_courseOffering(c_semester_id int, c_course_code varchar(10), c_letter_grades bytea)
    Language sql
As $$ insert into courseOffering values(default, c_semester_id, c_course_code, c_letter_grades) $$;

Create procedure usp_update_courseOffering(c_id int,new_semester_id int, new_course_code varchar(10), new_letter_grades bytea)
    Language sql
As $$ update courseOffering set semester_id = new_semester_id, course_code = new_course_code, letter_grades = new_letter_grades where id = c_id$$;

Create procedure usp_delete_courseOffering(c_id int)
    Language sql
As $$ delete from courseOffering where id = c_id $$;
----------------------------------------------------
create sequence assessment_id_seq;

CREATE TABLE assessment  (
    id int default nextval('assessment_id_seq') not null,
    courseOffering_id int,
    files bytea,
    weight float,
    PRIMARY KEY(id),
    FOREIGN KEY(courseOffering_id) REFERENCES courseOffering (id)
);
Create procedure usp_insert_assessment(a_course_offering_id int, a_weight float, a_files bytea)
    Language sql
As $$ insert into assessment values(default, a_course_offering_id, a_files, a_weight) $$;

Create procedure usp_update_assessment(a_id int,new_course_offering_id int, new_weight float, new_files bytea)
    Language sql
As $$ update assessment set courseOffering_id = new_course_offering_id, weight = new_weight, files = new_files where id = a_id $$;

Create procedure usp_delete_assessment(a_id int)
    Language sql
As $$ delete from assessment where id = a_id $$;
----------------------------------------------------
CREATE SEQUENCE question_id_seq;

CREATE TABLE question (
    id int default nextval('question_id_seq'),
    body varchar(1000),
    weight float,
    assessment_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(assessment_id) REFERENCES assessment (id)
);
Create procedure usp_insert_question(q_body varchar(1000), q_weight float, q_assessment_id int)
    Language sql
As $$ insert into question values(default, q_body, q_weight, q_assessment_id) $$;

Create procedure usp_update_question(q_id int,new_body varchar(1000), new_weight float, new_assessment_id int)
    Language sql
As $$ update question set body = new_body, weight = new_weight, assessment_id = new_assessment_id where id = q_id $$;

Create procedure usp_delete_question(q_id int)
    Language sql
As $$ delete from question where id = q_id $$;

----------------------------------------------------
CREATE TABLE question_courseLearningObjective(
    question_id int,
    courseLearningObjective_id int,
    Value smallint,
    PRIMARY KEY (courseLearningObjective_id, question_id),
    FOREIGN KEY (courseLearningObjective_id) REFERENCES courseLearningObjective (id),
    FOREIGN KEY (question_id) REFERENCES question (id)
);
Create procedure usp_insert_question_courseLearningObjective(q_question_id int, q_courseLearningObjective_id int, q_value smallint)
    Language sql
As $$ insert into question_courseLearningObjective values(q_question_id, q_courseLearningObjective_id, q_value)$$;

Create procedure usp_update_question_courseLearningObjective(q_question_id int, q_courseLearningObjective_id int, new_value smallint)
    Language sql
As $$ update question_courseLearningObjective set Value = new_value
      where question_id = q_question_id and courseLearningObjective_id = q_courseLearningObjective_id$$;

Create procedure usp_delete_question_courseLearningObjective(q_question_id int, q_courseLearningObjective_id int)
    Language sql
As $$ delete from question_courseLearningObjective where question_id = q_question_id and courseLearningObjective_id = q_courseLearningObjective_id $$;

----------------------------------------------------

CREATE TABLE question_keyLearningOutcome(
    question_id int,
    key_learning_outcome_id int,
    Value smallint,
    PRIMARY KEY (question_id, key_learning_outcome_id),
    FOREIGN KEY (question_id) REFERENCES question(id),
    FOREIGN KEY (key_learning_outcome_id) REFERENCES keyLearningOutcome (id)
);
Create procedure usp_insert_question_keyLearningOutcome(q_question_id int, q_keyLearningOutcome_id int, q_value smallint)
    Language sql
As $$ insert into question_keyLearningOutcome values(q_question_id, q_keyLearningOutcome_id, q_value)$$;

Create procedure usp_update_question_keyLearningOutcome(q_question_id int, q_keyLearningOutcome_id int, new_value smallint)
    Language sql
As $$ update question_keyLearningOutcome set Value = new_value
       where question_id = q_question_id and key_learning_outcome_id = q_keyLearningOutcome_id$$;

Create procedure usp_delete_question_keyLearningOutcome(q_question_id int, q_keyLearningOutcome_id int)
    Language sql
As $$ delete from question_keyLearningOutcome where question_id = q_question_id and key_learning_outcome_id = q_keyLearningOutcome_id$$;

----------------------------------------------------
CREATE SEQUENCE section_id_seq;

CREATE TABLE section (
    id int default nextval('section_id_seq'),
    courseOffering_id int,
    number int,
    PRIMARY KEY (id),
    FOREIGN KEY (courseOffering_id) REFERENCES courseOffering (id)
);
Create procedure usp_insert_section(s_courseOffering_id int, s_number int)
    Language sql
As $$ insert into section values(default, s_courseOffering_id, s_number) $$;

Create procedure usp_update_section(s_id int,new_courseOffering_id int, new_number int)
    Language sql
As $$ update section set courseOffering_id = new_courseOffering_id, number = new_number where id = s_id$$;

Create procedure usp_delete_section(s_id int)
    Language sql
As $$delete from section where id = s_id$$;

----------------------------------------------------
CREATE TABLE section_instructor (
    section_id int,
    instructor_id int,
    PRIMARY KEY (section_id, instructor_id),
    FOREIGN KEY (section_id) REFERENCES section (id),
    FOREIGN KEY (instructor_id) REFERENCES instructor (id)
);
Create procedure usp_insert_section_instructor(s_section_id int, s_instructor_id int)
    Language sql
As $$ insert into section_instructor values(s_section_id, s_instructor_id)$$;

Create procedure usp_delete_section_instructor(s_section_id int, s_instructor_id int)
    Language sql
As $$ delete from section_instructor where section_id = s_section_id and instructor_id = s_instructor_id$$;

----------------------------------------------------
CREATE TABLE student  (
    id int,
    name varchar(30),
    surname varchar(30),
    dep_code varchar(10),
    PRIMARY KEY(id),
    FOREIGN KEY (dep_code) REFERENCES Department (Code)
);
Create procedure usp_insert_student(s_id int,s_name varchar(30), s_surname varchar(30), s_dep_code varchar(10))
    Language sql
As $$ insert into student values(s_id, s_name, s_surname, s_dep_code)  $$;

Create procedure usp_update_student(s_id int,new_name varchar(30), new_surname varchar(30), s_dep_code varchar(10))
    Language sql
As $$ update student set name = new_name, surname = new_surname, dep_code = s_dep_code where id = s_id$$;

Create procedure usp_delete_student(s_id int)
    Language sql
As $$ delete from student where id = s_id$$;

----------------------------------------------------
CREATE TABLE  section_student(
    section_id int,
    student_id int,
    PRIMARY KEY(section_id, student_id),
    FOREIGN KEY(section_id) REFERENCES section(id),
    FOREIGN KEY(student_id) REFERENCES student(id)
);
Create procedure usp_insert_section_student(s_section_id int, s_student_id int)
    Language sql
As $$ insert into section_student values(s_section_id, s_student_id)  $$;

Create procedure usp_delete_section_student(s_section_id int, s_student_id int)
    Language sql
As $$ delete from section_student where section_id = s_section_id and student_id = s_student_id$$;

----------------------------------------------------
CREATE TABLE assessment_student (
    student_id int,
    assessment_id int,
    grade float,
    PRIMARY KEY(student_id, assessment_id),
    FOREIGN KEY(student_id) REFERENCES student(id),
    FOREIGN KEY(assessment_id) REFERENCES assessment(id)
);
Create procedure usp_insert_assessment_student(a_student_id int, a_assessment_id int, a_grade float)
    Language sql
As $$ insert into assessment_student values(a_student_id, a_assessment_id, a_grade)  $$;

Create procedure usp_update_assessment_student(a_student_id int, a_assessment_id int, new_grade float)
    Language sql
As $$ update assessment_student set grade = new_grade
       where assessment_id = a_assessment_id and student_id = a_student_id$$;

Create procedure usp_delete_assessment_student(a_student_id int, a_assessment_id int)
    Language sql
As $$ delete from assessment_student where student_id = a_student_id and assessment_id = a_assessment_id$$;

----------------------------------------------------
CREATE SEQUENCE quiz_id_seq;

CREATE TABLE quiz (
    id int default nextval('quiz_id_seq'),
    courseOffering_id int,
    files bytea,
    weight float,
    duration smallint,
    date date,
    PRIMARY KEY(id)
);
Create procedure usp_insert_quiz(q_course_offering_id int,q_files bytea,q_weight float, q_duration smallint,q_date date)
    Language sql
As $$ insert into quiz values(default, q_course_offering_id, q_files, q_weight, q_duration, q_date)  $$;

Create procedure usp_update_quiz(q_id int,new_course_offering_id int,new_files bytea,new_weight float, new_duration smallint,new_date date)
    Language sql
As $$ update quiz set courseOffering_id = new_course_offering_id, files = new_files,
                      weight = new_weight, duration = new_duration, date = new_date
                        where id = q_id$$;

Create procedure usp_delete_quiz(q_id int)
    Language sql
As $$ delete from quiz where id = q_id$$;

----------------------------------------------------
CREATE SEQUENCE assignment_id_seq;

CREATE TABLE assignment (
    id int default nextval('assignment_id_seq'),
    courseOffering_id int,
    files bytea,
    weight float,
    start_date date,
    due_date date,
    PRIMARY KEY(id)
);
Create procedure usp_insert_assignment(a_course_offering_id int,a_files bytea,a_weight float, a_start_date date, a_due_date date)
    Language sql
As $$ insert into assignment values(default, a_course_offering_id, a_files, a_weight, a_start_date, a_due_date)$$;

Create procedure usp_update_assignment(a_id int,new_course_offering_id int,new_files bytea,new_weight float, new_start_date date, new_duedate date)
    Language sql
As $$ update assignment set courseOffering_id = new_course_offering_id, files = new_files, weight = new_weight, start_date = new_start_date,
                            due_date = new_duedate where id = a_id$$;

Create procedure usp_delete_assignment(a_id int)
    Language sql
As $$ delete from assignment where id = a_id$$;

----------------------------------------------------
CREATE sequence midterm_id_seq;

CREATE TABLE midterm (
    id int default nextval('midterm_id_seq'),
    courseOffering_id int,
    files bytea,
    weight float,
    room varchar(10),
    date date,
    duration smallint,
    PRIMARY KEY(id)
);
Create procedure usp_insert_midterm(m_course_offering_id int,m_files bytea ,m_weight float, m_room varchar(10),m_date date, m_duration smallint)
    Language sql
As $$ insert into midterm values(default, m_course_offering_id, m_files, m_weight, m_room, m_date, m_duration) $$;

Create procedure usp_update_midterm(m_id int,new_course_offering_id int,new_files bytea ,new_weight float,
                            new_room varchar(10),new_date date, new_duration smallint)
    Language sql
As $$ update midterm set courseOffering_id = new_course_offering_id, files = new_files, weight = new_weight,
                        room = new_room, date = new_date, duration = new_duration where id = m_id $$;

Create procedure usp_delete_midterm(m_id int)
    Language sql
As $$ delete from midterm where id = m_id$$;

----------------------------------------------------
CREATE SEQUENCE final_id_seq;

CREATE TABLE final (
    id int default nextval('final_id_seq'),
    courseOffering_id int,
    files bytea,
    weight float,
    room varchar(10),
    date date,
    duration smallint,
    PRIMARY KEY(id)
);
Create procedure usp_insert_final(f_course_offering_id int,f_files bytea ,f_weight float,f_room varchar(10) ,f_date date,
                                 f_duration smallint)
    Language sql
As $$  insert into final values(default, f_course_offering_id, f_files, f_weight, f_room, f_date, f_duration) $$;

Create procedure usp_update_final(f_id int,new_course_offering_id int,new_files bytea ,new_weight float,new_room varchar(10) ,new_date date,
                                  new_duration smallint)
    Language sql
As $$ update final set courseOffering_id = new_course_offering_id, files = new_files, weight = new_weight, room = new_room,
        date = new_date, duration = new_duration where id = f_id$$;

Create procedure usp_delete_final(f_id int)
    Language sql
As $$ delete from final where id = f_id $$;

----------------------------------------------------
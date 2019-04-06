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

Create procedure usp_update_department(new_code Varchar(10), new_name varchar(25) )
Language sql
As $$ update Department set Code=new_code, Name=new_name  where Code = new_code$$;

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

Create procedure usp_update_curriculum  (new_version int, new_dept_code Varchar(10), c_id int)
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

Create procedure usp_update_keyLearningOutcome  (new_body varchar(1000) , new_dept_code varchar(10), o_id int)
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

Create procedure usp_update_semester (new_type varchar(10), new_year char(4),s_id int)
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

Create procedure usp_update_curriculum_course(new_curriculum_id int, new_course_code varchar(10),
                                              c_curriculum_id int, c_course_code varchar(10))
    Language sql
As $$ update curriculum_course set curriculum_id = new_curriculum_id, course_code = new_course_code
        where curriculum_id = c_curriculum_id and course_code = c_course_code$$;

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

----------------------------------------------------

CREATE TABLE question_courseLearningObjective(
                                                 question_id int,
                                                 courseLearningObjective_id int,
                                                 Value smallint,
                                                 PRIMARY KEY (courseLearningObjective_id, question_id),
                                                 FOREIGN KEY (courseLearningObjective_id) REFERENCES courseLearningObjective (id),
                                                 FOREIGN KEY (question_id) REFERENCES question (id)
);

----------------------------------------------------

CREATE TABLE question_keyLearningOutcome(
                                            question_id int,
                                            key_learning_outcome_id int,
                                            Value smallint,
                                            PRIMARY KEY (question_id, key_learning_outcome_id),
                                            FOREIGN KEY (question_id) REFERENCES question(id),
                                            FOREIGN KEY (key_learning_outcome_id) REFERENCES keyLearningOutcome (id)
);

----------------------------------------------------

CREATE SEQUENCE section_id_seq;

CREATE TABLE section (
                         id int default nextval('section_id_seq'),
                         courseOffering_id int,
                         number int,
                         PRIMARY KEY (id),
                         FOREIGN KEY (courseOffering_id) REFERENCES courseOffering (id)
);

----------------------------------------------------

CREATE TABLE section_instructor (
                                    section_id int,
                                    instructor_id int,
                                    PRIMARY KEY (section_id, instructor_id),
                                    FOREIGN KEY (section_id) REFERENCES section (id),
                                    FOREIGN KEY (instructor_id) REFERENCES instructor (id)
);

----------------------------------------------------

CREATE SEQUENCE student_id_seq;

CREATE TABLE student  (
                          id int default nextval('student_id_seq'),
                          name varchar(30),
                          surname varchar(30),
                          PRIMARY KEY(id)
);

----------------------------------------------------

CREATE TABLE  section_student(
                                 section_id int,
                                 student_id int,
                                 PRIMARY KEY(section_id, student_id),
                                 FOREIGN KEY(section_id) REFERENCES section(id),
                                 FOREIGN KEY(student_id) REFERENCES student(id)
);

----------------------------------------------------

CREATE TABLE assessment_student (
                                    student_id int,
                                    assessment_id int,
                                    grade float,
                                    PRIMARY KEY(student_id, assessment_id),
                                    FOREIGN KEY(student_id) REFERENCES student(id),
                                    FOREIGN KEY(assessment_id) REFERENCES assessment(id)
);

----------------------------------------------------

CREATE SEQUENCE quiz_id_seq;

CREATE TABLE quiz (
                      id int default nextval('quiz_id_seq'),
                      duration smallint,
                      PRIMARY KEY(id)
);

----------------------------------------------------

CREATE SEQUENCE assignment_id_seq;

CREATE TABLE assignment (
                            id int default nextval('assignment_id_seq'),
                            start_date date,
                            due_date date,
                            PRIMARY KEY(id)
);

----------------------------------------------------

CREATE sequence midterm_id_seq;

CREATE TABLE midterm (
                         id int default nextval('midterm_id_seq'),
                         room smallint,
                         date date,
                         duration smallint,
                         PRIMARY KEY(id)
);

----------------------------------------------------

CREATE SEQUENCE final_id_seq;

CREATE TABLE final (
                       id int default nextval('final_id_seq'),
                       room smallint,
                       date date,
                       duration smallint,
                       PRIMARY KEY(id)
);

----------------------------------------------------
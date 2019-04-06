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

Create procedure usp_update_semester (s_type varchar(10), s_year char(4),s_id int)
    Language sql
As $$ update semester set type = s_type, year = s_year where id = s_id$$;

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

-------------------------------------------------
CREATE TABLE course (
    code varchar(10),
    name varchar(255),
    credit smallint,
    PRIMARY KEY(code)
);

-------------------------------------------------
CREATE TABLE curriculum_course(
    curriculum_id int,
    course_code varchar(10),
    PRIMARY KEY(curriculum_id , course_code),
    FOREIGN KEY(curriculum_id) REFERENCES Curriculum (id),
    FOREIGN KEY(course_code) REFERENCES course (Code)
);

-----------------------------------------------
create sequence course_learning_objective_id_seq;

CREATE TABLE courseLearningObjective(
    id int default nextval('course_learning_objective_id_seq') not null,
    course_code varchar(10),
    Body varchar(1000) ,
    PRIMARY KEY(Id),
    FOREIGN KEY(course_code) REFERENCES course (code)
);

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
---------------------------------------------------
CREATE TABLE question (
    id int,
    body varchar(1000),
    weight float,
    assessment_id int,
    PRIMARY KEY(id),
    FOREIGN KEY(assessment_id) REFERENCES assessment (id)
);

CREATE TABLE question_courseLearningObjective(
    question_id int,
    courseLearningObjective_id int,
    Value smallint,
    PRIMARY KEY (courseLearningObjective_id, question_id),
    FOREIGN KEY (courseLearningObjective_id) REFERENCES courseLearningObjective (id),
    FOREIGN KEY (question_id) REFERENCES question (id)
);

CREATE TABLE question_keyLearningOutcome(
    question_id int,
    key_learning_outcome_id int,
    Value smallint,
    PRIMARY KEY (question_id, key_learning_outcome_id),
    FOREIGN KEY (question_id) REFERENCES question(id),
    FOREIGN KEY (key_learning_outcome_id) REFERENCES keyLearningOutcome (id)
);

CREATE TABLE section (
    id int,
    courseOffering_id int,
    number int,
    PRIMARY KEY (id),
    FOREIGN KEY (courseOffering_id) REFERENCES courseOffering (id)
);

CREATE TABLE section_instructor (
    section_id int,
    instructor_id int,
    PRIMARY KEY (section_id, instructor_id),
    FOREIGN KEY (section_id) REFERENCES section (id),
    FOREIGN KEY (instructor_id) REFERENCES instructor (id)
);

CREATE TABLE student  (
    id int,
    name varchar(30),
    surname varchar(30),
    PRIMARY KEY(id)
);

CREATE TABLE  section_student(
    section_id int,
    student_id int,
    PRIMARY KEY(section_id, student_id),
    FOREIGN KEY(section_id) REFERENCES section(id),
    FOREIGN KEY(student_id) REFERENCES student(id)
);

CREATE TABLE assessment_student (
    student_id int,
    assessment_id int,
    grade float,
    PRIMARY KEY(student_id, assessment_id),
    FOREIGN KEY(student_id) REFERENCES student(id),
    FOREIGN KEY(assessment_id) REFERENCES assessment(id)
);

CREATE TABLE quiz (
    id int,
    duration smallint,
    PRIMARY KEY(id)
);

CREATE TABLE assignment (
    id int,
    start_date date,
    due_date date,
    PRIMARY KEY(id)
);

CREATE TABLE midterm (
    id int,
    room smallint,
    date date,
    duration smallint,
    PRIMARY KEY(id)
);

CREATE TABLE final (
    id int,
    room smallint,
    date date,
    duration smallint,
    PRIMARY KEY(id)
);




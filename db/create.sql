CREATE TABLE Department(
    Code    Varchar(10),
    Name varchar(25),
    PRIMARY KEY (code)
);

CREATE TABLE Curriculum (
    id int,
    version int,
    dept_code Varchar(10),
    PRIMARY KEY (id),
    FOREIGN KEY (dept_code) REFERENCES Department(code)
);

CREATE TABLE keyLearningOutcome(
    id int,
    body varchar(1000),
    dept_code varchar(10),
    PRIMARY KEY (id),
    FOREIGN KEY (dept_code) REFERENCES Department(code)
);

CREATE TABLE semester (
    id int,
    type varchar(10),
    year char(4),
    PRIMARY KEY(id)
);

CREATE TABLE instructor(
    id int,
    name varchar(255),
    Surname varchar(255),
    dept_code Varchar(10),
    PRIMARY KEY(id),
    FOREIGN KEY(dept_code) REFERENCES Department (code)
);

CREATE TABLE course (
    code varchar(10),
    name varchar(255),
    credit smallint,
    PRIMARY KEY(code)
);

CREATE TABLE curriculum_course(
    curriculum_id int,
    course_code varchar(10),
    PRIMARY KEY(curriculum_id , course_code),
    FOREIGN KEY(curriculum_id) REFERENCES Curriculum (id),
    FOREIGN KEY(course_code) REFERENCES course (Code)
);

CREATE TABLE courseLearningObjective(
    id int,
    course_code varchar(10),
    Body varchar(1000) ,
    PRIMARY KEY(Id),
    FOREIGN KEY(course_code) REFERENCES course (code)
);

CREATE TABLE courseOffering (
    id int,
    semester_id int,
    course_code varchar(10),
    letter_grades bytea,
    PRIMARY KEY(id),
    FOREIGN KEY(semester_id) REFERENCES semester(id),
    FOREIGN KEY(course_code) REFERENCES course (code)
);

CREATE TABLE assessment  (
    id int,
    courseOffering_id int,
    files bytea,
    weight float,
    PRIMARY KEY(id),
    FOREIGN KEY(courseOffering_id) REFERENCES courseOffering (id)
);

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



create table Subjects(
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(500)
);

CREATE TABLE Questions(
    id INT PRIMARY KEY IDENTITY(1, 1),
    subject_id INT,
    title NVARCHAR(500),
    text NVARCHAR(MAX),
    hardness INT,
    uploaded FLOAT,
);

CREATE TABLE Users(
    id INT PRIMARY KEY IDENTITY(1, 1),
    username NVARCHAR(100),
    password NVARCHAR(100),
    email NVARCHAR(100)
);

CREATE TABLE User_subjects(
    user_id INT,
    subject_id INT
);

CREATE TABLE User_questions(
    user_id INT,
    question_id INT
);
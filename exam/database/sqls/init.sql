create table Subjects(
    id INT PRIMARY KEY IDENTITY(1, 1),
    name NVARCHAR(500),
    user_id INT
);


CREATE TABLE Questions(
    id INT PRIMARY KEY IDENTITY(1, 1),
    user_id INT,
    subject_id INT,
    title NVARCHAR(500),
    text NVARCHAR(MAX),
    hardness INT,
    uploaded FLOAT
);

CREATE TABLE Users(
    id INT PRIMARY KEY IDENTITY(1, 1),
    password NVARCHAR(100),
    email NVARCHAR(100)
);
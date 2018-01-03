create table Subjects(
    id integer primary key,
    name NVARCHAR,
    user_id INT
);


CREATE TABLE Questions(
    id integer primary key,
    user_id INT,
    subject_id INT,
    title NVARCHAR,
    text NVARCHAR,
    hardness INT,
    uploaded FLOAT
);

CREATE TABLE Users(
    id integer primary key,
    password NVARCHAR,
    email NVARCHAR
);
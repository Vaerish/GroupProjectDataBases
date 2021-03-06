#ENTITY CODE

CREATE TABLE Account(
    username VARCHAR(20) PRIMARY KEY,
    user_password VARCHAR(50),
    most_compatible_user VARCHAR(20),
    FOREIGN KEY (most_compatible_user)
        REFERENCES Account(username)
        ON DELETE CASCADE
 );
 
 CREATE TABLE Account2(
    Attempt INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(20),
    previous_scores VARCHAR(4),
    FOREIGN KEY(username)
        REFERENCES Account(username)
        ON DELETE CASCADE,
    PRIMARY KEY(username, Attempt)
 );
 
 CREATE TABLE Famous_Figure(
    name VARCHAR(20) PRIMARY KEY,
    personality_type VARCHAR(4),
    occupation VARCHAR(80),
    appears_in VARCHAR(80)
 );
 
 CREATE TABLE Personality(
    E_I ENUM('E','I') NOT NULL,
    N_O ENUM('N','O') NOT NULL,
    T_F ENUM('T','F') NOT NULL,
    J_P ENUM('J','P') NOT NULL,
    personality_full_name VARCHAR(4) PRIMARY KEY,
    short_description VARCHAR(1000)
);

CREATE TABLE Question(
    question_number INTEGER PRIMARY KEY,
    question_text VARCHAR(150)
);

CREATE TABLE Answer(
    question_number INTEGER,
    answer_number INTEGER,
    answer_text VARCHAR(50),
    E_I_weight INTEGER,
    N_O_weight INTEGER,
    T_F_weight INTEGER,
    J_P_weight INTEGER,
    FOREIGN KEY(question_number)
        REFERENCES Question(question_number)
        ON DELETE CASCADE,
    PRIMARY KEY(question_number,answer_number)
);
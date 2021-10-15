/* Creating a new database */
CREATE DATABASE final_project_db;

/* Selecting for use the new database*/
USE final_project_db;


/* Creating User's Table*/
CREATE TABLE users(
    id_user INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_type CHAR(1) NOT NULL,
	firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(150) NOT NULL,
    city VARCHAR(40) NOT NULL,
    state CHAR(50) NOT NULL,
    password VARCHAR(250) NOT NULL,
    biography VARCHAR(400),
    isHired BOOLEAN,
    org_name VARCHAR(80),
    created_at DATETIME,
    updated_at DATETIME
);


/* Creating Language's Table*/
CREATE TABLE languages(
    id_language INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    lang_name VARCHAR(30) NOT NULL
);

/* Filling languages' table */
INSERT INTO languages(lang_name)
VALUES('HTML'),('CSS'),('Ruby'),('Python'),('SQL'),('JavaScript'),('Java'),('C++'),('Google+'),('Swift'),('Kotlin'),('Android');


/* Creating Frameworks's Table*/
CREATE TABLE framewors(
    id_framework INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    frame_name VARCHAR(30) NOT NULL
);


/* Filling frameworks's table */
INSERT INTO frameworks(frame_name)
VALUES('Flask'),('Django'),('Reils'),('Spring'),('Laravel'),('Angular'),('NodeJS'),('JavaScript'),('Google+'),('Swift'),('Kotlin'),('Android');


/* Creating Joining Table between language & developer*/
CREATE TABLE languages_developer(
    id_language INT NOT NULL,
    FOREIGN KEY (id_language) REFERENCES languages(id_language),
    id_user INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

/* Creating Joining Table between framework & developer*/
CREATE TABLE framework_developer(
    id_framework INT NOT NULL,
    FOREIGN KEY (id_framework) REFERENCES frameworks(id_framework),
    id_user INT NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user)
);

/* Creating Positions' Table*/
CREATE TABLE positions(
    id_position INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name_position VARCHAR(80) NOT NULL,
    descr_position VARCHAR(300) NOT NULL,
    isClosed BOOLEAN NOT NULL,
    id_organization INT NOT NULL,
    FOREIGN KEY (id_organization) REFERENCES users (id_user),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    
);

/* Creating Joining Table between language & positions*/
CREATE TABLE languages_positions(
    id_language INT NOT NULL,
    FOREIGN KEY (id_language) REFERENCES languages(id_language),
    id_position INT NOT NULL,
    FOREIGN KEY (id_position) REFERENCES positions(id_position)
);

/* Creating Joining Table between organizations & developer*/
CREATE TABLE organization_developer(
    id_developer INT NOT NULL,
    FOREIGN KEY (id_developer) REFERENCES users(id_user),
    id_organization INT NOT NULL,
    FOREIGN KEY (id_organization) REFERENCES users(id_user)
);



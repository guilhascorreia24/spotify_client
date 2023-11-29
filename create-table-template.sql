-- Active: 1701030489775@@127.0.0.1@5432@spotify
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

CREATE TABLE Artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Albums (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INT REFERENCES Artists(artist_id),
    release_date DATE
);

CREATE TABLE Songs (
    song_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist_id INT REFERENCES Artists(artist_id),
    album_id INT REFERENCES Albums(album_id),
    genre VARCHAR(50),
    release_date DATE
);

CREATE TABLE UserHistory (
    history_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES Users(user_id),
    song_id INT REFERENCES Songs(song_id),
    timestamp TIMESTAMP NOT NULL
);

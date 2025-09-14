USE ut2artist;

CREATE TABLE IF NOT EXISTS artist
(
    artist_id INT PRIMARY KEY AUTO_INCREMENT UNIQUE,
    name VARCHAR (255) NOT NULL,
    genre VARCHAR (255)
    );

CREATE TABLE IF NOT EXISTS album
(
    album_id INT PRIMARY KEY AUTO_INCREMENT,
    album_name VARCHAR (255) NOT NULL,
    artist_id INT,
    CONSTRAINT fk_artist_id FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
    );

CREATE TABLE IF NOT EXISTS song
(
    song_id INT PRIMARY KEY AUTO_INCREMENT,
    song_name VARCHAR (255) NOT NULL,
    artist_id INT,
    album_id INT,
    CONSTRAINT fk_song_artist_id FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
    CONSTRAINT fk_song_album_id FOREIGN KEY (album_id) REFERENCES album(album_id)
    );
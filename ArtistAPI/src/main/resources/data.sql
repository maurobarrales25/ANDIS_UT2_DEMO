USE ut2artist;

INSERT IGNORE INTO artist (name, genre) VALUES ('Queen', 'Rock');
INSERT IGNORE INTO artist (name, genre) VALUES ('Foo Fighters', 'Rock');

INSERT IGNORE INTO album(album_name, artist_id) VALUES ('Echoes of Silence Patience and Grace', '2');

INSERT IGNORE INTO song (song_name, artist_id, album_id) VALUES
('The Pretender', 2, 1),
('Let It Die', 2, 1),
('Erase/Replace', 2, 1),
('Long Road to Ruin', 2, 1),
('Come Alive', 2, 1),
('Stranger Things Have Happened', 2, 1),
('Cheer Up, Boys (Your Make Up Is Running)', 2, 1),
('Summer\'s End', 2, 1),
('Ballad of the Beaconsfield Miners', 2, 1),
('Statues', 2, 1),
('Home', 2, 1);



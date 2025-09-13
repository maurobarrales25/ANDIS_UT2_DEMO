ALTER USER postgres WITH ENCRYPTED PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE usersdb TO postgres;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
INSERT INTO users (id, name, email) VALUES
    (1, 'pepe', 'pepe@gmail.com'),
    (2, 'lucia', 'lucia@outlook.com')
ON CONFLICT (id) DO NOTHING;
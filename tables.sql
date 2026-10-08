-- user table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- skin_assessments table
CREATE TABLE skin_assessments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    age INTEGER NOT NULL,
    skin_type VARCHAR(50) NOT NULL,
    skin_tone VARCHAR(50) NOT NULL,
    concerns VARCHAR(255) NOT NULL,
    health_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--hair_assessments table
CREATE TABLE hair_assessments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    hair_type VARCHAR(50) NOT NULL,
    concerns VARCHAR(255) NOT NULL,
    hair_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


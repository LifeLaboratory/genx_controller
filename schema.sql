CREATE TYPE statuses AS ENUM ('pending', 'scheduled', 'succeded');


CREATE TABLE Node(
  id SERIAL PRIMARY KEY,
  ip text,
  status text
);

CREATE TABLE Cert(
  id SERIAL PRIMARY KEY,
  nodeid integer,
  data text
)
CREATE TYPE statuses AS ENUM ('running', 'blocked');


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
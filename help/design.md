# First iteration:

- Define a paste with bare minimum fields
    - Name (or title)
    - text
    - slug
- Create a server with POST, GET
- Don't worry about providing a client, use curl or the like to access the server:x


# Endpoints

## Create a new paste

    POST /new 

## Read a paste

    GET /<id>

# Database Design

- Use sqlite
- 1 single table

create table bits (id text, name text, content text);


# Design Issues

- How to I generate IDs?
    - Use serial number is easier, but not secured
    - Can use generated words + number, but have to worry about uniqueness
- Security is not a conern for now. Not yet.



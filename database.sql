CREATE USER root WITH ENCRYPTED PASSWORD 'hola123';
ALTER USER root WITH SUPERUSER;
CREATE DATABASE monitoreo WITH OWNER root;

CREATE USER user1 WITH ENCRYPTED PASSWORD 'hola123';
CREATE USER user2 WITH ENCRYPTED PASSWORD 'hola123';

\c monitoreo

CREATE TABLE cambio(
		idCambio SERIAL PRIMARY KEY,
		descripcion VARCHAR(30),
		numeroCa INT NOT NULL
);

CREATE TABLE malware(
		idMalware SERIAL PRIMARY KEY,
		tipoM VARCHAR(10) NOT NULL,
		descripcion VARCHAR(30),
		idCambio INT REFERENCES cambio(idCambio) NOT NULL,
);



CREATE TABLE archivo(
		idArchivo SERIAL PRIMARY KEY,
		nombre VARCHAR(30) NOT NULL,
		ubicacion VARCHAR(50) NOT NULL,
		md5 VARCHAR(100) NOT NULL,
		fechaCre TIMESTAMP NOT NULL
);



CREATE TABLE dominio(
		idDominio SERIAL PRIMARY KEY,
		nombre VARCHAR(30),
		ip VARCHAR(15) NOT NULL,
		segmento VARCHAR(20) 
);


CREATE TABLE servicio(
		idServicio SERIAL PRIMARY KEY,
		nombre VARCHAR(30) NOT NULL,
		cms VARCHAR(20),
		idDominio INT REFERENCES dominio(idDominio) NOT NULL,
<<<<<<< Updated upstream

);


CREATE TABLE top(
		idTop SERIAL PRIMARY KEY,
		idDominio INT REFERENCES dominio(idDominio) NOT NULL
);


CREATE TABLE ArDomCam(
		idArchivo SERIAL REFERENCES archivo(idArchivo),
		idDominio SERIAL REFERENCES dominio(idDominio),
		idCambio SERIAL REFERENCES cambio(idCambio),
		ultimaMod TIMESTAMP,

		CONSTRAINT PKliDomCam PRIMARY KEY(idArchivo, idDominio, idCambio, ultimaMod)
=======
		idCambio INT REFERENCES cambio(idCambio) NOT NULL,
		ultimaMod TIMESTAMP,
		CONSTRAINT PKliDomCam PRIMARY KEY(idLinea, idDominio, idCambio, ultimaMod)
>>>>>>> Stashed changes
);

CREATE USER root WITH ENCRYPTED PASSWORD 'hola123';
ALTER USER root WITH SUPERUSER;
CREATE DATABASE monitoreo WITH OWNER root;

CREATE USER user1 WITH ENCRYPTED PASSWORD 'hola123';
CREATE USER user2 WITH ENCRYPTED PASSWORD 'hola123';

\c monitoreo

CREATE TABLE malware(
		idMalware INT PRIMARY KEY,
		tipoM VARCHAR(10) NOT NULL,
		descripcion VARCHAR(30),
		notificacion CHAR(1),
		correo VARCHAR(30),

		CONSTRAINT CKnotificacion
		CHECK(notificacion IN ('S','s','N','n'))
);

CREATE TABLE cambio(
		idCambio INT PRIMARY KEY,
		descripcion VARCHAR(30),
		numeroCa INT NOT NULL,
		idMalware INT REFERENCES malware(idMalware) NOT NULL
);

CREATE TABLE linea(
		idLinea INT PRIMARY KEY,
		nombre VARCHAR(30) NOT NULL,
		ubicacion VARCHAR(50) NOT NULL,
		md5 VARCHAR(100) NOT NULL,
		fechaCre TIMESTAMP NOT NULL
);

CREATE TABLE servicio(
		idServicio INT PRIMARY KEY,
		nombre VARCHAR(30) NOT NULL,
		cms CHAR(1),

		CONSTRAINT CKcms
		CHECK(cms IN ('S','s','N','n'))
);

CREATE TABLE dominio(
		idDominio INT PRIMARY KEY,
		nombre VARCHAR(30) NOT NULL,
		ip VARCHAR(15) NOT NULL,
		subdom VARCHAR(30) NOT NULL,
		numSub INT NOT NULL,
		segmento VARCHAR(20) NOT NULL,
		idServicio INT REFERENCES servicio(idServicio) NOT NULL
);

CREATE TABLE liDomCam(
		idLinea INT REFERENCES linea(idLinea) NOT NULL,
		idDominio INT REFERENCES dominio(idDominio) NOT NULL,
		idCambio INT REFERENCES cambio(idCambio) NOT NULL,
		ultimaMod TIMESTAMP PRIMARY KEY

		CONSTRAINT PKliDomCam PRIMARY KEY(idLinea, idDominio, idCambio, ultimaMod)
);

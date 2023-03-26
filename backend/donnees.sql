CREATE TABLE utilisateur
(
  id_joueur INTEGER PRIMARY KEY NOT NULL,
  pseudo VARCHAR(200) NOT NULL,
  mdp VARCHAR(100) NOT NULL,
  darkmode BOOLEAN NOT NULL,
  path_pic VARCHAR(200) NOT NULL
);

CREATE TABLE partie
(
  id_partie INTEGER NOT NULL PRIMARY KEY,
  id_joueur INTEGER NOT NULL,
  id_parametre INTEGER NOT NULL,
  victoire BOOLEAN,
  a_trouve VARCHAR(20) NOT NULL,
  coup1 VARCHAR(20),
  coup2 VARCHAR(20),
  coup3 VARCHAR(20),
  coup4 VARCHAR(20),
  coup5 VARCHAR(20),
  coup6 VARCHAR(20),
  coup7 VARCHAR(20),
  coup8 VARCHAR(20),
  coup9 VARCHAR(20),
  coup10 VARCHAR(20),
  coup11 VARCHAR(20),
  coup12 VARCHAR(20),
  coup13 VARCHAR(20),
  coup14 VARCHAR(20),
  coup15 VARCHAR(20),
  FOREIGN KEY (id_joueur) REFERENCES utilisateur(id_joueur),
  FOREIGN KEY (id_parametre) REFERENCES parametre(id_parametre)
);

CREATE TABLE parametre
(
  id_parametre INTEGER PRIMARY KEY NOT NULL,
  nb_coups INTEGER(20) NOT NULL,
  nb_lettres INTEGER NOT NULL,
  FOREIGN KEY (id_parametre) REFERENCES parametre(id_parametre)
);

CREATE TABLE statistiques
(
  id_joueur INTEGER PRIMARY KEY NOT NULL,
  nb_parties INTEGER NOT NULL,
  nb_victoires INTEGER NOT NULL,
  FOREIGN KEY (id_joueur) REFERENCES utilisateur(id_joueur)
);

CREATE TABLE succes
(
  id_joueur INTEGER PRIMARY KEY NOT NULL,
  succes1 BOOLEAN NOT NULL,
  succes2 BOOLEAN NOT NULL,
  succes3 BOOLEAN NOT NULL,
  succes4 BOOLEAN NOT NULL,
  FOREIGN KEY (id_joueur) REFERENCES utilisateur(id_joueur)
);

INSERT INTO utilisateur VALUES (0, 'public', 'tncy', '1', '../static/0.jpg');
INSERT INTO utilisateur VALUES (1, 'Aurélien', 'tncy', '1',"../static/1.jpg");
INSERT INTO utilisateur VALUES (2, 'Tanguy', 'tncy', '1',"../static/2.jpeg");
INSERT INTO utilisateur VALUES (3, 'Thibault', 'tncy', '1',"../static/3.jpeg");
INSERT INTO utilisateur VALUES (4, 'Guillaume', 'tncy', '1',"../static/4.jpeg");
INSERT INTO utilisateur VALUES (5, 'telecomnancy', 'tncy', '0',"../static/5.png");

INSERT INTO statistiques VALUES (0,0,0);
INSERT INTO statistiques VALUES (1,0,0);
INSERT INTO statistiques VALUES (2,0,0);
INSERT INTO statistiques VALUES (3,0,0);
INSERT INTO statistiques VALUES (4,0,0);
INSERT INTO statistiques VALUES (5,0,0);

INSERT INTO succes VALUES (0,0,0,0,0);
INSERT INTO succes VALUES (1,0,0,0,0);
INSERT INTO succes VALUES (2,0,0,0,0);
INSERT INTO succes VALUES (3,0,0,0,0);
INSERT INTO succes VALUES (4,0,0,0,0);
INSERT INTO succes VALUES (5,0,0,0,0);
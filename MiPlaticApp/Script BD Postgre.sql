--Insertar datos
INSERT INTO cajadb.users(username, password, balance)
VALUES ('jaime', 'jaime', 1000000);

--Ver informacion
SELECT username, password, balance
FROM cajadb.users
WHERE username='rigo';

--validar las transaciones realizadas
SELECT id, username, date, value, actual_balance
FROM cajadb.transactions;

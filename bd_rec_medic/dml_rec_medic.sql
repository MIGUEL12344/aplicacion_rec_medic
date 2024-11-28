--insertar a Medicamento
INSERT INTO Medicamento (Nombre, Dosis_Rec, Descripción) VALUES 
('Paracetamol', '500mg cada 8 horas', 'Analgésico y antipirético utilizado para tratar el dolor y la fiebre.'),
('Ibuprofeno', '400mg cada 6 horas', 'Antiinflamatorio no esteroideo (AINE) utilizado para reducir el dolor y la inflamación.'),
('Amoxicilina', '250mg cada 8 horas', 'Antibiótico utilizado para tratar diversas infecciones bacterianas.'),
('Loratadina', '10mg una vez al día', 'Antihistamínico utilizado para aliviar los síntomas de alergias.'),
('Metformina', '500mg dos veces al día', 'Medicamento para el tratamiento de la diabetes tipo 2, ayuda a controlar el nivel de azúcar en la sangre.');

--insertar a Recordatorios
INSERT INTO Recordatorio (Fecha_Hora, ID_Medicamento) VALUES 
('2024-11-28 08:00:00', 1),
('2024-11-28 14:00:00', 1),
('2024-11-28 08:00:00', 2),
('2024-11-28 14:00:00', 2),
('2024-11-28 08:00:00', 3);

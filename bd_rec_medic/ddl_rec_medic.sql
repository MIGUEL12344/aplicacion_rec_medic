-- Crear tabla Medicamento
CREATE TABLE IF NOT EXISTS Medicamento (
    ID_Medicamento INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombre TEXT NOT NULL,
    Dosis_Rec TEXT NOT NULL,
    Descripción TEXT
);

-- Crear tabla Recordatorio
CREATE TABLE IF NOT EXISTS Recordatorio (
    ID_Recordatorio INTEGER PRIMARY KEY AUTOINCREMENT,
    Fecha_Hora TEXT NOT NULL,
    ID_Medicamento INTEGER,
    FOREIGN KEY (ID_Medicamento) REFERENCES Medicamento(ID_Medicamento)
);

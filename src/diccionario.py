MAPPING_MARITAL_STATUS = {
    "Soltero/a": 1,
    "Casado/a": 2,
    "Viudo/a": 3,
    "Divorciado/a": 4,
    "Unión libre": 5,
    "Separado/a legalmente": 6
}

# --- Modo de aplicación ---
MAPPING_APPLICATION_MODE = {
    "1ª fase - contingente general": 1,
    "Ordenanza No. 612/93": 2,
    "1ª fase - contingente especial (Islas Azores)": 5,
    "Titular de otro curso superior": 7,
    "Ordenanza No. 854-B/99": 10,
    "Estudiante internacional (pregrado)": 15,
    "1ª fase - contingente especial (Islas Madeira)": 16,
    "2ª fase - contingente general": 17,
    "3ª fase - contingente general": 18,
    "Ordenanza No. 533-A/99, ítem b2) (Plan Diferente)": 26,
    "Ordenanza No. 533-A/99, ítem b3) (Otra Institución)": 27,
    "Mayores de 23 años": 39,
    "Transferencia": 42,
    "Cambio de carrera": 43,
    "Titulares de diploma de especialización tecnológica": 44,
    "Cambio de institución/carrera": 51,
    "Titulares de diploma de ciclo corto": 53,
    "Cambio de institución/carrera (Internacional)": 57
}

# --- Orden de aplicación ---
# (0 = primera opción, 9 = última opción)
MAPPING_APPLICATION_ORDER = {f"Opción {i+1}": i for i in range(10)}

# --- Carrera o programa académico ---
MAPPING_COURSE = {
    "Tecnologías de Producción de Biocombustibles": 33,
    "Diseño de Animación y Multimedia": 171,
    "Trabajo Social (jornada nocturna)": 8014,
    "Agronomía": 9003,
    "Diseño de Comunicación": 9070,
    "Enfermería Veterinaria": 9085,
    "Ingeniería Informática": 9119,
    "Equinocultura": 9130,
    "Administración de Empresas": 9147,
    "Trabajo Social": 9238,
    "Turismo": 9254,
    "Enfermería": 9500,
    "Higiene Oral": 9556,
    "Gestión de Publicidad y Marketing": 9670,
    "Periodismo y Comunicación": 9773,
    "Educación Básica": 9853,
    "Administración (jornada nocturna)": 9991
}

# --- Tipo de jornada ---
MAPPING_DAYTIME_ATTENDANCE = {
    "Diurna": 1,
    "Nocturna": 0
}

# --- Calificación previa ---
MAPPING_PREVIOUS_QUALIFICATION = {
    "Educación secundaria": 1,
    "Educación superior - licenciatura": 2,
    "Educación superior - grado": 3,
    "Educación superior - maestría": 4,
    "Educación superior - doctorado": 5,
    "Frecuencia de educación superior": 6,
    "12° año no completado": 9,
    "11° año no completado": 10,
    "Otro - 11° año de escolaridad": 12,
    "10° año de escolaridad": 14,
    "10° año no completado": 15,
    "Educación básica 3er ciclo (9°/10°/11°)": 19,
    "Educación básica 2° ciclo (6°/7°/8°)": 38,
    "Curso de especialización tecnológica": 39,
    "Educación superior - grado (1er ciclo)": 40,
    "Curso técnico profesional superior": 42,
    "Educación superior - maestría (2° ciclo)": 43
}

# --- Nacionalidad ---
MAPPING_NACIONALITY = {
    "Portuguesa": 1,
    "Alemana": 2,
    "Española": 6,
    "Italiana": 11,
    "Neerlandesa": 13,
    "Inglesa": 14,
    "Lituana": 17,
    "Angoleña": 21,
    "Caboverdiana": 22,
    "Guineana": 24,
    "Mozambiqueña": 25,
    "Santotomense": 26,
    "Turca": 32,
    "Brasileña": 41,
    "Rumana": 62,
    "Moldava": 100,
    "Mexicana": 101,
    "Ucraniana": 103,
    "Rusa": 105,
    "Cubana": 108,
    "Colombiana": 109
}

# --- Nivel educativo de la madre ---
MAPPING_MOTHER_QUALIFICATION = {
    "Educación secundaria (12° año)": 1,
    "Educación superior - licenciatura": 2,
    "Educación superior - grado": 3,
    "Educación superior - maestría": 4,
    "Educación superior - doctorado": 5,
    "Frecuencia de educación superior": 6,
    "12° año no completado": 9,
    "11° año no completado": 10,
    "7° año (antiguo)": 11,
    "Otro - 11° año": 12,
    "10° año de escolaridad": 14,
    "Curso de comercio general": 18,
    "Educación básica 3er ciclo (9°/10°/11°)": 19,
    "Curso técnico-profesional": 22,
    "7° año de escolaridad": 26,
    "2° ciclo de escuela secundaria": 27,
    "9° año no completado": 29,
    "8° año de escolaridad": 30,
    "Desconocido": 34,
    "No sabe leer ni escribir": 35,
    "Sabe leer sin haber completado el 4° año": 36,
    "Educación básica 1er ciclo (4°/5° año)": 37,
    "Educación básica 2° ciclo (6°/7°/8°)": 38,
    "Curso de especialización tecnológica": 39,
    "Educación superior - grado (1er ciclo)": 40,
    "Estudios superiores especializados": 41,
    "Curso técnico profesional superior": 42,
    "Educación superior - maestría (2° ciclo)": 43,
    "Educación superior - doctorado (3° ciclo)": 44
}

# --- Nivel educativo del padre ---
MAPPING_FATHER_QUALIFICATION = {
    "Educación secundaria (12° año)": 1,
    "Educación superior - licenciatura": 2,
    "Educación superior - grado": 3,
    "Educación superior - maestría": 4,
    "Educación superior - doctorado": 5,
    "Frecuencia de educación superior": 6,
    "12° año no completado": 9,
    "11° año no completado": 10,
    "7° año (antiguo)": 11,
    "Otro - 11° año": 12,
    "2° año de bachillerato complementario": 13,
    "10° año de escolaridad": 14,
    "Curso de comercio general": 18,
    "Educación básica 3er ciclo (9°/10°/11°)": 19,
    "Curso de escuela secundaria complementaria": 20,
    "Curso técnico-profesional": 22,
    "Curso complementario no concluido": 25,
    "7° año de escolaridad": 26,
    "2° ciclo de escuela secundaria": 27,
    "9° año no completado": 29,
    "8° año de escolaridad": 30,
    "Curso general de administración y comercio": 31,
    "Curso complementario de contabilidad y administración": 33,
    "Desconocido": 34,
    "No sabe leer ni escribir": 35,
    "Sabe leer sin haber completado el 4° año": 36,
    "Educación básica 1er ciclo (4°/5° año)": 37,
    "Educación básica 2° ciclo (6°/7°/8°)": 38,
    "Curso de especialización tecnológica": 39,
    "Educación superior - grado (1er ciclo)": 40,
    "Estudios superiores especializados": 41,
    "Curso técnico profesional superior": 42,
    "Educación superior - maestría (2° ciclo)": 43,
    "Educación superior - doctorado (3° ciclo)": 44
}

MAPPING_MOTHER_OCCUPATION = {
    "Estudiante": 0,
    "Representantes del poder legislativo, directores y gerentes ejecutivos": 1,
    "Especialistas en actividades intelectuales y científicas": 2,
    "Técnicos y profesiones de nivel intermedio": 3,
    "Personal administrativo": 4,
    "Servicios personales, seguridad, vigilancia y ventas": 5,
    "Agricultores y trabajadores calificados en agricultura, pesca y silvicultura": 6,
    "Trabajadores calificados en industria, construcción y oficios": 7,
    "Operadores de instalaciones, máquinas y ensambladores": 8,
    "Trabajadores no calificados": 9,
    "Profesiones de las fuerzas armadas": 10,
    "Otra situación": 90,
    "(en blanco)": 99,
    "Profesionales de la salud": 122,
    "Docentes": 123,
    "Especialistas en tecnologías de la información y comunicación (TIC)": 125,
    "Técnicos de nivel intermedio en ciencias e ingeniería": 131,
    "Técnicos y profesionales de salud de nivel intermedio": 132,
    "Técnicos de nivel intermedio en derecho, servicios sociales, deportes y cultura": 134,
    "Oficinistas, secretarios generales y operadores de procesamiento de datos": 141,
    "Operadores de datos, contabilidad, finanzas y registros": 143,
    "Otro personal de apoyo administrativo": 144,
    "Trabajadores de servicios personales": 151,
    "Vendedores": 152,
    "Trabajadores de atención personal y similares": 153,
    "Trabajadores calificados de la construcción y similares (excepto electricistas)": 171,
    "Trabajadores calificados en impresión, joyería, artesanía y afines": 173,
    "Trabajadores en procesamiento de alimentos, madera, confección y otras industrias": 175,
    "Personal de limpieza": 191,
    "Trabajadores no calificados en agricultura, ganadería, pesca y silvicultura": 192,
    "Trabajadores no calificados en industria extractiva, construcción, manufactura y transporte": 193,
    "Auxiliares en la preparación de comidas": 194
}

# --- Ocupación del padre ---
MAPPING_FATHER_OCCUPATION = {
    "Estudiante": 0,
    "Representantes del poder legislativo, directores y gerentes ejecutivos": 1,
    "Especialistas en actividades intelectuales y científicas": 2,
    "Técnicos y profesiones de nivel intermedio": 3,
    "Personal administrativo": 4,
    "Servicios personales, seguridad, vigilancia y ventas": 5,
    "Agricultores y trabajadores calificados en agricultura, pesca y silvicultura": 6,
    "Trabajadores calificados en industria, construcción y oficios": 7,
    "Operadores de instalaciones, máquinas y ensambladores": 8,
    "Trabajadores no calificados": 9,
    "Profesiones de las fuerzas armadas": 10,
    "Otra situación": 90,
    "(en blanco)": 99,
    "Oficiales de las fuerzas armadas": 101,
    "Sargentos de las fuerzas armadas": 102,
    "Otro personal de las fuerzas armadas": 103,
    "Directores de servicios administrativos y comerciales": 112,
    "Directores de hotelería, comercio y otros servicios": 114,
    "Especialistas en ciencias físicas, matemáticas e ingeniería": 121,
    "Profesionales de la salud": 122,
    "Docentes": 123,
    "Especialistas en finanzas, contabilidad, relaciones públicas y organización administrativa": 124,
    "Técnicos de nivel intermedio en ciencias e ingeniería": 131,
    "Técnicos y profesionales de salud de nivel intermedio": 132,
    "Técnicos de nivel intermedio en derecho, servicios sociales, deportes y cultura": 134,
    "Técnicos en tecnologías de la información y comunicación": 135,
    "Oficinistas, secretarios generales y operadores de procesamiento de datos": 141,
    "Operadores de datos, contabilidad, finanzas y registros": 143,
    "Otro personal de apoyo administrativo": 144,
    "Trabajadores de servicios personales": 151,
    "Vendedores": 152,
    "Trabajadores de atención personal y similares": 153,
    "Personal de protección y seguridad": 154,
    "Agricultores orientados al mercado y trabajadores calificados en producción animal": 161,
    "Agricultores, pescadores y cazadores de subsistencia": 163,
    "Trabajadores calificados de la construcción y similares (excepto electricistas)": 171,
    "Trabajadores calificados en metalurgia y metalmecánica": 172,
    "Trabajadores calificados en electricidad y electrónica": 174,
    "Trabajadores en procesamiento de alimentos, madera, confección y otras industrias": 175,
    "Operadores de plantas y maquinaria fija": 181,
    "Trabajadores de ensamblaje": 182,
    "Conductores de vehículos y operadores de equipo móvil": 183,
    "Trabajadores no calificados en agricultura, ganadería, pesca y silvicultura": 192,
    "Trabajadores no calificados en industria extractiva, construcción, manufactura y transporte": 193,
    "Auxiliares en la preparación de comidas": 194,
    "Vendedores ambulantes (excepto alimentos) y prestadores de servicios callejeros": 195
}

# --- Variables binarias (sí/no) ---
MAPPING_BINARY = {
    "Sí": 1,
    "No": 0
}

# --- Género ---
MAPPING_GENDER = {
    "Masculino": 1,
    "Femenino": 0
}


# ===============================================================
# Diccionario maestro
# ===============================================================
MAPPINGS = {
    "Marital status": MAPPING_MARITAL_STATUS,
    "Application mode": MAPPING_APPLICATION_MODE,
    "Application order": MAPPING_APPLICATION_ORDER,
    "Course": MAPPING_COURSE,
    "Daytime/evening attendance\t": MAPPING_DAYTIME_ATTENDANCE,
    "Previous qualification": MAPPING_PREVIOUS_QUALIFICATION,
    "Nacionality": MAPPING_NACIONALITY,
    "Mother's qualification": MAPPING_MOTHER_QUALIFICATION,
    "Father's qualification": MAPPING_FATHER_QUALIFICATION,
    "Mother's occupation": MAPPING_MOTHER_OCCUPATION,
    "Father's occupation": MAPPING_FATHER_OCCUPATION,
    "Displaced": MAPPING_BINARY,
    "Educational special needs": MAPPING_BINARY,
    "Debtor": MAPPING_BINARY,
    "Tuition fees up to date": MAPPING_BINARY,
    "Scholarship holder": MAPPING_BINARY,
    "International": MAPPING_BINARY,
    "Gender": MAPPING_GENDER
}

def get_mapping(feature_name):
    """Devuelve el diccionario de mapeo para una columna dada"""
    return MAPPINGS.get(feature_name, None)
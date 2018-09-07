from neomodel import *
from neomodel import install_all_labels, remove_all_labels


# remove_all_labels()
# install_all_labels()


# clear_neo4j_database(db)
# TODO set label and help_text

class Curso(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(required=True, unique_index=True)
    cod = StringProperty(unique=True,required=True)
    sinonimos = ArrayProperty(StringProperty(), required=False)
    descripcion = StringProperty(required=False)
    pre_requisitos = StringProperty(required=False)
    edicion = StringProperty(required=False)
    oferta = StringProperty(required=False)
    tematica = StringProperty(required=False)
    fecha_inscripcion = DateProperty(default_now=True)
    fecha_inicio = DateProperty(default_now=True)
    esfuerzo_estimado = StringProperty(default=0)
    duracion = StringProperty(required=False)
    link = StringProperty(default="http://opencampus.utpl.edu.ec/")
    INSTITUCIONES = {
        "U": "UTPL",
        "O": "Otro",
    }
    institucion = StringProperty(choices=INSTITUCIONES, default="U")
    archivado = BooleanProperty(default=False)
    docente = RelationshipTo('Docente', 'HAS_A_DOCENTE', cardinality=OneOrMore)
    competencia = RelationshipTo('Competencia', 'HAS_A_COMPETENCIA', cardinality=OneOrMore)
    reto = RelationshipTo('Reto', 'HAS_A_RETO', cardinality=OneOrMore)
    contenido = RelationshipTo('Contenido', 'HAS_A_CONTENIDO', cardinality=OneOrMore)


class Docente(StructuredNode):
    uid = UniqueIdProperty()
    nombre = StringProperty(unique_index=True, required=True)
    N_ACADEMICO = {
        "TN": "Nivel Técnico",
        "CN": "Tercer Nivel",
        "T": "Cuarto Nivel",
    }
    nivel_academico = StringProperty(default="T", choices=N_ACADEMICO)
    email = EmailProperty(required=False)
    resumen = StringProperty(required=False)
    curso = RelationshipTo('Curso', 'TEACHES', cardinality=OneOrMore)


class Competencia(StructuredNode):
    competencia = StringProperty(unique=True, required=True)
    curso = RelationshipTo(Curso, 'IS_FROM', cardinality=OneOrMore)


class Reto(StructuredNode):
    titulo_reto = StringProperty(unique=True, required=True)
    fecha_inicio = DateTimeProperty(default_now=True)
    fecha_fin = DateTimeProperty(default_now=True)
    descripcion = StringProperty(required=False)
    curso = RelationshipTo(Curso, 'IS_FROM', cardinality=OneOrMore)


class Contenido(StructuredNode):
    orden = StringProperty(required=True)
    contenido = StringProperty(unique=True, required=True)
    curso = RelationshipTo(Curso, 'IS_FROM', cardinality=OneOrMore)

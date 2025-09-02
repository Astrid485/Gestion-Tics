from django.db import models


class Ambiente(models.Model):
    idambiente = models.AutoField(primary_key=True)
    ambiente = models.CharField(max_length=250)

    class Meta:
        db_table = 'ambiente'


class Area(models.Model):
    idarea = models.AutoField(primary_key=True)
    area = models.CharField(max_length=150)

    class Meta:
        db_table = 'area'


class Caracterizacion(models.Model):
    idcaracterizacion = models.AutoField(primary_key=True)
    caracterizacion = models.CharField(max_length=100)

    class Meta:
        db_table = 'caracterizacion'


class Tipoidentificacion(models.Model):
    idtipoidentificacion = models.AutoField(primary_key=True)
    tipoidentificacion = models.CharField(max_length=20)

    class Meta:
        db_table = 'tipoidentificacion'


class Aspirantes(models.Model):
    idaspirante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    idcaracterizacion = models.ForeignKey(Caracterizacion, on_delete=models.CASCADE, db_column='idcaracterizacion')
    telefono = models.CharField(unique=True, max_length=50)
    pdf = models.TextField(blank=True, null=True)
    tipoidentificacion = models.ForeignKey(Tipoidentificacion, on_delete=models.CASCADE, db_column='tipoidentificacion')
    numeroidentificacion = models.IntegerField(unique=True)
    correo = models.CharField(unique=True, max_length=255)
    fecha = models.DateField()

    class Meta:
        db_table = 'aspirantes'


class Departamentos(models.Model):
    codigodepartamentos = models.AutoField(primary_key=True)
    departamentos = models.CharField(max_length=200)

    class Meta:
        db_table = 'departamentos'


class Tipoempresa(models.Model):
    idtipoempresa = models.AutoField(primary_key=True)
    tipoempresa = models.CharField(max_length=100)

    class Meta:
        db_table = 'tipoempresa'


class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    nombreempresa = models.CharField(unique=True, max_length=255)
    representanteempresa = models.CharField(max_length=50)
    correoempresa = models.CharField(unique=True, max_length=200)
    nitempresa = models.IntegerField(unique=True)
    idtipoempresa = models.ForeignKey(Tipoempresa, on_delete=models.CASCADE, db_column='idtipoempresa')

    class Meta:
        db_table = 'empresa'


class Estados(models.Model):
    idestado = models.AutoField(primary_key=True)
    estados = models.CharField(max_length=50)

    class Meta:
        db_table = 'estados'


class Horario(models.Model):
    idhorario = models.AutoField(primary_key=True)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    mes1 = models.TextField(blank=True, null=True)
    mes2 = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'horario'


class Jornada(models.Model):
    idjornada = models.AutoField(primary_key=True)
    jornada = models.CharField(max_length=100)

    class Meta:
        db_table = 'jornada'


class Modalidad(models.Model):
    idmodalidad = models.AutoField(primary_key=True)
    modalidad = models.CharField(max_length=50)

    class Meta:
        db_table = 'modalidad'


class Municipios(models.Model):
    codigomunicipio = models.AutoField(primary_key=True)
    municipio = models.CharField(max_length=255)
    codigodepartamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE, db_column='codigodepartamento')

    class Meta:
        db_table = 'municipio'


class Programaespecial(models.Model):
    idespecial = models.AutoField(primary_key=True)
    programaespecial = models.CharField(max_length=100)

    class Meta:
        db_table = 'programaespecial'


class Programaformacion(models.Model):
    codigoprograma = models.AutoField(primary_key=True)
    verision = models.CharField(max_length=250)
    nombreprograma = models.TextField(blank=True, null=True)
    horas = models.IntegerField()
    idarea = models.ForeignKey(Area, on_delete=models.CASCADE, db_column='idarea')
    idmodalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, db_column='idmodalidad')

    class Meta:
        db_table = 'programaformacion'


class Rol(models.Model):
    idrol = models.AutoField(primary_key=True)
    nombrerol = models.CharField(max_length=20)

    class Meta:
        db_table = 'rol'


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, db_column='rol')
    tipoidentificacion = models.ForeignKey(Tipoidentificacion, on_delete=models.CASCADE, db_column='tipoidentificacion')
    numeroidentificacion = models.IntegerField(unique=True)
    correo = models.CharField(unique=True, max_length=255)
    clave = models.CharField(max_length=255)
    fecha = models.DateField()

    class Meta:
        db_table = 'usuario'


class Tiposolicitud(models.Model):
    idtiposolicitud = models.AutoField(primary_key=True)
    tiposolicitud = models.CharField(max_length=10)

    class Meta:
        db_table = 'tiposolicitud'


class Solicitud(models.Model):
    idsolicitud = models.AutoField(primary_key=True)
    idtiposolicitud = models.ForeignKey(Tiposolicitud, on_delete=models.CASCADE, db_column='idtiposolicitud')
    codigosolicitud = models.IntegerField(blank=True, null=True)
    codigoprograma = models.ForeignKey(Programaformacion, on_delete=models.CASCADE, db_column='codigoprograma')
    idhorario = models.ForeignKey(Horario, on_delete=models.CASCADE, db_column='idhorario')
    cupo = models.IntegerField()
    idmodalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, db_column='idmodalidad')
    codigomunicipio = models.ForeignKey(Municipios, on_delete=models.CASCADE, db_column='codigomunicipio')
    direccion = models.CharField(max_length=255)
    idusuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='idusuario')
    idempresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='idempresa', blank=True, null=True)
    subsectoreconomico = models.CharField(max_length=100, blank=True, null=True)
    idespecial = models.ForeignKey(Programaespecial, on_delete=models.CASCADE, db_column='idespecial')
    convenio = models.CharField(max_length=20, blank=True, null=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, db_column='ambiente', blank=True, null=True)
    fechasolicitud = models.DateField()

    class Meta:
        db_table = 'solicitud'


class Ficha(models.Model):
    idficha = models.AutoField(primary_key=True)
    codigoficha = models.IntegerField(unique=True)
    idsolicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='idsolicitud')
    idestado = models.ForeignKey(Estados, on_delete=models.CASCADE, db_column='idestado')
    observacion = models.TextField()

    class Meta:
        db_table = 'ficha'

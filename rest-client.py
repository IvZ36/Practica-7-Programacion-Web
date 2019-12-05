import unirest
import json

estudiantes = unirest.get("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json" })

print "Listado de Estudiantes: \n" + str(estudiantes.body)

matricula = 1
estudianteX = unirest.get("http://localhost:4567/rest/estudiantes/" + str(matricula), headers={ "Accept": "application/json" })

print "Estudiante #1 consultado: \n" + str(estudianteX.body)

crearEstudiante = unirest.post("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json", "Content-Type": "application/json" }, params=json.dumps({ "nombre": "Joaquinn", "correo": "balaguer857@pucmm.edu.com", "carrera": "ITT" }))
print "Estudiante nuevo creado: \n" + str(crearEstudiante.body)

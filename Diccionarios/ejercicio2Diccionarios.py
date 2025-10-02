asignatura1={"nombre":"servidor","profesor":"JI","horas":7}
asignatura2={"nombre":"cliente","profesor":"David","horas":6}
persona={"nombre":"David", "esprofe":True,"edad":37,"asignaturas":[asignatura1,asignatura2]}
# del(persona["esprofe"])
# print(persona)

for i in asignatura1.keys():
    print(i)
for j in asignatura1.items():
    print(j)
for t in asignatura1.values():
    print(t)

# pablo=persona.copy()
# pablo["nombre"]="Pablo"

# print(persona.pop("nombre"))
# print(pablo["nombre"])

# alumnos=[]
# alumnos.append(persona)
# print(alumnos[0]["asignaturas"][1]["horas"])
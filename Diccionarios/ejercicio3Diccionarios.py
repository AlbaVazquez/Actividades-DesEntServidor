notas={"mates":9,"servidor":4,"programacion":7,"fol":6}
asignatura1={"nombre":"servidor","profesor":"JI","horas":7}
asignatura2={"nombre":"cliente","profesor":"David","horas":6}
persona1={"nombre":"David", "esprofe":True,"edad":37,"asignaturas":[asignatura1,asignatura2],"notas":notas}
persona2={"nombre":"David", "esprofe":True,"edad":37,"asignaturas":[asignatura1,asignatura2],"notas":{"cliente":3,"IPE2":10}}

alumnos=[]
alumnos.append(persona1)
alumnos.append(persona2)

for a in alumnos:
    x=list(a["notas"].values())
    print(f"Media de {a['nombre']}:{sum(notas.values())/len(notas)}")
    #FORMA 1:
    # for nombre_asig,nota_asig in a["notas"].items():
    #     if(nota_asig<5):
    #         print(nombre_asig,nota_asig)
    suspensos={nombre_asig:nota_asig for nombre_asig,nota_asig in a["notas"].items() if nota_asig<5}
    print(suspensos)
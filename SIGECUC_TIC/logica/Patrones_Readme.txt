#Patron de diseño Builder:
Builder
- interfaz abstracta para crear productos.
Concrete Builder
- implementación del Builder
- construye y reúne las partes necesarias para construir los productos
Director
- construye un objeto usando el patrón Builder
Producto
-  El objeto complejo bajo construcción
*Problema: La inscripcion de un docente o aspirante ledaer teacher  
comrpomete 3 modelos de la base de datos Persona, Historial laboral
e Historial Academico
*Solucion: El patron builder nos permitira contruir con la informacion
ligenciada por el usuarios cada uno de los datos necesarios para 
construir cada formulario y asi poder obtener como producto final
la inscripcion de un aspirante docente

#Patron de diseño mediador(Mediator)
Permite reducir la complejidad en la comunicacion entre dos objetos,
este patron va a hacer el mediador de las tareas que puede realizar un
master teacher o un leader teacher con sus perfiles de usuario

#Patron de diseño Fabrica(Factory)
Permite fabricar el perfil especifico para el tipo de usuario logeado
unicamente contruye el template con el contexto indicado para el 
tipo de usuario
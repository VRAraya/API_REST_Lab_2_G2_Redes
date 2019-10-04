# API_REST_Lab_2_G2_Redes

API Rest : Laboratorio 2 del Grupo 2 de Redes y Comunicación de Datos - UTEM

## Métodos a implementar

- Validación dígito verificador:

El método debe recibir un rut (por ejemplo 12345678-9) y devolver un indicador de si es válido o no en función del cálculo del dígito verificador. Para lograr lo anterior, deberá implementar el algoritmo de dígito verificador usado en Chile.

- Nombre Propio:

El método debe recibir un apellido paterno (un campo de entrada), un apellido materno (otro campo), los nombres (todos los nombres, juntos, en otro campo) y un indicador del género de la persona (M o F). El método debe devolver el nombre completo en formato “NOMBRES AP_PATERNO AP_MATERNO”, antecedido del “saludo” según el género (Sr. para M; Sra. para F). Adicionalmente, el nombre completo debe venir formateado con el estilo “nombre propio” (o proper case) que significa todo en minúsculas, excepto la inicial (por ejemplo “Sr. Jorge Daniel González Urrutia”). Note que los nombres/apellidos recibidos como parámetros pueden venir en minúsculas, mayúsculas o alguna combinación.

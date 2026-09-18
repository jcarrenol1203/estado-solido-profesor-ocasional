---
name: evaluar
description: Genera una evaluación tipo checklist (mezcla de preguntas numéricas, de deducción formal y conceptuales) sobre uno o varios subtemas de Estado Sólido que el usuario dice dominar, corrige sus respuestas contra las notas y actualiza progreso.md con el resultado y las debilidades detectadas.
---

# /evaluar — checklist de dominio de un tema

Argumento: el tema o alcance a evaluar, ej. `/evaluar cadena diatómica`,
`/evaluar hasta densidad de estados`, `/evaluar 00_cristalografia_basica`.

## Pasos

1. Lee `progreso/progreso.md` para ubicar qué subtema(s) corresponden al
   argumento del usuario (usa los IDs de subtema tal como aparecen en la
   tabla de progreso).
2. Lee **solo** el/los archivos de `notas/` de esos subtemas (nunca el PDF).
   Presta especial atención a la sección "### Puntos clave para dominar este
   tema" de cada uno — son la base de las preguntas.
3. Genera un set de **~5 preguntas mezcladas** (ajusta el número según cuántos
   subtemas se estén evaluando juntos, pero no hagas exámenes gigantes de una
   sola vez):
   - Al menos 1-2 numéricas/de cálculo (con datos concretos).
   - Al menos 1-2 de deducción formal (pedir derivar una relación desde
     primeros principios, como hace el PDF).
   - Al menos 1 conceptual (pedir explicar el "por qué" físico de algo).
   - Cada pregunta debe apuntar a uno o más de los "puntos clave" del
     subtema — no inventes preguntas fuera de lo que las notas cubren.
4. Presenta las preguntas juntas de una vez (no interrogatorio uno-por-uno)
   y espera la respuesta completa del usuario.
5. Corrige contra las notas. Para cada pregunta:
   - Di si está correcta, parcialmente correcta o incorrecta.
   - Si hay error, señala **la razón conceptual concreta** del error, no
     solo "está mal" — y cita el punto clave/página relevante de la nota.
6. Actualiza `progreso/progreso.md`:
   - Si el desempeño en un subtema fue sólido (todas o casi todas sus
     preguntas bien): márcalo `dominado`, con fecha, en la tabla de
     progreso.
   - Si hubo fallas: déjalo `en progreso` y añade en la columna/sección de
     debilidades una descripción concreta de qué falló (no genérica), para
     que una futura evaluación se enfoque ahí.
   - Agrega una línea al log de evaluaciones (fecha, subtema(s), resultado
     resumido).
7. Cierra ofreciendo (sin ejecutarlo tú mismo salvo que el usuario diga que
   sí) actualizar el dashboard visual con `/dashboard`.

## No hacer

- No marques `dominado` un subtema que no fue evaluado en esta sesión.
- No generes preguntas sobre subtemas fuera del alcance pedido.
- No leas el PDF salvo que las notas del subtema tengan un vacío evidente
  para plantear una pregunta que sí pidió el usuario — y avísalo si pasa.

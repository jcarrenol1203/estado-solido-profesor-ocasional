---
name: evaluar
description: Genera una evaluación tipo checklist (mezcla de preguntas numéricas, de deducción formal y conceptuales, incluyendo variantes del banco de exámenes viejos) sobre uno o varios subtemas de Estado Sólido (Parcial 1 o Parcial 2) que el usuario dice dominar, corrige sus respuestas contra las notas y actualiza Parcial_N/progreso/<persona>.md (Isa o Juan) con el resultado y las debilidades detectadas.
---

# /evaluar — checklist de dominio de un tema

Argumento: el tema o alcance a evaluar, ej. `/evaluar cadena diatómica`,
`/evaluar hasta densidad de estados`, `/evaluar 00_cristalografia_basica`.

## Pasos

0. **Parcial y perfil activos.** Hay dos bloques: `Parcial_1/` (vibraciones de
   red) y `Parcial_2/` (metales y electrón libre). Deduce el parcial por el
   tema pedido; si es ambiguo, pregunta "¿Parcial 1 o Parcial 2?". Define
   `BASE=Parcial_N/` y úsalo como prefijo de todas las rutas (`BASE/notas/`,
   `BASE/progreso/`, `BASE/examenes/`). Cada bloque tiene dos perfiles
   independientes: Isa y Juan (`BASE/progreso/isa.md` y `BASE/progreso/juan.md`;
   si el archivo del perfil no existe, créalo copiando
   `BASE/progreso/progreso.template.md`). Si no sabes ya, en esta sesión,
   quién está evaluando, pregunta "¿Isa o Juan?" antes de generar el
   checklist. Todos los pasos siguientes leen y escriben exclusivamente
   `BASE/progreso/<persona>.md` (nunca el archivo de la otra persona, ni el del
   otro parcial, nunca `Parcial_1/progreso/progreso.legacy.md`, que está
   deprecado).
1. Lee `BASE/progreso/<persona>.md` para ubicar qué subtema(s) corresponden al
   argumento del usuario (usa los IDs de subtema tal como aparecen en la
   tabla de progreso).
2. Lee **solo** el/los archivos de `BASE/notas/` de esos subtemas (nunca el PDF).
   Presta especial atención a la sección "### Puntos clave para dominar este
   tema" de cada uno — son la base de las preguntas. Lee también, filtrado a
   esos mismos subtemas, `BASE/examenes/banco_preguntas.md` (preguntas reales de
   parciales/talleres viejos) y de paso revisa `BASE/examenes/analisis_temas.md`
   si el alcance pedido es amplio (varios subtemas o "hasta X") — prioriza
   ahí los subtemas marcados como "calientes" (más preguntados en exámenes
   viejos).
3. Genera un set de **~5 preguntas mezcladas** (ajusta el número según cuántos
   subtemas se estén evaluando juntos, pero no hagas exámenes gigantes de una
   sola vez):
   - Al menos 1-2 numéricas/de cálculo (con datos concretos).
   - Al menos 1-2 de deducción formal (pedir derivar una relación desde
     primeros principios, como hace el PDF).
   - Al menos 1 conceptual (pedir explicar el "por qué" físico de algo).
   - Cada pregunta debe apuntar a uno o más de los "puntos clave" del
     subtema — no inventes preguntas fuera de lo que las notas cubren.
   - Cuando `BASE/examenes/banco_preguntas.md` tenga una pregunta real relevante,
     puedes **adaptarla** (cambiar los datos numéricos, reformular el
     enunciado) en vez de inventar una desde cero — así el usuario practica
     con el estilo real de examen. No la copies literalmente si el usuario
     ya la resolvió antes (revisa si hay solución manuscrita indicada en el
     banco) para no repetir la misma pregunta que ya vio.
4. Presenta las preguntas juntas de una vez (no interrogatorio uno-por-uno)
   y espera la respuesta completa del usuario.
5. Corrige contra las notas. Para cada pregunta:
   - Di si está correcta, parcialmente correcta o incorrecta.
   - Si hay error, señala **la razón conceptual concreta** del error, no
     solo "está mal" — y cita el punto clave/página relevante de la nota.
6. Actualiza `BASE/progreso/<persona>.md`:
   - Si el desempeño en un subtema fue sólido (todas o casi todas sus
     preguntas bien): márcalo `dominado`, con fecha, en la tabla de
     progreso.
   - Si hubo fallas: déjalo `en progreso` y añade en la columna/sección de
     debilidades una descripción concreta de qué falló (no genérica), para
     que una futura evaluación se enfoque ahí.
   - Agrega una línea al log de evaluaciones (fecha, subtema(s), resultado
     resumido).
   - Si la evaluación usó una pregunta adaptada de `BASE/examenes/banco_preguntas.md`,
     puedes marcar esa fuente como intentada en la tabla "Parciales y
     talleres" del perfil (estado, nota aproximada si aplica, fecha).
7. Cierra ofreciendo (sin ejecutarlo tú mismo salvo que el usuario diga que
   sí) actualizar el dashboard visual con `/dashboard <persona>`.

## No hacer

- No marques `dominado` un subtema que no fue evaluado en esta sesión.
- No generes preguntas sobre subtemas fuera del alcance pedido.
- No leas el PDF salvo que las notas del subtema tengan un vacío evidente
  para plantear una pregunta que sí pidió el usuario — y avísalo si pasa.
- No releas los archivos crudos de los exámenes viejos (`Parcial_1/Parciales y
  Talleres/` o `Parcial_2/Talleres_Parciales/`) — usa siempre
  `BASE/examenes/banco_preguntas.md`, `BASE/examenes/analisis_temas.md` y, si
  hay conflicto, `BASE/examenes/guia_teoria_por_examen.md`.
- No toques ni actualices `BASE/progreso/<otra-persona>.md` ni el progreso del
  otro parcial — cada evaluación pertenece a un único perfil y parcial activos.

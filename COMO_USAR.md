# Cómo usar este sistema de estudio (y compartirlo)

> Guía única del repo. Si tienes una duda de **cómo usar** el sistema, pregúntale a Claude ("¿cómo marco un avance?", "¿cómo comparto con Isa?"): responde leyendo este archivo. Si la guía no cubre tu duda, Claude lo dice y la añade aquí.

## 1. Qué es

Un "profesor ocasional" hecho con Claude Code. Cada parcial es una carpeta (`Parcial_1/` vibraciones, `Parcial_2/` metales y electrón libre) con sus notas, exámenes viejos y su progreso. Dos personas (Isa y Juan) lo usan con perfiles de progreso **independientes**.

```
Parcial_2/
  CLAUDE.md        reglas que Claude lee al abrir la carpeta
  teoria/          teoría con figuras (diapositivas 1-70 + Pavlov)
  practica/        ejercicios resueltos paso a paso
  examen/          examen propuesto (sin clave en el repo)
  examenes_resueltos/   exámenes viejos resueltos (solo lo de alcance)
  notas/           extracción del PDF (base de /duda y /evaluar)
  progreso/        juan.md, isa.md  <- tu estado y tus pendientes
.claude/skills/    /duda  /evaluar  /dashboard
COMO_USAR.md       esta guía
```

## 2. Los tres comandos

| Comando | Para qué | Qué escribe |
|---|---|---|
| `/duda <pregunta>` | Resolver una duda puntual, con página fuente | Pasa a "en progreso" los ítems de teoría que toca (si estaban pendientes; nunca baja un estado) y, si queda algo abierto, anota una fila en **Pendientes** |
| `/evaluar <tema>` | Checklist de preguntas sobre lo que dices dominar; corrige | Debilidades en **Pendientes** y log (el avance lo marcas tú en el tablero) |
| `/dashboard <persona>` | Publicar/actualizar tu tablero | Nada (lo lee todo) |

Siempre dile quién eres ("Juan" o "Isa"): Claude no mezcla los perfiles.

## 3. Tu tablero (artifact)

Pestañas: **Resumen · Teoría · Práctica · Examen · Exámenes viejos · Pendientes**. Todo el contenido está dentro del tablero.

- **Avance:** `/duda` lo mueve solo hacia adelante (pendiente → en progreso). En Teoría, Práctica y Exámenes viejos toca el botón de cada ítem (pendiente → en progreso → hecho), o usa "Marcar todo hecho" del bloque. También por comando:
  - `/dashboard juan marcar T.drude.1.1 hecho` (un ítem)
  - `/dashboard juan marcar T.cal hecho` (por prefijo: `T.` teoría, `P.` práctica, `V.` exámenes viejos)
  - `/dashboard juan marcar teoria "en progreso"` (sección completa)
  - `/dashboard juan reiniciar practica`
- **Examen:** Parte 1 opción múltiple (elige a-e), Parte 2 desarrollo (caja por literal). Se guarda solo. Cuando termines: `/dashboard juan calificar examen` (o "califica examen"). Verás la nota y la retroalimentación en el tablero.
- **Pendientes:** salen del archivo `progreso/<persona>.md` (sección "Pendientes y por mejorar"). El tablero los **lee al publicarse**: tras anotar pendientes nuevos, corre `/dashboard <persona>` para verlos.

El avance de checklists vive en la base de datos del tablero; los pendientes y el log, en el `.md`.

## 4. Pendientes y por mejorar (`progreso/<persona>.md`)

Tabla entre `<!-- PENDIENTES:START -->` y `<!-- PENDIENTES:END -->`:

```
| # | Fecha | Subtema | Tipo | Descripción | Estado |
| 1 | 2026-11-22 | cal.2 | duda | No entiendo por qué C_e ~ T y no ~ T/T_F | abierto |
```

- **Tipo:** `duda` (sigues sin entender) · `repasar` (flojo en una evaluación) · `error-material` (error o vacío en teoría/notas) · `mejora` (algo que quieres que se agregue/cambie).
- **Estado:** `abierto` o `resuelto`. No uses `|` en la descripción.
- Se agregan solos con `/duda` y `/evaluar`, o dile a Claude: *"anota un pendiente en cal.2: repasar la estimación de C_e"*. Para cerrarlos: *"marca resuelto el pendiente 3"*. También puedes editar el `.md` a mano.

## 5. Compartir con otra persona (Isa ↔ Juan o un compañero nuevo)

Hay **dos cosas** que compartir:

**a) El repo (material y progreso) — vía GitHub**
1. Clona: `git clone git@github.com:jcarrenol1203/estado-solido-profesor-ocasional.git` y entra a `Parcial_2/`.
2. Pon tus PDFs del curso en `Parcial_2/Diapositivas/` (los `.pdf` no se suben a git, salvo los marcados como excepción en `.gitignore`).
3. Si no existe tu perfil, copia `progreso/progreso.template.md` a `progreso/<tu_nombre>.md`.
4. Abre Claude Code en `Parcial_2/` y usa los comandos (Claude lee `CLAUDE.md` solo).
5. Cada quien edita **solo su** `progreso/<nombre>.md`: así los `git pull` / `git push` no chocan. Haz `git pull` antes de empezar y `git push` al terminar (Claude hace el commit si se lo pides).

**b) El tablero (artifact) — vía el menú Compartir de claude.ai**
- Cada persona tiene su tablero, privado por defecto. Para que pueda marcar avance y responder el examen, el dueño del tablero debe compartirlo con permiso de **Contributor** (o Editor) desde el menú Compartir del artifact. Con solo "ver" se lee, pero no se guarda nada.
- Cada tablero tiene su propia base de datos: lo que marca una persona no aparece en el de la otra.
- Para un tablero nuevo (otra persona): pídele a Claude `/dashboard <nombre>`; crea el artifact y guarda su URL en `progreso/<nombre>.md`.

## 6. Preguntas frecuentes

- **No veo mis pendientes nuevos en el tablero.** Se leen al publicar: `/dashboard <persona>`.
- **Marqué un ítem y no cambió.** Revisa el banner amarillo ("modo local"): sin permiso de Contributor se guarda solo en tu navegador.
- **¿Dónde está la clave del examen?** No está en el repo ni en el tablero visible; Claude la guarda con acceso de admin y la usa al calificar.
- **¿Puedo preguntar cosas fuera de alcance?** Sí; Claude responde y avisa que está fuera del parcial (no toca tu estado).
- **Claude no conoce algo de esta guía.** Dile "actualiza COMO_USAR.md con esto" y lo agrega.

## 7. Reglas de oro

1. Dile siempre quién eres.
2. No leas ni pidas releer los PDFs completos: ya están extraídos en `notas/`.
3. Cada quien toca solo su `progreso/<nombre>.md` y su tablero.
4. Tras cambios en el `.md`, vuelve a publicar el tablero.

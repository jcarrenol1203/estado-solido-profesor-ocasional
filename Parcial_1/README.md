# Estado Sólido — "profesor ocasional" con Claude Code

Sistema de auto-estudio para el curso de Estado Sólido (UNAL, sede Medellín),
construido sobre [Claude Code](https://claude.com/claude-code). La idea no es
que la IA dicte clase: es que actúe como un profesor al que le tocas la puerta
con una duda puntual, y que después te tome un examen corto para confirmar
que de verdad dominas el tema.

Cubre la primera parte del curso, **Vibraciones de red** (cristalografía,
enlaces, ondas elásticas, calor específico, cadenas mono/diatómicas, redes 3D,
conductividad térmica de fonones).

## Cómo funciona

1. El PDF del curso se leyó **una sola vez** y se extrajo completo a
   `notas/*.md`, con ecuaciones, derivaciones y cita de página `[p. N]`.
   Claude nunca vuelve a leer el PDF: responde siempre desde las notas.
2. Cada subtema termina con una sección **"Puntos clave para dominar este
   tema"** — esa lista es la base de las evaluaciones.
3. `progreso/progreso.md` es la fuente de verdad de tu avance: 35 subtemas
   con estado `no visto` / `en progreso` / `dominado`, debilidades detectadas
   y log de evaluaciones.

## Los tres comandos

| Comando | Qué hace |
|---|---|
| `/duda <pregunta>` | Responde una duda concreta, corto y con cita de página. Marca el subtema como `en progreso`. |
| `/evaluar <tema>` | Cuando dices "ya domino X": genera ~5 preguntas mezcladas (cálculo, deducción formal, conceptual), corrige contra las notas y actualiza `progreso.md` con debilidades específicas. |
| `/dashboard` | Publica un tablero visual del progreso como página web (Claude Artifact). |

Regla del flujo: la evaluación solo se corre cuando tú la pides — Claude no
te examina por su cuenta.

## Instalación

Necesitas Claude Code instalado y autenticado.

```bash
git clone https://github.com/jcarrenol1203/estado-solido-profesor-ocasional.git
cd estado-solido-profesor-ocasional
cp progreso/progreso.template.md progreso/progreso.md
claude
```

Con eso ya puedes usar `/duda`, `/evaluar` y `/dashboard`. Las notas de
Vibraciones de red ya vienen extraídas, así que **no necesitas el PDF** para
empezar. Si quieres tenerlo a mano para ver las diapositivas originales,
ponlo en la raíz de la carpeta (los `.pdf` y `.doc` están en `.gitignore`
y no se suben al repo — son material del profesor).

## Estructura

```
CLAUDE.md                      # instrucciones para Claude: rol, reglas, flujo
.claude/skills/
  duda/SKILL.md
  evaluar/SKILL.md
  dashboard/SKILL.md
notas/                         # contenido del curso extraído, por subtema
  00_cristalografia_basica.md
  00b_enlaces_fuerzas_interatomicas.md
  01_ondas_elasticas_y_densidad_estados.md
  01b_cadena_monoatomica_discreta.md
  02_cadena_diatomica.md
  03_densidad_estados_calor_especifico.md
  05_vibraciones_red_3D.md
  06_temas_adicionales.md
  07_resumen_arquitectura_materia.md   # resumen visual (21 diap.) verificado vs. las notas
progreso/
  progreso.template.md         # punto de partida en blanco (35 subtemas)
  progreso.md                  # tu avance personal (ignorado por git)
```

## Estudiar en grupo

Cada persona trabaja sobre su propia copia del repo y su propio
`progreso.md`. Para comparar avances, cada quien publica su `/dashboard` y
comparte el link. Si quieren un tablero único donde todos marquen su
progreso en la misma página, el artifact se puede reconstruir con una base
de datos compartida — está en la lista de mejoras.

## Adaptarlo a otro curso

El sistema no depende del contenido: para otra materia basta con extraer el
material a `notas/*.md` (un archivo por bloque, cada subtema cerrando con
sus "Puntos clave"), regenerar la tabla de `progreso.template.md` con los
nuevos IDs, y ajustar `CLAUDE.md`.

# Resumen visual: "Arquitectura Dinámica de la Materia: Vibraciones de Red en Sólidos"

> **Fuente:** `Arquitectura_de_la_Materia.pdf` (21 diapositivas, generado con Gemini Notebook a partir del PDF principal). Es un **resumen pedagógico**, no material del profesor: útil para explicaciones cortas y visuales, pero ante cualquier diferencia manda `vibraciones de red(ultima versión).pdf` (vía `notas/00-06`). Extraído una sola vez; no releer. Citas como `[r. N]` = diapositiva N del resumen.

## Estructura en "actos" y dónde vive cada cosa en las notas

| Acto / diapositivas | Contenido | Nota detallada |
|---|---|---|
| Portada [r. 1] | Del espacio real al de momentos y la termodinámica de fonones | — |
| Acto 1 [r. 2-4] | Simbología real (a,b,c; R; m,n,p; V_c). Cristal → red espacial (sin significado físico) → base (átomo/grupo por nodo) → estructura = red + base. Invariancia traslacional (A=B=C). R = m**a**+n**b**+p**c** con índices enteros y vectores base no colineales | `00_cristalografia_basica.md` §1-5 |
| Acto 2 [r. 5-7] | Simbología recíproca (a\*,b\*,c\*; G_n; V\*). Espacio real (posiciones, longitud; geometría/defectos) vs. recíproco (1/longitud; difracción, momento electrónico, dispersión de fonones), "mutuamente conjugadas". a\* = (b×c)/V_c; V_c = a·(b×c); a·a\*=1, a·b\*=0 | `00_cristalografia_basica.md` §8 |
| Acto 3 [r. 8-11] | Simbología de ondas (q, ω, λ, v_p, v_g, v_s). En red discreta λ no es única: q=π/2a (λ=4a) y q'=q+2π/a (λ'=4a/5) dan los mismos desplazamientos; ω(q) periódica. v_g transporta la energía; onda estacionaria ⇒ v_g=0. v_p=ω/\|q\|, v_g=dω/dq; λ≫a ⇒ medio no dispersivo (v_g=v_p=v_s) | `01b_cadena_monoatomica_discreta.md` (velocidades, periodicidad) |
| Acto 4 [r. 12-14] | 1ZB = celda primitiva del espacio recíproco; L, N. ω(q)=ω_m\|sin(qa/2)\| en [-π/a, π/a]; q fuera de la 1ZB es redundante. PBC: q=n·2π/L ⇒ (2π/a)/(2π/L)=L/a=N modos en la 1ZB | `01b_cadena_monoatomica_discreta.md`, `01_ondas_elasticas...md` (PBC), `00_...` §9 (1ZB) |
| Acto 5 [r. 15-18] | LA/TA; en direcciones de alta simetría ([100]) ondas puras L o T; ω_L>ω_T (fuerza restauradora longitudinal mayor). Acústicas: fase, ω→0 con q→0, siempre 3 (1 LA + 2 TA). Ópticas: contrafase, momento dipolar (absorción IR), ω≠0 en q→0, 3r−3 ramas. Al medido (neutrones/rayos X inelásticos) a lo largo de [110] y [100]; teoría de grupos dicta la degeneración; se ajustan las constantes de fuerza α | `05_vibraciones_red_3D.md`, `02_cadena_diatomica.md` |
| Acto 6 [r. 19-21] | Solo armónico ⇒ l→∞, ρ_térmica=0, κ→∞; la resistividad real viene de la anarmonicidad (colisión fonón-fonón). Normal: q₁+q₂=q₃ (dentro de 1ZB), conserva flujo, no da resistencia. Umklapp: q₁+q₂=q₃+**G**=q₄, q₄ casi opuesta a q₁,q₂, invierte/atenúa flujo, fuente de resistencia a T alta | `06_temas_adicionales.md` §"Procesos normales vs. Umklapp" |

## Verificación contra las notas (resultado)

**Coincide sin cambios:** todo lo anterior salvo lo listado abajo. En particular verifiqué: 3r−3 ramas ópticas, 3 acústicas (1 LA + 2 TA), N modos en la 1ZB, q=π/2a ↔ q'=q+2π/a (λ=4a ↔ 4a/5, ya está en `01b` línea 95), v_g=0 en onda estacionaria, ω_L>ω_T, Al [110]/[100] con neutrones/rayos X, N vs. U y T alta.

**Diferencias / cuidados detectados (ninguna cambia el contenido del curso):**

1. **Convención del recíproco mezclada.** El resumen define a\*=(b×c)/V_c (**sin 2π**, cristalográfica, V\*=1/V_c) pero después usa la 1ZB y la periodicidad de ω(q) con **2π/a** y π/a (convención **con 2π**). **Estandarizado:** `00_...` §8 ahora tiene una tabla comparativa y etiqueta cada fórmula como **[A]** (sin 2π) o **[B]** (con 2π). Regla del proyecto: para fonones (`01`-`06`) y para leer este resumen se usa siempre **[B]** (1ZB=±π/a, G=2π/a, V\*=(2π)³/V_c); la a\*=(b×c)/V_c de la diap. 6 debe leerse como [A] y multiplicarse por 2π.
2. **Errata en [r. 7]:** el determinante escrito con asteriscos (b_y\*c_z − …) es un error tipográfico del resumen; los componentes de b y c en el producto cruz **no** llevan asterisco (son vectores de la red directa). Errata menor en [r. 8]: "idénticc".
3. **Interpretación geométrica que faltaba en las notas** [r. 7]: \|b×c\| es el área de la cara de la celda perpendicular a **a\***, y por eso a\* ⟂ plano (b,c). Se agregó a `00_...` §8.
4. **1ZB = celda unitaria primitiva del espacio recíproco** [r. 12]: ya estaba como "Wigner-Seitz de la recíproca" (`00_...` §9); se agregó la equivalencia explícita.
5. **Simplificación del resumen** [r. 16]: "ópticas: ω máxima en el centro de zona". Es cierto en la cadena diatómica (ω_max en q=0), pero no es una regla general de toda rama óptica; para examen usar la afirmación fiable: **ω≠0 en q→0**.
6. **Afirmación fuerte** [r. 20]: "los Procesos U SON la fuente primaria de resistencia térmica intrínseca a T alta" — coincide con el PDF principal (`06_...`, p. 186), pero a T baja el límite es geométrico/de tamaño (K∝T³), no Umklapp.

## Uso sugerido

- `/duda`: si la duda es conceptual/visual (¿qué es una zona de Brillouin?, ¿N vs. U?), la estructura por "actos" de arriba sirve como guion corto; citar siempre la nota detallada y su `[p. N]` del PDF principal.
- `/evaluar`: no aporta preguntas nuevas (no hay ejercicios), pero los puntos 1-3 y 5 de arriba son buenas preguntas conceptuales de "trampa" (convenciones de 2π, ω máxima en centro de zona).

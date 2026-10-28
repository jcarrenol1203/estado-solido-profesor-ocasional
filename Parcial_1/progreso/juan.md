# Progreso — Vibraciones de red (perfil: Juan)

Fuente de verdad del avance de **Juan** en este bloque del curso. La leen y
actualizan los skills `/duda`, `/evaluar` y `/dashboard` cuando el perfil
activo es Juan. Nunca se llena "a mano" desde el PDF ni desde los exámenes
viejos — todo sale de `notas/*.md` y `examenes/*.md`.

Este archivo reemplaza a `progreso/progreso.md` (ahora `progreso/progreso.legacy.md`,
solo como respaldo histórico), migrado el 2026-09-26 al dividir el sistema en
dos perfiles independientes (Juan e Isa — ver `progreso/isa.md`).

Estados posibles: `no visto` | `en progreso` | `dominado`.

**Dashboard URL:** https://claude.ai/artifact/ET1c6uP2osyBq2a7KrdDq1

---

## Resumen rápido (41 subtemas)

| ID | Subtema | Archivo | Estado | Última evaluación |
|---|---|---|---|---|
| crist.1 | Definición de cristal y orden atómico | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.2 | Red cristalina como abstracción geométrica | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.3 | Redes de Bravais vs. no-Bravais | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.4 | Vectores base y vectores de red | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.5 | Celda unitaria, primitiva y Wigner-Seitz | 00_cristalografia_basica.md | en progreso | 2026-10-01 |
| crist.6 | Sistemas cristalinos (7 sistemas) | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.7 | Monocristal vs. policristal | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.8 | Red recíproca (derivación completa) | 00_cristalografia_basica.md | dominado | 2026-09-26 |
| crist.9 | Primera zona de Brillouin (SC/BCC/FCC) | 00_cristalografia_basica.md | en progreso | 2026-10-01 |
| enlace.1 | Origen de las fuerzas interatómicas | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.2 | Enlace iónico | 00b_enlaces_fuerzas_interatomicas.md | en progreso | 2026-09-28 |
| enlace.3 | Enlace covalente | 00b_enlaces_fuerzas_interatomicas.md | en progreso | 2026-10-01 |
| enlace.4 | Enlace mixto (II-VI, III-V) | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.5 | Enlace metálico | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.6 | Enlace de Van der Waals | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.7 | Alotropía | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.8 | Energía de cohesión y constante de Madelung | 00b_enlaces_fuerzas_interatomicas.md | dominado | 2026-09-28 |
| enlace.9 | Modelo de jellium (ion en mar de electrones) | 00b_enlaces_fuerzas_interatomicas.md | no visto | — |
| ondas.1 | Motivación: ondas de sonido y vibraciones de red | 01_ondas_elasticas_y_densidad_estados.md | dominado | 2026-09-30 |
| ondas.2 | Ecuación de onda elástica (medio continuo 1D) | 01_ondas_elasticas_y_densidad_estados.md | dominado | 2026-09-30 |
| ondas.3 | Densidad de estados g(ω) en 1D (continuo) | 01_ondas_elasticas_y_densidad_estados.md | dominado | 2026-09-30 |
| ondas.4 | Densidad de estados g(ω) en 3D (continuo) | 01_ondas_elasticas_y_densidad_estados.md | dominado | 2026-09-30 |
| monoat.1 | Cadena monoatómica discreta: ecuación de movimiento, ω(q), velocidades y g(ω) | 01b_cadena_monoatomica_discreta.md | dominado | 2026-10-01 |
| monoat.2 | Cadena monoatómica con acoplamiento a segundos vecinos | 01b_cadena_monoatomica_discreta.md | dominado | 2026-10-01 |
| calor.1 | Ley de Dulong-Petit | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.2 | Teoría clásica (equipartición) | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.3 | Modelo de Einstein | 03_densidad_estados_calor_especifico.md | dominado* | 2026-09-30 |
| calor.4 | Modelo de Debye | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.5 | Limitaciones del modelo de Debye | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.6 | El fonón (concepto, energía y momento) | 03_densidad_estados_calor_especifico.md | dominado* | 2026-09-30 |
| calor.7 | Estadística de fonones (Bose-Einstein, número de ocupación) | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.8 | Modelo de Debye en dimensión general D (1D/2D/3D) | 03_densidad_estados_calor_especifico.md | dominado | 2026-09-30 |
| calor.9 | Energía de punto cero en Debye | 03_densidad_estados_calor_especifico.md | en progreso | 2026-10-01 |
| calor.10 | Dispersión inelástica de fotones/neutrones por fonones | 03_densidad_estados_calor_especifico.md | en progreso | 2026-10-01 |
| calor.11 | Momento total real del cristal vs. momento cristalino ℏq | 03_densidad_estados_calor_especifico.md | en progreso | 2026-10-01 |
| diatom.1 | Cadena diatómica: ramas acústica/óptica, gap, modos | 02_cadena_diatomica.md | en progreso | 2026-10-01 |
| extra.1 | Anarmonicidad y expansión térmica | 06_temas_adicionales.md | dominado | 2026-09-30 |
| red3d.1 | Vibraciones en redes 3D (ramas, simetría, g(ω), C_V exacto) | 05_vibraciones_red_3D.md | en progreso | 2026-10-01 |
| extra.2 | Conductividad térmica de fonones | 06_temas_adicionales.md | dominado | 2026-10-01 |
| extra.3 | Mecanismos de dispersión de fonones (Umklapp) | 06_temas_adicionales.md | dominado | 2026-10-01 |
| extra.4 | Aplicaciones de ondas acústicas (ultrasonido, microondas) | 06_temas_adicionales.md | en progreso | 2026-10-01 |

*(Nota de orden: igual que en el archivo original — `extra.1` va después de `calor.7`/`calor.8-11` y antes de `monoat.1`/`monoat.2`/`diatom.1`/`red3d.1` en el temario real del PDF. `extra.2-4` van al final, tras `red3d.1`. La tabla de arriba está en orden alfabético de ID por simplicidad de lectura; el orden de estudio recomendado es el de la sección "Checklist detallado" más abajo. Los subtemas `monoat.2`, `calor.8-11` y `enlace.9` no vienen del PDF — vienen de vacíos detectados en `Parciales y Talleres/`, ver `examenes/analisis_temas.md`.)*

**Debilidades vigentes:**
- **Examen ABCD 4, solo teórico (22 preguntas), 2026-10-01:** 19/22. Fallos: (P4, enlace.3) el enlace covalente es direccional (orbitales hibridados, p. ej. sp³ con 4 vecinos en el diamante); eligió «no direccional». (P13, calor.9) el punto cero NO afecta C_V (E₀ es constante en T y C_V=∂E/∂T lo elimina); sí se ve en ⟨u²⟩(T→0)≠0; eligió «calor específico a T baja». Es la 2ª vez que confunde dónde aparece el punto cero (también en el examen 1, P9). (P22, extra.4) la onda se amplifica si v_drift>v_s (los electrones ceden energía a la onda); eligió «las impurezas dispersan». enlace.3 vuelve a `en progreso`; calor.9 y extra.4 siguen `en progreso`. Sin fallos en cristalografía, ondas, Einstein/Debye, fonón, cadenas, 3D, anarmonicidad ni Umklapp. P16 del examen 3 sigue sin respuesta de Juan.
- **Examen ABCD 3 (22 preguntas), 2026-10-01:** 8 fallos, 11 aciertos reales + P15 correcta (la dio por hecha, es solo reemplazar) + P17 dada por buena a pedido de Juan (restar ω_opt−ω_ac, no evaluada) + P16 pendiente de aclarar. Fallos: (P1, crist.5) la celda primitiva BCC tiene V=a³/2 (la convencional tiene 2 puntos); eligió a³. (P3, crist.9) la 1ª ZB de BCC es el dodecaedro rómbico; eligió octaedro truncado. Es el mismo cruce BCC/FCC del examen 1 al revés; regla: la ZB de una red es la celda W-S de su recíproca (ZB de BCC = W-S de FCC = dodecaedro rómbico; ZB de FCC = W-S de BCC = octaedro truncado). (P12, calor.7) n̄=1/(e−1)=0.58 para ħω=k_BT; eligió 1.00. (P13, calor.9) rms=√(4.6×10⁻²² m²)=2.1×10⁻¹¹ m=0.21 Å; eligió 0.02 Å (potencia de 10). (P14, calor.10) los fonones de borde sí existen; la luz visible no los alcanza porque q≤2k~10⁷ m⁻¹≪π/a~10¹⁰ m⁻¹; eligió «no existen». (P18, diatom.1) en q=π/a, rama acústica, solo se mueven los átomos pesados (ω²=2α/M₁); los ligeros quedan en reposo (u₂=0); eligió ambos en fase. (P20, red3d.1) 1 mol de NaCl (r=2) a T alta: 6R; eligió 3R; **tercer fallo seguido en olvidar el factor r** (3rNk_B). (P21, extra.1) ⟨Δx⟩=3bk_BT/β²≈5.0×10⁻¹² m a 600 K; eligió 5.0×10⁻¹⁴ (2 potencias de 10 de menos). Patrón: errores de potencias de 10 siguen en 3 de 8 fallos. crist.5, calor.10 y diatom.1 vuelven a `en progreso`; calor.7 y extra.1 quedan `dominado` con esta nota (fallos aritméticos).
- **Examen ABCD 2 (22 preguntas), 2026-10-01:** 17/22. Fallos: (P7, ondas.4) calculó mal el factor 1/v_L³+2/v_T³ con v_L=2v_T: da 1/8+2=17/8 (1/v_T³), no 5/2 (no elevó v_L al cubo). (P8, ondas.2) v=√(Y/ρ)=√(1.25×10⁷)=3.5×10³ m/s; eligió 1.1×10⁴ (error de un factor 10 en la raíz). (P10, calor.9, 2º fallo seguido) E₀=(9/8)RΘ_D=1.125·8.314·344≈3.2 kJ/mol; eligió 32 kJ/mol (otro factor 10). (P20, red3d.1) a T≫θ_D, C_V→3rNk_B=12Nk_B con r=4; eligió 3Nk_B (olvidó que hay 3r modos por celda, 3rN en total). (P22, extra.4) el efecto acustoeléctrico amplifica la onda cuando v_drift>v_s, no cuando v_drift<v_s. Patrón: 3 de los 5 fallos son deslices numéricos de potencias de 10 o de cubos, no conceptuales; ondas.2 y ondas.4 se dejan en `dominado` con esta nota. red3d.1 y extra.4 vuelven a `en progreso`.
- **Examen ABCD tipo parcial 2026-1S (22 preguntas), 2026-10-01:** 19/22. Fallos: (P2, crist.9) eligió dodecaedro rómbico para la 1ª ZB de FCC; esa es la de BCC, la de FCC es el octaedro truncado [p. 36] (recuerda: la ZB de la FCC es la celda W-S de su recíproca BCC, y viceversa). (P9, calor.9) eligió que E₀=(9/8)Nk_Bθ_D aporta una constante a C_V; C_V=∂E/∂T la elimina, y lo que sí queda es ⟨u²⟩(0)=9ħ/(4Mω_D), mayor en sólidos ligeros o blandos. (P10, calor.11) eligió ħq como momento total con un modo q excitado; el momento mecánico es 0 por Σe^{iqna}=0 (q≠0 en la 1ª ZB), y ħq es cuasi-momento. Los tres vuelven a `en progreso`.
- **Bloque 0b:**
  - enlace.2: al contrastar NaCl con un metal (ronda 2, 2026-09-28) listó σ baja y transparencia visible, pero omitió el pico de reflectividad en el IR lejano, la temperatura de fusión alta y la presión de vapor baja [p. 39]. Un repaso rápido de esa lista lo cierra.
  - enlace.9 (jellium): la resolvió bien en la ronda 2 (R, Gauss, ω², cobre ≈ 2.8×10¹³ rad/s, v ≈ 3.9×10³ m/s), pero Juan pidió dejarlo en `no visto`: es solo un primer contacto, quiere repasarlo cuando avance más en la teoría.
- **Bloque 1 (ondas.1-4):** `dominado`, sin errores. Tres matices menores a pulir: nombrar el acoplamiento entre vecinos como causa de la propagación de energía (ondas.1), definir q = 2π/λ además de sus unidades (ondas.2), y explicitar la igualdad dN = g(ω)dω entre el cascarón en q y el intervalo en ω (ondas.4).
- **Bloque 2 (calor.1-11), 2026-09-30:** 9 de 11 dominados por evaluación; calor.3 y calor.6 marcados `dominado*` por pedido de Juan, sin reevaluar. Puntos a repasar:
  - calor.3 (Einstein): al explicar por qué predice caída exponencial y no T³, dio solo la mitad (una única ω_E, ningún oscilador se excita a T baja) y omitió el contraste con el cristal real: los modos colectivos de baja frecuencia sí se excitan a T baja y dan el T³ [p. 96]. Además, la derivación de ε̄ y el valor numérico de C_V(T=2θ_E) ≈ 0.98·3R quedaron sin revisar (Juan los dio por hechos en su cuaderno).
  - calor.6 (fonón): en las diferencias fonón/fotón dio otras válidas (necesita medio; momento cristalino vs real) pero no las dos de la diapositiva [p. 100]: v_g=f(λ) por la relación de dispersión y ω_max limitada por ω_corte.
  - Matiz menor en calor.11: explicó P_mec=0 en palabras (los movimientos se compensan); falta citar la suma geométrica Σe^(iqna)=0 para q≠0 en la 1ª ZB.
  - Las derivaciones P1a, P2a-b y P3a las dio Juan por hechas en su cuaderno y no se revisaron aquí; los subtemas calor.1, 2 y 4 se marcaron por el resto de sus respuestas.
- **Bloque 3 (extra.1), 2026-09-30:** `dominado`, 4 de 5 preguntas sólidas (P1-P4, con la deducción completa de ⟨Δx⟩=3bk_BT/β²). Matiz: en P5 dijo que faltaba el valor de b (el enunciado daba b=8×10¹⁰ N/m², β=20 N/m, a=2.5 Å) y en su lugar estimó ⟨Δx⟩=α_L·a·T con el α_L de P1, lo que es circular. Con los datos dados salen ⟨Δx⟩≈2.5×10⁻¹² m a 300 K (≈1% de a), ≈5.0×10⁻¹² m a 600 K (≈2%) y α_L≈3.3×10⁻⁵ K⁻¹ (mismo orden que el 1.7×10⁻⁵ de P1, no idéntico). Falta solo ese cálculo numérico.
- **Bloques 4-5 (monoat.1, monoat.2, diatom.1), 2026-10-01:** los tres `dominado`, 5/5 correctas en una evaluación corta **sin demostraciones** (a pedido de Juan). Quedó sin evaluar, para una futura revisión dirigida: la derivación de ω(q) con segundos vecinos y de la ecuación secular diatómica, el vector de Debye q_D de la cadena con segundos vecinos, y las ondas evanescentes en el gap (q complejo, constante de atenuación κ; Juan mostró confusión en /duda y pidió explicación dos veces). Matiz en P3: su v_g(q=0)=v_s es correcto; la nota original de monoat.2 decía que se anulaba (error mío, ya corregido).
- **Bloque 6 (red3d.1), 2026-10-01:** `dominado`, 5/5 correctas en una evaluación corta **sin demostraciones** (a pedido de Juan). Sin evaluar: el armado de la ecuación de movimiento vectorial y de la secular 3×3, el procedimiento de comparación con el experimento (ajustar α con ω(**q**) medida por rayos X o neutrones [p. 161]) y el ejemplo del Ge. Matiz de nombre: llamó «inversión temporal» a ω(−q)=ω(q); es física válida, pero la diapositiva lo nombra simetría de inversión [p. 162].
- **Bloque 7 (extra.2, extra.3, extra.4), 2026-10-01:** los tres `dominado`, 5/5 correctas en una evaluación corta **sin demostraciones** (a pedido de Juan). Sin evaluar: la derivación de la ecuación de difusión [p. 171-172] y de K∝1/T a T alta (Parcial SS2020 #1), la forma de ℓ(T) en cada régimen, la interacción espín-fonón [p. 193-194], el amplificador acústico de MgO [p. 193] y las ondas Rayleigh [p. 196]. Las p. 177-178 siguen sin cubrir en las notas. Matiz en P5b: faltó el detalle microscópico del efecto acustoeléctrico (más electrones en la ladera descendente del potencial, que «deslizan» hacia el fondo y ceden energía a la onda [p. 195]); la condición v_drift > v_s y la transferencia de energía estaban bien.
- Bloque 0 completo (crist.1-9): sin debilidades, `dominado` limpio.
- Debilidades del 0b detectadas en la ronda 1 (enlace.1/3 covalente cuántico, enlace.5 propiedades ópticas del metal, enlace.6 Van der Waals, enlace.8 ζ_b y signo en U₀): resueltas en la ronda 2.

## Parciales y talleres (banco de examenes viejos)

| ID | Tipo | Estado | Nota | Fecha |
|---|---|---|---|---|
| P-2026-1S | Parcial (18 selección múltiple) | no intentado | — | — |
| P-2025-01 | Parcial (abierto, 2 imágenes) | no intentado | — | — |
| P-SS2020 | Parcial (abierto, 4 preguntas) | no intentado | — | — |
| T-SS2020 | Taller (abierto, 8 preguntas) | no intentado | — | — |
| T-2025-II | Taller (abierto, 7 preguntas) | no intentado | — | — |
| T-2025-01 | Taller (abierto, 4 preguntas) | no intentado | — | — |
| QS1 | Question set conceptual (10 preguntas) | no intentado | — | — |
| QS2 | Question set conceptual (10 preguntas) | no intentado | — | — |
| QS3 | Question set conceptual (10 preguntas) | no intentado | — | — |
| QS4 | Question set conceptual (10 preguntas) | no intentado | — | — |
| QS5 | Question set conceptual (10 preguntas) | no intentado | — | — |
| QS6 | Question set conceptual (11 preguntas) | no intentado | — | — |

## Log de evaluaciones

- **2026-09-26** — Bloque 0 completo (crist.1-9), 9 preguntas mixtas (algunas adaptadas de QS1). Resultado real de la evaluación: 6/9 dominados (crist.1, crist.2, crist.3, crist.4, crist.5, crist.8). 3 en progreso (crist.6, crist.7, crist.9).
- **2026-09-26** — El usuario pidió marcar crist.6, crist.7 y crist.9 como `dominado*` sin nueva evaluación ("son solo conceptos básicos, bajo mis riesgos"). Aplicado tal cual, con asterisco y nota de debilidad original conservada arriba para trazabilidad.
- **2026-09-26** — Repetición dirigida a los "temas a mejorar" de Bloque 0 (crist.6, crist.7, crist.9), 4 preguntas. Resultado: crist.9 resuelto de verdad → `dominado` limpio. crist.6 (clasificación de sistemas) y crist.7 (orden de magnitud de la mosaicidad) siguen con debilidad real, aunque distinta a la original — permanecen `dominado*`.
- **2026-09-26** — Segunda repetición sobre crist.6 y crist.7 (2 preguntas de clasificación + 1 numérica + 1 conceptual). Resultado: 3/4 sólidas, la conceptual de crist.7 quedó incompleta pero sobre un matiz fuera del checklist original (resolución angular vs. ancho de mancha de Bragg). Bloque 0 completo pasa a `dominado` limpio, sin asteriscos.

- **2026-09-28** — Bloque 0b (enlace.1-8) + intro a jellium (enlace.9), 7 preguntas. Resultado: enlace.4, enlace.7 y enlace.8 → `dominado`. enlace.1, 2, 3, 5, 6 quedan `en progreso` (ver debilidades). Pregunta 7 (jellium) sin responder; enlace.9 sigue `en progreso`.
- **2026-09-28** — Ronda 2 del bloque 0b sobre las debilidades de la ronda 1 + jellium, 7 preguntas. Resultado: 7/7 correctas. enlace.1, 3, 5, 6 → `dominado`. enlace.2 sigue `en progreso` (propiedades ópticas del NaCl incompletas). enlace.9 (jellium) respondido bien, pero por pedido explícito de Juan queda en `no visto` para repasar más adelante.
- **2026-09-30** — Bloque 1 completo (ondas.1-4), 6 preguntas mixtas (P1 numérica v_s y ω_max, P2 deducción ecuación de onda, P3 conceptual, P4 g(ω) 1D con condiciones periódicas y fijas, P5 g(ω) 3D con v_L≠v_T, P6 conceptual polarización y factor V; adaptadas de QS2 #5-#9, sin calor específico). Resultado: 6/6 correctas. ondas.1, 2, 3, 4 → `dominado`. Matices menores anotados en debilidades vigentes.
- **2026-09-30** — Bloque 2 completo (calor.1-11), 8 preguntas mixtas (P1 Dulong-Petit y cobre, P2 Einstein, P3 ω_D y θ_D con ley T³ por esfera térmica, P4 velocidad promedio de Debye y θ_D, P5 Debye en D dimensiones, P6 punto cero, P7 dispersión Brillouin, P8 fonón, Bose-Einstein y momento cristalino; adaptadas de QS3, Parcial 2026-1S y talleres). Juan dio por hechas en su cuaderno P1a, P2a-b y P3a. Resultado: calor.1, 2, 4, 5, 7, 8, 9, 10 y 11 → `dominado`. calor.3 y calor.6 quedaron `en progreso` (ver debilidades).
- **2026-09-30** — Juan pidió marcar calor.3 y calor.6 como listos sin reevaluar. Aplicado tal cual: ambos pasan a `dominado*` (asterisco = marcado por pedido del usuario, con los puntos a repasar conservados en debilidades). Bloque 2 completo: 11/11 (9 evaluados + 2 con asterisco).
- **2026-09-30** — Bloque 3 (extra.1, anarmonicidad y expansión térmica), 5 preguntas (P1 gas vs sólido y α_L, P2 por qué el potencial armónico no expande, P3 pozo asimétrico y término cúbico, P4 deducción de ⟨Δx⟩=3bk_BT/β², P5 numérica con b, β y a; adaptadas de QS4 #4 y #5). Resultado: P1-P4 correctas; P5 sin usar los datos del enunciado (ver debilidades). extra.1 → `dominado`.
- **2026-10-01** — Bloques 4-5 (monoat.1, monoat.2, diatom.1), 5 preguntas cortas sin demostraciones, a pedido de Juan (P1 numérica ω_m, v_s, v_g, v_p; P2 zona de Brillouin, conteo de modos y van Hove; P3 segundos vecinos, v_s y v_g; P4 numérica diatómica con bordes de zona, ω óptica en q=0 y A₂/A₁; P5 conceptual gap, absorción IR y 2N modos; adaptadas de Parcial SS2020 #2 y QS5 #4, #5, #7). Resultado: 5/5 correctas. monoat.1, monoat.2 y diatom.1 → `dominado`. Pendientes anotados en debilidades.
- **2026-10-01** — Bloque 6 (red3d.1), 5 preguntas cortas sin demostraciones, a pedido de Juan (P1 numérica conteo de ramas y modos con r=4, N=10²⁰; P2 polarización LA/TA y ω_L>ω_T; P3 simetrías de ω_j(q); P4 método del contorno, g total y picos de van Hove; P5 fórmula exacta de C_V, Debye vs Einstein y límite de alta T 3rNk_B; sin preguntas del banco de exámenes para este subtema). Resultado: 5/5 correctas. red3d.1 → `dominado`.
- **2026-10-01** — Bloque 7 (extra.2, extra.3, extra.4), 5 preguntas cortas sin demostraciones, a pedido de Juan (P1 numérica K=⅓C_Vvℓ para Si y cambio de ℓ entre 273 K y 20 K; P2 K como propiedad de no equilibrio y difusión frente a onda; P3 los tres mecanismos de dispersión, inefectividad a T<10 K y barras de LiF; P4 procesos normales frente a Umklapp; P5 haz coherente piezoeléctrico, efecto acustoeléctrico y línea de retardo de 8 cm; adaptadas de QS6 #1, #5, #7, #8, #10 y #11). Resultado: 5/5 correctas. extra.2, extra.3 y extra.4 → `dominado`.
- **2026-10-01** — Examen ABCD (22 preguntas, 5 opciones) de todo el bloque, estilo Parcial 2026-1S (originales, no las del banco). Resultado: 19/22. Acertó cristalografía (recíproca FCC), Madelung, alotropía, g(ω) 1D, θ_D numérico, Einstein/Debye a T baja, neutrones, Bose-Einstein, cadenas mono/diatómica, 3D, anarmonicidad, conductividad térmica, Umklapp y acústica. Falló P2 (crist.9), P9 (calor.9), P10 (calor.11) → `en progreso`.
- **2026-10-01** — Examen ABCD 2 (22 preguntas, 5 opciones, originales) de todo el bloque, con foco en los fallos del examen 1. Resultado: 17/22. Mejoró crist.9 (P3 q≡q+G bien) y calor.11 (P9 cuasi-momento bien). Falló P7 (ondas.4), P8 (ondas.2), P10 (calor.9), P20 (red3d.1), P22 (extra.4); ver debilidades.
- **2026-10-01** — Examen ABCD 3 (22 preguntas, originales). Resultado: 11 aciertos + P15 correcta + P17 dada por buena a pedido + P16 por aclarar; 8 fallos (P1, 3, 12, 13, 14, 18, 20, 21). crist.5, calor.10 y diatom.1 → `en progreso`; crist.9, calor.9 y red3d.1 siguen `en progreso`. Ver debilidades.
- **2026-10-01** — Examen ABCD 4 (22 preguntas, solo teórico, originales). Resultado: 19/22. Fallos P4 (enlace.3), P13 (calor.9), P22 (extra.4). enlace.3 → `en progreso`; calor.9 y extra.4 siguen `en progreso`.

---

## Checklist detallado — qué debes saber, tema por tema

Orden de estudio recomendado (sigue el orden real del PDF, con los subtemas
nuevos intercalados en su bloque temático). Cada subtema tiene su rango de
páginas (o su fuente de examen, si no viene del PDF) para consulta puntual.

### Bloque 0 — Cristalografía básica [p. 4-36]

Ver `notas/00_cristalografia_basica.md` para el checklist completo de
crist.1-9 (idéntico al de `progreso.legacy.md`, sin cambios).

### Bloque 0b — Enlaces y fuerzas interatómicas [p. 37-54 + examen]

Ver `notas/00b_enlaces_fuerzas_interatomicas.md` para enlace.1-8 (sin
cambios). Nuevo:

**enlace.9 — Modelo de jellium (ion en mar de electrones)** [fuente: examen — Taller SS2020 #4]
- Plantear el modelo (ion +e en el centro de una esfera de electrones de conducción de densidad n, radio R por neutralidad de carga) y derivar, vía ley de Gauss, que el campo dentro de la esfera crece linealmente con el desplazamiento.
- Derivar ω²=ne²/(3ε₀M) (equivalentemente e²/4πε₀MR³) como frecuencia de oscilación armónica del ion desplazado.
- Estimar el orden de magnitud de ω y de la velocidad del sonido en un metal a partir de este modelo, sin invocar la teoría del electrón libre.

### Bloque 1 — Ondas elásticas (medio continuo) [p. 45-66]

Ver `notas/01_ondas_elasticas_y_densidad_estados.md` para ondas.1-4 (sin cambios).

### Bloque 2 — Calor específico de la red [p. 67-103 + examen]

Ver `notas/03_densidad_estados_calor_especifico.md` para calor.1-7 (sin
cambios). Nuevos:

**calor.8 — Modelo de Debye en dimensión general D** [fuente: examen — Taller SS2020 #1, #6; Taller 2025-II #5]
- Saber que g(ω)∝ω^(D-1) en dimensión D, generalizando el conteo de estados 1D/3D ya visto.
- Reproducir el argumento de la "esfera/círculo térmica" en D dimensiones dando C_V∝T^D.
- Derivar explícitamente C_V(1D)∝T y C_V(2D)∝T² a T baja.

**calor.9 — Energía de punto cero en Debye** [fuente: examen — Taller 01-2025 #2, #3]
- Derivar E₀=(9/8)Nk_BΘ_D integrando ℏω/2 sobre g(ω)=9Nω²/ω_D³.
- Escribir ⟨u²⟩=(9ℏ/Mω_D³)∫₀^ωD[n̄(ω)+1/2]ω dω y evaluar su límite T→0.
- Explicar por qué el punto cero es mayor en sólidos ligeros o "blandos" (M o Θ_D pequeños).

**calor.10 — Dispersión inelástica de fotones/neutrones por fonones** [fuente: examen — Taller SS2020 #5, Taller 2025-II #6]
- Plantear conservación de energía y momento cristalino en la dispersión de un fotón/neutrón por un fonón.
- Usar la ley de cosenos en el triángulo de vectores de onda para hallar q, y Ω=v_sq para hallar la frecuencia del fonón.
- Distinguir el caso fotón (k_i≈k_f) del caso neutrón (energía cambia apreciablemente).

**calor.11 — Momento total real vs. momento cristalino ℏq** [fuente: examen — Taller 2025-II #1, Taller SS2020 #8]
- Derivar que el momento mecánico total de un cristal con un modo q≠0 excitado es exactamente cero (suma geométrica de raíces de la unidad).
- Explicar que ℏq es momento cristalino/cuasi-momento, no un momento mecánico real — se conserva solo módulo ℏG.

### Bloque 3 — Anarmonicidad (introducción) [p. 104-108]

Ver `notas/06_temas_adicionales.md` para extra.1 (sin cambios).

### Bloque 4 — Cadena monoatómica discreta [p. 109-141 + examen]

Ver `notas/01b_cadena_monoatomica_discreta.md` para monoat.1 (sin cambios). Nuevo:

**monoat.2 — Cadena monoatómica con acoplamiento a segundos vecinos** [fuente: examen — Parcial SS2020 #2]
- Derivar Mω²=2α₁(1-cos qa)+2α₂(1-cos 2qa) para acoplamiento a primeros y segundos vecinos.
- Obtener v_g generalizado y mostrar que sigue anulándose en q=π/a (en q=0 NO se anula: v_g→v_s, límite 0/0).
- Derivar v_s=a√((α₁+4α₂)/M) en el límite q→0.
- Entender que el vector de Debye q_D=π/a de esta cadena no cambia al agregar el segundo vecino.

### Bloque 5 — Cadena diatómica [p. 142-153]

Ver `notas/02_cadena_diatomica.md` para diatom.1 (sin cambios).

### Bloque 6 — Vibraciones en redes 3D [p. 154-172]

Ver `notas/05_vibraciones_red_3D.md` para red3d.1 (sin cambios).

### Bloque 7 — Conductividad térmica y aplicaciones [p. 169-196]

Ver `notas/06_temas_adicionales.md` para extra.2-4 (sin cambios).

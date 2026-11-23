# Progreso — Parcial 2 (metales y electrón libre)

Fuente de verdad del avance del usuario en este bloque del curso. La leen y actualizan los skills `/duda`, `/evaluar` y `/dashboard` (con `BASE=Parcial_2/`). Nunca se llena "a mano" desde el PDF — todo sale de `notas/*.md`.

Estados posibles: `no visto` | `en progreso` | `dominado` | `fuera de alcance`.

**Alcance del parcial: diapositivas 1-70 de `Metales 2021.pdf`** (según el profesor). Los subtemas `fuera de alcance` (p. >70, o temas de exámenes viejos que dependen de ellas) **no cuentan** en el % de avance ni se evalúan salvo que se pida. Subtemas en alcance: metal.1, gas1d.1, interac.1, drude.1-3, cal.1, cal.2, fermi3d.1, fermi3d.2, extra.3, vib.6.

**Lectura recomendada por el profesor:** Pavlov (Pavlov & Khokhlov, *Física del estado sólido*) como texto de apoyo para estos temas; el mapeo capítulo↔diapositivas está en `notas/08_mapa_pavlov.md` (cada subtema del checklist lleva su referencia "Pavlov: §… p. …").

**Dashboard URL:** https://claude.ai/artifact/LLC4kbKYAmUL7bLB8DeWyt

---

## Resumen rápido (27 subtemas; **12 en alcance**, 15 fuera)

| ID | Subtema | Archivo | Estado | Última evaluación |
|---|---|---|---|---|
| metal.1 | Metales, cristal metálico y concentración de e⁻ ($N=Z_vN_A\rho/M$) | 00_metales_y_gas_de_electrones.md | no visto | — |
| gas1d.1 | Gas de Fermi 1D: niveles, Pauli y $E_F$ | 00_metales_y_gas_de_electrones.md | no visto | — |
| interac.1 | Interacciones e⁻-ion y e⁻-e⁻; gas de e⁻ vs. gas ordinario | 00_metales_y_gas_de_electrones.md | no visto | — |
| drude.1 | Ley de Ohm y ecuación de Drude: $\sigma=Ne^2\tau/m^*$ | 01_modelo_de_drude.md | no visto | — |
| drude.2 | Tiempo de relajación, camino libre, movilidad, Joule | 01_modelo_de_drude.md | no visto | — |
| drude.3 | Origen de $\tau$: ondas de materia, Matthiessen, $\rho(T)$ | 01_modelo_de_drude.md | no visto | — |
| cal.1 | Calor específico electrónico: fracaso clásico | 02_estadistica_fermi_calor_especifico.md | no visto | — |
| cal.2 | Fermi-Dirac, potencial químico, $T_F$ y $C_e\propto T$ | 02_estadistica_fermi_calor_especifico.md | no visto | — |
| cal.3 | Energía interna del gas de Fermi, $U(T)$ | 02_estadistica_fermi_calor_especifico.md | fuera de alcance | — |
| fermi3d.1 | Gas 3D: ondas planas, $k_F$, $E_F$, $v_F$ | 03_gas_de_fermi_3D.md | no visto | — |
| fermi3d.2 | Densidad de estados $D(\varepsilon)$, $E_0$, presión y módulo de rigidez | 03_gas_de_fermi_3D.md | no visto | — |
| fermi3d.3 | Superficie de Fermi | 03_gas_de_fermi_3D.md | fuera de alcance | — |
| trans.1 | Conductividad eléctrica cuántica (esfera desplazada) | 04_transporte.md | fuera de alcance | — |
| trans.2 | Conductividad térmica y Wiedemann-Franz | 04_transporte.md | fuera de alcance | — |
| trans.3 | Resonancia ciclotrónica | 04_transporte.md | fuera de alcance | — |
| trans.4 | Efecto Hall | 04_transporte.md | fuera de alcance | — |
| term.1 | Emisión termoiónica y Richardson-Dushman | 05_emision_termoionica_y_fallas.md | fuera de alcance | — |
| falla.1 | Fallas del modelo del e⁻ libre | 05_emision_termoionica_y_fallas.md | fuera de alcance | — |
| extra.1 | Electrones casi libres: bandas, gaps, aislante/semiconductor/metal | 06_temas_de_examen_fuera_del_pdf.md | fuera de alcance | — |
| extra.2 | Zener magnético | 06_temas_de_examen_fuera_del_pdf.md | fuera de alcance | — |
| extra.3 | Escalas relativistas y astrofísicas del gas de Fermi | 06_temas_de_examen_fuera_del_pdf.md | no visto | — |
| vib.1 | Velocidad de fase/grupo y medios dispersivos | 07_vibraciones_para_parcial_2026_1S.md | fuera de alcance | — |
| vib.2 | Cadena monoatómica: aliasing, $\lambda=2a$, $g(\omega)$ en $\pi/a$ | 07_vibraciones_para_parcial_2026_1S.md | fuera de alcance | — |
| vib.3 | Modos normales, Bragg y ramas acústicas ($\omega_L>\omega_T$) | 07_vibraciones_para_parcial_2026_1S.md | fuera de alcance | — |
| vib.4 | Cadena diatómica: ramas, gap, $M\to m$, borde de zona | 07_vibraciones_para_parcial_2026_1S.md | fuera de alcance | — |
| vib.5 | Umklapp y conductividad térmica de fonones | 07_vibraciones_para_parcial_2026_1S.md | fuera de alcance | — |
| vib.6 | Definición de $E_F$ a $T=0$ (pregunta de metales del parcial) | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |

*(Nota de orden: el orden de estudio recomendado es el de la sección "Checklist detallado" más abajo, que sigue el temario de las diapositivas. `extra.1-3` no vienen del PDF — salen de vacíos detectados en `Talleres_Parciales/`, ver `examenes/analisis_temas.md`.)*

**Debilidades vigentes:** ninguna todavía (no se ha hecho ninguna evaluación).

<!-- CHECKLISTS:START -->
## Seguimiento de checklists

Generado por `.claude/skills/dashboard/tools.py sync`; cambia solo las columnas Estado y Nota (el texto sale de los `.md` de contenido).
Estados: teoría/práctica/viejos `pendiente | en progreso | hecho`; examen `pendiente | entregado | calificado` (Nota = `obtenido/máximo`).

### Teoría (43 ítems)

| ID | Ítem | Estado | Nota |
|---|---|---|---|
| T.metal.1.1 | Describir el cristal metálico (pozos $U$ + gas de e⁻ libres) y cómo el e⁻ 3s del Na pasa a e⁻ de conducción | pendiente | — |
| T.metal.1.2 | Calcular $N=Z_vN_A\rho/M$ y distinguir monovalentes de divalentes | pendiente | — |
| T.metal.1.3 | Éxitos (Ohm, W-F) y fracasos (calor específico, camino libre largo) de la teoría clásica | pendiente | — |
| T.metal.1.4 | Las dos razones de la "transparencia" del cristal (periodicidad y Pauli) | pendiente | — |
| T.metal.1.5 | Pavlov §2.6: enlace metálico y modelo iónico de la energía de cohesión ($r_s/a_0=1.6$) | pendiente | — |
| T.gas1d.1.1 | Deducir $\varepsilon_n=\hbar^2\pi^2n^2/2mL^2$ desde $\psi(0)=\psi(L)=0$ | pendiente | — |
| T.gas1d.1.2 | Estado exacto vs. aproximado de $N$ e⁻ (exacto solo sin interacción) | pendiente | — |
| T.gas1d.1.3 | Pauli en 1D: 2 e⁻ por nivel, condición $2n_F=N$ | pendiente | — |
| T.gas1d.1.4 | Calcular $\varepsilon_F$ en 1D y construir el estado fundamental | pendiente | — |
| T.interac.1.1 | Por qué e⁻-ion (seudopotencial, apantallamiento) y e⁻-e⁻ (Pauli + energía mínima) son débiles | pendiente | — |
| T.interac.1.2 | Gas de e⁻ vs. gas ordinario (densidad, plasma, FD vs. MB, $E(T{=}0)\neq0$) y las dos aproximaciones de Pavlov §7.1 | pendiente | — |
| T.drude.1.1 | Escribir $m^*\dot{\mathbf v}=-e\mathbf E-m^*\mathbf v/\tau$ y resolver el estacionario $v_d=-e\tau E/m^*$ | pendiente | — |
| T.drude.1.2 | Deducir $\mathbf J=-Nev_d$ y $\sigma=Ne^2\tau/m^*$ (y compararlo con Pavlov 6.92-6.96) | pendiente | — |
| T.drude.1.3 | Explicar $v_r\gg v_d$ y que la ley de Ohm es empírica con rango de validez | pendiente | — |
| T.drude.1.4 | Usar $v_d=I/(neA)$ en un alambre | pendiente | — |
| T.drude.2.1 | Interpretar $\tau$: $e^{-t/\tau}$, vida media de supervivencia, $1/\tau$ = frecuencia de colisión | pendiente | — |
| T.drude.2.2 | Relacionar $\ell=v\tau$, $\sigma=Ne^2\ell/m^*v$ y la movilidad $\mu=e\tau/m^*$, $\sigma=Ne\mu$ | pendiente | — |
| T.drude.2.3 | Órdenes de magnitud: $v_d\sim10^{-2}$ m/s, $v_r\sim10^6$ m/s, $\tau\sim10^{-14}$ s, $\ell\sim10^2$ Å | pendiente | — |
| T.drude.2.4 | Explicar $\sigma_m/\sigma_i\sim10^{23}$ y demostrar $P=\sigma E^2\Rightarrow I^2R$ | pendiente | — |
| T.drude.3.1 | Por qué e⁻-e⁻ no cambian $v_d$ ni $J$ y qué colisiones sí | pendiente | — |
| T.drude.3.2 | Resolver la paradoja $\ell\sim100$ Å $\gg a$: red perfecta no dispersa (ondas de materia) | pendiente | — |
| T.drude.3.3 | Enunciar y usar la regla de Matthiessen y la resistividad residual | pendiente | — |
| T.drude.3.4 | Límites de $\rho_{ph}$: $\propto T$ ($T\gg\theta$), $\sim T^5$ (experimental, Debye) y por qué Einstein no basta | pendiente | — |
| T.drude.3.5 | Efecto Kondo como violación de Matthiessen | pendiente | — |
| T.drude.3.6 | Mostrar que con dispersión clásica $\rho\propto T^{3/2}$ y comparar con Pavlov §7.13 ($\rho\propto T$) | pendiente | — |
| T.cal.1.1 | Calcular el valor clásico $C_e=\tfrac32R$ y $C_{total}=4.5R$ y compararlo con el experimental ($\approx3R$) | pendiente | — |
| T.cal.1.2 | Explicar que falla la estadística (MB), no la idea de e⁻ libres (Pavlov p. 200) | pendiente | — |
| T.cal.2.1 | Explicar por qué solo los e⁻ cercanos a $E_F$ (dentro de $k_BT$) absorben energía (Pauli) | pendiente | — |
| T.cal.2.2 | Escribir $f(E)$; mostrar $f(\mu)=\tfrac12$, $\mu(0)=E_F$ y el límite MB en la cola | pendiente | — |
| T.cal.2.3 | Reconstruir $C_e\approx2R\,T/T_F$ (exacto $\tfrac{\pi^2}{2}R\,T/T_F$) y calcular $T_F=E_F/k_B$ | pendiente | — |
| T.cal.2.4 | Dar $C=\gamma T+\beta T^3$ y decir cuál domina a $T\ll\theta_D$ (Pavlov 6.66-6.67) | pendiente | — |
| T.cal.2.5 | Comparar $C_{el}$ y $C_{red}$ y hallar la $T$ en que son del mismo orden | pendiente | — |
| T.cal.2.6 | Anchura de $f(E)$: de 90 % a 10 % ⇒ $\Delta E=2\ln9\,k_BT\approx4.4k_BT$ | pendiente | — |
| T.fermi3d.1.1 | Ventaja de las condiciones periódicas y ondas planas $e^{i\mathbf k\cdot\mathbf r}$ con $k_i=2\pi n_i/L$ ($n_i$ enteros ±) | pendiente | — |
| T.fermi3d.1.2 | Derivar $k_F$ y $E_F$ contando estados en la esfera (factor 2 de espín; volumen por estado $(2\pi/L)^3$) | pendiente | — |
| T.fermi3d.1.3 | Calcular $E_F$, $T_F$, $v_F$ desde $N/V$ (Na, Cu) y comparar con la diap. 67 | pendiente | — |
| T.fermi3d.1.4 | $\langle v\rangle=\tfrac34v_F$ y $\langle E\rangle=\tfrac35E_F$ a $T=0$ | pendiente | — |
| T.fermi3d.2.1 | Derivar $N(\varepsilon)\propto\varepsilon^{3/2}$, $D(\varepsilon)\propto\varepsilon^{1/2}$ y $D(E_F)=3N/2E_F$ | pendiente | — |
| T.fermi3d.2.2 | Usar $N=\int Df$ y entender qué muestra $D\cdot f$ | pendiente | — |
| T.fermi3d.2.3 | Obtener $E_0=\tfrac35NE_F$, $P=\tfrac25nE_F$ y $B=\tfrac23nE_F$ usando $E_F\propto V^{-2/3}$ | pendiente | — |
| T.extra.3.1 | Estimar $N$ de una estrella ($N\approx M/m_p$) y calcular $E_F$ no relativista | pendiente | — |
| T.extra.3.2 | Reconocer cuándo $E_F\gtrsim mc^2$ y usar $E_F\approx\hbar c(3\pi^2n)^{1/3}$; dar $T_F$, $v_F$ y $\langle v\rangle=\tfrac34v_F$ | pendiente | — |
| T.vib.6.1 | Definir $E_F$ a $T=0$ como el nivel ocupado más alto y distinguirlo de $\mu(T)$, de $\tfrac35E_F$ y de la función trabajo | pendiente | — |

### Práctica (35 ítems)

| ID | Ítem | Estado | Nota |
|---|---|---|---|
| P.metal.1.1 | Concentración $N=Z_vN_A\rho/M$ de Cu, Al, Mg, Na | pendiente | — |
| P.metal.1.2 | Fracción de volumen de los iones en Na (y la inconsistencia de la diap. 7) | pendiente | — |
| P.metal.1.3 | Equilibrio del modelo iónico de Pavlov, $r_s/a_0=1.6$ | pendiente | — |
| P.gas1d.1.1 | Deducir $\varepsilon_n$ desde las condiciones de frontera | pendiente | — |
| P.gas1d.1.2 | $N=6$ e⁻ en 1 nm: $\varepsilon_F$ y excitación mínima | pendiente | — |
| P.gas1d.1.3 | $N=10$ e⁻ en 2 nm, degeneración y caso $N$ impar | pendiente | — |
| P.interac.1.1 | Coulomb desnudo vs. $E_F$ y por qué el modelo funciona | pendiente | — |
| P.interac.1.2 | Gas de e⁻ vs. aire con números | pendiente | — |
| P.drude.1.1 | Deducir $\sigma=Ne^2\tau/m^*$ desde la ecuación de Drude | pendiente | — |
| P.drude.1.2 | $\tau$, $\ell$ y $\mu$ del Cu a partir de $\sigma$ | pendiente | — |
| P.drude.1.3 | $v_d$ vs. $v_F$ en un alambre y en el Na | pendiente | — |
| P.drude.2.1 | Deducir $n(t)=n_0e^{-t/\tau}$ y $t_{av}=\tau$ | pendiente | — |
| P.drude.2.2 | Efecto Joule: $R$, $P=I^2R$ y verificación con $\sigma E^2$ | pendiente | — |
| P.drude.2.3 | Estimar $\sigma_m/\sigma_{sc}$ con $N$ y $v_r$ | pendiente | — |
| P.drude.3.1 | Paradoja del camino libre: choque clásico vs. experimento | pendiente | — |
| P.drude.3.2 | Regla de Matthiessen con números | pendiente | — |
| P.drude.3.3 | Deducir $\rho_{ph}\propto T$ (y $T^{3/2}$ clásico) | pendiente | — |
| P.cal.1.1 | $C_e$ y $C_{total}$ clásicos vs. experimento | pendiente | — |
| P.cal.2.1 | Tabla de $f(E)$ y límite de MB; $f$ a $E_F\pm0.1$ eV | pendiente | — |
| P.cal.2.2 | $T_F$, $T/T_F$ y $C_e$ de Cu y Na a 300 K | pendiente | — |
| P.cal.2.3 | Coeficiente $\gamma$ de Sommerfeld del Cu | pendiente | — |
| P.cal.2.4 | Separar $\gamma$ y $\beta$ de datos de $C/T$ vs. $T^2$ | pendiente | — |
| P.cal.2.5 | Corrección térmica de $\mu$ (Pavlov 6.57) | pendiente | — |
| P.cal.2.6 | Reconstruir la estimación $C_e\approx2RT/T_F$ | pendiente | — |
| P.cal.2.7 | Ancho 99 %→1 % de $f(E)$ | pendiente | — |
| P.fermi3d.1.1 | Deducir $k_F$, $E_F$, $v_F$ contando estados | pendiente | — |
| P.fermi3d.1.2 | $k_F$, $E_F$, $T_F$, $v_F$ de Na, Cu y Al | pendiente | — |
| P.fermi3d.1.3 | Deducir $\langle v\rangle=\tfrac34v_F$ y $\langle E\rangle=\tfrac35E_F$ | pendiente | — |
| P.fermi3d.1.4 | Paredes rígidas vs. periódicas y espaciado de $\mathbf k$ | pendiente | — |
| P.fermi3d.2.1 | Deducir $D(\varepsilon)$ y $D(E_F)=3N/2E_F$ | pendiente | — |
| P.fermi3d.2.2 | $D(E_F)$ del Cu y e⁻ en la franja $k_BT$ | pendiente | — |
| P.fermi3d.2.3 | $E_0$, $P$ y $B$ del Cu | pendiente | — |
| P.extra.3.1 | Enana blanca: $E_F$ no relativista, ultrarrelativista y exacta | pendiente | — |
| P.extra.3.2 | Pulsar y límite ultrarrelativista | pendiente | — |
| P.vib.6.1 | Distinguir $E_F$, $\tfrac35E_F$, $\mu$ y $\phi$ (y `P-2026-1S #11`) | pendiente | — |

### Examen (20 ítems)

| ID | Ítem | Estado | Nota |
|---|---|---|---|
| EX.E.1 | Magnesio: $n$, $k_F$, $E_F$, $T_F$, $v_F$ (`metal.1`, `fermi3d.1`) — 0.5 | pendiente | — |
| EX.E.2 | Alambre de Al (`drude.1`, `drude.2`) — 0.8 | pendiente | — |
| EX.E.3 | Matthiessen en Al (`drude.3`) — 0.6 | pendiente | — |
| EX.E.4 | Potasio a baja $T$ (`cal.2`) — 0.8 | pendiente | — |
| EX.E.5 | Litio: $D(E_F)$, $P$, $B$ (`fermi3d.2`) — 0.7 | pendiente | — |
| EX.E.6 | Gas de e⁻ 2D (`fermi3d.1`, `fermi3d.2`) — 0.7 | pendiente | — |
| EX.E.7 | Cadena de 8 e⁻ (`gas1d.1`) — 0.5 | pendiente | — |
| EX.E.8 | Enana blanca (`extra.3`) — 0.4 | pendiente | — |
| EX.T.1 | Metal y concentración (`metal.1`) — 0.4 | pendiente | — |
| EX.T.2 | Transparencia del cristal (`metal.1`) — 0.4 | pendiente | — |
| EX.T.3 | Gas 1D (`gas1d.1`) — 0.4 | pendiente | — |
| EX.T.4 | Interacciones (`interac.1`) — 0.4 | pendiente | — |
| EX.T.5 | Ley de Ohm microscópica (`drude.1`) — 0.4 | pendiente | — |
| EX.T.6 | $\tau$, $\ell$, $\mu$ (`drude.2`) — 0.4 | pendiente | — |
| EX.T.7 | Qué colisiones cuentan (`drude.3`) — 0.4 | pendiente | — |
| EX.T.8 | Resistividad y Matthiessen (`drude.3`) — 0.5 | pendiente | — |
| EX.T.9 | Calor específico (`cal.1`, `cal.2`) — 0.5 | pendiente | — |
| EX.T.10 | Fermi-Dirac (`cal.2`) — 0.4 | pendiente | — |
| EX.T.11 | Gas 3D (`fermi3d.1`) — 0.4 | pendiente | — |
| EX.T.12 | $D(\varepsilon)$ y definición de $E_F$ (`fermi3d.2`, `vib.6`) — 0.5 | pendiente | — |

### Exámenes viejos (25 ítems)

| ID | Ítem | Estado | Nota |
|---|---|---|---|
| V.P2501.1 | #1 — $n$ del Li desde $E_F$ y verificación con $\rho$ | pendiente | — |
| V.P2501.2 | #2 — Plata: $E_F$, $T_F$ y degeneración | pendiente | — |
| V.P2501.3a | #3(a) — Energía media cuántica vs. clásica | pendiente | — |
| V.P2501.3b | #3(b) — $E_F$ y $v_F$ con $n=4\times10^{28}$ m⁻³ | pendiente | — |
| V.P2501.4b | #4(b) — Significado de $T_F$ y su efecto en $C_e$ | pendiente | — |
| V.P2501.4c | #4(c) — Gas de Fermi vs. aire | pendiente | — |
| V.P2501.4f | #4(f) — Por qué e⁻-e⁻ no cambia $v_d$ | pendiente | — |
| V.P2501.4g | #4(g) — Origen de la cuantización de la energía | pendiente | — |
| V.P252S.1 | #1 — Camino libre medio del Cu con $v_F$ | pendiente | — |
| V.P252S.2 | #2 — Sol colapsado: $E_F$, $T_F$, $\langle v\rangle$ | pendiente | — |
| V.P252S.3 | #3 — Fracción excitada $T/T_F$ en Cu y Na | pendiente | — |
| V.P252S.4a | #4(a) — Gas de Fermi vs. aire | pendiente | — |
| V.P261S.11 | #11 — Definición de $E_F$ a $T=0$ | pendiente | — |
| V.T25II.1 | #1 — Ancho 90 %→10 % de $f(E)$ | pendiente | — |
| V.T25II.2 | #2 — $\rho\propto T^{3/2}$ con $v$ térmica clásica | pendiente | — |
| V.T25II.3 | #3 — Enana blanca, límite relativista y pulsar | pendiente | — |
| V.T25II.5 | #5 — Módulo de rigidez $B=\tfrac23nE_F$ y tabla | pendiente | — |
| V.T25II.6 | #6 — $v_d$ y $v_d/v_F$ en cable de Cu | pendiente | — |
| V.T25II.7 | #7 — Presión $P=\tfrac25nE_F$ | pendiente | — |
| V.T25II.8 | #8 — $C_{red}$ vs. $C_{el}$ y $T$ de cruce | pendiente | — |
| V.TSS20.2 | #2 — $E_F$ y $v_F$ del Cu | pendiente | — |
| V.TSS20.3 | #3 — He³ líquido: $E_F$ y $T_F$ | pendiente | — |
| V.TSS20.4 | #4 — $T_F$ y $T/T_F$ de Cu, Na y Ag | pendiente | — |
| V.TSS20.5 | #5 — Pérdida de potencia $=I^2R$ | pendiente | — |
| V.TSS20.6 | #6 — $\Delta E_F/E_F=-2\alpha\Delta T$ | pendiente | — |

<!-- CHECKLISTS:END -->

## Parciales y talleres (banco de examenes viejos)

| ID | Tipo | Estado | Nota | Fecha |
|---|---|---|---|---|
| P-2025-2S | Parcial (abierto, 4 preguntas, con solución manuscrita) | no intentado | — | — |
| P-2025-01 | Parcial (abierto, 4 preguntas, #4 con 7 literales) | no intentado | — | — |
| P-2026-1S | Parcial II (20 selección múltiple: 19 vibraciones de red + 1 metales) | no intentado | — | — |
| T-2025-II | Taller (abierto, 8 problemas) | no intentado | — | — |
| T-SS2020 | Taller (abierto, 6 problemas) | no intentado | — | — |

## Log de evaluaciones

*(vacío — se llenará cada vez que se use `/evaluar`)*

---

## Checklist detallado — qué debes saber, tema por tema

Orden de estudio recomendado (sigue el orden de las diapositivas). Cada subtema tiene su rango de páginas de `Metales 2021.pdf`.

### Bloque 0 — Metales y gas de e⁻ [p. 1-23]

**metal.1 — Metales, cristal metálico y $N$** [p. 1-13] · Pavlov: §6.1 p. 200
- Describir pozos $U$ + gas de e⁻ libres; e⁻ de valencia → conducción (Na 3s, ~15 % del volumen son iones).
- Calcular $N=Z_vN_A\rho/M$; monovalentes vs. divalentes.
- Éxitos (Ohm, W-F) y fracasos (calor específico, $\ell$ largo) de la teoría clásica; las dos razones de la "transparencia".

**gas1d.1 — Gas de Fermi 1D** [p. 13-19] · Pavlov: (no está en Pavlov)
- $\varepsilon_n=\hbar^2\pi^2n^2/2mL^2$ desde $\psi(0)=\psi(L)=0$; estado exacto vs. aproximado.
- Pauli: 2 e⁻ por nivel; $2n_F=N$; $\varepsilon_F$ en 1D.

**interac.1 — Interacciones** [p. 19-23] · Pavlov: §7.1 pp. 235-236
- Por qué e⁻-ion (seudopotencial, apantallamiento) y e⁻-e⁻ (Pauli, energía mínima, hueco de Fermi) son débiles.
- Gas de e⁻ vs. gas ordinario: FD vs. MB, densidad, plasma.

### Bloque 1 — Drude [p. 24-50]

**drude.1 — Ohm y Drude** [p. 24-30] · Pavlov: §7.1 pp. 235-236 (solo mención)
- $m^*\dot v=-eE-m^*v/\tau$, $v_d=-e\tau E/m^*$, $J=-Nev_d$, $\sigma=Ne^2\tau/m^*$; $v_r\gg v_d$.

**drude.2 — $\tau$, $\ell$, $\mu$** [p. 31-37] · Pavlov: §7.1 pp. 235-236 (solo mención)
- $e^{-t/\tau}$, $\ell=v\tau$, $\mu=e\tau/m^*$, $\sigma=Ne\mu$; órdenes de magnitud; $\sigma_m/\sigma_i\sim10^{23}$; Joule $=I^2R$.

**drude.3 — Origen de $\tau$** [p. 38-50] · Pavlov: §7.13 pp. 286-287
- e⁻-e⁻ conservan $J$; red perfecta no dispersa; fonones e impurezas; Matthiessen; $\rho_{ph}\propto T$ ($T\gg\theta$) y $T^5$ ($T\ll\theta$); Kondo.

### Bloque 2 — Estadística de Fermi y calor específico [p. 51-61 en alcance; cal.3 (p. 70-71, 106-109) fuera]

**cal.1 — Fracaso clásico** [p. 51-53] · Pavlov: §6.1 p. 200
- $C_e=\tfrac32R$, $C_{total}=4.5R$ vs. experimento $\approx3R$.

**cal.2 — FD y $C_e$** [p. 53-61] · Pavlov: §6.1 pp. 201-206
- $f(E)$, $f(\mu)=\tfrac12$, $\mu(0)=E_F$, cola MB; $C_e\approx2R\,T/T_F$ ($\tfrac{\pi^2}{2}R\,T/T_F$); $C=\gamma T+\beta T^3$; anchura 90→10 % $=4.4k_BT$.

**cal.3 — $U(T)$** [p. 70-71, 106-109] — ⛔ fuera de alcance (p. >70)
- Truco de sumar la identidad de $N$; integrales de e⁻ excitados y huecos.

### Bloque 3 — Gas de Fermi 3D [p. 62-70 en alcance; SF p. 72-73 fuera]

**fermi3d.1 — $k_F$, $E_F$, $v_F$** [p. 62-67] · Pavlov: §6.1 pp. 202-204
- Condiciones periódicas → $e^{i\mathbf k\cdot\mathbf r}$, $k_i=2\pi n_i/L$; derivar $k_F=(3\pi^2n)^{1/3}$; $E_F$, $T_F$, $v_F$; $\langle v\rangle=\tfrac34v_F$.

**fermi3d.2 — $D(\varepsilon)$** [p. 68-70] · Pavlov: §6.1 pp. 203-206
- $N(\varepsilon)\propto\varepsilon^{3/2}$, $D(E_F)=3N/2E_F$, $E_0=\tfrac35NE_F$, $P=\tfrac25nE_F$, $B=\tfrac23nE_F$.

**fermi3d.3 — Superficie de Fermi** [p. 72-73] — ⛔ fuera de alcance
- Esfera en $\mathbf k$/$\mathbf v$; casi independiente de $T$; propiedad característica del metal.

### Bloque 4 — Transporte [p. 74-91] — ⛔ fuera de alcance (todo p. >70)

**trans.1 — $\sigma$ cuántica** [p. 74-79]
- Esfera desplazada $\delta k=-eE\tau/\hbar$; solo e⁻ de la SF; $\sigma=Ne^2\tau_F/m^*$.

**trans.2 — W-F** [p. 80-83]
- $K=\tfrac13C_Vv_F\ell_F$, $K/\sigma=LT$, $L=\tfrac{\pi^2}{3}(k_B/e)^2$; por qué falla en aislantes.

**trans.3 — Ciclotrón** [p. 84-87]
- $\omega_c=eB/m^*$; absorción resonante; $\omega_c\tau\gg1$; medir $m^*$.

**trans.4 — Hall** [p. 88-91]
- $R_H=-1/Ne$; $R_H>0$ ⇒ huecos; qué cambia al invertir $B$.

### Bloque 5 — Termoiónica y fallas [p. 92-105] — ⛔ fuera de alcance

**term.1 — Termoiónica** [p. 92-104]
- $\phi=E_{vac}-E_F$; $J=AT^2e^{-\phi/k_BT}$, $A=120$ A/cm²K²; Schottky; gráfica de Richardson.

**falla.1 — Fallas del modelo** [p. 105]
- $\sigma\propto N$ falla, $R_H>0$, SF no esférica, sin aislantes → bandas.

### Bloque 6 — Temas de examen fuera del PDF (sin páginas) — extra.3 en alcance; extra.1-2 ⛔ fuera

**extra.1 — Bandas casi libres**
- Gaps en fronteras de zona; electrón más afectado; metal/semiconductor/aislante con paridad y solapamiento; grafito vs. diamante; alcalinos.

**extra.2 — Zener magnético**
- Condición $\hbar\omega_cE_F\gtrsim E_g^2$.

**extra.3 — Astrofísica/relativista**
- $N\approx M/m_p$; $E_F$ no relativista y relativista $\hbar c(3\pi^2n)^{1/3}$; $T_F$, $\langle v\rangle$.

### Bloque 7 — Vibraciones de red del Parcial II 2026-1S (sin páginas de este PDF) — vib.6 en alcance; vib.1-5 ⛔ fuera (son del bloque de vibraciones, `Parcial_1/`)

**vib.1 — Fase y grupo** (`P-2026-1S #1, #8`)
- $v_f=\omega/q$, $v_g=d\omega/dq$; medio dispersivo ⇔ $v_f\ne v_g$; $v_g$ periódica como $\omega(q)$; $v_g\to v_s$ a $q\to0$.

**vib.2 — Cadena monoatómica** (`#2, #3, #7`)
- Aliasing $q\equiv q+G$ ($6a$ y $6a/7$ iguales); $\lambda=2a$ ⇒ contrafase; $v_g(\pi/a)=0$ ⇒ $g(\omega)\to\infty$.

**vib.3 — Modos normales y ramas** (`#6, #9, #10`)
- Conteo de modos con condiciones de frontera (cuerda vibrante); Bragg = onda + periodicidad; $\omega_L>\omega_T$ por fuerzas restauradoras (Newton).

**vib.4 — Cadena diatómica** (`#4, #5, #12, #13, #14, #15`)
- Acústica: centro de masa se mueve; óptica: fijo. Borde: $\omega_A=\sqrt{2C/M}$, $\omega_O=\sqrt{2C/m}$, $v_g=0$ en ambas; $M\to m$ cierra el gap; masas↑ ⇒ $\omega\downarrow$; en la óptica del borde solo se mueven los átomos ligeros; gap ⇒ $q$ complejo.

**vib.5 — Umklapp y $\kappa$ de fonones** (`#16-#20`)
- N conserva $\hbar q$, U lo cambia en $\hbar G$; U requiere $|q|\gtrsim|G|/2$ y da la resistencia a $T$ alta ($\kappa\propto1/T$); $\kappa\propto T^3$ a $T\to0$ en cristal finito; ópticos aportan poco ($v_g\approx0$).

**vib.6 — $E_F$ a $T=0$** (`#11`)
- Nivel ocupado más alto; no confundir con $\mu(T)$, energía media $\tfrac35E_F$ o función trabajo.

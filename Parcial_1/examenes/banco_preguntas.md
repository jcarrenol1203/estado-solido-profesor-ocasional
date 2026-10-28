# Banco de preguntas — parciales, talleres y question sets viejos

> Extracción única de `Parciales y Talleres/Parcial1/` (regla dura: no releer
> esos archivos crudos — ver `analisis_temas.md` para el índice de fuentes y
> `CLAUDE.md` para la regla completa). Cada pregunta cita su fuente corta
> entre corchetes; el tipo (numérica / deducción / conceptual) y si hay
> solución manuscrita del usuario disponible en `Parciales y Talleres/`.
>
> Usado por `/evaluar` para mezclar preguntas reales de examen (adaptadas,
> no copiadas literalmente cuando el usuario ya las resolvió) con preguntas
> nuevas basadas en `notas/*.md`.

## crist.1 — Definición de cristal y orden atómico
- Por qué solo el cuarzo (no el vidrio) se clasifica como sólido cristalino en sentido estricto, pese a que ambos están hechos de tetraedros SiO₄. **[QS1 #1]** — conceptual.

## crist.2 — Red cristalina como abstracción geométrica
- Crítica al error conceptual de tratar un sólido como "cuerpo rígido continuo": qué fenómenos (ramas ópticas, difracción de Bragg, bandas electrónicas) no tienen análogo en el continuo. **[QS1 #2]** — conceptual.

## crist.3 — Redes de Bravais vs. no-Bravais
- El grafeno como contraejemplo de "todo arreglo periódico de átomos idénticos es Bravais": por qué es una red triangular con base de 2 átomos. **[QS1 #3]** — conceptual. *(ya incorporado como contenido en `notas/00_cristalografia_basica.md`)*

## crist.5 — Celda unitaria, primitiva y Wigner-Seitz
- Relación entre el área de una celda primitiva paralelogramo y la celda de Wigner-Seitz de la misma red (misma área, forma distinta). **[QS1 #4]** — conceptual.
- Por qué una celda convencional no-primitiva no "contiene más información física" que una primitiva, solo más puntos de red. **[QS1 #5]** — conceptual.

## crist.7 — Monocristal vs. policristal
- Justificación física de por qué un monocristal real de Na (~1 cm³) se trata como "cuasi-perfecto" a T baja (superficie/volumen, impurezas, amplitud de vibración). **[QS1 #6]** — conceptual.
- Por qué un monocristal da manchas de Bragg agudas y un polvo da anillos de Debye-Scherrer continuos (mosaicidad, orientación de cristalitos). **[QS1 #7]** — conceptual.

## crist.8 — Red recíproca
- Por qué la red recíproca es más útil que trabajar directamente con la red directa (Fourier de la densidad periódica, picos delta en G). **[QS1 #8]** — conceptual.
- Error de usar la convención cristalográfica `aᵢ·bⱼ=δᵢⱼ` en vez de la convención de física `aᵢ·bⱼ=2πδᵢⱼ`, y su consecuencia física (invariancia de fase de Bloch bajo k→k+G). **[QS1 #9]** — conceptual.

## crist.9 — Primera zona de Brillouin
- Por qué la "segunda zona de Brillouin" NO es un cubo concéntrico más grande, sino una región de igual volumen hecha de piezas disjuntas fuera de la 1ª ZB. **[QS1 #10]** — conceptual.

## enlace.1 — Origen de las fuerzas interatómicas
- Por qué enlace iónico y covalente no son "el mismo fenómeno con distinto grado de transferencia de carga": el covalente requiere reducción de energía cinética cuántica (deslocalización), sin análogo electrostático clásico. **[QS2 #1]** — conceptual.

## enlace.5 — Enlace metálico
- *(ver enlace.9 más abajo — extensión cuantitativa del enlace metálico)*

## enlace.8 — Energía de cohesión y constante de Madelung
- Por qué la suma de Madelung en 3D es condicionalmente convergente y requiere agrupar por cascarones neutros (método de Evjen), a diferencia de la suma 1D. **[QS2 #2]** — conceptual.
- A partir de `|U_coh|≈7.9 eV` y `k_BT≈0.026 eV` a 300K, qué explica correctamente el alto punto de fusión y baja presión de vapor de los cristales iónicos. **[QS2 #3]** — conceptual/numérica.
- Por qué se necesita un término repulsivo `A/r^b` y no basta un modelo de "esferas duras que se tocan" (origen cuántico: Pauli + solapamiento de nubes electrónicas, curvatura de U en r₀ ligada al módulo de compresibilidad). **[QS2 #4]** — conceptual.
- Por qué el NaCl es estable pese a que la fase "colapsada" (tipo plasma denso) tendría menor energía electrostática — niveles de energía cuantizados. **[Parcial 2026-1S #12]** — conceptual.
- Por qué Madelung y Born pudieron calcular la constante de fuerza usando solo primeros vecinos. **[Parcial 2026-1S #17]** — conceptual.

## enlace.9 — Modelo de jellium (ion en mar de electrones)
- Ion puntual de masa M y carga e en un mar de electrones de conducción (densidad n definiendo un radio R por neutralidad de carga): (a) derivar ω=(e²/(πε₀MR³))^(1/2) vía ley de Gauss aplicada a la esfera de carga desplazada; (b) estimar el valor de ω; (c) estimar el orden de magnitud de la velocidad del sonido en el metal. **[Taller SS2020 #4 / imagen Parcial 2025-01(2)]** — deducción + numérica. *(solución manuscrita disponible en "Talleres Parcial 1 - Mi Solucion.pdf")*. Contenido ya incorporado en `notas/00b_enlaces_fuerzas_interatomicas.md`.

## ondas.2 — Ecuación de onda elástica (medio continuo 1D)
- Por qué `ω=v_sq` (lineal, no dispersivo) falla cuando λ se acerca al espaciamiento interatómico: el medio deja de comportarse como continuo. **[QS2 #5]** — conceptual.
- Estimar `ω_max~v_s/a` dados v_s y a, e identificar la región espectral (rango THz/infrarrojo lejano, mismo orden que ω_D). **[QS2 #9]** — numérica.
- Por qué medir ondas elásticas a frecuencias audibles no distingue enlace iónico de covalente al nivel cualitativo, pero sí lo hace a nivel cuantitativo (Y, ρ) y vía la rama óptica (ausente en el continuo). **[QS2 #10]** — conceptual. *(cruza con diatom.1)*

## ondas.3 — Densidad de estados g(ω) en 1D (continuo)
- Por qué condiciones de frontera periódicas y de extremos fijos dan la misma `g(ω)` en el límite termodinámico L→∞, aunque cuantizan q de forma distinta (`π/L` vs `2π/L`). **[QS2 #6]** — conceptual.

## ondas.4 — Densidad de estados g(ω) en 3D (continuo)
- Generalización de `g(ω)` cuando `v_L≠v_T` (factor `1/v_L³+2/v_T³`) y qué polarización domina el calor específico a T baja (la transversal, por tener v menor). **[QS2 #7]** — conceptual. *(cruza con calor.5, velocidad promedio de Debye)*
- Papel del factor de volumen V en `g(ω)=Vω²/(2π²v_s³)`: por qué es un artefacto de normalización que se cancela en cantidades intensivas (c_V=C_V/V). **[QS2 #8]** — conceptual.

## monoat.1 — Cadena monoatómica discreta (dispersión, v_g, 1ª ZB)
- Cadena monoatómica: `ω²=(4α/M)sen²(qa/2)`; hallar los valores de q para los que la onda NO se propaga. **[Taller 2025-II #3 / Taller 01-2025 #1]** — deducción. *(solución manuscrita disponible)*
- Por qué la dispersión no es simplemente `ω=v_sq` como en el continuo: la discreteness de la red dispersa la onda para λ~a. **[QS4 #6]** — conceptual.
- En el borde de zona `q=π/a`: interpretación física de la onda estacionaria (`v_g=0`), análoga a la condición de Bragg a incidencia normal. **[QS4 #7]** — conceptual.
- Estimación numérica `ω_m~10¹³s⁻¹` con `α~10³dyn/cm`, `M~10⁻²⁴g`, y por qué esta frecuencia es del mismo orden para casi cualquier sólido (rango estrecho de Y/ρ y 1/a). **[QS4 #8]** — numérica/conceptual.
- Crítica a "si v_g=0 en el borde de zona, la energía elástica del modo desaparece": confusión entre almacenamiento y transporte de energía (la energía ℏω(n̄+1/2) sigue ahí, solo el flujo neto es cero). **[QS4 #9]** — conceptual.
- Por qué se restringe q a la primera zona de Brillouin en vez de usar toda la recta real: dos q que difieren en `2π/a` producen el mismo patrón de desplazamientos atómicos. **[QS4 #10]** — conceptual.
- Por qué la constante de fuerza atómica necesita una relación funcional (resolver la ecuación diferencial de movimiento), análogo a por qué el índice de refracción no es un número arbitrario. **[Parcial 2026-1S #9]** — conceptual.
- Diferencia de fase para un período espacial de una longitud de onda. **[Parcial 2026-1S #10]** — conceptual.
- Cómo estimar la velocidad del sonido a partir de `ω(q)`: pendiente/derivada en la región de q pequeño. **[Parcial 2026-1S #18]** — conceptual.

## monoat.2 — Cadena monoatómica con acoplamiento a segundos vecinos
- Cadena de N átomos, `ω²=(2α/M)[A(1-cos ka)+B(1-cos 2ka)]`: hallar (a) velocidad de grupo, (b) longitudes de onda de ondas estacionarias, (c) velocidad del sonido, (d) densidad de modos, la de Debye y el vector de onda de Debye k_D. **[Parcial SS2020 #2 / imagen Parcial 2025-01]** — deducción larga, 4 subpartes. *(solución manuscrita disponible)*. Contenido ya incorporado en `notas/01b_cadena_monoatomica_discreta.md`.

## diatom.1 — Cadena diatómica
- Cadena diatómica con `C=5×10³dyn/cm`, `M₁=5.9×10⁻²³g`, `M₂=3.8×10⁻²³g` (Parcial SS2020 #3) o `M₂=3.9×10⁻²³g` (Taller 2025-II #2, que además trae la errata `α=5×10¹³` por `5×10³` dyn/cm): calcular las frecuencias en el límite de la 1ª ZB. **[Parcial SS2020 #3 / Taller 2025-II #2]** — numérica. *(solución manuscrita disponible)*
- Por qué la ecuación secular 2×2 (2 átomos/celda) da dos ramas ω±(q), no una. **[QS5 #1]** — conceptual.
- En el borde de zona, cuál sublattice vibra en cada rama (amplitud del átomo ligero se anula en ω₋, del pesado en ω₊). **[QS5 #2]** — conceptual.
- Por qué la masa efectiva de la rama acústica a q→0 es `M₁+M₂` (cuerpo rígido) y no la masa reducida. **[QS5 #3]** — conceptual.
- Por qué la razón de amplitudes óptica `A₂/A₁=-M₁/M₂` (centro de masa fijo, sin traslación neta de la celda). **[QS5 #4]** — conceptual.
- Por qué solo la rama óptica (no la acústica) absorbe en el infrarrojo en un cristal iónico: momento dipolar oscilante por sublattices cargadas fuera de fase. **[QS5 #5]** — conceptual.
- Interpretación física de la brecha prohibida: modos evanescentes (q complejo), no ondas armónicas estacionarias del espectro. **[QS5 #6]** — conceptual.
- Qué pasa con la brecha cuando `M₁→M₂`: se cierra y las dos ramas se funden en la dispersión de la cadena monoatómica (celda efectiva se reduce a la mitad). **[QS5 #7]** — conceptual.
- Por qué no se duplica el conteo de modos al extender q más allá de la 1ª ZB diatómica (`q` y `q+G` son el mismo modo físico). **[QS5 #8]** — conceptual.

## calor.1 — Ley de Dulong-Petit
*(sin preguntas de examen específicas — ver calor.2 para la justificación clásica)*

## calor.2 — Teoría clásica (equipartición)
- Por qué se usa estadística de Maxwell-Boltzmann (no Bose-Einstein) para los 3N osciladores clásicos, pese a ser objetos cuánticos en el tratamiento moderno. **[QS3 #1]** — conceptual.
- Rol exacto del teorema de equipartición al llegar a `3R`, y por qué la predicción falla a T baja (niveles discretos no accesibles con cuantos ~k_BT). **[QS3 #2]** — conceptual.

## calor.3 — Modelo de Einstein
- Por qué `ε̄→k_BT` (no `½k_BT`) en el límite de alta T del modelo de Einstein: un oscilador 1D tiene 2 grados cuadráticos (cinético+potencial). **[QS3 #3]** — conceptual.
- Por qué Einstein predice caída exponencial de C_V a T baja en vez del `T³` experimental: una sola frecuencia ω_E, sin modos colectivos de baja frecuencia. **[QS3 #4]** — conceptual.
- Evaluar `C_V` en `T=Θ_E` (Cu, Θ_E=240K): resulta `≈0.92×3R`, no `3R` exacto ni `0`. **[QS3 #5]** — numérica.
- Por qué el modelo de Einstein NO incluye la energía de punto cero `½ℏω` en su tratamiento estándar (ver calor.9 para el punto cero en Debye). **[Parcial 2026-1S #2]** — conceptual.
- Por qué es válido usar Maxwell-Boltzmann en Einstein pese a que el átomo es un objeto cuántico (distinguibilidad por sitio de red, sin exclusión de Pauli). **[Parcial 2026-1S #13]** — conceptual.
- Por qué Einstein falla a T baja: los modos de baja frecuencia pueden absorber energía y el modelo los ignora. **[Parcial 2026-1S #14]** — conceptual.

## calor.4 — Modelo de Debye
- V/F razonado: a T=80K, ¿un sólido con Θ_D=100K tiene mayor C que uno con Θ_D=200K? ¿la λ mínima de fonones es menor cuanto mayor es la constante de red? ¿hay tantos tipos de fonones como átomos? ¿se pueden escuchar las vibraciones térmicas? **[Parcial SS2020 #4.1]** — conceptual (4 subpartes). *(solución manuscrita disponible)*
- Qué fonones contribuyen más a la energía total a T dada; contraste modos colectivos (Debye) vs. osciladores independientes (Einstein); ¿hay ondas de sonido en moléculas pequeñas? ¿cómo se explica el sonido en gases? **[Parcial SS2020 #4.2]** — conceptual (3 subpartes). *(solución manuscrita disponible)*
- Estimar la energía térmica clásica de 1 mol de Cu a T=Θ_D (Θ_D=340K); calcular la energía real de Debye y comparar (aproximando la curva de Debye por una recta desde el origen hasta T=Θ_D); orden de magnitud del desplazamiento máximo de un átomo de Cu a Θ_D vs. distancia interatómica. **[Taller 01-2025 #4 / Taller 2025-II #7]** — numérica + deducción, 3 subpartes. *(solución manuscrita disponible)*
- Motivación física de `∫₀^ωD g(ω)dω=3N` (contar grados de libertad, no solo ajustar Dulong-Petit por construcción). **[QS3 #6]** — conceptual.
- Por qué `ω_D` SÍ depende de la masa atómica M (vía `v_s=√(Y/ρ)`, `ρ=nM`): `ω_D∝M^(-1/2)`. **[QS3 #7]** — conceptual.
- Argumento cualitativo de la "esfera térmica" para derivar `C_V∝T³` (número de modos excitados `∝T³`, cada uno aporta `~k_BT`). **[QS3 #8]** — conceptual. *(ver calor.8 para la generalización a D dimensiones)*
- Por qué `g(ω)∝ω²` en Debye (medio continuo isotrópico). **[Parcial 2026-1S #4]** — conceptual.
- Por qué Debye funciona mejor que Einstein a T baja. **[Parcial 2026-1S #5]** — conceptual.
- Diferencia de Θ_D entre plomo y carbono (diamante): masa y rigidez. **[Parcial 2026-1S #8]** — conceptual.
- Numérica: `ω_D` de Debye para una red SC con `a=3Å`, `v_s=4.2×10⁵cm/s`. **[Parcial 2026-1S #11]** — numérica (única del examen 2026-1S).
- Comparación cualitativa de `C_V` entre dos sólidos con distinto Θ_D a la misma T. **[Parcial 2026-1S #16]** — conceptual.

## calor.5 — Limitaciones del modelo de Debye
- Con `v_ℓ=6000m/s`, `v_T=3000m/s`: la velocidad promedio de Debye está dominada por la más lenta (`v̄` mucho más cerca de `v_T` que la media aritmética), y `Θ_D` resulta más bajo que si solo se usara `v_ℓ`. **[QS3 #9]** — numérica/conceptual.
- Por qué `Θ_D` extraído de datos experimentales varía ~10% con T: la dispersión real se desvía de `ω=v_sq` cerca del borde de zona. **[QS3 #10]** — conceptual.

## calor.6 — El fonón
- Qué fonones (frecuencia) contribuyen más a la energía a una T dada (los de `λ→2a`, cerca del borde de zona, donde `g(ω)` es mayor; respuesta c del examen). **[Parcial 2026-1S #6]** — conceptual. *(Corregido: antes decía `λ→a`.)*
- Diferencia física entre fonón y fotón: la velocidad del fonón depende de λ (dispersión no trivial), el fotón en el vacío no. **[Parcial 2026-1S #15]** — conceptual.

## calor.7 — Estadística de fonones
- Por qué NO se necesita un potencial químico `μ≠0` para el gas de fonones: su número no se conserva (se crean/destruyen libremente), `∂F/∂N=0 ⟹ μ=0`. **[QS4 #2]** — conceptual.
- Por qué `ε̄→k_BT` a T alta es la misma física que la equipartición clásica: el espaciamiento discreto `ℏω` se vuelve despreciable frente a `k_BT`. **[QS4 #3]** — conceptual.
- Por qué el número de ocupación por modo puede ser muy pequeño o muy grande (`n̄→0` a T baja, `n̄≈k_BT/ℏω→∞` a T alta). **[Parcial 2026-1S #7]** — conceptual.
- Justificación de la estadística de Bose-Einstein para el gas de fonones (indistinguibles, sin Pauli). **[Parcial 2026-1S #3]** — conceptual.

## calor.8 — Modelo de Debye en dimensión general D
- Usando Debye, calcular `C_V` de una red monoatómica 1D a T bajas comparado con `Θ_D=v/(k_Ba)`. **[Taller SS2020 #1]** — numérica/deducción.
- Red cuadrada 2D (constante K, `ω(q)=(4K/m)^(1/2)sen(qa/2)`): obtener `g(ω)=dN/dω`; a T alta hallar el desplazamiento cuadrático medio y comentar la estabilidad de cristales 2D. **[Taller SS2020 #6]** — deducción.
- Dependencia de `C_V` con T para un cristal 2D a T bajas (`∝T²`). **[Taller 2025-II #5 / Taller SS2020 #5, mismo enunciado]** — deducción.
- Contenido ya incorporado en `notas/03_densidad_estados_calor_especifico.md` (sección 8).

## calor.9 — Energía de punto cero en Debye
- Estimar el desplazamiento cuadrático medio de átomos de Li metálico en T→0 por energía de punto cero, con `Θ_D(Li)=344K` y `⟨u²⟩=(9ℏ/Mω_D³)∫₀^ωD(n̄+1/2)ω dω`. **[Taller 01-2025 #2 / Taller SS2020 #7 / Taller 2025-II #4]** — numérica + deducción. *(solución manuscrita disponible)*
- Energía de punto cero de un cristal vía Debye; estimarla para helio sólido con `Θ_D≈24K`. **[Taller 01-2025 #3]** — numérica + deducción. *(solución manuscrita disponible)*
- Contenido ya incorporado en `notas/03_densidad_estados_calor_especifico.md` (sección 9).

## calor.10 — Dispersión inelástica de fotones/neutrones por fonones
- Dispersión de un fotón (`n=1.5`, `v_s=4×10⁵cm/s`) con `λ_incidente=3.14Å`, `λ_dispersada=5Å`: hallar la frecuencia del fonón involucrado. **[Taller SS2020 #5]** — numérica. *(solución manuscrita disponible)*
- Dispersión de neutrones por un fonón (`λ_i=3.14Å`, `λ_f=5Å`, ángulo 45° entre `q'` y `q`): hallar `λ` (o `ω`) del fonón, usando conservación de energía/momento y ley de cosenos (resultado: `λ_fonón≈4.41Å`, `Ω≈7.6×10¹² rad/s`). **[Taller 2025-II #6]** — numérica. *(Corregido: el enunciado anterior mezclaba los datos del fotón de Taller SS2020 #5; ver `guia_teoria_por_examen.md` §3.5.)*
- Contenido ya incorporado en `notas/03_densidad_estados_calor_especifico.md` (sección 10).

## calor.11 — Momento total real vs. momento cristalino ℏq
- Momento lineal total de un cristal monoatómico 1D de N átomos con 1 fonón de vector de onda q excitado (resultado: es cero, no ℏq). **[Taller 2025-II #1 / Taller SS2020 #8 / Parcial SS2020, último ítem]** — deducción/conceptual. *(solución manuscrita disponible)*
- Por qué `ℏq` no obedece la 3ª ley de Newton como un momento mecánico real: es momento cristalino, conservado solo módulo `ℏG` (relevante en procesos Umklapp). **[QS4 #1]** — conceptual.
- Contenido ya incorporado en `notas/03_densidad_estados_calor_especifico.md` (sección 11).

## extra.1 — Anarmonicidad y expansión térmica
- Por qué un potencial armónico puro (parabólico, simétrico) da expansión térmica exactamente nula, aunque la amplitud de vibración crezca con T (⟨x⟩=0 a toda T). **[QS4 #4]** — conceptual.
- Por qué el término cúbico `-bx³` (no el cuártico) es el responsable de romper la simetría y dar `⟨x⟩=3bk_BT/β²∝T`. **[QS4 #5]** — conceptual.

## extra.2 — Conductividad térmica de fonones
- A `T>Θ_D`, derivar `K∝1/T` a partir del número aproximado de fonones excitados a T alta. **[Parcial SS2020 #1]** — deducción. *(solución manuscrita disponible)*
- Por qué la ecuación de conducción de calor es de difusión (no de onda) aunque los fonones viajen a `v_s`: el camino libre medio finito ℓ aleatoriza la dirección de propagación. **[QS6 #1]** — conceptual.
- Validez de `ΔV=0 ⟹ ΔU=C_VΔT` en un sólido típico (coeficientes de expansión térmica muy pequeños). **[QS6 #2]** — conceptual.
- Peculiaridad del "gas de fonones" al aplicar `K=⅓C_Vvℓ` en un rango amplio de T: el número de fonones no se conserva, `C_V(T)` ya absorbe esa dependencia. **[QS6 #3]** — conceptual.
- Para SiO₂: `ℓ` cambia 4 órdenes de magnitud entre 273K y 20K pero K cae solo modestamente — explicar por la caída simultánea de `C_V∝T³`. **[QS6 #4]** — numérica/conceptual.

## extra.3 — Mecanismos de dispersión de fonones (Umklapp)
- Ranking de dominancia de los 3 mecanismos de dispersión (fonón-fonón, impureza, frontera) con T, y la forma funcional de ℓ(T) en cada régimen. **[QS6 #5]** — conceptual.
- Por qué la dispersión por impurezas es inefectiva a T bajo (`λ≫D_imp`, régimen tipo Rayleigh). **[QS6 #6]** — conceptual.
- Dos barras de LiF de distinto diámetro: por qué `K(T)` coincide a T alta pero diverge a T baja (`ℓ` satura en el diámetro de la muestra). **[QS6 #7]** — conceptual.
- Por qué solo los procesos Umklapp (no los normales) contribuyen a la resistividad térmica (los normales conservan el momento cristalino total del gas de fonones que transporta calor). **[QS6 #8]** — conceptual.
- Por qué los procesos Umklapp se suprimen exponencialmente a T baja, dando `ℓ∝exp(Θ_D/2T)`. **[QS6 #9]** — conceptual.

## extra.4 — Aplicaciones de ondas acústicas
- Por qué los haces de fonones coherentes generados piezoeléctricamente (eficiencia ~10⁻⁴) se prefieren sobre los fonones térmicos para estudiar dispersión en sólidos (control de dirección, polarización y frecuencia). **[QS6 #10]** — conceptual.
- Mecanismo del efecto acustoeléctrico: por qué la amplificación ocurre cuando `v_drift>v_s` (electrones deslizándose por los mínimos de un potencial piezoeléctrico viajero). **[QS6 #11]** — conceptual.

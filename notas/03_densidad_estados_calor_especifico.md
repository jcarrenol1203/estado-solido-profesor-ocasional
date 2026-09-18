# Teoría del calor específico: Dulong-Petit, Einstein y Debye

## 1. Ley de Dulong-Petit (resultado experimental clásico)

Definición de capacidad calorífica molar a volumen constante:

`C_molar = ΔQ/ΔT`; en proceso a V=cte., `ΔQ = ΔE`, por lo tanto:

`C_V = (∂E/∂T)_V`  [p. 67]

**Observación experimental**: para casi todas las sustancias sólidas, a temperatura suficientemente alta, `C_V ≈ 6 cal/(K·mol) = 3R` (con `R ≈ 2 cal/(K·mol)`). A bajas T, `C_V` decae aproximadamente como `T³`. Esta constancia a alta T es la **ley de Dulong-Petit** [p. 67].

Conversión de unidades: `R = 8.314 J/mol ⟹ C_V = 3R = 24.9 J/(mol·K) = 2.5×10⁻⁴ eV/(K·molécula)` [p. 67].

### Puntos clave para dominar este tema
- Sabe enunciar la ley de Dulong-Petit: C_V → 3R ≈ 6 cal/(K·mol) a alta temperatura, para prácticamente cualquier sólido cristalino.
- Conoce el comportamiento cualitativo completo: C_V ~ T³ a T baja, saturando en 3R a T alta.
- Puede convertir C_V=3R entre distintas unidades (cal/K·mol, J/mol·K, eV/K·molécula).

## 2. Teoría clásica (equipartición) del calor específico

Modelo simple: la red se representa como átomos unidos por resortes (osciladores). Al aumentar T, aumenta la energía interna E_interna, que tiene componentes cinética (E_k) y potencial (E_p) del movimiento vibracional de átomos/iones [p. 68].

Se modela el sólido como `N` osciladores 3D independientes, cada uno con frecuencia:

`ω = √(α/m)`

donde α es la constante de fuerza interatómica [p. 68].

`N osciladores 3D independientes ≡ 3N osciladores 1D desacoplados` [p. 69]

### Distribución de Maxwell-Boltzmann y energía media por oscilador (clásico)

Se define:
- `f(ε)` ≡ número promedio de partículas ocupando un estado cuántico individual de energía ε.
- `g(ε)dε` ≡ número de estados cuánticos en el intervalo dε alrededor de ε.
- `N(ε)dε ≡` número de partículas en dε `= f(ε)·g(ε)·dε`  [p. 69]

Para un sistema de osciladores 1D con niveles de energía muy próximos (no degenerados, con separación ΔE tal que `dε >> ℏω`), se puede tratar la energía como continua:

`g(ε)dε ≡ dε/ℏω`  [p. 70]

La energía media por partícula (usando la distribución de Maxwell-Boltzmann clásica `f(ε)_MB = e^α·e^(-ε/k_BT)`):

`E/N = ∫ε·N(ε)dε / ∫N(ε)dε = ∫ε·e^(-ε/k_BT)dε / ∫e^(-ε/k_BT)dε = k_BT`  [p. 70]

### Resultado clásico: energía y calor específico

`E = N·k_BT`; y usando `N_3D ≡ 3N_1D`:

`E = 3N·k_BT`  [p. 71]

`C_V = (∂E/∂T)_V = 3N·k_B`

Numéricamente: `= 2.58×10⁻⁴ eV/(K·molécula)` [p. 71]

Para una mol (N=N_A, número de Avogadro):

`C_V = 3N_A·k_B = 3R ≈ 6 cal/(K·mol)`  [p. 71]

Esto reproduce exactamente la ley de Dulong-Petit, con la interpretación de **equipartición**:

`E/N = E̅_k/N + E̅_p/N = (1/2)k_BT + (1/2)k_BT = k_BT`  [p. 71]

(cada oscilador 1D contribuye 1/2 k_BT de energía cinética y 1/2 k_BT de energía potencial, en promedio, por el teorema de equipartición).

### Puntos clave para dominar este tema
- Puede justificar la ley de Dulong-Petit desde la mecánica estadística clásica: modelar el sólido como 3N osciladores armónicos 1D independientes en equilibrio térmico con distribución de Maxwell-Boltzmann.
- Sabe derivar que la energía media por oscilador 1D clásico es E/N=k_BT, y explicarlo vía equipartición (1/2 k_BT cinética + 1/2 k_BT potencial).
- Puede derivar E=3Nk_BT y C_V=3Nk_B=3R a partir de tratar cada átomo como 3 osciladores 1D independientes.
- Entiende que este resultado clásico predice C_V constante (=3R) a TODA temperatura, lo cual contradice el comportamiento experimental a bajas T (falla del modelo clásico).

## 3. Modelo de Einstein

### Cuantización de la energía del oscilador aislado

Cada átomo se trata como un oscilador (o 3 osciladores 1D desacoplados). Cuánticamente, un oscilador armónico aislado tiene niveles de energía:

`ε_n = (n + 1/2)ℏω`,  n = 0, 1, 2, ...  [p. 72]

### Por qué el modelo clásico falla a T baja

Cuando `T→0`, `k_BT` se vuelve pequeño, eventualmente `k_BT << ℏω`. En este régimen, los valores discretos permitidos de energía son importantes: NO existen muchos valores permitidos de energía en un intervalo dε (al contrario de lo asumido clásicamente). La energía suministrada en cantidades ~k_BT no logra excitar al oscilador a estados más altos [p. 73].

Por esto, se debe reemplazar el modelo de energía continua `g(ε)dε` por un conjunto de **niveles discretos** con separación ΔE grande y factor de degeneración `g_n`. Para un oscilador 1D, `g_n = 1` (degeneración simple) [p. 73].

### Cálculo de la energía media del oscilador cuántico en equilibrio térmico

El sólido se modela como osciladores en contacto con un baño térmico (no aislados), con energía `ε_n = nℏω` (tomando el cero de energía en el estado base, ignorando el término de punto cero ℏω/2) [p. 74].

La energía media en equilibrio térmico:

`ε̄ = [Σ_(n=0)^∞ ε_n·e^(-ε_n/k_BT)] / [Σ_(n=0)^∞ e^(-ε_n/k_BT)]`  [p. 74]

Esto se puede reescribir usando el truco de la derivada logarítmica:

`ε̄ = -∂/∂(1/k_BT) · ln[Σ_(n=0)^∞ e^(-ε_n/k_BT)]`  [p. 75]

Sustituyendo `ε_n = nℏω` y realizando la suma geométrica, se obtiene el resultado central:

`ε̄ = ℏω / (e^(ℏω/k_BT) - 1)`  [p. 75]

### Límites de la energía media

- **T alta** (`k_BT >> ℏω`): usando `e^(ℏω/k_BT) ≈ 1 + ℏω/k_BT + ...`, se obtiene `ε̄ → k_BT`. Es decir, **el modelo cuántico reproduce el resultado clásico** [p. 75].
- **T baja** (`k_BT << ℏω`): `ε̄ → 0` (el oscilador se "congela" en su estado fundamental) — esto refleja la **naturaleza cuántica del movimiento** [p. 76].

Diagrama cualitativo: ε̄ vs T muestra una recta (comportamiento clásico) que se dobla hacia cero a bajas T (comportamiento cuántico), con el "codo" ubicado aproximadamente en `T ~ ℏω/k_B` [p. 75].

### Justificación de por qué la estadística de Maxwell-Boltzmann es aplicable aquí
Dos condiciones del problema permiten aplicar M-B [p. 77]:
a. Los niveles del oscilador NO están restringidos por el principio de exclusión de Pauli.
b. Cada átomo vibrante está localizado en un sitio de red específico y distinguible (no son partículas idénticas indistinguibles en el sentido cuántico de bosones/fermiones libres).

### Energía total y calor específico del sólido de Einstein

Cada átomo ≡ 3 osciladores armónicos ⟹ existen `3N_A` osciladores (para una mol). La energía total:

`E = 3N_A · ℏω_E / (e^(ℏω_E/k_BT) - 1)`  [p. 78]

donde `ω_E` es la **frecuencia de Einstein** ≡ la frecuencia común (única) asumida para todos los osciladores.

Derivando respecto a T:

`C_V = 3R·(ℏω_E/k_BT)² · e^(ℏω_E/k_BT) / (e^(ℏω_E/k_BT) - 1)²`  [p. 78]

### Temperatura de Einstein θ_E

Se define el parámetro de ajuste `θ_E` mediante `k_B·θ_E = ℏω_E` [p. 79]:

`C_V = 3R·(θ_E/T)² · e^(θ_E/T) / (e^(θ_E/T) - 1)²`  [p. 79]

Cuando `T→0`, `C_V→0`. Este modelo ajusta razonablemente bien datos experimentales (ej. Cu: `θ_E = 240 K ⟹ ω_E ≈ 2.5×10¹³ s⁻¹`) [p. 79].

### Límites extremos de C_V (modelo de Einstein)

**(1) T alta** (`T >> θ_E`): el oscilador está en un estado cuántico altamente excitado. Usando `e^(θ_E/T) ≈ 1+θ_E/T+...`:

`C_V → 3R`  (recupera Dulong-Petit) [p. 80]

**(2) T baja** (`T << θ_E`): `e^(θ_E/T) >> 1`, entonces:

`C_V ≈ 3R·(θ_E/T)²·e^(-θ_E/T) = B(T)·e^(-θ_E/T)  ⟹  C_V → 0` (exponencialmente) [p. 80]

### Fallo del modelo de Einstein a baja T
**Experimentalmente**, `C_V → 0` cuando `T→0` siguiendo una ley `~T³` (potencia), **no** una caída exponencial. El modelo de Einstein predice decaimiento exponencial, lo cual **no coincide** con el experimento a T baja [p. 81].

Nota adicional: a `T=θ_E` (es decir, `θ_E/T=1`), `C_V=0.925·(3R)`, por lo que se dice que para `T≥θ_E` el modelo clásico es una buena aproximación, mientras que para `T<θ_E` los efectos cuánticos son relevantes. En general, `θ_E ~ 200 K` para la mayoría de sustancias cristalinas [p. 81].

**Razón física del fallo**: el modelo de Einstein asume que TODOS los osciladores tienen la MISMA frecuencia ω_E. Pero en realidad existen modos con ω muy pequeña (ω<<) que SÍ pueden absorber calor incluso a T muy baja (donde `ℏω<<k_BT` para esos modos específicos), contribuyendo con energía de cuantización adicional. Al ignorar estos modos de baja frecuencia, el modelo de Einstein predice un "congelamiento" (C_V muy pequeño) más abrupto del que se observa experimentalmente [p. 96].

### Puntos clave para dominar este tema
- Puede escribir de memoria ε̄ = ℏω/(e^(ℏω/k_BT)-1) y explicar su derivación a partir de la suma sobre estados discretos ε_n=nℏω con pesos de Boltzmann.
- Sabe demostrar los dos límites: T alta → ε̄→k_BT (clásico); T baja → ε̄→0 (congelamiento cuántico).
- Puede derivar C_V=3R(θ_E/T)²·e^(θ_E/T)/(e^(θ_E/T)-1)² a partir de E=3N_Aℏω_E/(e^(ℏω_E/k_BT)-1), con k_Bθ_E=ℏω_E.
- Sabe demostrar los límites de C_V: →3R a T>>θ_E (Dulong-Petit), →0 exponencialmente (~e^(-θ_E/T)) a T<<θ_E.
- Puede explicar POR QUÉ el modelo de Einstein falla cualitativamente a T baja: predice decaimiento exponencial de C_V, pero el experimento muestra C_V~T³; la causa es la suposición (incorrecta) de que todos los átomos vibran con una única frecuencia común ω_E, ignorando los modos colectivos de baja frecuencia que sí se excitan fácilmente a T baja.
- Sabe justificar por qué es válido usar estadística de Maxwell-Boltzmann para los osciladores de red: no hay restricción de Pauli, y los átomos son distinguibles por su sitio de red.

## 4. Modelo de Debye

### Motivación: modos colectivos de vibración

El modelo de Einstein trata a los átomos como osciladores INDEPENDIENTES, pero los átomos en realidad **interactúan** entre sí (mediante fuerzas tipo resorte, F~-x). Como resultado, **la red se mueve como un todo**, dando lugar a **modos colectivos de vibración** [p. 82].

El ejemplo prototípico de modo colectivo es el sonido: los átomos se mueven con amplitudes y relaciones de fase fijas entre sí. Debye postula que **todos los modos de vibración de la red tienen un carácter similar al de las ondas de sonido**:

`ω = v_s·q`  [p. 83]

**Diferencia clave con Einstein**: en el modelo de Debye existe todo un **espectro** de frecuencias ω (con ω=0 en q=0), mientras que en el modelo de Einstein hay una única frecuencia ω_E para todos los osciladores [p. 83].

### Cálculo de la energía total (integrando sobre el espectro de modos)

Cada modo se trata como un oscilador armónico simple con energía media:

`ε̄(ω) = ℏω/(e^(ℏω/k_BT)-1)`  (igual fórmula que en Einstein, pero ahora aplicada modo por modo)

y densidad de estados (medio continuo isotrópico, 3D, incluyendo 3 polarizaciones):

`g(ω) = 3V/(2π)² · ω²/v_s³`  [p. 84]

*(Nota: esta es la misma expresión de la sección de "Ondas elásticas", escrita aquí con la constante 3V/(2π)² en vez de 3V/(2π²); ambas notaciones aparecen en las diapositivas y son equivalentes tras simplificar: g(ω)=3Vω²/(2π²v_s³).)*

La energía interna vibracional total de la red es la integral sobre todos los modos normales:

`dE = ε̄(ω)·g(ω)·dω`

`E = ∫ ε̄(ω)·g(ω)·dω`  [p. 84]

Físicamente: la red vibrante ≡ un conjunto de modos colectivos que vibran independientemente entre sí (como osciladores normales desacoplados) [p. 85].

Sustituyendo g(ω) y ε̄(ω):

`E = [3V/(2π²v_s³)] · ∫ ω² · ℏω/(e^(ℏω/k_BT)-1) dω`  [p. 85]

### Límites del espectro: frecuencia de corte de Debye ω_D

El límite inferior del espectro es `ω=0`. El límite superior es la **frecuencia de corte de Debye**, `ω_D` [p. 86].

El criterio para fijar ω_D es que el número TOTAL de modos normales debe ser igual al número de grados de libertad del sólido, `3N`:

`∫_0^(ω_D) g(ω)dω = 3N`  [p. 86]

### Cálculo de ω_D

`∫_0^(ω_D) [3V/(2π)²]·(ω²/v_s³) dω = 3N`

Resolviendo la integral:

`ω_D = v_s·(6π²n)^(1/3)`,  con `n = N/V` = concentración de átomos  [p. 87]

**Derivación geométrica equivalente**: el "radio de Debye" q_D (con `q_D ~ ω_D`) se define de modo que la esfera de radio q_D en el espacio q encierra exactamente N puntos (modos):

`V_esfera/V_(por punto) = (L/2π)³·(4/3)π·q_D³ = N`

`⟹ q_D = (6π²n)^(1/3)`  [p. 88]

### Derivación de C_V en el modelo de Debye

Partiendo de `E = [3V/(2π²v_s³)]·∫_0^(ω_D) ℏω³/(e^(ℏω/k_BT)-1) dω`, se deriva respecto a T:

`C_V = (∂E/∂T)_V = [3Vℏ²/(2π²v_s³k_BT²)] · ∫_0^(ω_D) ω⁴·e^(ℏω/k_BT) / (e^(ℏω/k_BT)-1)² dω`  [p. 89]

**Cambio de variable**: sea `x = ℏω/k_BT`, y se define la **temperatura de Debye** `θ_D` mediante `k_B·θ_D = ℏω_D`. Usando la relación `ω_D³/(6π²n) = v_s³`, se obtiene la forma final:

`C_V = 9R·(T/θ_D)³ · ∫_0^(θ_D/T) x⁴·e^x/(e^x-1)² dx`  [p. 89]

### Curva universal de C_V

Graficando `C_V` (en cal/gmol·K) contra `T/θ_D`, **todos los materiales colapsan sobre una misma curva universal** (con θ_D como único parámetro de ajuste por material) [p. 90]. Ejemplos de θ_D: Cu=343K, Ag=226K, Pb=102K, C(diamante)=1860K, así como valores para Li, Na, K, Au, Al, Ga, Ge, Si, NaCl, KCl, CaF₂, LiF, SiO₂, etc [p. 90].

### Relación entre θ_D y propiedades del material

`θ_D ~ ω_D ~ v_s·n^(1/3)`. Como `v_s` y `n` generalmente no dependen fuertemente de T, `θ_D` se trata como constante para cada material (`θ_D ≠ f(T)`, aproximadamente) [p. 91].

Valores típicos: `θ_D ~ 300 K` en general, lo que da `ω_D ≈ 3×10¹³ s⁻¹` [p. 91]. Ejemplo numérico: con `v_s=5×10⁵ cm/s` y `n=10²² átomos/cm³`: `ω_D ≈ 4×10¹³ s⁻¹` [p. 91].

Relación con constantes elásticas: usando `v_s=√(Y/ρ)` y `ρ=nM` (M = masa atómica, N_A = número de Avogadro):

`θ_D ~ ω_D ~ v_s·n^(1/3) ~ (Y/ρ)^(1/2)·n^(1/3) ~ (Y·N_A/(M/V))^(1/2)·n^(1/3)`

`⟹ θ_D ~ ω_D ~ (Y/(nM))^(1/2)·n^(1/3) ~ (Y/M)^(1/2)·n^(-1/6)`  [p. 91-92]

Esto muestra que materiales rígidos (Y grande) y ligeros (M pequeña) tienen θ_D (y ω_D) más altos — consistente con el diamante (C, muy rígido y ligero) teniendo el θ_D más alto de la lista (1860 K).

### Límites extremos de C_V en el modelo de Debye

**(1) T alta** (`T >> θ_D`): `x=θ_D/T << 1`, y usando `e^x≈1+x+...`:

`∫_0^(θ_D/T) x² dx = (1/3)(θ_D/T)³`

`⟹ C_V = 9R·(T/θ_D)³·(1/3)(θ_D/T)³ = 3R`  [p. 92]

(recupera Dulong-Petit)

**Argumento cualitativo equivalente**: a T>>θ_D, cada modo está altamente excitado, `ε̄=k_BT` para todos los modos, entonces:

`E = ∫ε̄(ω)g(ω)dω = k_BT·∫g(ω)dω = 3N_A·k_BT = 3RT ⟹ C_V=3R`  [p. 93]

`C_V` satura (se aproxima a 3R) alrededor de `T≈θ_D`; de hecho, en `T=θ_D` exactamente, `C_V≈0.95·(3R)` [p. 93].

**(2) T baja** (`T << θ_D`): el límite superior de la integral `θ_D/T → ∞`. Usando la integral conocida:

`∫_0^∞ x⁴e^x/(e^x-1)² dx = 4π⁴/15`

Se obtiene la famosa **ley T³ de Debye**:

`C_V = (12π⁴/5)·N·k_B·(T/θ_D)³`  [p. 94]

### Argumento cualitativo de la ley T³

Si `T<<`, solo existen pocos modos excitados (aquellos con `ℏω < k_BT`) [p. 94]. Considerando una "esfera térmica" en el espacio q de radio correspondiente a `ω=k_BT/ℏ`:

`# puntos (modos) dentro de la esfera ∝ q³ ~ ω³ ~ T³`  [p. 95]

Cada uno de estos modos excitados contribuye aproximadamente `ε̄=k_BT` de energía (están completamente excitados, en el régimen clásico local), por lo que:

`E_(total de excitación) ~ T·T³ = T⁴  ⟹  C_V = dE/dT ~ T³`  [p. 95]

### Puntos clave para dominar este tema
- Puede explicar la diferencia conceptual central entre Einstein (osciladores independientes, una sola ω) y Debye (modos colectivos con espectro continuo de ω, todos con carácter de onda de sonido ω=v_s q).
- Sabe derivar ω_D=v_s(6π²n)^(1/3) a partir de la condición de normalización ∫g(ω)dω=3N (igualando el número de modos al número de grados de libertad 3N).
- Puede escribir la fórmula completa de Debye C_V=9R(T/θ_D)³∫₀^(θ_D/T) x⁴e^x/(e^x-1)²dx, con x=ℏω/k_BT y k_Bθ_D=ℏω_D.
- Sabe derivar el límite de alta T (C_V→3R, recuperando Dulong-Petit) y explicar el argumento cualitativo alternativo (todos los modos con ε̄=k_BT).
- Puede derivar/reproducir la ley T³ de Debye a bajas T: C_V=(12π⁴/5)Nk_B(T/θ_D)³, usando ∫₀^∞ x⁴e^x/(e^x-1)²dx=4π⁴/15.
- Sabe dar el argumento cualitativo geométrico de la ley T³: el número de modos térmicamente excitados (con ℏω<k_BT) escala como el volumen de una esfera de radio q~T en el espacio recíproco, es decir ~T³, y cada uno aporta ~k_BT, dando E~T⁴ y C_V~T³.
- Entiende que θ_D~(Y/M)^(1/2)·n^(-1/6): materiales rígidos y ligeros tienen θ_D (y ω_D) más altos (ej. diamante).
- Sabe que el modelo de Debye SÍ reproduce correctamente el comportamiento experimental C_V~T³ a bajas T, a diferencia del modelo de Einstein (que predice decaimiento exponencial, incorrecto).

## 5. Limitaciones del modelo de Debye

Aunque el modelo de Debye funciona mucho mejor que el de Einstein, sigue siendo una **aproximación**, no un tratamiento exacto [p. 97]:

- La relación `ω = v_s·q` (lineal) NO es válida para todos los modos de excitación reales de una red cristalina discreta — es solo una aproximación válida en el límite de longitud de onda larga.
- Experimentalmente, `θ_D` no es exactamente constante con T: existe una discrepancia de alrededor de **10%** respecto al valor de Debye "puro" al comparar diferentes temperaturas [p. 97].
- La solución consistente requiere usar la relación de dispersión real `ω(q)` y la densidad de estados `g(ω)` correctas de la red discreta (en vez de la aproximación continua lineal).

### Consideración de velocidades longitudinal y transversal distintas

El modelo de Debye discutido aquí es para redes NO metálicas, monoatómicas. En general, `v_g(longitudinal) ≠ v_g(transversal)`. Para mantener el tratamiento simple, se sustituye v_s por una velocidad promedio `v̄` definida por [p. 98]:

`3/v_s³ = 1/v_l³ + 2/v_T³`

Sustituyendo en la integral de E se puede separar en contribuciones: `E = E_ℓ + E_T1 + E_T2` (una rama longitudinal + dos ramas transversales).

**Pregunta abierta planteada en la diapositiva**: el modelo de Debye considera que SOLO las vibraciones de red contribuyen a C_V — pero ¿qué ocurre en los metales, donde también hay electrones libres que contribuyen al calor específico? [p. 98] (Este punto se retomará más adelante en el curso, en el capítulo del electrón libre).

### Puntos clave para dominar este tema
- Sabe que el modelo de Debye es una aproximación (no exacta) porque asume ω=v_sq válida para TODOS los modos, cuando en realidad esto solo es cierto en el límite de q pequeño (λ grande).
- Conoce la discrepancia experimental típica (~10%) de θ_D respecto al valor ideal de Debye al variar T.
- Sabe cómo se define una velocidad de sonido promedio v̄ combinando velocidad longitudinal y transversal: 3/v_s³=1/v_l³+2/v_T³.
- Entiende que el modelo de Debye tal como se presenta aquí NO incluye la contribución de los electrones libres al calor específico de un metal — esto queda como pregunta abierta para el capítulo del electrón libre.

## 6. El fonón

### Cuantización de la energía de un modo normal

Cada modo normal de vibración (onda elástica) tiene energía cuantizada:

`E_(modo) = n·ℏω`  [p. 99]

Esto significa que **la energía elástica de una onda de sonido está cuantizada**, igual que la energía electromagnética está cuantizada en fotones.

### Definición de fonón

**Fonón** ≡ entidad tipo partícula (cuasipartícula) que lleva la unidad de energía del campo elástico en un modo particular de vibración [p. 99]:

`ε = ℏω ≡ E_(fonón)`

El fonón, como onda viajera, transporta momento (cantidad de movimiento):

`P = h/λ`; usando `λ = 2π/q`:

`P = ℏq`  [p. 99]

### Analogía y diferencias fonón-fotón

**Similitudes (fonón ≡ fotón)** [p. 100]:
- Ambos presentan dualidad onda-partícula.
- Ambos cumplen el principio de incertidumbre de Heisenberg.
- Ambos interactúan con otros cuantos y partículas (ej. electrones).

**Diferencias (fonón ≠ fotón)** [p. 100]:
- La velocidad de grupo del fonón `v_g = f(λ)` depende de la longitud de onda a través de la relación de dispersión (que en general NO es lineal, especialmente para redes discretas reales) — mientras que el fotón en el vacío tiene v_g=c constante.
- La frecuencia máxima del fonón, `ω_max`, está limitada por una **frecuencia de corte** `ω_corte` (asociada a la naturaleza discreta/vibracional de la red) — el fotón en el vacío no tiene tal límite superior.

### Puntos clave para dominar este tema
- Puede definir el fonón como el cuanto de energía de un modo normal de vibración de la red, con energía ε=ℏω y momento P=ℏq.
- Sabe explicar las similitudes conceptuales entre fonón y fotón (dualidad onda-partícula, principio de incertidumbre, capacidad de interactuar con otras partículas/cuantos).
- Puede señalar las diferencias clave: la velocidad de grupo del fonón depende de λ (relación de dispersión no trivial) y existe una frecuencia de corte ω_corte (asociada al carácter discreto/finito de la red), a diferencia del fotón en el vacío.

## 7. Estadística de fonones: reglas de selección, número de ocupación y consistencia estadística

> **Nota de origen:** esta sección complementa la sección 6 ("El fonón") con material de las páginas 101-103, que cierra formalmente el tratamiento cuántico de las vibraciones de red antes de pasar a anarmonicidad y a la cadena discreta.

### Reglas de selección del oscilador armónico cuántico

Para el oscilador armónico (transición entre niveles consecutivos, ej. de n=1 a n=2):

`Δn = ±1` y `Δε = ±ℏω`  [p. 101]

Estas son las **reglas de selección** que rigen la emisión/absorción de un fonón por un oscilador de red.

### Por qué el fonón se comporta como una partícula: estadística de Bose-Einstein

Pregunta guía: si fonón≡partícula (efectos causados por vibraciones ≡ propiedades asociadas a un gas de fonones libres), ¿es esto consistente? Respuesta: **sí**, porque [p. 101]:

a. El fonón es una partícula **indistinguible** de otro fonón (a diferencia de los átomos de la red, que son distinguibles por su sitio).
b. El fonón no tiene espín asociado a una restricción de exclusión de Pauli.

`⟹` la distribución de energía de un gas de fonones sigue la **estadística de Bose-Einstein**.

**Consecuencia importante**: los resultados obtenidos con estadística de Maxwell-Boltzmann (tratando los osciladores/átomos como partículas distinguibles, como en la derivación original de Einstein/Debye de la sección 3-4) **coinciden exactamente** con los resultados obtenidos tratando los fonones como partículas indistinguibles con estadística Bose-Einstein [p. 103]. Esta es una consistencia interna importante del modelo: da igual el punto de vista (osciladores normales distinguibles vs. gas de bosones indistinguibles), el resultado para E y C_V es el mismo.

### Número de fonones en un rango dω y contribución a la energía

Una onda de sonido ≡ un haz de fonones (con energía E y momento P asociados). El número de fonones en el rango (ω, ω+dω) es [p. 102]:

`N(ω)dω = f(ω)·g(ω)·dω = g(ω)dω / (e^(ℏω/k_BT) - 1)`

con la densidad de estados 3D (una polarización longitudinal + dos transversales, ya vista en la sección de "Ondas elásticas"):

`g(ω)dω = [3V/(2π²)]·(ω²/v_s³)·dω`  [p. 102]

de donde:

`N(ω)dω = [3V/(2π²v_s³)]·ω²dω / (e^(ℏω/k_BT)-1)`  [p. 102]

La contribución a la energía interna de los fonones en dω:

`dE = ε(ω)·N(ω)dω = ℏω·N(ω)dω = [3ℏV/(2π²v_s³)]·ω³dω/(e^(ℏω/k_BT)-1)`  [p. 102]

### Energía interna total del gas de fonones (forma equivalente en términos de N y ω_D)

Integrando entre `0<ω<ω_D` y usando la relación de normalización `ω_D³/(6π²n) = v_s³` (n=N/V), la energía interna del gas de fonones puede escribirse de forma compacta como [p. 103]:

`E_int = (9Nℏ/ω_D³)·∫₀^(ω_D) ω³dω/(e^(ℏω/k_BT)-1)`  [p. 103]

*(Esta expresión es algebraicamente idéntica a `E=[3V/(2π²v_s³)]∫₀^(ω_D)ℏω³/(e^(ℏω/k_BT)-1)dω` de la sección 4, solo que reescrita sustituyendo `v_s³` por `ω_D³/(6π²N/V)` — es la misma integral de Debye, expresada en términos de N y ω_D en vez de V y v_s. Sirve como verificación cruzada de consistencia entre ambas derivaciones.)*

### Energía media y número medio de ocupación de un modo (fonones)

Para un modo individual de frecuencia ω, con `ε = ℏω ≡ E_fonón`:

`ε̄ = ℏω/(e^(ℏω/k_BT)-1)` → energía media de fonones en ese modo (idéntica a la ε̄ de Einstein/Debye) [p. 103]

Se define además el **número medio de ocupación** del modo, `n̄`, tal que `ε̄ = n̄·ℏω`:

`n̄ = 1/(e^(ℏω/k_BT)-1)`  [p. 103]

Esta es la **distribución de Bose-Einstein** para el número de ocupación de un modo bosónico.

**Límites de n̄:**
- `T→0 ⟹ n̄→0` (modo "vacío" de fonones, congelado en el estado base).
- `T>>` (alta T, `k_BT>>ℏω`) `⟹ n̄ ≈ k_BT/ℏω` (número de ocupación crece linealmente con T; consistente con el límite clásico `ε̄→k_BT` visto en la sección 3, ya que `ε̄=n̄ℏω≈(k_BT/ℏω)·ℏω=k_BT`). [p. 103]

### Puntos clave para dominar este tema

- Conoce las reglas de selección del oscilador armónico cuántico: `Δn=±1`, `Δε=±ℏω`.
- Puede justificar por qué el gas de fonones obedece la estadística de Bose-Einstein: los fonones son indistinguibles entre sí y no están sujetos al principio de exclusión de Pauli.
- Sabe explicar por qué el resultado de Maxwell-Boltzmann (osciladores distinguibles) coincide exactamente con el resultado de Bose-Einstein (fonones indistinguibles) para la energía interna del sólido — es una consistencia interna del modelo, no una coincidencia.
- Puede escribir la distribución `N(ω)dω = g(ω)dω/(e^(ℏω/k_BT)-1)` (número de fonones en dω) y derivar de ahí `dE=ℏω·N(ω)dω`.
- Puede definir el número medio de ocupación de un modo `n̄=1/(e^(ℏω/k_BT)-1)` (distribución de Bose-Einstein), distinguirlo de la energía media `ε̄=n̄ℏω`, y calcular sus límites: `n̄→0` a T baja, `n̄≈k_BT/ℏω` a T alta.
- Puede verificar que `E=9Nℏ/ω_D³ ∫₀^(ω_D) ω³dω/(e^(ℏω/k_BT)-1)` es algebraicamente equivalente a la forma `E=3Vℏ/(2π²v_s³)∫ω³dω/(e^(ℏω/k_BT)-1)` de la sección de Debye, usando `ω_D³=6π²(N/V)v_s³`.

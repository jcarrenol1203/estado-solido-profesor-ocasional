# Ondas elásticas y densidad de estados (tratamiento de medio continuo)

> **Nota importante sobre alcance**: Esta sección presenta un tratamiento preliminar/motivacional de las vibraciones de red usando la **aproximación de medio continuo** (onda elástica clásica), que conduce a una relación de dispersión lineal `ω = v_s·q`. Esto es DISTINTO del tratamiento discreto de la cadena lineal monoatómica con ley de Hooke entre átomos vecinos (que da lugar a una relación de dispersión periódica no lineal, con primera zona de Brillouin, etc.). En las páginas revisadas (1-100 del PDF) **no aparece** la derivación de la ecuación de movimiento de la cadena discreta monoatómica (F=-α(2u_n-u_(n-1)-u_(n+1)) tipo). Es muy probable que esa derivación (sección 1.1 "Ecuación de movimiento" del temario) comience en la página 101 en adelante — el siguiente bloque de notas debe cubrirla explícitamente y no asumir que ya fue tratada aquí.

## 1. Motivación: ondas de sonido y vibraciones de red

Las ondas de sonido en un sólido tienen frecuencias ω mucho mayores que las del espectro auditivo humano (ω >> ω_sonido audible) [p. 45].

En un sólido, los átomos están fuertemente acoplados por fuerzas interatómicas. Conceptualmente:

`E_k térmica del átomo ≡ E_vibracional (de movimiento + acople entre vecinos) ≡ propagación como onda`

Es decir, en los cristales la energía térmica se transporta mediante ondas [p. 45].

**Cómo leer la diapositiva 45 (releída directamente del PDF):**
- Título: "ondas de sonido, relaciones de dispersión **∧** vibraciones de red" — la "∧" es un "y" (lógico). El tema es que las ondas de sonido en un sólido *son* las vibraciones de red.
- "ondas de sonido, espectro auditivo" está **tachado con una X roja**: significa "no hablamos del sonido audible". Sigue `ω >> ω_audible` (audible ≲ 2·10⁴ Hz; vibraciones de red hasta ~10¹³ Hz, ω_m = 2v_s/a ≈ 2·5000/3·10⁻¹⁰ ≈ 3·10¹³ rad/s).
- Cadena de "=" (en rojo): **no son igualdades matemáticas**, son "se manifiesta como": energía cinética térmica del átomo → energía vibracional (movimiento + acople con vecinos) → propagación como onda ⟹ la energía térmica viaja por ondas. Formalmente E_térmica = E_cinética + E_potencial (≈ mitad y mitad en el oscilador armónico); la diapositiva es informal.
- Texto cortado en el borde: "(F. interató)" = fuerzas interatómicas.

Fuentes externas (ej. luz) pueden excitar ondas acústicas en las redes cristalinas; estas ondas acústicas son importantes para las propiedades físicas de los cristales. El objetivo de esta sección es entender cómo se propagan las ondas de sonido en un sólido [p. 46].

### Puntos clave para dominar este tema
- Sabe justificar por qué el modelo de "espectro auditivo" no aplica a las vibraciones de red: las frecuencias relevantes son mucho mayores.
- Puede explicar conceptualmente que la energía vibracional/térmica de un cristal se transporta como ondas debido al acoplamiento entre átomos vecinos.

## 2. Derivación de la ecuación de onda elástica (medio continuo, 1D)

Se considera una barra sólida de sección A, y se analiza un elemento diferencial entre x y x+dx sometido a una onda longitudinal [p. 56].

Definiciones:
- `u(x,t)` = desplazamiento elástico en la posición x ≡ amplitud vibracional asociada al desplazamiento de la posición de equilibrio x.
- `ξ = du/dx` ≡ deformación (strain).
- `S = F/A = Y·ξ` ≡ esfuerzo (stress), donde Y es el módulo de Young.

### Aplicación de la 2ª ley de Newton al elemento diferencial

`ρ·A'·dx·(∂²u/∂t²) = [S(x+dx) - S(x)]·A'`  [p. 57]

Expandiendo `S(x+dx) - S(x) = (∂S/∂x)dx`, y usando `S = Y·(∂u/∂x)`, se obtiene la **ecuación de onda**:

`∂²u/∂x² - (ρ/Y)·∂²u/∂t² = 0`   ... (1)  [p. 57]

### Solución tipo onda plana y relación de dispersión

Se propone la solución `u(x,t) = A·e^(i(qx-ωt))`, con `q = 2π/λ` [p. 57].

Sustituyendo en (1):

`ω = v_s·q`  → **relación de dispersión** (lineal)

con la velocidad del sonido:

`v_s = √(Y/ρ)`  ⟹  `ω = q·√(Y/ρ)`  [p. 57]

- Esta relación `ω = v_s·q` describe el sonido en líquidos y gases también (análogo a `ω = c·q` para ondas electromagnéticas en el vacío) [p. 58].
- **Advertencia de validez**: esta relación NO es válida cuando `λ ≈ distancia interatómica` — el medio continuo deja de ser una buena aproximación cuando la longitud de onda se acerca a la escala atómica [p. 58].
- Ejemplo numérico: si `v_s = 5×10⁵ cm/s` y `ρ = 5 g/cm³`, entonces `Y = 1.25×10¹² g/(cm·s²)` [p. 58].

### Puntos clave para dominar este tema
- Puede derivar la ecuación de onda elástica 1D aplicando la 2ª ley de Newton a un elemento diferencial de un medio continuo, usando S=Yξ=Y·∂u/∂x.
- Sabe sustituir la solución de onda plana u(x,t)=Ae^(i(qx-ωt)) en la ecuación de onda para obtener la relación de dispersión ω=v_s·q, con v_s=√(Y/ρ).
- Entiende que ω=v_s·q es una relación LINEAL (no periódica), válida solo en el límite de longitud de onda larga (λ >> distancia interatómica), y sabe explicar por qué falla cuando λ se acerca al espaciado atómico.
- Puede resolver un problema numérico dado v_s y ρ para hallar el módulo de Young Y (o viceversa).

## 3. Densidad de estados g(ω) en 1D (condiciones de frontera periódicas)

### Cuantización de q por condiciones de frontera periódicas (tipo Born-von Karman)

Se considera una barra de longitud L. Puesto que u(x,t) y ω(q) dependen del número (finito) de átomos N, las condiciones de frontera hacen que ω y λ (y por tanto q) tomen valores **discretos** [p. 59].

Se imponen **condiciones de frontera periódicas**: el estado de oscilación en el extremo A es igual al estado de oscilación en el extremo B (equivalente a doblar la barra en un anillo) [p. 59]:

`u(x=0) = u(x=L)`

Con `u(x) = A·e^(iqx)`: `u(x=0) = 1`, `u(x=L) = e^(iqL) = 1` [p. 60].

Esto requiere `e^(in·2π) = 1` con `n ∈ ℤ` (n=0, ±1, ±2, ...), de donde:

`q = n·(2π/L) = 2π/λ`  [p. 60]

Cuando `L >>` (la muestra es macroscópica), el espaciamiento `Δq = 2π/L` es muy pequeño ⟹ la "red" de valores permitidos de q se vuelve **cuasi-contínua** [p. 60].

### Conteo de modos y definición de g(ω)

Sea dq un intervalo arbitrario en q. El número de modos contenidos en dq es:

`# modos en dq = dq/(2π/L) = (L/2π)·dq`  [p. 61]

Usando `ω = v_s·q ⟹ dω = v_s·dq`, se define la **densidad de estados** g(ω) tal que el número de modos con frecuencia entre (ω, ω+dω) es `g(ω)dω`:

`g(ω)dω = (L/2π)dq  ⟹  g(ω) = (L/2π)/(dω/dq)`  [p. 61]

### Factor 2 por las ramas ±q (ondas viajando en ambos sentidos)

Como existen ramas `ω = +v_s·q` y `ω = -v_s·q` (ondas propagándose en ambas direcciones), al contar solo |ω| (o ω positivo) hay que multiplicar por 2:

`g(ω) = (L/π)/(dω/dq)`  [p. 62]

En 1D, como `dω/dq = v_s` (constante, dispersión lineal):

`g(ω) = (L/π)/v_s = cte.`  [p. 62]

Es decir, **en 1D con dispersión lineal, la densidad de estados es constante** (no depende de ω).

### Puntos clave para dominar este tema
- Puede aplicar condiciones de frontera periódicas (tipo Born-von Karman) a una onda plana u(x)=Ae^iqx en una barra de longitud L, y derivar la cuantización q=n(2π/L).
- Sabe explicar por qué L grande (muestra macroscópica) hace que el espectro de q sea efectivamente continuo (Δq=2π/L→0).
- Puede derivar la fórmula general g(ω)=(L/2π)/(dω/dq) [más el factor 2 por las ramas ±q: g(ω)=(L/π)/(dω/dq)] a partir de contar modos en un intervalo dq.
- Sabe que, en 1D con relación de dispersión lineal ω=v_s q, la densidad de estados resulta constante: g(ω)=(L/π)/v_s.

## 4. Densidad de estados g(ω) en 3D

### Cuantización de q en 3D

Para una onda plana en 3D, `u(x)=A·e^(i(qₓx+qᵧy+q_zz)) = A·e^(iq·r)`, donde **q** apunta en la dirección de propagación y `|q| ∝ 1/λ` [p. 63].

Con condiciones de frontera periódicas en un cubo de lado L (`u(0)=u(L)` en las 3 direcciones):

`(qₓ, qᵧ, q_z) = [n(2π/L), m(2π/L), ℓ(2π/L)]`,  n, m, ℓ ∈ ℤ  [p. 63]

Esto define una red cúbica simple de puntos permitidos en el "espacio q", con volumen por punto:

`v_punto = (2π/L)³`  [p. 64]

### Conteo de modos dentro de una esfera de radio q

El número de modos con `|q| < q` es igual al número de puntos de esa red-q contenidos dentro de una esfera de radio q, es decir, el volumen de la esfera dividido por el volumen por punto:

`v_esfera = (4π/3)q³`

`v_esfera/v_punto = (L/2π)³ · (4π/3)q³`  [p. 64]

### Derivación de g(ω) en 3D

Derivando respecto a q para obtener el número de modos en el cascarón esférico (q, q+dq):

`d/dq(v_esf/v_punto) = [V/(2π)³]·4πq²·dq`  [p. 65]

donde `V=L³`. Esto es el número de modos/puntos en el cascarón (q, q+dq), que se identifica con `g(ω)dω`:

`g(ω)dω = [V/(2π)³]·4πq²·dq`  [p. 65]

Cambiando de variable con `ω = v_s·q` (⟹ `q=ω/v_s`, `dq = dω/v_s`):

`g(ω)dω = [V/(2π)³]·4π·(ω/v_s)²·(dω/v_s)`

**Resultado (para una sola polarización)**:

`g(ω) = V·ω² / (2π²·v_s³)`  [p. 65]

Es decir, `g(ω) ~ ω²` en 3D (crece cuadráticamente, a diferencia de la constante en 1D).

### Factor 3 por las polarizaciones (1 longitudinal + 2 transversales)

En 3D, para cada vector de onda **q** existen 3 modos de polarización posibles: 1 onda longitudinal y 2 transversales. Asumiendo un medio isotrópico (misma velocidad v_s para las 3 polarizaciones):

`g(ω) = 3V·ω² / (2π²·v_s³)`  [p. 66]

Con V=1 (normalizado): `g(ω) = 3ω²/(2π²v_s³)` [p. 66].

**Condición de validez**: esta expresión de g(ω) es válida si `λ << dimensión de la muestra`; en ese régimen, g(ω) NO depende de los detalles específicos de las condiciones de frontera elegidas [p. 66].

### Puntos clave para dominar este tema
- Puede derivar geométricamente (contando puntos dentro de una esfera de radio q en el espacio recíproco) la expresión g(ω)=Vω²/(2π²v_s³) para una polarización, usando ω=v_s q.
- Sabe explicar por qué en 3D g(ω)~ω² mientras que en 1D g(ω)=constante — la diferencia surge de contar puntos en un volumen esférico (∝q²dq) vs. un intervalo lineal (∝dq).
- Sabe incluir el factor 3 debido a las tres polarizaciones posibles (1 longitudinal + 2 transversales) en medios isotrópicos: g(ω)=3Vω²/(2π²v_s³).
- Entiende que esta fórmula asume un medio continuo isotrópico y es válida solo cuando λ es mucho menor que las dimensiones de la muestra (para que el resultado no dependa de las condiciones de frontera específicas).

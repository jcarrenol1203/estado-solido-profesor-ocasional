# Cadena lineal monoatómica discreta 1D (sección 1.1: Ecuación de movimiento)

> **Nota de origen:** este archivo cubre las páginas 109-141 del PDF. El archivo `01_ondas_elasticas_y_densidad_estados.md` (páginas 1-100, escrito por otro proceso) trata el modelo de **medio continuo** (ω=v_s·q, lineal) y advierte explícitamente que la derivación de Newton para la **cadena discreta** (F=-α(2u_n-u_{n-1}-u_{n+1})) no aparece en las páginas 1-100. Este archivo cubre exactamente esa derivación (sección 1.1 "Ecuación de movimiento" del temario) de forma completa: ecuación de movimiento, relación de dispersión periódica ω=ω_m|sin(qa/2)|, primera zona de Brillouin, velocidades de fase/grupo, y densidad de estados exacta con singularidad de van Hove. Es el complemento natural de `01_ondas_elasticas_y_densidad_estados.md`.

## Ecuación de movimiento y relación de dispersión

Cadena de átomos idénticos de masa $M$, separación de equilibrio $a$, con interacción armónica solo a primeros vecinos (constante de fuerza $\alpha$). Desplazamiento del átomo $n$: $u_n$. [p. 110]

- Fuerza sobre el átomo $n$ debida a $n+1$: $\alpha(u_{n+1}-u_n)$ [p. 110]
- Fuerza sobre el átomo $n$ debida a $n-1$: $\alpha(u_{n-1}-u_n)$ [p. 111]
- Ecuación de Newton para el átomo $n$:
$$M\frac{d^2u_n}{dt^2} = \alpha(u_{n+1}-u_n) + \alpha(u_{n-1}-u_n) = -\alpha(2u_n - u_{n+1}-u_{n-1})$$ [p. 111]
- En el límite continuo, para cada átomo se obtiene la ecuación de onda clásica $\dfrac{\partial^2 u}{\partial x^2} - \dfrac{\rho}{Y}\dfrac{\partial^2 u}{\partial t^2}=0$ (sistema extendido, $N$ ecuaciones diferenciales acopladas, con condiciones de frontera consideradas). [p. 111]

**Solución tipo onda viajera (modo normal):**
$$u_n(x,t) = A e^{i(qx_n-\omega t)}, \qquad x_n = na$$ [p. 112]

La fase se incrementa en $qa$ de un átomo al siguiente. Para la red, "modo normal" $\equiv$ "onda de propagación". [p. 112]

**Sustituyendo en la ecuación de movimiento:**
$$M(-\omega^2)e^{iqna} = -\alpha\left(2e^{iqna}-e^{iq(n+1)a}-e^{iq(n-1)a}\right)$$
$$M(-\omega^2) = -\alpha(2-e^{iqa}-e^{-iqa}) = 2\alpha(\cos qa - 1)$$
usando $e^{iy}+e^{-iy}=2\cos y$ y $1-\cos\theta = 2\sin^2(\theta/2)$: [p. 113]

$$\boxed{\omega = \omega_m\,|\sin(qa/2)|}, \qquad \omega_m = \left(\frac{4\alpha}{M}\right)^{1/2}$$ [p. 113]

Esta es la curva de dispersión completa (medio dispersivo), periódica en $q$, con máximo $\omega_m$ en $q=\pm\pi/a$.

## Límites físicos y relación con el continuo elástico

**Límite de longitud de onda larga** ($q\ll\pi/a \Leftrightarrow \lambda\gg 2a$): [p. 114]
- $0<\omega<\omega_m$ son las frecuencias transmitidas por la red $\Rightarrow$ **la red actúa como un filtro mecánico pasa-bajos**.
- $\sin(qa/2)\approx qa/2 \Rightarrow \omega \approx \dfrac{\omega_m a}{2}q$
- Comparando con $\omega = v_s q$ (continuo elástico): $v_s = \omega_m a/2 = a\sqrt{\alpha/M} \approx$ cte. [p. 114]

**Relación entre $\alpha$ y el módulo de Young $Y$** (red cúbica, planos atómicos): [p. 115]
$$v_s = \sqrt{Y/\rho} = \omega_m a/2 \;\Rightarrow\; v_s^2 = Y/\rho, \qquad \rho = M/a^3$$
$$\rho v_s^2 = Y = \rho a^2\frac{\alpha}{M} = \frac{M}{a^3}a^2\frac{\alpha}{M} \;\Rightarrow\; \boxed{\alpha = aY}$$ [p. 115]

**Estimación numérica** [p. 116]:
- $\alpha \approx (10^{-8}\text{ cm})(10^{11}\text{ g/cm·s}^2) \approx 10^3$ dinas/cm
- Con $M = 10^{-24}$ g (hidrógeno): $\omega_m \approx 10^{13}\text{ s}^{-1}$

**Comportamiento no lineal cuando $q$ aumenta:** la curva $\omega(q)$ se satura (no sigue siendo lineal) al acercarse a $q=\pi/a$; ahí $\omega_m=(4\alpha/M)^{1/2}$. [p. 116]

## Significado físico de los casos límite en $q$

- $q\ll$ ($\lambda\gg a$): fuerza de restauración pequeña $\Rightarrow \omega$ pequeña. En $q=0$ ($\lambda=\infty$): $\omega=0$, $F=0$ $\Rightarrow$ **movimiento de cuerpo rígido** (todos los átomos se mueven juntos, sin vibración relativa). [p. 117]
- $q=\pi/a$ ($\lambda=2a$): átomos vecinos vibran **exactamente fuera de fase** (cambio de fase $=2qa=2\pi$ entre segundos vecinos pero $\pi$ entre vecinos inmediatos); la fuerza de restauración es máxima $\Rightarrow \omega\to\omega_m$ (máximo). [p. 117, 127]

**Introducción de $\alpha(q)$ (constante de fuerza efectiva dependiente de $q$):** con $u_{n\pm1}=u_n e^{\pm iqa}$, sustituyendo en la ecuación de movimiento se obtiene un oscilador armónico efectivo: [p. 118]
$$M\frac{d^2u_n}{dt^2} = -\left[4\alpha\sin^2(qa/2)\right]u_n \quad (\text{análogo a } F=-kx)$$
$$\alpha(q) = 4\alpha\sin^2(qa/2), \qquad \omega=\sqrt{\alpha(q)/M}$$
Esto representa el "movimiento de átomos correlacionados". [p. 118]

## Velocidad de fase y velocidad de grupo

**Derivación de la envolvente (paquete de ondas) a partir de dos trenes de onda cercanos:** [p. 119]
$$u_1 = A\cos(kx-\omega t), \qquad u_2 = A\cos[(k+dk)x-(\omega+d\omega)t]$$
Usando $\cos\alpha+\cos\beta = 2\cos\tfrac12(\alpha-\beta)\cos\tfrac12(\alpha+\beta)$:
$$u_1+u_2 = 2A\cos(kx-\omega t)\cos\left(\tfrac12 t\,d\omega - \tfrac12 x\,dk\right)$$ [p. 120]

La envolvente tiene longitud de onda $\lambda_{env}=4\pi/dk$ (el doble que la portadora). Para un punto de fase constante de la envolvente:
$$\tfrac12 t\,d\omega - \tfrac12 x\,dk = 0 \;\Rightarrow\; x = \frac{d\omega}{dk}t = v_g t$$
$$\boxed{v_g = \frac{d\omega}{dq}} \qquad (\text{velocidad de grupo})$$ [p. 120]

- $v_{fase}$ de la envolvente $= d\omega/dk = v_g$; la energía de la onda **se transporta con $v_g$**, no con $v_p$. [p. 121]
- En los nodos, el medio está aproximadamente en equilibrio $\Rightarrow$ la energía no se propaga más allá de ese punto. [p. 121]
- Onda estacionaria: transporte neto de energía $=0 \Rightarrow v_g=0$. [p. 121]

**Caso no dispersivo (medio continuo, $\omega=v_sq$):** $v_g=v_p=v_s=$ cte $=d\omega/dq$. [p. 122]

**Dispersión** $\equiv$ situación en la que $v_g\neq v_p$; en un medio dispersivo $v_g,v_p\neq$ cte y son función de $\omega$; ya no se cumple $v=\lambda\nu=$ cte. [p. 122]

**Velocidad de fase completa de la red monoatómica:**
$$v_p = \frac{\omega}{q} = v_s\left|\frac{\sin(\tfrac12 qa)}{\tfrac12 qa}\right|$$ [p. 123]
Esta función tiene máximo $v_s$ en $q\to0$ y decae oscilando (con ceros) para $q$ mayor; en $q=\pi/a$, $v_p=2v_s/\pi$. [p. 123]

**Velocidad de grupo completa:**
$$v_g = \frac{\partial\omega}{\partial q} = \omega_m\frac{a}{2}\left|\cos\tfrac12 qa\right| = v_s\left|\cos\tfrac12 qa\right|$$ [p. 124]
- $v_g$ decrece monótonamente desde $v_s$ (en $q=0$) hasta **$v_g=0$ en $q=\pi/a$** (borde de zona). [p. 124, 125]

## Reflexión de Bragg en el borde de zona ($q=\pi/a$)

- $q=\pi/a \Rightarrow \lambda=2a$: la dispersión de la onda por los átomos discretos es **fuerte**. [p. 125]
- Las ondas reflejadas por átomos vecinos llegan desfasadas $\pi$ entre sí en general, pero para $\lambda=2a$ interfieren **constructivamente** ($N\lambda=2a$ tipo condición). [p. 125]
- $q=N\pi/a \Rightarrow$ reflexión máxima $\Rightarrow$ onda incidente + onda reflejada = **onda estacionaria** $\Rightarrow v_g=0$. [p. 126]
- Esto es análogo a la **condición de Bragg**: $2d\sin\theta = n\lambda$; con $\theta=\pi/2$ (incidencia normal), $\lambda=2d$. Esto ilustra la **naturaleza ondulatoria del campo acústico**. [p. 126]

## Simetría en el espacio $q$: primera zona de Brillouin (1D)

- $\omega(q)$ es periódica: $\omega(q+2\pi/a) = \omega(q)$ (periodicidad en el espacio $q$), y tiene simetría de reflexión respecto al origen: $\omega(-q)=\omega(q)$. Ambas simetrías provienen de la **simetría traslacional de la red real**. [p. 128, 134]

**Origen físico de la periodicidad — no unicidad de $\lambda$ en una red discreta:** [p. 129]
Para $q=\pi/2a$, $\lambda=4a$. Para $q'=q+2\pi/a$, $\lambda'=4a/5$. Ambas ondas, evaluadas **solo en las posiciones atómicas**, producen desplazamientos físicamente idénticos (son indistinguibles para la red discreta), aunque como funciones continuas se ven distintas. [p. 129]
$$q' = q + n\left(\frac{2\pi}{a}\right), \qquad n\in\mathbb{Z}^+ \;\Rightarrow\; \text{ondas físicamente idénticas}$$ [p. 130]

En consecuencia: **para una red discreta, la longitud de onda asociada a un conjunto de desplazamientos atómicos no es única** — varios valores de $q$ (y por tanto de $\lambda$) producen el mismo $\omega$ y el mismo patrón de desplazamientos. [p. 130, 131]

**Representación única:** basta restringir $q$ a un intervalo de longitud igual a un periodo de la red recíproca ($2\pi/a$):
$$-\frac{\pi}{a} < q < \frac{\pi}{a} \;\equiv\; \text{primera zona de Brillouin para la red 1D}$$ [p. 132, 134]
Dentro de este intervalo, $\lambda$ toma **el valor más grande posible** consistente con el conjunto de desplazamientos atómicos. [p. 132]
Las regiones $[-\pi/a,\pi/a]$, $[\pi/a,3\pi/a]$, etc. son equivalentes, relacionadas por traslaciones de $n\cdot2\pi/a$ en el espacio $q$. [p. 133]

## Conteo de modos normales en la primera zona de Brillouin

Con condiciones de frontera periódicas: $q = n\dfrac{2\pi}{L}$, $n=0,\pm1,\pm2,\dots$ [p. 135]

Número de puntos $q$ permitidos dentro de la 1ª ZB:
$$\frac{2\pi/a}{2\pi/L} = \frac{L}{a} = N$$ [p. 135]

$N$ = número total de átomos (o celdas unitarias) $\equiv$ número de grados de libertad. Varias ondas pueden propagarse simultáneamente (superposición) $\Rightarrow$ el movimiento arbitrario de la red se trata vía **análisis de Fourier**. [p. 135]

## Densidad de estados $g(\omega)$ para la cadena 1D (resultado exacto, con singularidad de van Hove)

Definiendo $g(q)$ como el número de estados por unidad de longitud en el espacio $q$: como los valores de $q$ están igualmente espaciados, **el número de estados permitidos = número de átomos** (para pocos átomos: puntos discretos separados; para muchos átomos: prácticamente continuo). [p. 136]

$$\frac{Na}{2\pi} = \text{cte.} = g(q) \quad (\text{estados por unidad de longitud en } q)$$
$$g(q)\,dq = \frac{Na}{2\pi}dq$$ [p. 137]

Cambiando variable a $\omega$:
$$g(\omega)\,d\omega = g(q)\,dq = \frac{Na}{2\pi}\frac{dq}{d\omega}\,d\omega = \frac{Na}{2\pi}\frac{1}{v_g}\,d\omega$$
usando $\partial q/\partial\omega = 1/v_g$ y $v_g = v_s|\cos(qa/2)|$. [p. 137]

Sustituyendo $v_g$ explícitamente:
$$g(\omega)\,d\omega = \frac{N}{2\pi}\frac{2}{\omega_m\cos(\tfrac12 qa)}\,d\omega$$ [p. 138]

Usando $\omega/\omega_m = |\sin(qa/2)|$, se obtiene $\cos(\tfrac12 qa) = \sqrt{\omega_m^2-\omega^2}/\omega_m$, y finalmente:

$$\boxed{g(\omega)\,d\omega = \frac{N}{\pi}\frac{d\omega}{\sqrt{\omega_m^2-\omega^2}}}$$ [p. 139]

**Comportamiento límite:**
- $\omega \ll \omega_m \Rightarrow g(\omega) \to N/(\pi\omega_m) \approx$ cte.
- $\omega \approx \omega_m \Rightarrow g(\omega) \to \infty$ (**singularidad de van Hove**, causada por $v_g\to0$ en el borde de zona: muchos valores de $q$ caen en un intervalo $d\omega$ pequeño). [p. 139]

**Comparación red discreta vs. modelo continuo:** para $\omega$ pequeña ambas coinciden; la línea discreta diverge en $\omega_m$ mientras que el modelo continuo (tipo Debye, cortado en $\omega_D$) sigue plano/otra forma más allá. El área bajo ambas curvas debe ser igual a $N$ (número total de modos). [p. 164-165, coherente con lo visto aquí]

## Comparación con una cuerda vibrante de extremos fijos

Número de modos normales de vibración posibles = número de soluciones independientes de la ecuación de onda que satisfacen las condiciones de frontera. [p. 140]

$$u(x,t) = A\sin(k_nx)\sin(\omega t), \qquad k_n = n\frac{\pi}{L}, \qquad \lambda = \frac{2L}{n}$$ [p. 140]

Si la "cuerda" son $N$ átomos discretos separados $a$: $k_{max}=\pi/a \Rightarrow \lambda=2a$. Para $k>k_{max}$ se repite una configuración ya descrita dentro de la 1ª ZB. [p. 141]

Con $a=L/(N-1)$: los modos permitidos son $k=\pi/L,\,2\pi/L,\dots,(N-1)\pi/L \Rightarrow$ existen $(N-1)$ modos aparentes, pero el modo $k=(N-1)\pi/L$ (que da $\lambda=2a$) queda **excluido** porque en él el átomo extremo no vibra (nodo forzado por la condición de frontera fija). [p. 141]

$$\Rightarrow \#\text{modos normales} = N-2 \approx N \quad (\text{para } N\gg1)$$ [p. 141]

## Cadena monoatómica con acoplamiento a segundos vecinos (monoat.2)

> **Nota de origen:** esta sección no proviene del PDF principal — se agrega a partir de un ejercicio de examen viejo (Parcial SS2020 #2, repetido en la imagen "Parcial 1 - 2025-01") que extiende la cadena monoatómica más allá de primeros vecinos. [fuente: examen — Parcial SS2020 #2]

Se añade una segunda constante de fuerza $\alpha_2$ que acopla cada átomo con sus **segundos vecinos** (a distancia $2a$), además de la constante $\alpha_1$ a primeros vecinos:

$$M\ddot u_n = -\alpha_1(2u_n-u_{n+1}-u_{n-1}) - \alpha_2(2u_n-u_{n+2}-u_{n-2})$$

Sustituyendo $u_n=Ae^{i(qna-\omega t)}$ (mismo procedimiento que con solo primeros vecinos, aplicado dos veces):

$$\boxed{M\omega^2 = 2\alpha_1(1-\cos qa) + 2\alpha_2(1-\cos 2qa)}$$

que es la forma $\omega^2=(2\alpha/M)[A(1-\cos qa)+B(1-\cos 2qa)]$ del enunciado, con $A,B$ proporcionales a $\alpha_1,\alpha_2$.

**Velocidad de grupo generalizada:** derivando implícitamente,

$$v_g = \frac{d\omega}{dq} = \frac{a\left[\alpha_1\sin(qa) + 2\alpha_2\sin(2qa)\right]}{M\omega}$$

En $q=\pi/a$, tanto $\sin(qa)$ como $\sin(2qa)$ se anulan y $\omega\neq0$ $\Rightarrow v_g=0$, **igual que en la cadena a solo primeros vecinos** (reflexión de Bragg con $\lambda=2a$, onda estacionaria): el segundo vecino no cambia dónde ocurre esa onda estacionaria, solo cambia la forma de $\omega(q)$ entre los extremos.

En $q=0$ el numerador y $\omega$ se anulan a la vez (límite $0/0$) y $v_g\to v_s$, **no** cero: con $\omega\approx v_sq$, $v_g=d\omega/dq=v_s$, igual que en la cadena de primeros vecinos donde $v_g=v_s|\cos(qa/2)|\to v_s$ [p. 124]. (Corrección 2026-10-01: la versión anterior de esta nota decía que $v_g=0$ en $q=0$, lo cual es incorrecto.)

**Velocidad del sonido (límite $q\to0$):** expandiendo $1-\cos\theta\approx\theta^2/2$ a orden más bajo,

$$M\omega^2 \approx \alpha_1(qa)^2 + 4\alpha_2(qa)^2 = (qa)^2(\alpha_1+4\alpha_2) \;\Rightarrow\; \boxed{v_s = a\sqrt{\frac{\alpha_1+4\alpha_2}{M}}}$$

El segundo vecino contribuye **4 veces más** que uno de primeros vecinos igual de fuerte (por el factor $(2a)^2/a^2=4$ al derivar dos veces respecto a $q$), reflejando que está al doble de distancia.

**Densidad de estados y vector de Debye generalizados:** la definición $g(\omega)\,d\omega=g(q)\,dq=\frac{Na}{2\pi}\frac{dq}{v_g}$ sigue siendo válida con el $v_g(q)$ generalizado de arriba (ya no tiene forma cerrada simple como $N/(\pi\sqrt{\omega_m^2-\omega^2})$, pero se evalúa numéricamente punto a punto). El conteo total de modos en la 1ª zona de Brillouin **no cambia**: sigue siendo exactamente $N$ (un valor de $q$ por átomo, independiente de cuántos vecinos se acoplen), así que el "vector de Debye" de esta cadena 1D — definido igualando $\int_0^{q_D} g(q)\,dq=N$ — coincide, como en el caso de un solo vecino, con el propio borde de zona $q_D=\pi/a$: en 1D, a diferencia de Debye en 3D, el modelo de Debye lineal cortado en $q_D$ reproduce exactamente el número real de modos solo si $q_D$ se toma igual al borde de zona verdadero (la aproximación lineal $\omega=v_sq$ subestima $\omega$ cerca del borde, pero el conteo de modos permitidos por las condiciones de frontera no depende de la forma de $\omega(q)$).

### Puntos clave para dominar este tema (monoat.2)

- Puede derivar $M\omega^2=2\alpha_1(1-\cos qa)+2\alpha_2(1-\cos 2qa)$ para una cadena monoatómica con acoplamiento a primeros y segundos vecinos, identificando la forma $A(1-\cos qa)+B(1-\cos 2qa)$ típica de examen.
- Sabe obtener $v_g=a[\alpha_1\sin qa+2\alpha_2\sin 2qa]/(M\omega)$ y mostrar que sigue anulándose en $q=0$ y $q=\pi/a$ (mismas condiciones de onda estacionaria que con un solo vecino).
- Puede derivar $v_s=a\sqrt{(\alpha_1+4\alpha_2)/M}$ en el límite $q\to0$ y explicar el factor 4 del segundo vecino.
- Entiende que el número total de modos en la 1ª ZB (y por tanto el "vector de Debye" $q_D=\pi/a$ de esta cadena) no depende de cuántos vecinos se incluyan en el acoplamiento — solo la forma de $\omega(q)$ cambia.

### Puntos clave para dominar este tema

- Puede reproducir la derivación completa desde $M\ddot u_n = -\alpha(2u_n-u_{n+1}-u_{n-1})$ hasta $\omega=\omega_m|\sin(qa/2)|$ usando la sustitución $u_n=Ae^{i(qna-\omega t)}$ y las identidades trigonométricas $e^{iy}+e^{-iy}=2\cos y$, $1-\cos\theta=2\sin^2(\theta/2)$.
- Sabe justificar por qué la red actúa como **filtro pasa-bajos mecánico** (solo se transmiten $0<\omega<\omega_m$) y calcular $v_s=\omega_m a/2=a\sqrt{\alpha/M}$ comparando con el límite continuo $\omega=v_sq$.
- Puede derivar $\alpha=aY$ a partir de $v_s^2=Y/\rho$ y $\rho=M/a^3$, y hacer la estimación numérica $\omega_m\sim10^{13}\,\text{s}^{-1}$ para $\alpha\sim10^3$ dinas/cm y $M\sim10^{-24}$ g.
- Puede explicar físicamente por qué $\omega=0$ en $q=0$ (cuerpo rígido, $F=0$) mientras que $v_g\to v_s\neq0$ ahí, y por qué $v_g=0$ en $q=\pi/a$ (onda estacionaria por reflexión de Bragg, $2d\sin\theta=n\lambda$ con $\lambda=2a$), distinguiendo $\omega=0$ en $q=0$ del cero de $v_g$ en el borde de zona.
- Puede derivar la envolvente de dos trenes de onda ($u_1+u_2=2A\cos(kx-\omega t)\cos(\tfrac12 td\omega-\tfrac12 xdk)$) y de ahí obtener $v_g=d\omega/dk$, explicando que la energía viaja con $v_g$ y no con $v_p$.
- Entiende por qué en una red discreta un conjunto de desplazamientos atómicos no determina $\lambda$ de forma única ($q'=q+n\cdot2\pi/a$ da ondas físicamente idénticas), y por qué esto obliga a restringir la representación a la primera zona de Brillouin $-\pi/a<q<\pi/a$.
- Puede derivar la densidad de estados exacta 1D $g(\omega)=\dfrac{N}{\pi\sqrt{\omega_m^2-\omega^2}}$ y explicar el origen físico de la divergencia (singularidad de van Hove) en $\omega=\omega_m$ como consecuencia de $v_g\to0$.
- Sabe contar los modos normales de la cadena finita: $N$ átomos $\Rightarrow$ $N$ valores de $q$ en la 1ª ZB con condiciones periódicas, o $N-2\approx N$ modos con extremos fijos (excluyendo el modo con $\lambda=2a$ donde el átomo extremo no vibra).

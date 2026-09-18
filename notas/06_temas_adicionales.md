# Temas adicionales: anarmonicidad, conductividad térmica y aplicaciones de ondas acústicas

## 1. Anarmonicidad y expansión térmica

### Motivación: por qué los sólidos casi no se expanden en la aproximación armónica

Comparación cualitativa gas ideal vs. sólido ante el mismo ΔT=1 [p. 104]:
- Gas ideal: P=1 atm, T=300K → T=301K produce ΔV/V ~ 1/300.
- Sólido: mismo ΔT=1 produce ΔV/V ~ 1/20.000 (mucho menor).

**Razón física**: en el sólido los átomos están fijados en sus sitios de red por fuerzas interatómicas fuertes (F≫), a diferencia de las partículas libres de un gas. [p. 104]

### El modelo armónico predice expansión térmica nula

Modelo estándar: átomo en su posición de equilibrio conectado a vecinos por resortes (fuerza armónica, F∝-x). [p. 105]

**Resultado clave**: en la aproximación armónica pura, la expansión térmica es **exactamente cero**. [p. 105]

Sin embargo, experimentalmente la expansión térmica de un sólido es pequeña pero **no nula** (≠0). Esto implica que la fuerza interatómica real no es exactamente la de Hooke:

`F_interatómica ≠ F_Hooke ⟹ anarmonicidad` [p. 105]

### Explicación mediante el pozo de potencial asimétrico

Se modela la energía potencial interatómica $U(x)$ de un átomo en un cristal 1D como un pozo de potencial (energía de enlace de tipo iónico), con el eje de equilibrio marcado y con $U(x)$ **asimétrico**: sube más rápido en el lado de compresión (x pequeño) que en el lado de estiramiento (x grande, donde $U(x)\to$ constante = energía total de disociación). [p. 106]

Si un átomo tiene energía cinética $E_k=p_x^2/2m$ y energía total $\varepsilon$, vibra entre los puntos de retorno $A$ y $B$ (con $B>A$ en distancia desde el eje de equilibrio, debido a la asimetría del pozo). A $T=0$, el átomo está en reposo en el fondo del pozo, con distancia de equilibrio $d_{equil.}=a$. [p. 106]

**Caso simétrico (fuerza de Hooke, $U(x)$ parabólico):** los puntos de retorno $A$ y $B$ son equidistantes del punto de equilibrio $O'$. La probabilidad de desplazamiento $+\Delta x$ es igual a la de $-\Delta x$ (por simetría), de modo que la distancia media entre átomos $\bar d = a$ (independiente de la energía/temperatura): $\bar d = f(A, E_{total})$ pero como $A$ y $B$ son simétricos, no hay corrimiento neto. [p. 107]

**Caso real (pozo asimétrico):** $U(x)$ no es parabólico $\Rightarrow$ $A$ y $B$ no son equidistantes del equilibrio. El átomo pasa más tiempo en el lado de $B$ (más alejado, donde $U(x)$ es más plano) que en el lado de $A$: el tiempo de tránsito $O'\to B\to O'$ es mayor que $O'\to A\to O'$. [p. 107] Esto produce una **distancia media entre átomos mayor que $a$**: $\bar d > a$, y como $E_{partícula}\uparrow \Rightarrow \bar d\uparrow$: **la red se expande al aumentar T**. [p. 108]

**Regla general**: si las fuerzas interatómicas reales difieren mucho de las de Hooke, la expansión térmica es mayor. [p. 108]

### Tratamiento cuantitativo

Se expande $U(x)$ alrededor del punto de equilibrio incluyendo términos anarmónicos (cúbico y cuártico):

$$U(x) = \tfrac12\beta x^2 - bx^3 - cx^4 + \dots$$ [p. 108]

El término cúbico ($-bx^3$) es el responsable de la asimetría del pozo y, por tanto, de la expansión térmica neta. Usando la distribución de Maxwell-Boltzmann clásica sobre este potencial, se puede demostrar (ejercicio propuesto en la diapositiva) que el desplazamiento medio térmico es:

$$\langle \Delta x\rangle = \frac{3bk_BT}{\beta^2}$$ [p. 108]

Este resultado muestra explícitamente que $\langle\Delta x\rangle \propto T$ (a primer orden) y que **depende del coeficiente anarmónico $b$** — si $b=0$ (potencial puramente armónico/simétrico), $\langle\Delta x\rangle=0$, consistente con lo discutido arriba.

### Puntos clave para dominar este tema

- Sabe explicar por qué la aproximación armónica pura predice expansión térmica exactamente nula, y por qué esto contradice (parcialmente) el experimento.
- Puede argumentar, a partir de la asimetría del pozo de potencial interatómico $U(x)$, por qué $\bar d > a$ y por qué $\bar d$ aumenta con la temperatura (mayor tiempo relativo pasado en el lado más ancho del pozo).
- Sabe escribir la expansión anarmónica $U(x)=\tfrac12\beta x^2-bx^3-cx^4+\dots$ e identificar que el término cúbico ($b$) es el responsable de la asimetría y por tanto de la expansión térmica neta.
- Conoce el resultado $\langle\Delta x\rangle=3bk_BT/\beta^2$ y sabe que es proporcional a $T$ y al coeficiente anarmónico $b$ (se anula si $b=0$).
- Puede contrastar cuantitativamente gas ideal ($\Delta V/V\sim1/300$ por $\Delta T=1$ a 300K) vs. sólido típico ($\Delta V/V\sim1/20000$), explicando la diferencia por la rigidez de los enlaces en el sólido.

## 2. Conductividad térmica de fonones

### Definición y contexto termodinámico

La conductividad térmica es una **propiedad de estado de no equilibrio térmico** (a diferencia del calor específico, que es de equilibrio). Ejemplo: dos bloques de Cu a $T_1\neq T_2$ puestos en contacto evolucionan hacia el equilibrio a $T_3$. [p. 169]

La función de distribución de equilibrio (Bose-Einstein) **no es aplicable directamente** a estados de no equilibrio; hay que encontrar funciones de distribución válidas para condiciones de no equilibrio. Si la desviación del equilibrio es pequeña, su cálculo es más simple (primera aproximación). [p. 169]

**Segunda aproximación (la usada aquí)**: usar teoría cinética para tratar sistemas con flujo de energía o materia en estado *estacionario*. El calor $Q$ es transportado por agentes independientes: en aislantes, por fonones ($\hbar\omega$, "gas de $\hbar\omega$"); en metales, por electrones y fonones, con la contribución electrónica dominando ($e^->\hbar\omega$). [p. 170]

### Derivación de la ecuación de difusión del calor

Considerando un elemento de volumen entre $x$ y $x+\Delta x$, con flujo de calor definido por la **ley de Fourier**:

$$\frac{\Delta Q}{\Delta t} = -KA\frac{\Delta T}{\Delta x}$$

donde $K$ es la **conductividad térmica**. [p. 171]

Aplicando la 1ª ley de la termodinámica al elemento ($\Delta U_1-\Delta U_2$ = cambio de energía interna en $\Delta t$, con $\Delta V\approx0$ dado que la expansión térmica en sólidos es despreciable):

$$\frac{\Delta U}{\Delta t} = \frac{\Delta U_1}{\Delta t}-\frac{\Delta U_2}{\Delta t} = \frac{\Delta Q_1}{\Delta t}-\frac{\Delta Q_2}{\Delta t}$$ [p. 171]

Con $\Delta U/\Delta V = \Delta u$ (densidad de energía) y expandiendo la diferencia de flujos en serie de Taylor:

$$\frac{\partial u}{\partial t} = K\frac{\partial^2T}{\partial x^2}, \qquad du = C_V\,dT$$

$$\boxed{\frac{\partial T}{\partial t} = \frac{K}{C_V}\frac{\partial^2T}{\partial x^2}}$$ [p. 172]

Esta es la **ecuación de difusión del calor** (distribución de $T$ en un material uniforme con flujo de $Q$). **Importante**: esta ecuación **no es una ecuación de onda** — su solución no tiene la forma $e^{i(kx-\omega t)}$; la dependencia temporal es una exponencial real (decaimiento difusivo, no oscilatorio). [p. 172]

### Modelo de guía de onda acústica (analogía, aunque físicamente incorrecta)

Un intento de modelar la conductividad térmica desde el oscilador armónico: la energía térmica se transporta como ondas de sonido, y el cristal actúa como una "guía de onda acústica" (análogo a una guía de onda electromagnética que transporta microondas a $v=c$, aquí la energía viaja a $v_s$). [p. 173]

**Este modelo NO concuerda con el experimento**: predice una ecuación de onda, pero la evidencia experimental es la ecuación de difusión (sin oscilación). Sin embargo, el modelo de guía de onda acústica (aunque erróneo en su forma literal) **sí sirve** como punto de partida útil para resolver el problema mediante teoría cinética. [p. 173]

### Analogía con teoría cinética de gases: fórmula de conducción térmica

Usando el modelo de Debye ($\omega_m=v_sq$), cada fonón contribuye al flujo de energía cinética: $E_k=\bar\varepsilon_{av}v_x=\bar\varepsilon_{av}v_s\cos\theta$. Si no hay gradiente de $T$, el flujo hacia la derecha se cancela con el flujo hacia la izquierda (transporte neto nulo). Si existe un gradiente $\nabla T$ (con $T_2<T_1$), el flujo neto es no nulo porque la densidad de fonones difiere: $N_p/V|_{T_2} < N_p/V|_{T_1}$. [p. 174]

Los fonones ($\hbar\omega$) viajan en todas las direcciones (todos los $q$ en la zona de Brillouin) $\equiv$ análogo a las moléculas de un gas ordinario $\Rightarrow$ son aplicables los conceptos de **teoría cinética de gases**: [p. 175]

$$\boxed{K = \frac{1}{3}C_V\,v\,\ell}$$

donde $v$ es la velocidad del fonón (típicamente $v_s$) y $\ell$ es el **camino libre medio** del fonón. [p. 175]

La dependencia de $K$ con $T$ entra a través de $C_V(T)$, $\ell(T)$ (determinado por procesos de colisión en el sólido) y $v(T)$. [p. 175]

### Valores experimentales de $K$ y $\ell$

Tabla de conductividad térmica $K$ (watt/m·K) y camino libre medio $\ell$ para varias sustancias, a 273K y a 20K: [p. 176]

| Sustancia | K (273K) | ℓ (Å, 273K) | K (20K) | ℓ (cm, 20K) |
|---|---|---|---|---|
| SiO₂ (cuarzo) | 14 | 97 | 760 | 7.5×10⁻³ |
| CaFe₂ | 11 | 72 | 85 | 1.0×10⁻³ |
| NaCl | 6.4 | 67 | 45 | 2.3×10⁻³ |
| Si | 150 | 430 | 4200 | 4.1×10⁻³ |
| Ge | 70 | 330 | 1300 | 4.5×10⁻³ |

Nótese que $\ell$ crece varios órdenes de magnitud al bajar la temperatura (de Å a fracciones de cm), reflejando la disminución drástica de la dispersión fonón-fonón a T baja.

### Puntos clave para dominar este tema

- Sabe explicar por qué la conductividad térmica es una propiedad de *no equilibrio*, y por qué se aborda con teoría cinética en vez de con la función de distribución de equilibrio.
- Puede derivar la ecuación de difusión del calor $\partial T/\partial t = (K/C_V)\partial^2T/\partial x^2$ a partir de la ley de Fourier y la 1ª ley de la termodinámica, y explicar por qué NO es una ecuación de onda (solución exponencial real, no oscilatoria).
- Entiende por qué el modelo de "guía de onda acústica" para el transporte de calor es físicamente incorrecto (predice ecuación de onda, contradice el experimento), pero resulta útil como paso intermedio hacia el tratamiento cinético correcto.
- Puede escribir de memoria $K=\tfrac13 C_V v\ell$ (fórmula de teoría cinética de gases aplicada al gas de fonones) e identificar qué factores dependen de T ($C_V$, $\ell$, $v$).
- Sabe que $\ell$ (camino libre medio del fonón) aumenta dramáticamente al bajar T (de escala atómica ~100 Å a temperatura ambiente, a fracciones de cm a 20K), reflejando la reducción de la dispersión fonón-fonón.

## 3. Mecanismos de dispersión de fonones

Existen tres mecanismos principales que limitan el camino libre medio $\ell$ de un fonón: [p. 179]

1. **Dispersión fonón-fonón** ($\hbar\omega\to\hbar\omega$): causada por el **acoplamiento anarmónico** entre modos normales. En la aproximación armónica pura, los fonones son modos normales **independientes** (no interactúan entre sí); solo la anarmonicidad permite que un fonón disperse a otro. [p. 179, 180]
2. **Dispersión fonón-imperfección** ($\hbar\omega\to$ impurezas, dislocaciones): las imperfecciones cristalinas destruyen la periodicidad perfecta de la red, dispersando al fonón. A mayor concentración de impurezas o mayor diferencia de masa entre impureza y átomo huésped, mayor dispersión (menor $\ell$). [p. 179, 181]
3. **Dispersión fonón-frontera externa del cristal** (efecto geométrico o de talla).

### Dependencia con la temperatura

- **Dispersión fonón-fonón**: importante a **T alta** (muchos fonones excitados cerca de las fronteras de zona de Brillouin), con $\ell \sim 1/T$. Los procesos responsables de esta dispersión a T alta son específicamente los **procesos Umklapp** (ver más abajo). [p. 180, 186]
- **Dispersión fonón-fonón y fonón-impureza a T<10K**: ambas son **inefectivas** a T muy baja, porque (a) la concentración de fonones excitados es muy pequeña, y (b) los fonones excitados tienen $\lambda$ muy grande ($\gg$ tamaño de la impureza $D$), de modo que la intensidad de dispersión (función de $D/\lambda$) es despreciable cuando $D/\lambda\ll1$. [p. 182]
- **Dispersión por fronteras externas ("efecto geométrico o de talla")**: es el **mecanismo primario de dispersión a T baja**. Cuando $\lambda$ se hace comparable a las dimensiones de la muestra, $\ell\approx D$ (diámetro/tamaño de la muestra), de modo que $\ell$ se vuelve función explícita de la geometría de la muestra (y de T, a través de qué $\lambda$ predomina a cada T). [p. 182, 183]

**Ejemplo experimental (LiF)**: se mide $K(T)$ para barras de distinta sección transversal (7.55×6.97 mm vs. 1.23×0.91 mm). Ambas curvas muestran $K\sim T^3$ a T baja (régimen dominado por el efecto geométrico/de talla) y $K\sim1/T$ a T alta (régimen dominado por dispersión fonón-fonón), con un máximo de $K$ entre ambos regímenes (~25-50K); la barra más delgada tiene menor $K$ máximo (más dispersión geométrica al tener menor $D$). [p. 183]

### Procesos normales vs. procesos Umklapp

Al colisionar dos fonones con vectores de onda $\vec q_1$ y $\vec q_2$ dentro de la primera zona de Brillouin, se conserva la energía y el "cuasi-momento": $\vec q_3 = \vec q_1+\vec q_2$. [p. 184]

**Proceso normal**: si $\vec q_3$ cae **dentro** de la 1ª ZB, entonces el momento (y por tanto el flujo de calor, $\sim v_x$) se conserva exactamente antes y después de la colisión $\Rightarrow$ **este proceso NO afecta la resistividad térmica** ni el flujo de energía neto del sistema fonónico. [p. 184]

**Consecuencia importante**: si solo existieran procesos normales, $\ell\to\infty \Rightarrow \rho_{térmica}=0 \Rightarrow \sigma_{térmica}\to\infty$ (usando $K=\tfrac13 C_V vL$, con $L$ = tamaño de la muestra). Es decir, **los procesos normales por sí solos no pueden explicar la resistividad térmica finita observada**; debe haber otro mecanismo. [p. 185]

**Proceso Umklapp**: si $\vec q_3$ cae **fuera** de la 1ª ZB (es decir, $q_x$ o $q_y > \pi/a$, $\lambda<2a$), entonces hay que sumarle un vector de la red recíproca $\vec G$ para traerlo de vuelta a la 1ª ZB:

$$\vec q_1+\vec q_2 = \vec q_3 + \vec G = \vec q_4, \qquad G=2\pi a^*$$ [p. 185]

El vector resultante $\vec q_4$ (fonón efectivo generado en la colisión) viaja en una dirección **casi opuesta** a $\vec q_1$ y $\vec q_2$, de modo que el flujo de calor antes y después de la colisión son de **sentido opuesto**: el proceso Umklapp "revierte" (reversa) el flujo de energía. [p. 185, 186]

**Interpretación física**: en un proceso Umklapp, el momento extra $\Delta p$ (equivalente a $\hbar G$) es transferido al centro de masa de toda la red cristalina. En promedio, los procesos Umklapp hacen que el flujo neto de energía tienda a $0$ $\Rightarrow$ **restauran el equilibrio térmico** después de una colisión, y son los responsables de que $\ell$ sea finito (y por tanto $K$ finito) a temperaturas altas. Son efectivos quando hay muchos fonones excitados cerca de las fronteras de la zona de Brillouin, es decir, a **T alta**. [p. 186]

### Puntos clave para dominar este tema

- Puede nombrar y distinguir los tres mecanismos de dispersión de fonones (fonón-fonón, fonón-impureza, fonón-frontera) y su rango de temperatura de dominancia.
- Sabe explicar por qué a T<10K los mecanismos fonón-fonón y fonón-impureza son inefectivos (baja concentración de fonones excitados, λ grande comparada con el tamaño de las impurezas), dejando el efecto geométrico/de talla como mecanismo dominante ($\ell\approx D$, diámetro de la muestra).
- Puede interpretar la curva experimental de LiF: $K\sim T^3$ a T baja (efecto geométrico) y $K\sim1/T$ a T alta (dispersión fonón-fonón vía procesos Umklapp), con un máximo intermedio que depende del tamaño de la muestra.
- Puede distinguir un **proceso normal** ($\vec q_1+\vec q_2=\vec q_3$ dentro de la 1ª ZB, no afecta la resistividad térmica) de un **proceso Umklapp** ($\vec q_1+\vec q_2=\vec q_3+\vec G=\vec q_4$, con $\vec q_4$ fuera/regresado por $\vec G$, que sí reversa el flujo de calor).
- Sabe explicar por qué solo procesos normales darían conductividad térmica infinita ($\ell\to\infty$), y por qué son los procesos Umklapp los que dan resistividad térmica finita, siendo más efectivos a T alta (más fonones cerca del borde de zona).

## 4. Aplicaciones de ondas acústicas de alta frecuencia (ultrasonido, microondas)

### Generación de ondas acústicas coherentes en el rango de microondas

Ondas acústicas con $\omega\approx10^{10}\,\text{s}^{-1}$ ($\lambda\sim10^{-5}$cm) están en el rango de **microondas** (también llamadas ondas ultrasónicas); como $\lambda\gg a$, es válida la aproximación de medio continuo. [p. 187]

**Generación mediante transductor piezoeléctrico de cuarzo**: un campo electromagnético (microondas) acopla al cuarzo vía el **efecto piezoeléctrico**. La terminal de la barra de cuarzo oscila, y esa oscilación se propaga como onda elástica en el cuarzo y luego en la muestra en contacto. Parte de la energía electromagnética se convierte en energía elástica. El cuarzo actúa como **transductor** que acopla ondas electromagnéticas con la muestra. [p. 188]

- La eficiencia de conversión **disminuye** al aumentar $\omega$ (típicamente $\sim10^{-4}$). [p. 188]
- Para tener energía elástica apreciable se requiere energía electromagnética pulsada de varios Watts, con pulsos de duración $\sim1\,\mu$s. [p. 188]

**Ventaja de un haz de fonones coherente generado así** (vs. fonones térmicos generados por $\Delta T$): dirección, frecuencia y polarización del haz son **controlables**; en cambio los fonones térmicos se generan en todas direcciones, todas las polarizaciones y un rango amplio de $\omega$, siendo difíciles de controlar. [p. 189]

### Medición de propiedades del sólido con ultrasonido

Mayor $\omega$ del haz $\Rightarrow$ mayor cantidad de información del experimento. Valores típicos: $\omega\sim1$-$16$ GHz. [p. 190]

Cantidades físicas medidas: la velocidad del sonido $v_s$ (midiendo el tiempo de propagación del pulso) y el coeficiente de atenuación (midiendo la amplitud del eco tras reflexión) $\Rightarrow$ ambas dan información sobre la **estructura interna del sólido**. La atenuación aumenta con $\omega$ y con $T$, por lo que suele medirse a temperaturas de helio líquido. [p. 190]

### Aplicaciones tecnológicas

1. **Líneas de atenuación acústicas de microondas.** [p. 191]
2. **Amplificadores/líneas de retardo de atenuación**: se convierte la onda electromagnética (velocidad $c$) en onda acústica (velocidad $v_s$) y de vuelta a electromagnética. Como $v_s/c\sim10^{-5}$, la onda viaja mucho más lenta $\Rightarrow$ se logra un retardo equivalente al de un cable electromagnético mucho más largo. Ejemplo: una muestra acústica de $\ell=5$cm equivale a $L=5$km de cable electromagnético puro. [p. 191]

### Interacción del haz coherente con procesos físicos del sólido

Al propagarse un haz de fonones coherente por el cristal, sufre dispersión por: imperfecciones, fonones térmicos, y electrones (en metales). Midiendo el efecto de esta dispersión sobre el haz, se obtiene información sobre los fonones térmicos y las imperfecciones presentes. [p. 192]

**Interacción entre dos fonones coherentes** (ejemplo experimental en MgO, $\omega_1=16.45$ GHz, $\omega_2=8.5$ GHz, acopladas anarmónicamente): al pulsar a $\omega_1$, aumenta la intensidad de $\omega_2$ $\Rightarrow$ la red de MgO actúa como un **amplificador acústico**. [p. 193]

### Interacción espín-fonón

Con campo magnético $B\neq0$, los niveles de espín de una impureza paramagnética (ej. Mn²⁺ en cuarzo, Cr³⁺ en MgO) se separan en $E_1$, $E_2$ (efecto Zeeman). Si $\hbar\omega=\Delta E$, el fonón es **absorbido** por el sistema de espines, invirtiendo un espín por cada fonón absorbido. [p. 193, 194]

El estudio de la absorción de $\hbar\omega$ da información sobre la estructura energética de las impurezas y la intensidad de su acoplamiento con los fonones. En la situación normal el haz se atenúa; en algunos casos (inversión de población de espines) la muestra puede **amplificar** el haz de fonones. [p. 194]

### Efecto acustoeléctrico en semiconductores piezoeléctricos

Una onda acústica en un semiconductor piezoeléctrico acopla fuertemente a los electrones de conducción (el acople piezoeléctrico es fuerte en estos materiales). [p. 195]

Si la velocidad de arrastre de los electrones $v_{drift}$ es mayor que $v_s$ ($v_s<v_{drift}$), se transfiere energía del haz de electrones a la onda acústica $\Rightarrow$ **la onda se amplifica** (análogo a un tubo de ondas progresivas). Mecanismo microscópico: en un potencial periódico (el de la onda), hay más electrones en el lado descendente ("vientre") del pozo que en la cúspide; estos electrones "deslizan" hacia el fondo, transfiriendo su energía cinética a energía elástica de la onda. [p. 195]

**Aplicaciones**: amplificadores de líneas de atenuación usando CdS o ZnO ($\omega\sim14$ GHz), con amplificación de hasta 100 dB/cm a $\omega\sim1$-$2$ GHz. También se usan **ondas de red superficiales (ondas Rayleigh)** en dispositivos ultrasónicos: si el espesor de la muestra $d\sim\lambda$, la onda se atenúa casi por completo; las ondas superficiales son más fáciles de acoplar a un circuito externo (mediante transductores interdigitales, en una "línea de atenuación de ondas superficiales"). [p. 196]

### Puntos clave para dominar este tema

- Puede describir el mecanismo de generación de un haz de fonones coherente vía un transductor piezoeléctrico de cuarzo excitado por microondas, y explicar por qué la eficiencia de conversión cae al aumentar $\omega$.
- Sabe justificar por qué un haz de fonones coherente y controlable (dirección, ω, polarización) es preferible a los fonones térmicos generados por $\Delta T$ para estudiar procesos físicos del sólido.
- Entiende el principio de una línea de retardo/atenuación acústica: al convertir la señal electromagnética en onda acústica ($v_s/c\sim10^{-5}$), se logra un retardo equivalente a un cable electromagnético miles de veces más largo.
- Puede explicar el mecanismo de interacción espín-fonón (absorción resonante cuando $\hbar\omega=\Delta E_{Zeeman}$, con inversión de espín) y su uso para estudiar impurezas paramagnéticas.
- Puede explicar el efecto acustoeléctrico (amplificación de una onda acústica por un haz de electrones de arrastre cuando $v_{drift}>v_s$ en un semiconductor piezoeléctrico) y nombrar una aplicación (amplificadores CdS/ZnO, líneas de atenuación de ondas superficiales tipo Rayleigh).

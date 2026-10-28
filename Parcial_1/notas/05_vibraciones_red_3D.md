# Vibraciones de átomos en una red tridimensional (sección 1.4)

> Cubre las páginas 154-172 del PDF: generalización de la ecuación de movimiento a 3D, polarización de las ondas, ramas acústicas/ópticas en redes no-Bravais (r átomos/celda), simetría del espacio $q$ en 3D, densidad de estados general $g(\omega)$ para una red 3D real, y la fórmula exacta del calor específico que enmarca a Debye y Einstein como aproximaciones.

## Red 3D monoatómica: ecuación de movimiento y polarización

Red monoatómica con 1 átomo/celda unitaria. Para cada átomo, la ecuación de movimiento (análoga a la 1D pero vectorial):

$$M\frac{d^2\vec u_n}{dt^2} = \alpha(\vec u_{n+1}-\vec u_n)+\alpha(\vec u_{n-1}-\vec u_n) = -\alpha(2\vec u_n-\vec u_{n+1}-\vec u_{n-1})$$

con solución tipo onda:
$$\vec u_n(\vec x) = \vec A\, e^{i(\vec q\cdot\vec r-\omega t)}$$ [p. 154]

- $\vec q$ especifica la longitud de onda $\lambda$ **y** la dirección de propagación.
- $\vec A$ especifica la amplitud **y** la dirección de vibración del átomo $\Rightarrow$ define la **polarización** de la onda (longitudinal o transversal). [p. 154]

### Ecuación secular 3×3

Sustituyendo en la ecuación de movimiento se obtienen **3 ecuaciones simultáneas acopladas** en las componentes $A_x,A_y,A_z$ $\equiv$ una ecuación matricial 3×3. De la ecuación secular (determinante 3×3, **cúbica en $\omega^2$**) se obtienen **3 raíces** $\Rightarrow$ 3 funciones $\omega(\vec q)$ distintas para cada dirección $\vec q$: son las **3 ramas acústicas de la red 3D monoatómica**. Repitiendo para todas las direcciones de $\vec q$ se obtiene el contorno completo de $\omega$. [p. 155]

### Las tres ramas: LA, TA, TA

Las tres ramas difieren en su **polarización**: [p. 156]
- **1 rama longitudinal (LA)**: $\vec A \parallel \vec q$.
- **2 ramas transversales (TA)**: $\vec A \perp \vec q$ (dos direcciones transversales independientes).

En **direcciones de alta simetría** del cristal (ej. $[100]$, $[110]$, $[001]$), las ondas son longitudinales o transversales **puras**. En direcciones **no simétricas**, las ondas tienen carácter mezclado (ni puramente longitudinal ni puramente transversal). [p. 156]

En general $\omega_L > \omega_T$ porque la fuerza de restauración longitudinal es mayor que la transversal ($F_L>F_T$): al desplazar átomos transversalmente, la componente de fuerza que los devuelve al equilibrio es menor que si el desplazamiento fuese a lo largo de la línea de enlace. [p. 156]

**Ejemplo experimental (Al, red FCC)**: curvas de dispersión medidas mostrando ramas LA y TA a lo largo de direcciones $[110]$ y $[100]$, graficadas como $\nu$ (en $10^{13}\text{s}^{-1}$) vs. $q/q_{max}$. Se observa que la rama LA tiene mayor $\omega$ que la(s) TA en todo el rango. [p. 157]

## Generalización a redes no-Bravais (r átomos por celda unitaria)

La polarización y la degeneración de las ramas están relacionadas con la simetría cristalina respecto a la dirección de propagación (formalmente tratado con **teoría de grupos**). [p. 158]

Para una red 3D **no-Bravais** (celda unitaria con más de 1 átomo, es decir $r$ átomos/celda): [p. 158]

$$\exists\; r \text{ átomos/celda} \;\Rightarrow\; \exists\; 3r \text{ curvas de dispersión (ramas)}, \text{ de las cuales:}$$
$$3 \text{ son acústicas}, \qquad 3r-3 \text{ son ópticas}$$

### Justificación matemática

La ecuación de movimiento para cada átomo de la celda da lugar a $r$ ecuaciones **vectoriales** $\equiv 3r$ ecuaciones escalares, o 1 ecuación matricial de orden $3r\times3r$. La ecuación secular resultante tiene **grado $3r$ en $\omega^2$** $\Rightarrow$ existen $3r$ raíces $\Rightarrow$ **$3r$ ramas**: 3 acústicas y $3r-3$ ópticas. [p. 159, 160]

De las $3r-3$ ramas ópticas y las 3 acústicas, en direcciones de simetría se distinguen (análogo al caso diatómico 1D, pero generalizado a 3D): [p. 160]
- Acústicas: $TA_1$, $TA_2$, $LA$
- Ópticas: $LO$, $TO$ (y sus análogos degenerados según la dirección $\vec q$: $[100]$, $[110]$, $[001]$)

**Ejemplo experimental (Ge)**: curvas de dispersión a lo largo de $[111]$ y $[100]$ mostrando las 4 ramas típicas de una red diamante (con base de 2 átomos/celda, $r=2\Rightarrow 3r=6$ ramas, pero por degeneraciones se observan 4 curvas distintas: LO, TO, LA, TA). [p. 160]

### Comparación experimental-teórica

El procedimiento general para comparar teoría y experimento: [p. 161]
1. Asumir $\alpha$ correspondiente a la interacción del átomo con varios vecinos (no solo primeros vecinos).
2. Sustituir en la ecuación de movimiento.
3. Resolver las ecuaciones seculares $\Rightarrow$ obtener $\omega(\vec q)_{teórico}$.
4. Comparar con $\omega(\vec q)_{experimental}$ (medido por dispersión inelástica de rayos X o de neutrones) para **ajustar $\alpha$**.

## Simetría en el espacio $q$ (1ª zona de Brillouin en 3D)

Para la rama $j$-ésima, $\omega=\omega_j(\vec q)$ satisface las propiedades de simetría: [p. 162]
- **Periodicidad**: $\omega_j(\vec q+\vec G) = \omega_j(\vec q)$, donde $\vec G$ es un vector de la red recíproca.
- **Simetría de inversión**: $\omega_j(-\vec q) = \omega_j(\vec q)$.
- $\omega_j(\vec q)$ posee la **simetría rotacional de la red real** (heredada del grupo puntual del cristal).

**Ejemplo (Al, FCC)**: se muestra la forma de la 1ª zona de Brillouin (poliedro característico FCC) junto con un mapa de contornos de $\omega$ constante para la rama LA en el plano $q_x$-$q_y$, con simetría cuadrada visible respecto a los ejes $[100]$/$[010]$. **Importante**: la simetría se aplica a **cada rama individualmente**; no relaciona ramas diferentes entre sí. [p. 163]

## Densidad de estados $g(\omega)$ general para una red 3D real

### Repaso: cálculo para red discreta 1D (comparación)

$$g(\omega)\,d\omega \equiv \#\text{modos en el rango }(\omega,\omega+d\omega)$$

Para la red 1D discreta: $g(\omega)=(L/\pi)/(d\omega/dq)$. Con la línea de dispersión continua ($\omega=v_sq$): $g(\omega)=(L/\pi)/v_s=$cte. Con la línea discreta real ($\omega=\omega_m|\sin(qa/2)|$):
$$g(\omega) = \frac{2L}{\pi a\omega_m}\left|\cos(qa/2)\right|^{-1}$$ [p. 164]

El área bajo la curva discreta hasta $\omega_m$ es igual (por normalización, $A\equiv N$) al área bajo el modelo continuo cortado en $\omega_D$ ($A'\equiv N$); cerca de $\omega_m$, $\omega(q)$ se vuelve plana $\Rightarrow$ existen muchos valores de $q$ en un $d\omega$ pequeño (**singularidad de van Hove**, ya vista en detalle para la cadena monoatómica 1D). [p. 165]

### Método del contorno para redes 3D

Para la rama $j$-ésima, se traza el contorno $\omega_j(\vec q)=\omega$ y el contorno $\omega_j(\vec q+d\vec q)=\omega+d\omega$ en el espacio $\vec q$; **contar el número de modos entre ambas superficies** da $g_j(\omega)\,d\omega$. En principio $g_j(\omega)$ queda determinada una vez conocida $\omega_j(\vec q)$ completa (numéricamente, por conteo geométrico entre superficies de iso-frecuencia). [p. 166]

### Forma general de $g(\omega)$ para un cristal real

Como $\omega_j(\vec q)$ real (con la curvatura real de la red, determinada por $\alpha(\text{cristal})$) no es una simple parábola, la forma de $g_j(\omega)$ tampoco es una simple ley de potencia en todo el rango: cerca del origen ($q$ pequeño) $g_j(\omega)\sim\omega^2$ (comportamiento tipo Debye, modos acústicos), pero a $\omega$ mayor aparecen picos y hombros característicos de cada material, seguidos de una caída abrupta en $\omega\to\pi/a$ (borde de zona). [p. 167]

La densidad de estados **total** es la suma sobre todas las ramas:
$$g(\omega)_{total} = \sum_j g_j(\omega)$$ [p. 167]

**Ejemplo experimental (Cu)**: $g(\omega)$ medida muestra una forma tipo $\omega^2$ a bajo $\omega$ (como predice Debye), con **picos y valles** debidos a la interferencia/superposición de varias ramas, y una caída abrupta cerca de $\omega\approx4.5\times10^{13}$rad/s. Se compara con la línea punteada del modelo de Debye ($g(\omega)\propto\omega^2$ hasta $\omega_D$), mostrando que el modelo de Debye es solo una aproximación suave que ignora la estructura fina real. [p. 167]

## Teoría exacta del calor específico: síntesis Debye + Einstein

La **aproximación de Debye** ($g(\omega)\propto\omega^2$, válida en el límite de longitud de onda larga) es una buena aproximación **solo cerca del centro de la zona de Brillouin** (modos acústicos de $q$ pequeño). Para los **modos ópticos**, donde $\omega\not\approx f(q)$ (las ramas ópticas son casi planas, $\omega\approx$ cte.), es más apropiado el **modelo de Einstein**. [p. 168]

La teoría **exacta** simplemente usa la $g(\omega)$ real del cristal (suma de todas las ramas, como la medida para Cu arriba) en las fórmulas generales ya vistas:

$$E = \int \bar\varepsilon(\omega)\,g(\omega)\,d\omega, \qquad \bar\varepsilon(\omega) = \frac{\hbar\omega}{e^{\hbar\omega/k_BT}-1}$$

$$\boxed{C_V = k_B\int\left(\frac{\hbar\omega}{k_BT}\right)^2 e^{\hbar\omega/k_BT}\left(e^{\hbar\omega/k_BT}-1\right)^{-2}g(\omega)\,d\omega}$$ [p. 168]

Es decir: **Debye y Einstein son dos límites/aproximaciones distintas de esta misma fórmula exacta**, cada una válida en una región distinta del espectro de $g(\omega)$ (Debye para la parte acústica de baja $\omega$, Einstein para las bandas ópticas casi planas).

### Puntos clave para dominar este tema

- Puede escribir la ecuación de movimiento vectorial de la red 3D monoatómica y explicar por qué el vector $\vec A$ de la solución de onda define la **polarización** (longitudinal/transversal) mientras que $\vec q$ define $\lambda$ y la dirección de propagación.
- Sabe que la ecuación secular de una red monoatómica 3D es cúbica en $\omega^2$ (matriz 3×3) y da lugar a **3 ramas acústicas** (1 LA + 2 TA), puras en direcciones de alta simetría y de carácter mezclado en direcciones no simétricas.
- Puede generalizar a redes no-Bravais con $r$ átomos/celda: ecuación secular de grado $3r$ en $\omega^2$ (matriz $3r\times3r$) $\Rightarrow$ $3r$ ramas totales = **3 acústicas + $(3r-3)$ ópticas**, y aplicarlo a un ejemplo como Ge ($r=2$).
- Conoce las propiedades de simetría de $\omega_j(\vec q)$ en 3D: periodicidad $\omega_j(\vec q+\vec G)=\omega_j(\vec q)$, inversión $\omega_j(-\vec q)=\omega_j(\vec q)$, simetría rotacional heredada de la red real — y sabe que estas simetrías aplican a **cada rama por separado**, no relacionan ramas distintas entre sí.
- Puede describir el método de conteo por contorno de iso-frecuencia en el espacio $\vec q$ para calcular $g_j(\omega)$ de una rama real en 3D, y explicar por qué $g(\omega)_{total}=\sum_j g_j(\omega)$ presenta picos/hombros (a diferencia de la forma suave $\propto\omega^2$ de Debye).
- Entiende que la fórmula exacta $C_V=k_B\int(\hbar\omega/k_BT)^2e^{\hbar\omega/k_BT}(e^{\hbar\omega/k_BT}-1)^{-2}g(\omega)d\omega$ contiene a Debye y Einstein como aproximaciones válidas en regiones distintas de $g(\omega)$: Debye cerca del centro de zona (acústicos), Einstein para bandas ópticas planas.

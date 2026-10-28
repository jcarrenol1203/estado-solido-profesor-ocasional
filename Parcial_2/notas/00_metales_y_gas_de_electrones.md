# Metales y gas de electrones libres (bloque 0)

> **Nota de origen:** cubre las páginas 1-23 de `Diapositivas/Metales 2021.pdf` (109 págs., O. Morán, "Lecture 2025"). Las diapositivas son esquemáticas; las ecuaciones se reconstruyeron del texto extraído y de las figuras. Los números de página `[p. N]` son los de la diapositiva.

## 1. Metales, cristal metálico y concentración de electrones (`metal.1`)

**Propiedades físicas comunes:** dureza alta, conductividad térmica $K$ alta, densidad alta, reflectividad óptica alta. [p. 3]

**Cristal metálico:** pozos de potencial $U$ (los iones) dentro de los cuales un **gas de electrones libres** está confinado (el "fluido sutil" de los metales). El descubrimiento del electrón por Thomson dio base firme al modelo. [p. 4]

**Historia del modelo:** [p. 4-5]
- Teoría de **Drude-Lorentz (1909)**: primera teoría cuantitativa de propiedades eléctricas de metales (gas clásico).
- **Mecánica cuántica + estadística de Fermi-Dirac** (principio de Pauli): modelo apropiado para metales.
- Imagen más simple del electrón libre: no considera la distribución de energía térmica ni las colisiones. Los efectos de las colisiones llevan a la distribución de equilibrio de $E$ (a través del camino libre medio $\ell$); la distribución para sistemas fuera de equilibrio incorpora la estadística de Fermi-Dirac y el principio de Pauli.

**Metales alcalinos (Li, Na, K, Rb, Cs):** [p. 6-8]
- Átomo libre de Na: $1s^2 2s^2 2p^6 3s^1$ → núcleo + 10 e⁻ de *core* (capas llenas, estables) + 1 e⁻ de valencia en el estado 3s (radio $r\sim 1.9$ Å).
- En el metal, el e⁻ 3s se **deslocaliza** por el solapamiento de orbitales 3s de átomos vecinos: se vuelve electrón de conducción (banda de conducción 3s). El Na metálico es **bcc**, $a=4.2$ Å, vecinos más próximos a 3.7 Å.
- Radio del ion libre Na⁺ = 0.98 Å (volumen ~3.9 Å³): los iones ocupan solo ~15 % del volumen del cristal; el resto es "mar" de electrones.

**Metales nobles (Cu, Ag, Au):** iones más grandes, vecinos más próximos a 1.83 Å → los iones pueden entrar casi en "contacto". A 300 K: alcalinos → **bcc**; nobles → **fcc**. [p. 9-10]

**Cuántos electrones de conducción hay:** se conoce la valencia y el número de átomos por unidad de volumen. [p. 10]
- Monovalentes: Na, K, Cu, Ag, Au (1 e⁻ por átomo). Divalentes: Be, Mg, Zn, Ca (2 e⁻ por átomo).
- Concentración de átomos: $\rho/M$ por $N_A$, es decir

$$N = \frac{Z_v N_A\,\rho}{M}\ \ [\text{átomos/cm}^3],\qquad Z_v=\text{valencia},\ M=\text{peso atómico},\ \rho=\text{densidad}$$

Ejemplo (Na bcc, 2 átomos/celda): $N/V=2/(4.2\text{ Å})^3=3\times10^{22}$ cm⁻³. [p. 67]

**Éxitos y fracasos de la teoría clásica:** [p. 11-12]
- Éxitos: (1) derivación de la **ley de Ohm**; (2) relación entre conductividad eléctrica y térmica (Wiedemann-Franz).
- Fracaso (1): el **calor específico electrónico** $C_{V,e}$ (falla la distribución de Maxwell, no el modelo del e⁻ libre).
- Fracaso (2): los e⁻ de conducción pueden viajar en línea recta, libres, sobre **varias distancias atómicas** (a $T$ baja, en muestras puras, hasta $10^8$ distancias interatómicas ≈ 1 cm).

**¿Por qué la materia condensada es "transparente" a los electrones de conducción?** [p. 12]
1. Los e⁻ no son desviados por los iones de un potencial $U$ **periódico**: las ondas de materia se propagan sin obstrucción en una estructura periódica.
2. Solo son dispersados ocasionalmente por otros e⁻, y esto está limitado por el **principio de exclusión de Pauli**.

**Gas de Fermi de electrones libres** = gas de electrones libres que obedecen el principio de exclusión de Pauli. [p. 13]

### Puntos clave para dominar este tema
- Describir el cristal metálico como pozos $U$ con un gas de e⁻ libres confinados, y por qué el modelo de e⁻ libre sirve aun sabiendo que los iones están ahí.
- Explicar cómo el e⁻ de valencia del átomo (ej. 3s del Na) pasa a e⁻ de conducción; dar el volumen que ocupan los iones (~15 %).
- Calcular $N=Z_v N_A\rho/M$ y distinguir monovalentes de divalentes.
- Enumerar éxitos (ley de Ohm, Wiedemann-Franz) y fracasos (calor específico electrónico, camino libre largo) de la teoría clásica.
- Dar las **dos razones** de la "transparencia" cristalina (periodicidad → ondas de materia no se dispersan; Pauli limita la dispersión e⁻-e⁻).

---

## 2. Gas de Fermi en 1D: niveles de energía y $E_F$ (`gas1d.1`)

Electrón de masa $m$ confinado a una distancia $L$ por potenciales infinitamente altos ($U=0$ dentro). [p. 13-14]

$$H\psi_n=-\frac{\hbar^2}{2m}\frac{d^2\psi_n}{dx^2}=\varepsilon_n\psi_n,\qquad \psi_n(0)=\psi_n(L)=0$$

**Estado cuántico exacto vs. aproximado:** el nivel $\psi_n$ es solución de la ecuación de onda de **un solo** electrón; un estado cuántico aproximado de $N$ e⁻ se construye asignando a los $N$ e⁻ $N$ niveles distintos. El modelo es **exacto solo si no hay interacción** entre partículas. [p. 14]

Soluciones (ondas estacionarias): [p. 15-16]

$$\psi_n(x)=A\sin\!\left(\frac{n\pi}{L}x\right),\qquad \lambda_n=\frac{2L}{n},\qquad
\varepsilon_n=\frac{\hbar^2k_n^2}{2m}=\frac{\hbar^2}{2m}\left(\frac{n\pi}{L}\right)^2=\frac{h^2}{8mL^2}\,n^2$$

($n=1$: $\lambda=2L$; $n=2$: $\lambda=L$; $n=3$: $\lambda=\frac23L$; la energía crece como $n^2$: relación 1 : 4 : 9.) **La cuantización viene de las condiciones de frontera** (confinamiento), no es un postulado extra. [p. 15-16]

**Principio de exclusión de Pauli:** dos e⁻ no pueden coincidir en todos los números cuánticos. En 1D los números cuánticos son $n$ y $m_s=\pm\frac12$ → **cada nivel $n$ aloja 2 e⁻**. Estado fundamental con $N=6$ e⁻: ocupados $n=1,2,3$ (dos e⁻ cada uno). [p. 17]

- Varios niveles pueden tener la misma $\varepsilon$: el número de niveles con esa $\varepsilon$ es el **grado de degeneración**. [p. 18]
- Nivel ocupado más alto $=n_F$; con $N$ par la condición es $2n_F=N$. [p. 18]

**Energía de Fermi (1D):** energía del nivel ocupado más alto del estado fundamental de $N$ electrones: [p. 18]

$$\varepsilon_F=\frac{\hbar^2}{2m}\left(\frac{n_F\pi}{L}\right)^2=\frac{\hbar^2}{2m}\left(\frac{N\pi}{2L}\right)^2$$

### Puntos clave para dominar este tema
- Escribir $\varepsilon_n=\hbar^2\pi^2n^2/(2mL^2)$ y mostrar que sale de $\psi(0)=\psi(L)=0$ (la cuantización no es una suposición).
- Distinguir estado exacto de $N$ partículas vs. estado aproximado hecho con niveles de una partícula (exacto solo sin interacción).
- Aplicar Pauli: 2 e⁻ por nivel $n$ ($m_s=\pm\frac12$); condición $2n_F=N$.
- Calcular $\varepsilon_F$ en 1D y construir el estado fundamental de $N$ e⁻.

---

## 3. Interacciones y por qué el gas de e⁻ libres funciona (`interac.1`)

**Modelo:** e⁻ se mueven sin colisiones salvo la reflexión en la superficie; el potencial $U$ solo los **confina** dentro del cristal. Analogía: moléculas de gas ideal. [p. 19]

**¿Por qué es razonable ignorar la interacción e⁻-ion?** [p. 20]
- La interacción Coulomb ion-e⁻ se **apantalla** (corto alcance); el potencial neto es un **seudopotencial débil** (muy débil en alcalinos). 
- Argumento alternativo: por incertidumbre $\Delta x\Delta p\sim\hbar$, $mv^2\sim\hbar^2/(2m\,\Delta x^2)$; la probabilidad de estar muy cerca de un ion es pequeña (para $r\gg$ radio del ion la interacción es débil).

**¿Por qué es débil la interacción e⁻-e⁻?** [p. 21-22]
1. **Principio de exclusión de Pauli** (e⁻ del mismo espín se mantienen separados: "hueco de Fermi", deficiencia de e⁻ alrededor de cada e⁻).
2. **Principio de energía mínima**: si la separación $d$ fuese muy pequeña ($d\ll\lambda$) la energía de Coulomb sería muy alta; el sistema minimiza $E$ separando los e⁻.
- Resultado: cada e⁻ queda acompañado de su "hueco" (carga positiva efectiva) → **apantallamiento**: el conjunto e⁻ + hueco se comporta como un objeto de interacción débil con los otros. Tamaño del hueco $r\sim 1$ Å, valor exacto $f$(concentración de e⁻).

**¿Es un gas de e⁻ igual a un gas ordinario?** [p. 23]
| | gas de e⁻ en un metal | gas ordinario |
|---|---|---|
| concentración | $N\sim10^{29}$ e⁻/m³ | $N\sim10^{25}$ moléculas/m³ |
| carga | $q=-1.6\times10^{-19}$ C → **plasma denso** | $q=0$ → gas neutro |
| estadística | Fermi-Dirac (Pauli) | Maxwell-Boltzmann |

### Puntos clave para dominar este tema
- Argumentar por qué la interacción e⁻-ion (seudopotencial débil, apantallamiento) y e⁻-e⁻ (Pauli + energía mínima → hueco de Fermi) es débil.
- Enunciar analogías y diferencias entre el gas de e⁻ y un gas ordinario (aire): densidad ~$10^4$ veces mayor, carga/plasma, FD vs. MB, energía a $T=0$ ≠ 0. (Pregunta recurrente de parcial: `P-2025-01 #4c`, `P-2025-2S #4a`.)

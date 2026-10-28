# Calor específico electrónico y estadística de Fermi-Dirac (bloque 2)

> **Nota de origen:** cubre las páginas 51-61 y el suplemento 106-109 de `Diapositivas/Metales 2021.pdf`. El cálculo de $U(T)$ de las págs. 106-109 es el "Anhang zu die Wärmekapazität des Elektronengases".

## 7. Calor específico electrónico: el fracaso clásico (`cal.1`)

Modelo Drude-Lorentz: los e⁻ son partículas libres en equilibrio que cumplen leyes clásicas (mecánica, magnetismo, estadística). Teoría cinética de gases: [p. 51-52]

$$E=\tfrac32k_BT\ \text{por e}^-,\qquad E_{mol}=\tfrac32N_Ak_BT=\tfrac32RT\ \Rightarrow\ C_{e}=\tfrac32R\approx3\ \text{cal/mol·K}$$

Predicción total a $T$ alta: $C=C_{red}+C_e=3R+\tfrac32R=4.5R\approx9$ cal/mol·K. [p. 53]

**Experimento:** $C_{total}\approx3R\approx6$ cal/mol·K (igual que un aislante). Mediciones exactas: $C_e\ll\tfrac32R$, de hecho $C_e\sim10^{-2}\cdot\tfrac32R$. La contribución electrónica prácticamente **no aparece** a temperatura ambiente → el gas de e⁻ **no** se comporta como gas clásico (falla Maxwell-Boltzmann, no el modelo del e⁻ libre). [p. 53]

### Puntos clave para dominar este tema
- Calcular el valor clásico $C_e=\tfrac32R$ y $C_{total}=4.5R$, y compararlo con el experimental ($\approx3R$, $C_e\sim10^{-2}$ del clásico).
- Explicar que lo que falla es la estadística (MB), no la idea de e⁻ libres.

---

## 8. Distribución de Fermi-Dirac, $T_F$ y $C_e=\gamma T$ (`cal.2`)

**Estado fundamental ($T=0$):** los $N$ e⁻ llenan los niveles de menor energía hasta $E_F\sim5$ eV (Pauli). Ocupación: [p. 53-56]

$$f(E)\big|_{T=0}=\begin{cases}1&E<E_F\\0&E>E_F\end{cases}$$

**$T>0$:** la energía térmica **no se reparte igual** entre todos los e⁻. Tratamiento clásico (cada e⁻ absorbe $\tfrac32k_BT$) es falso: e⁻ con $E\ll E_F$ **no pueden absorber** energía (los niveles vecinos están llenos, Pauli). La energía térmica por e⁻ es $k_BT\approx25$ meV $\ll E_F$ a 300 K; solo los e⁻ próximos a $E_F$ se excitan. [p. 54-55]

**Distribución de Fermi-Dirac** (probabilidad de ocupación de un orbital de energía $E$ en equilibrio térmico): [p. 55-56]

$$f(E)=\frac{1}{e^{(E-\mu)/k_BT}+1}$$

**Estimación del calor específico:** [p. 57-58]
- Solo los e⁻ dentro de $\sim k_BT$ de $E_F$ se excitan: fracción $\sim k_BT/E_F$ → número excitado por mol $\approx N_Ak_BT/E_F$.
- Cada uno absorbe $\sim k_BT$: energía térmica por mol $\bar E\approx N_A(k_BT)^2/E_F$.
- $C_e=\partial\bar E/\partial T\approx 2Rk_B T/E_F$.

Resultado (con $E_F=k_BT_F$): [p. 58-59]

$$C_e\approx2R\frac{T}{T_F}\qquad\left(\text{cálculo exacto: } C_e=\frac{\pi^2}{2}R\frac{k_BT}{E_F}=\frac{\pi^2}{2}R\frac{T}{T_F}\right)$$

- $T_F=E_F/k_B$: para $E_F=5$ eV, $T_F\approx50\,000$ K ($1\ \text{eV}\approx1.16\times10^4$ K).
- Factor de reducción respecto al clásico $\sim k_BT/E_F\sim5\times10^{-3}=1/200$ a 300 K. $C_e$ igualaría al clásico solo en $T=T_F$.
- $C_e\propto T$. Calor específico de la red: constante ($T\gg\theta_D$), $\propto T^3$ ($T\ll\theta_D$).
- Experimentalmente, a $T\ll\theta_D$, $T_F$: $C=C_{el}+C_{ph}=\gamma T+\beta T^3$ → $C/T=\gamma+\beta T^2$; a $T$ muy baja domina el término electrónico lineal. [p. 59]

**Potencial químico $\mu(T)$:** generalización de $E_F$. $\mu=\mu(T)$ se fija pidiendo que el número total de partículas sea $N$. [p. 60-61]
- A $T=0$: $\mu=E_F$ (porque $f$ cae de 1 a 0 en $E_F$). A $T>0$: $f(E=\mu)=\tfrac12$.
- Cola de la distribución ($E-\mu\gg k_BT$): $f(E)\approx e^{\mu/k_BT}e^{-E/k_BT}=C\,e^{-E/k_BT}$ → distribución de **Maxwell-Boltzmann**. [p. 61]

### Puntos clave para dominar este tema
- Explicar por qué solo los e⁻ cercanos a $E_F$ (dentro de $k_BT$) absorben energía (Pauli).
- Escribir $f(E)$, mostrar $f(\mu)=1/2$, $\mu(T{=}0)=E_F$, y el límite MB en la cola.
- Reconstruir $C_e\approx2R\,T/T_F$ (exacto $\tfrac{\pi^2}{2}R\,T/T_F$), calcular $T_F=E_F/k_B$ y la fracción excitada $\sim T/T_F$ (para Cu: 0.0037; Na: 0.008).
- Dar $C=\gamma T+\beta T^3$ y decir cuál domina a $T\ll\theta_D$.
- Comparar numéricamente $C_{el}$ vs. $C_{red}$ a 300 K y hallar la $T$ donde son del mismo orden (`T-2025-II #8`: con $T_F=5\text{ eV}/k_B$, $\theta_D=300$ K: $C_{red}=\tfrac{12\pi^4}{5}R(T/\theta_D)^3$ y $C_{el}=\tfrac{\pi^2}{2}R\,T/T_F$ → iguales a $T\approx3$ K).
- Anchura de $f(E)$: pasar de 90 % a 10 % ocupa $\Delta E=2\ln9\,k_BT\approx4.4\,k_BT$ (`T-2025-II #1`).

---

## 9. Energía interna del gas de Fermi: derivación de $U(T)$ (`cal.3`)

Con $D(\varepsilon)$ densidad de orbitales y $f(\varepsilon,T)$: $D(\varepsilon)f$ es la densidad de orbitales llenos. Incremento de energía: [p. 70-71, 106]

$$U=\int_0^\infty\varepsilon D f\,d\varepsilon-\int_0^{E_F}\varepsilon D\,d\varepsilon\quad(*)$$

Se usa que $N=\int_0^\infty D f\,d\varepsilon=\int_0^{E_F}D\,d\varepsilon$, de donde $E_F\!\left[\int_0^\infty Df\,d\varepsilon-\int_0^{E_F}D\,d\varepsilon\right]=0$ (**). Sumando (**) a (*) y separando integrales en $E_F$: [p. 106-108]

$$U=\underbrace{\int_{E_F}^\infty(\varepsilon-E_F)D f\,d\varepsilon}_{(1)}+\underbrace{\int_0^{E_F}(E_F-\varepsilon)[1-f]D\,d\varepsilon}_{(2)}$$

- (1): energía para excitar e⁻ del nivel de Fermi a niveles más altos.
- (2): energía para excitar e⁻ desde niveles debajo de $E_F$ hacia arriba (cada e⁻ que sale de un orbital deja un "hueco").
- $D f\,d\varepsilon$ = número de e⁻ excitados en $d\varepsilon$; $[1-f]$ = probabilidad de que un orbital con energía $\varepsilon$ esté vacío. [p. 109]
- Resultado: $U/(NE_F)$ crece con $k_BT/E_F$ (curva de la figura, de 0 a 1). [p. 71]

### Puntos clave para dominar este tema
- Reproducir el truco de sumar la identidad de conservación del número ($N$ fijo) para obtener $U=\int(\varepsilon-E_F)Df+\int(E_F-\varepsilon)(1-f)D$ (electrones excitados + huecos).
- Interpretar cada integral.

# Transporte de e⁻ en metales: conductividades, ciclotrón y Hall (bloque 4)

> **Nota de origen:** cubre las páginas 74-91 de `Diapositivas/Metales 2021.pdf`.

## 13. Conductividad eléctrica en el modelo cuántico (`trans.1`)

Para un e⁻ libre $m\mathbf v=\hbar\mathbf k$. Con $\mathbf E$ y $\mathbf B$: [p. 74]

$$\mathbf F=m\frac{d\mathbf v}{dt}=\hbar\frac{d\mathbf k}{dt}=-e(\mathbf E+\mathbf v\times\mathbf B)$$

Con $\mathbf B=0$: $\mathbf k(t)-\mathbf k(0)=-e\mathbf Et/\hbar$. Si en $t=0$ se aplica $E$, **toda la esfera de Fermi se desplaza** en $\delta\mathbf k=-e\mathbf Et/\hbar$ (el $\mathbf k$ de cada nivel aumenta en $\mathbf Ft/\hbar$); el impulso total es $N\hbar\delta\mathbf k$ y la energía del sistema aumenta en $N(\hbar\delta k)^2/2m$. [p. 74-75]

La dispersión de e⁻ con impurezas, defectos y fonones **mantiene** un **estado estacionario** con la esfera desplazada una cantidad fija: [p. 75-76]

$$\delta\mathbf k=-\frac{e\mathbf E\tau}{\hbar},\qquad \mathbf v_d=\frac{\hbar\delta\mathbf k}{m^*}=-\frac{e\tau}{m^*}\mathbf E$$

Los e⁻ **no compensados** (aquellos en el borde de la esfera sin pareja de $-\mathbf k$) producen $I\neq0$; $v_d\ll v_F$ (desplazamiento muy pequeño). [p. 76]

**Estimación de $J$:** la fracción de e⁻ no compensados es $\sim v_d/v_F$, es decir $N(v_d/v_F)$ e⁻, cada uno con velocidad $v_F$: [p. 77]

$$\mathbf J=-eN\frac{v_d}{v_F}v_F=-Ne\,v_d\ \Rightarrow\ \sigma=\frac{Ne^2\tau_F}{m^*},\qquad \tau_F=\frac{\ell_F}{v_F}\Rightarrow\sigma=\frac{Ne^2\ell_F}{m^*v_F}$$

**Comparación clásico vs. cuántico:** [p. 78]
- Clásico: *todos* los e⁻ se mueven con $v_d$ (pequeña).
- Cuántico: *pocos* e⁻ (los cercanos a la SF) se mueven con $v\sim v_F$ (grande).
- Las dos aproximaciones dan el **mismo** $\sigma$, pero la cuántica es conceptualmente más precisa, con $\tau=\tau_F$ y $\ell_F$ evaluada **en la SF**. A 300 K, $\ell_F\sim100$ Å; $\ell_F\propto1/T$ → $\rho\propto T$ ($T\gg\theta$).

**Relevancia de la SF:** el transporte de e⁻ depende de las propiedades y de la **forma de la SF**; los e⁻ internos son irrelevantes. [p. 79]

### Puntos clave para dominar este tema
- Explicar el desplazamiento rígido de la esfera de Fermi: $\delta\mathbf k=-e\mathbf E\tau/\hbar$ y por qué $\mathbf B=0$ da $\mathbf k(t)=\mathbf k(0)-e\mathbf Et/\hbar$.
- Mostrar que $J=-Nev_d$ y $\sigma=Ne^2\tau_F/m^*$ (idéntico formalmente al de Drude, pero solo los e⁻ de la SF participan, con $v_F$ y $\ell_F$).
- Contrastar la imagen clásica ("todos derivan despacio") con la cuántica ("pocos van rápido").
- Calcular $v_d/v_F$ para un alambre (Cu, 2 mm², 20 A: $v_d\approx7\times10^{-4}$ m/s, $v_d/v_F\approx5\times10^{-10}$, `T-2025-II #6`).

---

## 14. Conductividad térmica y ley de Wiedemann-Franz (`trans.2`)

Experimento: $J_Q=-K\,dT/dx$. En metales $K=K_e+K_{ph}$, con $K_{ph}\sim10^{-2}K_e$ (los e⁻ dominan). Los e⁻ del lado caliente ($T_2>T_1$) llevan más energía que los del frío, mientras la corriente de partículas neta es cero ($J_{neta}=0$). [p. 80]

**Evaluación de $K$** (teoría cinética): [p. 81-82]

$$K=\tfrac13C_Vv\ell,\qquad C_V=\frac{\pi^2}{2}\frac{Nk_B\,k_BT}{E_F}\ (\text{por volumen}),\ v\to v_F,\ \ell\to\ell_F,\ E_F=\tfrac12m^*v_F^2,\ \tau_F=\ell_F/v_F$$

$$K=\frac{\pi^2}{3}\frac{Nk_B^2T\,\tau_F}{m^*}$$

Valor típico: $K\sim50$ cal/(m·K·s). Con $\sigma=Ne^2\tau_F/m^*$:

$$\boxed{\frac K\sigma=\frac{\pi^2}{3}\left(\frac{k_B}{e}\right)^2T=L\,T}\quad(\text{ley de Wiedemann-Franz})$$

$L=\frac{\pi^2}3(k_B/e)^2$ = **número de Lorenz** ($L\approx5.8\times10^{-9}$ cal/s·K² en la versión de la diapositiva; $2.44\times10^{-8}$ W·Ω/K² en SI). [p. 82]

**Tabla** (K en cal/m·K·s, L en $10^{-9}$ cal/s·K²): Na 33 / 5.8; Cu 94 / 5.4; Ag 100 / 5.6; Au 71 / 5.9; Al 50 / 4.7; Cd 24 / 6.3; Ni 14 / 3.7; Fe 16 / 5.5. [p. 82]

**Discrepancias en $L$:** (1) modelo simplificado (e⁻ libres); (2) tratamiento simplificado para calcular $\tau$ en $K$ y en $\sigma$ (los $\tau$ no son idénticos en ambos procesos). Un tratamiento refinado da $L=L(\text{metal})$. [p. 83]

**Por qué un material con conductividad térmica alta puede tener $\sigma\approx0$ (ej. alúmina):** W-F aplica a conducción **electrónica**; en un aislante el calor lo llevan los **fonones** ($K_{ph}$), que no transportan carga, así que $K/\sigma$ no está dado por $LT$ (`P-2025-01 #4d`).

### Puntos clave para dominar este tema
- Deducir $K=\tfrac13C_Vv_F\ell_F$ con $C_V=\tfrac{\pi^2}{2}Nk_B(k_BT/E_F)$ y llegar a $K/\sigma=LT$ con $L=\tfrac{\pi^2}{3}(k_B/e)^2$.
- Decir por qué en metales $K_{ph}\ll K_e$.
- Explicar por qué W-F no vale para aislantes (alta $K$ de fonones, $\sigma\approx0$) y por qué $L$ varía entre metales.

---

## 15. Resonancia ciclotrónica (`trans.3`)

Electrón en $\mathbf B$ ($\mathbf E=0$): $F=-e(\mathbf v\times\mathbf B)=m_ac=mv^2/r$ → órbita circular con frecuencia angular **ciclotrónica** [p. 84]

$$\omega_c=\frac{eB}{m^*},\qquad \nu_c=\frac{\omega_c}{2\pi}\approx2.8\,B\ \text{GHz}\ (B\text{ en kG},\ m^*\approx m_e)$$

Para $B=1$ kG: $\nu_c=2.8$ GHz (microondas). [p. 84-85]

**Resonancia:** si una onda e.m. de frecuencia $\omega$ incide, los e⁻ absorben energía durante todo el ciclo cuando $\omega=\omega_c$ (se mueven sincronizados con la onda); si $\omega\neq\omega_c$ absorben durante parte del ciclo y en el resto, fuera de fase, **devuelven** la energía a la onda. El coeficiente de absorción $\alpha(\omega)$ tiene un máximo en $\omega_c$. [p. 85-86]

**Condición experimental:** pico bien definido solo si $\omega_c\tau\gg1$ (el e⁻ completa varios ciclos entre colisiones). Si $\omega_c\tau\lesssim1$ la curva es muy ancha y $\omega_c$ no es distinguible. Se logra con $B\sim5$ T y $T\sim5$ K (aumenta $\tau$ y $\omega_c$). [p. 87]

**Uso:** medir $m^*$ en metales y semiconductores: $\omega_c=eB/m^*$, precisión de $m^*$ = f(precisión de $\omega_c$ y $B$). [p. 87]

**Problema típico** (`T-2025-II #4`): "para que el e⁻ describa al menos una órbita completa" → $\omega_c\tau\gtrsim1$ (o $2\pi$ según el criterio): $B\gtrsim m/(e\tau)\approx1.9\times10^{-2}$ T para $\tau=3\times10^{-10}$ s (≈ 0.12 T si se exige $\omega_c\tau=2\pi$).

### Puntos clave para dominar este tema
- Deducir $\omega_c=eB/m^*$ de $F=-e\mathbf v\times\mathbf B$ y calcular $\nu_c$ para un $B$ dado.
- Explicar la absorción resonante (fase con la onda) y la condición $\omega_c\tau\gg1$ (alta $B$, baja $T$, muestra pura).
- Saber para qué sirve (medir $m^*$) y calcular el $B$ mínimo para una órbita completa.

---

## 16. Efecto Hall (`trans.4`)

Muestra con corriente $J_x$ y campo $B_z$: la fuerza de Lorentz $F_L=-e\,v_xB$ desvía los e⁻ hacia $-y$; se acumulan cargas en las caras y aparece un campo transversal $E_H$ (fuerza $F_H=-eE_H$ hacia $+y$). **Estado estacionario:** $F_H=F_L$. [p. 88-89]

$$eE_H=ev_xB\ \Rightarrow\ E_H=v_xB,\qquad J_x=N(-e)v_x\ \Rightarrow\ E_H=-\frac1{Ne}J_xB$$

$$\boxed{R_H=\frac{E_H}{J_xB}=-\frac1{Ne}}\quad(\text{constante de Hall}),\qquad N=-\frac1{R_He}$$

**Tabla** ($R_H\times10^{-10}$ V·m³/A·Wb, 300 K): Li −1.7; Na −2.5; Cu −0.55; Ag −0.84; Au −0.72; Zn **+0.3**; Cd **+0.6**; Al −0.3. [p. 90]
- $R_H>0$ ⇒ conducción por **huecos** (Zn, Cd, Be): **falla** del modelo de e⁻ libres. [p. 91]
- En metales comunes $J_x$ y la resistencia no dependen de $B$ (el efecto de $F_L$ es cancelado por $F_H$; los e⁻ fluyen horizontalmente → magnetorresistencia ≈ 0); en metales de transición, $R=R(B)$ (magnetorresistencia $\neq0$). [p. 91]

**Preguntas de parcial** (`P-2025-01 #4a`): al invertir $\mathbf B$, **cambia el signo** del voltaje Hall (porque $F_L$ cambia de sentido y $E_H$ cambia de signo: $E_H\propto B$); la **magnetorresistencia no cambia de signo** (depende de $B^2$ / es par en $B$, y en e⁻ libres es nula).

### Puntos clave para dominar este tema
- Deducir $R_H=-1/(Ne)$ igualando $F_H=F_L$ y usar $R_H$ para obtener $N$ y el **signo de los portadores**.
- Explicar por qué $R_H>0$ (Zn, Cd) contradice el modelo de e⁻ libres (huecos / SF no esférica).
- Responder qué cambia al invertir $B$: sí el signo de $V_H$; no el signo de la magnetorresistencia.

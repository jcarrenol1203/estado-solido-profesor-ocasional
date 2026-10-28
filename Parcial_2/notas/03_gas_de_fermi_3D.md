# Gas de Fermi 3D: $k_F$, $E_F$, densidad de estados y superficie de Fermi (bloque 3)

> **Nota de origen:** cubre las páginas 62-73 de `Diapositivas/Metales 2021.pdf`.

## 10. Estados del electrón libre en 3D: ondas planas y condiciones periódicas (`fermi3d.1`)

Partícula libre: $-\dfrac{\hbar^2}{2m}\nabla^2\psi_k=\varepsilon_k\psi_k$. Electrón en un cubo de arista $L$. Con condiciones de pared rígida $\psi=A\sin(n_x\pi x/L)\sin(n_y\pi y/L)\sin(n_z\pi z/L)$, $n_i\in\mathbb Z^+$. [p. 62]

**Condiciones de frontera periódicas** (Born-von Kármán): $\psi(x+L,y,z)=\psi(x,y,z)$ (y análogas). Ventajas: (1) puede asumirse un cristal infinito; (2) se desprecia la influencia de las fronteras externas. Las soluciones son **ondas planas viajeras**: [p. 63-64]

$$\psi_{\mathbf k}(\mathbf r)=e^{i\mathbf k\cdot\mathbf r},\qquad k_i=\frac{2\pi n_i}{L},\ \ n_i\in\mathbb Z\ (\text{positivos y negativos})$$

pues $e^{ik_x(x+L)}=e^{ik_xx}e^{i2\pi n}=e^{ik_xx}$. [p. 64]

$$\varepsilon_{\mathbf k}=\frac{\hbar^2k^2}{2m}=\frac{\hbar^2}{2m}(k_x^2+k_y^2+k_z^2)$$

Las $\psi_{\mathbf k}$ son funciones propias del momento: $\mathbf p\psi_{\mathbf k}=-i\hbar\nabla\psi_{\mathbf k}=\hbar\mathbf k\,\psi_{\mathbf k}$, con **velocidad** $\mathbf v=\hbar\mathbf k/m$. [p. 65]

**Estado fundamental de $N$ e⁻ libres:** los niveles ocupados son puntos del espacio $\mathbf k$ dentro de una **esfera de Fermi** de radio $k_F$; en su superficie $\varepsilon_F=\hbar^2k_F^2/2m$. [p. 65-66]

**Relación entre $N$ y $k_F$:** el volumen ocupado en $\mathbf k$ por un estado es $(2\pi/L)^3$; con 2 estados de espín por terna $(k_x,k_y,k_z)$: [p. 66]

$$2\cdot\frac{\tfrac43\pi k_F^3}{(2\pi/L)^3}=\frac{V}{3\pi^2}k_F^3=N\ \Rightarrow\ \boxed{k_F=\left(3\pi^2\frac NV\right)^{1/3}}$$

$$\boxed{E_F=\frac{\hbar^2}{2m}\left(3\pi^2\frac NV\right)^{2/3}},\qquad v_F=\frac{\hbar k_F}{m}=\frac\hbar m\left(3\pi^2\frac NV\right)^{1/3}$$

$E_F$ y $k_F$ quedan determinados **solo** por la concentración de e⁻ de valencia. [p. 66-67]

**Estimación para Na** (bcc, $a=4.2$ Å, 1 e⁻/átomo, 2 átomos/celda): $N/V=2/(4.2\text{ Å})^3=3\times10^{22}$ cm⁻³; $k_F\approx(3\pi^2\cdot3\times10^{22})^{1/3}\approx10^8$ cm⁻¹ $\approx1$ Å⁻¹; $E_F=\frac{\hbar^2k_F^2}{2m}=13.6\text{ eV}\,(k_Fa_0)^2\approx3.5$ eV ($a_0$ = radio de Bohr); $T_F=E_F/k_B\approx40\,000$ K; $v_F\sim10^6$ m/s. [p. 67]

**Velocidad promedio** (de uso en examen): $\langle v\rangle=\tfrac34v_F$ a $T=0$ (promedio sobre la esfera de Fermi; no está en las diapositivas, lo da el enunciado de `P-2025-2S #2`).

### Puntos clave para dominar este tema
- Explicar la ventaja de las condiciones periódicas y que dan ondas planas $e^{i\mathbf k\cdot\mathbf r}$ con $k_i=2\pi n_i/L$ ($n_i$ enteros ±).
- Derivar $k_F$ y $E_F$ contando estados en la esfera (factor 2 de espín, volumen por estado $(2\pi/L)^3$).
- Calcular $E_F$, $T_F$, $v_F$ a partir de $N/V$ (Na: 3.5 eV estimado / 3.2 obs.; Cu: 7 eV).
- Recordar que $\langle v\rangle=\tfrac34v_F$ y $\langle E\rangle=\tfrac35E_F$ a $T=0$.

---

## 11. Densidad de estados $D(\varepsilon)$ y energía interna (`fermi3d.2`)

$D(\varepsilon)$ = número de niveles por unidad de energía. De $\varepsilon=\frac{\hbar^2}{2m}\left(3\pi^2\frac NV\right)^{2/3}$ se despeja el número de niveles con energía $\le\varepsilon$: [p. 68]

$$N(\varepsilon)=\frac V{3\pi^2}\left(\frac{2m\varepsilon}{\hbar^2}\right)^{3/2},\qquad D(\varepsilon)=\frac{dN}{d\varepsilon}=\frac V{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}\varepsilon^{1/2}$$

Alternativa: de $\ln N=\tfrac32\ln\varepsilon+\text{cte}$ → $\frac{dN}{N}=\frac32\frac{d\varepsilon}{\varepsilon}$ → $\boxed{D(E_F)=\dfrac{3N}{2E_F}}$. [p. 69]

- $N=\int_0^\infty D(\varepsilon)f(\varepsilon)\,d\varepsilon$ (a $T=0$ el límite superior es $E_F$). [p. 69]
- $D(\varepsilon)f(\varepsilon,T)$ = densidad de orbitales llenos a $T>0$: la cola difusa de ancho $\sim k_BT$ alrededor de $E_F$. [p. 70]
- Energía interna: ver `cal.3` en `02_estadistica_fermi_calor_especifico.md`. A $T=0$, $E_0=\int_0^{E_F}\varepsilon D\,d\varepsilon=\tfrac35NE_F$ (energía promedio por e⁻ $=\tfrac35E_F$; dato de examen, `P-2025-01 #3`).
- Presión y módulo de rigidez a $T=0$ (de talleres): $P=-(\partial E_0/\partial V)_T=\tfrac23\frac{E_0}{V}=\tfrac25nE_F$; $B=-V(\partial P/\partial V)_T=\tfrac53P=\tfrac23nE_F$ (`T-2025-II #5, #7`), pues $E_F\propto V^{-2/3}$.

### Puntos clave para dominar este tema
- Derivar $N(\varepsilon)\propto\varepsilon^{3/2}$ y $D(\varepsilon)\propto\varepsilon^{1/2}$; probar $D(E_F)=3N/2E_F$.
- Usar $N=\int Df$ para fijar $\mu$ y entender qué muestra $D\cdot f$.
- Obtener $E_0=\tfrac35NE_F$, $P=\tfrac25nE_F$ y $B=\tfrac23nE_F$ (usando $E_F\propto V^{-2/3}$).

---

## 12. Superficie de Fermi (`fermi3d.3`)

Espacio de velocidades (ejes $v_x,v_y,v_z$) con $E=\tfrac12m^*v^2$: a $T=0$ los e⁻ ocupan una **esfera de Fermi** de radio $v_F$; la superficie $E_F=\tfrac12m^*v_F^2$ es la **superficie de Fermi (SF)**. [p. 72-73]
- A $T>0$ la SF **no se afecta apreciablemente** (pocos e⁻ excitados): es una identidad **permanente**, característica física real del metal, $v_F=(2E_F/m^*)^{1/2}\sim10^6$ m/s, independiente de $T$.
- $E_F=\frac{\hbar^2}{2m^*}(3\pi^2N/V)^{2/3}=f(N)$. Para $N\sim10^{23}$ cm⁻³, $E_F\sim5$ eV.
- Para metales reales la SF **no es esférica** (ver `falla.1` en `05_emision_termoionica_y_fallas.md`).

### Puntos clave para dominar este tema
- Definir la SF y la esfera de Fermi (en $\mathbf k$ y en $\mathbf v$); dar $v_F\sim10^6$ m/s.
- Explicar por qué la SF casi no cambia con $T$ y por qué es una propiedad característica del metal.

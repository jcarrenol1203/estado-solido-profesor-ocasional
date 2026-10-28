# Guía de teoría por examen — Parcial 1 (Vibraciones de red)

> **Qué es esto.** Para cada archivo de `Parciales y Talleres/Parcial1/` (salvo `Ejercicios Conceptuales de Practica/`): el **enunciado completo**, la **teoría necesaria** con la **página del PDF original** (`vibraciones de red(ultima versión).pdf`) y las **fórmulas**, y la **solución razonada**. En el parcial de opción múltiple (2026-1S): respuesta + por qué.
>
> **Convenciones.**
> - `[p. N]` = página del PDF original (tomada de los `[p. N]` de `notas/*.md`).
> - `[sin p.]` = contenido que **no está en el PDF**: se derivó a partir de exámenes viejos y vive en `notas/…` (calor.8–11, monoat.2, enlace.9).
> - `(F#)` = fórmula numerada de la **Hoja de fórmulas** (§2).
> - ⚠️ = errata del enunciado o respuesta de confianza media/baja. ✅ = número verificado por cálculo.
> - Unidades: se trabaja en SI; los enunciados en cgs se convierten (1 dyn/cm = 10⁻³ N/m, 1 g = 10⁻³ kg).
>
> **Aviso sobre fuentes.** Esta guía se hizo releyendo los archivos crudos (excepción explícita a la regla "no releer" de `CLAUDE.md`, pedida por el usuario). Al hacerlo se detectaron errores en `banco_preguntas.md` (ver §5).

---

## 0. Índice de archivos

| Archivo | Qué es | Sección |
|---|---|---|
| `Parcial_1-2026-1S.pdf` | Parcial 2026-1S, 18 preguntas de opción múltiple | §3.1 |
| `Parcial I (SS2020).pdf` | Parcial abierto (Q1, Q2, Q3, Q4.1, Q4.2, Q8) | §3.2 |
| `Parcial I (SS2020) - Mi solucion.pdf` | Tus manuscritos de ese parcial (solo contraste) | §3.2 (cuadros "Contraste") |
| `Parcial 1 - 2025-01.jpg` | Imagen: **mismo enunciado** que SS2020 Q1 y Q2 | §3.3 |
| `Parcial 1(2) - 2025-01.jpg` | Imagen: problema del jellium (Q5) | §3.3 |
| `Taller Vibraciones de red(SS2020).pdf` | Taller con 8 problemas | §3.4 |
| `Taller I (2025 II).pdf` / `Taller I(2025 II).doc` | Taller 2025-II, 7 problemas (el `.doc` es idéntico al PDF) | §3.5 |
| `Taller 1 - 01-2025(Solucion).pdf` | Taller 2025-01, 4 problemas **con tu solución** | §3.6 |
| `Talleres Parcial 1 - Mi Solucion.pdf` | Tu cuaderno de soluciones de SS2020 + 2025-II | §3.4, §3.5 (cuadros "Contraste") |
| `Apuntes P1-Vibraciones de la Red- E.pdf` | 49 pp. de apuntes de clase: **teoría**, no contiene preguntas (ya condensados en `notas/`) | §1 |
| `Ejercicios Conceptuales de Practica/QS1–QS6` | Excluidos por pedido del usuario | — |

---

## 1. Mapa tema → páginas del PDF

| Tema | Páginas | Nota donde está resumido |
|---|---|---|
| Enlaces, tipos de enlace (iónico, covalente, metálico, VdW) | 37–44 | `00b` §1–7 |
| Energía de cohesión, Madelung, repulsión de Born | 47–54 | `00b` §8 |
| Ondas de sonido / vibraciones de red (motivación) | 45–46 | `01` §1 |
| Ecuación de onda elástica continua, $\omega=v_sq$ | 56–58 | `01` §2 |
| $g(\omega)$ 1D (cond. de frontera periódicas, factor 2 de ±q) | 59–62 | `01` §3 |
| $g(\omega)$ 3D (esfera en $q$, factor 3 de polarizaciones) | 63–66 | `01` §4 |
| Dulong-Petit y teoría clásica (equipartición) | 67–71 | `03` §1–2 |
| **Einstein** (energía media, MB, $C_V$, fallo a T baja) | 72–81 | `03` §3 |
| **Debye** (modos colectivos, $\omega_D$, $C_V$, ley $T^3$) | 82–96 | `03` §4 |
| Limitaciones de Debye ($v_L\neq v_T$) | 97–98 | `03` §5 |
| **Fonón** (cuantización, BE, número de ocupación) | 99–103 | `03` §6–7 |
| Anarmonicidad y expansión térmica | 104–108 | `06` §1 |
| **Cadena monoatómica** (dispersión, $v_g$, Bragg, 1ª ZB, $g(\omega)$) | 110–141 | `01b` |
| **Cadena diatómica** (ramas, gap, amplitudes, conteo) | 142–153 | `02` |
| Red 3D, no-Bravais, $g(\omega)$ general | 154–168 | `05` |
| Conductividad térmica de fonones ($K=\tfrac13C_Vv\ell$) | 169–176 | `06` §2 |
| Mecanismos de dispersión, Umklapp | 179–186 | `06` §3 |
| Aplicaciones de ondas acústicas | 187–196 | `06` §4 |
| Debye en D dimensiones (1D, 2D) | [sin p.] | `03` §8 |
| Energía de punto cero, $\langle u^2\rangle$ | [sin p.] | `03` §9 |
| Dispersión inelástica fotón/neutrón–fonón | [sin p.] | `03` §10 |
| Momento real vs. cristalino $\hbar q$ | [sin p.] | `03` §11 |
| Cadena con 2os vecinos | [p. 124 relacionado] | `01b` (monoat.2) |
| Jellium (ion en mar de electrones) | [p. 42 relacionado] | `00b` §9 |

---

## 2. Hoja de fórmulas

**F1 — Continuo.** $v_s=\sqrt{Y/\rho}$, $\omega=v_sq$ [p. 57–58]. Válido solo para $\lambda\gg a$ [p. 114].

**F2 — Modos y $g(\omega)$.** $q=2\pi m/L$ (Born–von Kármán) [p. 59–60]. Cada $|q|$ aparece con $\pm q$ (factor 2) [p. 62].
- 1D: $g(\omega)=\dfrac{L}{\pi v_s}$ (constante) [p. 61–62]. En general $g(\omega)=\dfrac{L}{\pi\,v_g(\omega)}$.
- 3D: $g(\omega)=\dfrac{3V\omega^2}{2\pi^2v_s^3}$ [p. 65–66]; en Debye $g(\omega)=\dfrac{9N\omega^2}{\omega_D^3}$ (normalizada a $3N$) [p. 84–88].
- Dimensión $D$: $g(\omega)\propto\omega^{D-1}$ [sin p.].

**F3 — Clásico.** $\bar\varepsilon=k_BT$ por oscilador (1D: cinético + potencial); $E=3Nk_BT$; $C_V=3R\approx 24.9$ J/mol·K [p. 68–71]. En alta T a 1 mol: $3RT=24.94\,T$ J.

**F4 — Einstein.** Niveles $\varepsilon_n=n\hbar\omega$ (se omite $\tfrac12\hbar\omega$, constante) [p. 72]. $\bar\varepsilon=\dfrac{\hbar\omega}{e^{\hbar\omega/k_BT}-1}$ [p. 74–76]. $C_V=3Nk_B\left(\dfrac{\theta_E}{T}\right)^2\dfrac{e^{\theta_E/T}}{(e^{\theta_E/T}-1)^2}$ [p. 78–80], $k_B\theta_E=\hbar\omega_E$. En $T=\theta_E$: $C_V=0.92\times3R$ ✅. $T\ll\theta_E$: $C_V\propto e^{-\theta_E/T}$ (falla) [p. 81]. $T\gg\theta_E$: $3R$.

**F5 — Debye.** $E=\displaystyle\int_0^{\omega_D}\frac{\hbar\omega\,g(\omega)}{e^{\hbar\omega/k_BT}-1}d\omega=9Nk_BT\left(\frac{T}{\theta_D}\right)^3\int_0^{\theta_D/T}\frac{x^3}{e^x-1}dx$ [p. 84–89]. $C_V=9R\left(\dfrac{T}{\theta_D}\right)^3\displaystyle\int_0^{\theta_D/T}\frac{x^4e^x}{(e^x-1)^2}dx$ [p. 89].

**F6 — $\omega_D$ y $\theta_D$.** $\int_0^{\omega_D}g\,d\omega=3N\Rightarrow\omega_D=v_s(6\pi^2n)^{1/3}$, $n=N/V$ [p. 86–88]. $k_B\theta_D=\hbar\omega_D$. $\theta_D\sim(Y/M)^{1/2}n^{-1/6}$: rígido y ligero ⇒ $\theta_D$ alto (diamante 1860 K, Pb 102 K, Cu 343 K) [p. 90–92]. Red SC: $n=1/a^3$ ⇒ $\omega_D=(6\pi^2)^{1/3}v_s/a=3.898\,v_s/a$.

**F7 — Límites de Debye.** $T\gg\theta_D$: $C_V\to3R$ [p. 92–93]; en $T=\theta_D$: $C_V\approx0.95\times3R$ ✅ [p. 93]. $T\ll\theta_D$: $C_V=\dfrac{12\pi^4}{5}Nk_B\left(\dfrac{T}{\theta_D}\right)^3$, usando $\int_0^\infty\frac{x^4e^x}{(e^x-1)^2}dx=\frac{4\pi^4}{15}$ [p. 94]. Argumento de la "esfera térmica": modos excitados $\propto q^3\propto T^3$, cada uno $\sim k_BT$ ⇒ $E\propto T^4$, $C_V\propto T^3$ [p. 94–95]. Curva universal en $T/\theta_D$ [p. 90].

**F8 — Fonón.** $E_n=(n+\tfrac12)\hbar\omega$; fonón = cuanto de energía $\hbar\omega$, "momento" $\hbar q$ [p. 99–100]. Bose-Einstein, $\mu=0$ (número no conservado) [p. 101–103]. $\bar n=\dfrac{1}{e^{\hbar\omega/k_BT}-1}$: $\to0$ a T baja, $\approx k_BT/\hbar\omega$ a T alta [p. 103]. Número en $d\omega$: $N(\omega)d\omega=g\,d\omega/(e^{\hbar\omega/k_BT}-1)$, energía $dE=\hbar\omega N(\omega)d\omega\propto\omega^3/(e^x-1)$, con máximo en $x=\hbar\omega/k_BT\approx2.82$ ✅ [p. 102].

**F9 — Debye en $D$ dimensiones.** Con $\omega=v_sq$: $g\propto\omega^{D-1}$ y $C_V\propto T^D$ a T baja [sin p.]:
- 1D: $C_V=\dfrac{\pi Lk_B^2}{3\hbar v}T=\dfrac{\pi^2}{3}Nk_B\dfrac{T}{\theta_D}$ ✅ (usa $\int_0^\infty\frac{x}{e^x-1}dx=\frac{\pi^2}{6}$).
- 2D: $g=\dfrac{A\omega}{2\pi v^2}$, $C_V=\dfrac{3\zeta(3)Ak_B^3}{\pi\hbar^2v^2}T^2$ (usa $\int_0^\infty\frac{x^2}{e^x-1}dx=2\zeta(3)$, $\zeta(3)=1.202$).
- 3D: $T^3$ (F7).

**F10 — Punto cero y desplazamientos.** $E_0=\int_0^{\omega_D}g\,\tfrac12\hbar\omega\,d\omega=\tfrac98N\hbar\omega_D=\tfrac98Nk_B\theta_D$ [sin p.]. $\langle u^2\rangle=\dfrac{9\hbar}{M\omega_D^3}\displaystyle\int_0^{\omega_D}(\bar n+\tfrac12)\omega\,d\omega$; a $T\to0$: $\langle u^2\rangle_0=\dfrac{9\hbar}{4M\omega_D}=\dfrac{9\hbar^2}{4Mk_B\theta_D}$ [sin p.]. Alta T clásico (Einstein): $\tfrac12M\omega_E^2\langle u_x^2\rangle=\tfrac12k_BT\Rightarrow\langle u_x^2\rangle=\dfrac{k_BT}{M\omega_E^2}$.

**F11 — Cadena monoatómica.** $M\ddot u_n=-\alpha(2u_n-u_{n+1}-u_{n-1})$, $u_n=Ae^{i(qna-\omega t)}$ ⇒ $\omega=\omega_m|\sin(qa/2)|$, $\omega_m=2\sqrt{\alpha/M}$ [p. 110–113]. $v_s=\omega_ma/2=a\sqrt{\alpha/M}$ [p. 114–116]; $v_p=\omega/q$; $v_g=v_s\cos(qa/2)$ [p. 119–124]. $v_g=0$ en $q=\pm\pi/a$ ($\lambda=2a$, onda estacionaria, reflexión de Bragg $2a=n\lambda$) [p. 125–126]. $q\equiv q+2\pi/a$ ⇒ 1ª ZB $-\pi/a<q\le\pi/a$ [p. 128–134]. $N$ modos en la ZB [p. 135]. $g(\omega)=\dfrac{2N}{\pi\sqrt{\omega_m^2-\omega^2}}$ (singularidad de van Hove en $\omega_m$) [p. 136–139]. Cuerda: $\lambda_{min}=2a$ [p. 141].

**F12 — Cadena con 2os vecinos [sin p.].** $\omega^2=\frac{2}{M}[A(1-\cos ka)+B(1-\cos2ka)]$; $v_g=\dfrac{a[A\sin ka+2B\sin2ka]}{M\omega}$; $v_s=a\sqrt{(A+4B)/M}$; $g(\omega)=L/(\pi v_g)$.

**F13 — Cadena diatómica.** $\omega^2=\alpha\left(\tfrac1{M_1}+\tfrac1{M_2}\right)\pm\alpha\sqrt{\left(\tfrac1{M_1}+\tfrac1{M_2}\right)^2-\tfrac{4\sin^2(\cdot)}{M_1M_2}}$ [p. 144] (en el enunciado de examen $\sin^2(qa/2)$ con $a$ = celda; en las notas $\sin^2(qa)$ con $a$ = espaciamiento atómico: equivalen). Signo $-$ acústica, $+$ óptica. $q=0$: acústica $0$, óptica $\sqrt{2\alpha(1/M_1+1/M_2)}$ [p. 145]. **Borde de zona:** la raíz vale $|1/M_1-1/M_2|$ ⇒ $\omega_{ac}=\sqrt{2\alpha/M_{pesada}}$, $\omega_{ópt}=\sqrt{2\alpha/M_{ligera}}$; entre ambas hay un **gap** [p. 145]. Acústica $q\to0$: $v=a\sqrt{2\alpha/(M_1+M_2)}$ [p. 146]. Amplitudes: acústica $A_2/A_1=1$, óptica $A_2/A_1=-M_1/M_2$ [p. 147–148]. Gap: $q$ complejo, onda evanescente [p. 149–151]. Óptica absorbe IR (dipolo oscilante) [p. 152]. $2N$ modos [p. 153]. 3D: 3 ramas por átomo de la base, $3r$ en total [p. 154–160].

**F14 — Conductividad.** $K=\tfrac13C_Vv\ell$ [p. 174–175]. $T>\theta_D$: $C_V=3Nk_B$ cte., $\ell\propto1/\bar n\propto1/T$ ⇒ $K\propto1/T$ [p. 183–186]. Solo Umklapp da resistencia térmica; a T baja $\ell\propto e^{\theta_D/2T}$ y luego $\ell$ satura en el tamaño de la muestra [p. 179–186].

**F15 — Dispersión inelástica [sin p.].** $E_i=E_f\mp\hbar\Omega$, $\vec k_i=\vec k_f\mp\vec q\ (\mathrm{mod}\ \vec G)$. Ley de cosenos $q^2=k_i^2+k_f^2-2k_ik_f\cos\theta$; fotón ($k_i\approx k_f=k=2\pi n/\lambda_0$): $q=2k\sin(\theta/2)$, $\Omega=v_sq$. Neutrón: $E=\hbar^2k^2/2m_n$, $k=2\pi/\lambda$, $\hbar\Omega=E_i-E_f$.

**F16 — Momento [sin p.].** $P_{mec}=M\sum_n\dot u_n\propto\sum_{n=0}^{N-1}e^{iqna}=0$ para $q=2\pi m/Na$, $m\ne0$ (mod $N$). $\hbar q$ es momento *cristalino* (definido mod $\hbar G$).

**F17 — Jellium [sin p.; ver p. 42].** $n\tfrac43\pi R^3=1$; carga encerrada $-e(r/R)^3$; Gauss: $F=-\dfrac{e^2}{4\pi\varepsilon_0R^3}r$ ⇒ $\omega^2=\dfrac{e^2}{4\pi\varepsilon_0MR^3}=\dfrac{ne^2}{3\varepsilon_0M}$.

**F18 — Madelung [p. 47–54].** $U_{ij}=\pm\dfrac{q^2}{4\pi\varepsilon_0r_{ij}}+\dfrac{A}{r_{ij}^b}$; $U_i(r)=-\dfrac{\alpha q^2}{4\pi\varepsilon_0r}+\dfrac{A\zeta_b}{r^b}$; $\alpha_{1D}=2\ln2=1.386$, $\alpha_{NaCl}=6-\tfrac{12}{\sqrt2}+\tfrac{8}{\sqrt3}-\dots=1.7476$. $E_{enlace}(NaCl)=-7.9$ eV vs. $k_BT(300K)\approx0.026$ eV.

**Constantes útiles.** $\hbar=1.0546\times10^{-34}$ J·s, $k_B=1.3806\times10^{-23}$ J/K, $R=8.314$ J/mol·K, $u=1.6605\times10^{-27}$ kg, $m_n=1.6749\times10^{-27}$ kg, $e=1.602\times10^{-19}$ C, $\varepsilon_0=8.854\times10^{-12}$ F/m.

---

## 3. Los exámenes, uno por uno

### 3.1 `Parcial_1-2026-1S.pdf` — Parcial 1 (S I 2026), Física del Estado Sólido, UNAL Medellín

18 preguntas de opción múltiple. La 11 vale 1 punto (marcada en el original).

**P1.** *Si pretende medir el calor específico de una red de una monocapa aislada de átomos (un cristal 2D) a temperaturas muy bajas, ¿qué dependencia de la temperatura se esperaría?* a. ∝ $T^3$ · b. ∝ $T^2$ · c. ∝ $T$ · d. independiente de $T$ · e. $C_v$ de un sistema 2D no se puede medir.
**Respuesta: b.**
*Por qué:* en 2D, $g(\omega)\propto\omega$ (círculo en $q$). A T baja $E\sim\int\hbar\omega\,g\,\bar n\,d\omega\propto T^3$ ⇒ $C_V=dE/dT\propto T^2$. Equivalente al argumento de la "esfera térmica": modos excitados $\propto q^2\propto T^2$, cada uno $k_BT$ ⇒ $C_V\propto T^2$. *Teoría:* F9, F7 [p. 94–95] + calor.8 [sin p.]. *Descartes:* a es el caso 3D; c el 1D; d es la predicción clásica (alta T).

**P2.** *La energía de punto cero en el oscilador armónico no es considerada en el modelo de Einstein del calor específico. La razón para ello es:* a. El modelo de Einstein considera un oscilador armónico clásico en lugar de uno cuántico. · b. La energía del punto cero no se puede definir para un oscilador armónico cuántico. · c. En el modelo se considera solamente la diferencia entre niveles energéticos. · d. La consideración de la energía de punto cero llevaría a resultados contradictorios en la teoría de $C_v$. · e. La energía de punto cero es mejor definida en el modelo de Debye.
**Respuesta: c.**
*Por qué:* el modelo usa $\varepsilon_n=n\hbar\omega$ [p. 72]. El término $\tfrac12\hbar\omega$ añade a $E$ la constante $\tfrac32N\hbar\omega_E$, independiente de $T$, y $C_V=\partial E/\partial T$ la elimina: solo importan las diferencias entre niveles. *Descartes:* a es falso (Einstein es cuántico); b falso (está bien definida); d falso (no hay contradicción: simplemente no afecta); e no explica la omisión. *Teoría:* F4, F10.

**P3.** *¿Cuál de las siguientes estadísticas de equilibrio describe la distribución de fonones a una temperatura $T$?* a. Pauli · b. Bose-Einstein · c. Fermi-Dirac · d. Maxwell-Boltzmann · e. Al fonón no lo rige ninguna estadística.
**Respuesta: b.**
*Por qué:* los fonones son indistinguibles, no están sujetos a exclusión de Pauli (varios en el mismo modo) y su número no se conserva ($\mu=0$) ⇒ $\bar n=1/(e^{\hbar\omega/k_BT}-1)$. *Teoría:* F8 [p. 101–103]. (MB aparece en Einstein por otra razón: ver P13.)

**P4.** *En el modelo de Debye, se supone que la densidad de estados de fonones $g(\omega)\propto\omega^2$ hasta una frecuencia de corte máxima ($\omega_d$). Esta derivación se basa en el trato de la red cristalina como:* a. colección de osciladores armónicos cuánticos aislados · b. un medio continuo elástico isótropo · c. cadena lineal periódica discreta con base de dos átomos · d. gas de partículas clásicas no interactuantes · e. gas de Bose-Einstein.
**Respuesta: b.**
*Por qué:* $g\propto\omega^2$ sale de contar puntos $q$ en una esfera con $\omega=v_sq$ (medio continuo isótropo), cortando en $\omega_D$ para que haya $3N$ modos. *Descartes:* a es Einstein; c daría $g$ con singularidad de van Hove, no $\omega^2$. *Teoría:* F2, F6 [p. 63–66, 82–88].

**P5.** *¿Por qué el modelo de Debye del calor específico funciona mucho mejor que el modelo de Einstein a temperaturas bajas?* a. El calor específico de baja temperatura está dominado por fonones de alta frecuencia (ópticos), que el modelo de Debye describe perfectamente. · b. A temperaturas bajas, sólo se excitan fonones acústicos (ondas sonoras) de frecuencia baja y longitud de onda larga. El modelo de Debye incluye la contribución electrónica a $C_v$, mientras que el modelo de Einstein la ignora. · c. El modelo de Debye tiene en cuenta la expansión de la red a medida que la temperatura cambia. · d. En realidad ambos modelos explican bien el comportamiento de $C_v$ a temperaturas bajas.
**Respuesta: b** ⚠️ *(es la menos mala).*
*Por qué:* la primera frase de b es la razón física correcta: a T baja solo se excitan modos acústicos de $\hbar\omega\lesssim k_BT$, que Debye sí incluye (espectro continuo hasta $\omega\to0$, $\omega=v_sq$) y Einstein no (una sola $\omega_E$ ⇒ caída exponencial en lugar de $T^3$). **La segunda frase es falsa**: Debye no incluye contribución electrónica (es un modelo solo de red). Pero las otras opciones son peor: a es falso (los ópticos son de alta $\omega$ y se congelan primero), c es falso (ninguno incluye expansión), d es falso (Einstein falla). *Teoría:* F4–F7 [p. 81, 94–97].

**P6.** *Los fonones con una mayor contribución a la energía del sistema son aquellos con longitud de onda $\lambda\to$:* a. $3a$ · b. $(1/2)a$ · c. $2a$ · d. $5a$ · e. $a$.
**Respuesta: c ($2a$).**
*Por qué:* $dE=\hbar\omega\,g(\omega)\bar n\,d\omega$ con $g\propto\omega^2$ creciente: dominan los modos de mayor frecuencia, es decir los de menor $\lambda$ posible, que en la red es $\lambda_{min}=2a$ (borde de zona $q=\pi/a$) [p. 128–134, 141]. $\lambda=a/2$ es imposible (más corta que $2a$ = $q$ fuera de la 1ª ZB, indistinguible de otro modo). *Matiz:* en Debye 3D el corte efectivo es $\lambda_D=2\pi/q_D\approx1.6a$ (no es opción); $a$ también está por debajo de $2a$. ⚠️ *Nota:* `banco_preguntas.md` decía "$\lambda\to a$"; el criterio del curso es $\lambda_{min}=2a$ (ver tu propia respuesta de SS2020 Q4.1b).

**P7.** *El número de fonones en un estado puede ser:* a. únicamente de una unidad · b. solamente del orden del número de Avogadro · c. muy pequeña o muy grande · d. imposible de calcular en la teoría de sólidos cristalinos · e. independiente de la energía del sistema.
**Respuesta: c.**
*Por qué:* $\bar n=1/(e^{\hbar\omega/k_BT}-1)$ va de $\to0$ (T baja o $\hbar\omega\gg k_BT$) a $\approx k_BT/\hbar\omega\gg1$ (T alta o $\omega$ baja); a diferencia de fermiones no hay tope. Depende de la energía del sistema (T), luego e es falso. *Teoría:* F8 [p. 103].

**P8.** *La diferencia en el valor para la temperatura de Debye del plomo y del carbono radica en:* a. la diferencia en las propiedades térmicas de ambos compuestos · b. la dificultad mayor para medir el calor específico del plomo · c. la dificultad mayor para medir el calor específico del carbono · d. la imposibilidad de obtener muestras con suficiente pureza · e. la diferencia en las propiedades mecánicas.
**Respuesta: e.**
*Por qué:* $\theta_D\sim\omega_D\sim v_sn^{1/3}\sim(Y/M)^{1/2}n^{-1/6}$: rigidez ($Y$) y masa. Diamante ($\theta_D=1860$ K): rígido y ligero; Pb ($102$ K): blando y pesado. *Teoría:* F6 [p. 90–92].

**P9.** *En un cálculo cuantitativo de la relación de dispersión es frecuente que la constante de fuerza atómica muestre una relación funcional similar a la relación mostrada por el índice de refracción. En el primer caso, esta relación es necesaria para:* a. demostrar que los átomos son osciladores armónicos · b. determinar la cuantización de la energía vibracional · c. poder solucionar las ecuaciones diferenciales de movimiento · d. demostrar que el movimiento de los átomos es correlacionado · e. poder calcular la relación de dispersión.
**Respuesta: e** ⚠️ *(confianza media; el rival es c).*
*Por qué:* el índice de refracción $n(\omega)$ es lo que da la dispersión de la luz, $\omega(k)=ck/n(\omega)$; análogamente, la dependencia funcional de la constante de fuerza (alcance de la interacción, vecinos) es lo que determina $\omega(q)$. La ecuación diferencial se resuelve igual con cualquier $\alpha$ (sustitución de onda plana); lo que cambia el resultado es la forma de $\omega(q)$. *Teoría:* F11–F12 [p. 110–113, 124].

**P10.** *El transporte de una onda en una red cristalina se hace manteniendo una relación de fase fija. Para tener un periodo espacial de una longitud de onda en la red, la diferencia de fase debería ser:* a. $a$ · b. $(1/2)a$ · c. $2a$ · d. $a^2$ · e. En un cristal las relaciones de fase no son fijas.
**Respuesta: a** ⚠️ *(confianza baja: enunciado ambiguo).*
*Por qué:* entre dos átomos vecinos la fase relativa es $\varphi=qa$ (de $u_n\propto e^{iqna}$): depende linealmente de la separación $a$, y las otras opciones ($a/2$, $2a$, $a^2$) no tienen esa dependencia. e contradice la premisa del enunciado ("relación de fase fija"). *Teoría:* [p. 119–124, 128–133] ($q\equiv q+2\pi/a$: la fase $qa$ se define mod $2\pi$).

**P11 (1 punto).** *La frecuencia máxima (en el modelo de Debye) de los modos de vibración de una red cúbica simple de constante de red $a=3$ Å y velocidad del sonido $v_s=4.2\times10^5$ cm/s es:* a. $1.5\times10^{13}$ m/s · b. $7.7\times10^8$ m/s · c. $8.7\times10^{13}$ rad/s · d. $5.4\times10^{13}$ m/s · e. Imposible de calcular con la información suministrada.
**Respuesta: d** ⚠️ *(unidades "m/s" son errata de rad/s).*
*Cálculo ✅:* $n=1/a^3$ (un átomo por celda en SC) ⇒ $\omega_D=v_s(6\pi^2n)^{1/3}=\dfrac{(6\pi^2)^{1/3}v_s}{a}=\dfrac{3.898\times4.2\times10^3\ \text{m/s}}{3\times10^{-10}\ \text{m}}=5.46\times10^{13}\ \text{rad/s}$. *Descartes:* c ($8.7\times10^{13}$) $\approx v_s\cdot2\pi/a$ (ignora el factor $(6\pi^2)^{1/3}$/usa la longitud de onda $a$ en vez de contar modos); b y a no tienen la magnitud ni las unidades. *Teoría:* F6 [p. 86–88].

**P12.** *La energía de enlace del NaCl es igual a $-7.9$ eV. Sin embargo, esta energía es mucho menor que la energía de un plasma denso. El cristal de NaCl es entonces estable porque:* a. La estructura del NaCl es tipo diamante · b. Los átomos están ligados por fuerzas tipo Van der Waals · c. Los átomos están ligados por fuerzas tipo covalente · d. Los niveles de energía en la sustancia están separados · e. El NaCl puede describirse en términos de la mecánica clásica.
**Respuesta: d.**
*Por qué:* clásicamente el colapso total sería el mínimo de energía; la mecánica cuántica impone niveles discretos (principio de Pauli/solapamiento de nubes ⇒ repulsión de corto alcance, $A/r^b$) que mantienen un equilibrio a $r\sim$ Å. *Descartes:* a, b, c son falsos (NaCl: iónico, rocksalt); e es la causa del colapso, no de la estabilidad. *Teoría:* F18 [p. 47–50].

**P13.** *En el modelo del calor específico de Einstein se utiliza la función de distribución clásica de Maxwell-Boltzmann sabiendo que el átomo es un sistema cuántico; la escogencia se justifica debido a:* a. En realidad la función clásica no funciona · b. El carácter probabilístico de esta función · c. Distinguibilidad de los osciladores · d. El espectro de frecuencias considerado en el modelo de Einstein · e. Los valores de las energías de los osciladores.
**Respuesta: c.**
*Por qué:* cada oscilador está localizado en su sitio de red ⇒ es distinguible por su posición (no hay intercambio ni exclusión), lo que justifica MB para el conjunto de osciladores aunque cada uno tenga niveles cuánticos. (Coincide con el resultado de BE para fonones, F8.) *Teoría:* [p. 77].

**P14.** *El modelo de Einstein para el calor específico falla a temperaturas bajas (caída exponencial). Esta falla tiene su origen en el hecho:* a. El modelo es clásico · b. El modelo considera la función de distribución clásica de Maxwell-Boltzmann · c. Modos de frecuencias bajas pueden absorber energía · d. Se usa una relación de dispersión no lineal · e. La distribución de energía de los osciladores considerada (la del radiador de cuerpo negro) no es la apropiada.
**Respuesta: c.**
*Por qué:* Einstein tiene una única $\omega_E$ ⇒ a $k_BT\ll\hbar\omega_E$ nada se excita ($e^{-\theta_E/T}$). En el sólido real existen modos acústicos de $\omega\to0$ que sí absorben energía ⇒ $T^3$ (Debye). *Teoría:* F4, F7 [p. 81, 96].

**P15.** *El fonón no es exactamente igual al fotón, principalmente porque:* a. El fotón es un cuanto de luz · b. La energía del fonón no está cuantizada como la del fotón · c. La velocidad del fonón puede tener dependencia con la frecuencia · d. El campo de las vibraciones elásticas puede describirse clásicamente · e. El fonón no cumple la ley de Bragg.
**Respuesta: c.**
*Por qué:* en el vacío $\omega=ck$ (lineal, sin dispersión); el fonón tiene $\omega(q)$ no trivial (p. ej. $\omega=\omega_m|\sin(qa/2)|$, $v_g=v_s\cos(qa/2)$) y además su momento $\hbar q$ es cristalino. *Descartes:* b falso (está cuantizada, $\hbar\omega$); d y a no son diferencias esenciales; e falso. *Teoría:* F8, F11 [p. 99–100, 119–124].

**P16.** *Se mide el calor específico de un sólido A y de un sólido B a una temperatura de 80 K. Para el sólido A se obtiene una temperatura de Debye de 100 K y para el B de 200 K. Este resultado implica que:* a. El calor específico de A es igual al de B · b. El calor específico de A es menor que el de B · c. El calor específico de A es mayor que el de B · d. La sustancia A conduce el calor de manera más eficiente que B · e. La sustancia B tiene un peso molecular más grande que el de A.
**Respuesta: c.**
*Por qué:* $C_V$ es función universal de $T/\theta_D$ y creciente. A: $T/\theta_D=0.8$ ($C\approx0.93\times3R$); B: $0.4$ ($C\approx0.75\times3R$) ✅ (calculado con la integral de Debye). Nada implica conductividad ni masas. *Teoría:* F7 [p. 90–94].

**P17.** *La formación de un cristal se da básicamente por la conjugación de fuerzas atractivas y repulsivas entre los átomos. La interrelación entre estas fuerzas no es trivial. Sin embargo, Madelung y Born lograron determinar la constante de fuerza atómica para un cristal. La determinación fue relativamente simple debido a que:* a. se consideró un sistema tridimensional · b. se consideró un sistema bidimensional · c. se consideró solamente la interacción entre primeros vecinos · d. se consideró la interacción entre varios vecinos · e. los cálculos en ese modelo no fueron satisfactorios.
**Respuesta: c.**
*Por qué:* el término repulsivo $A/r^b$ con $b\gg1$ decae tan rápido que basta el vecino más próximo, mientras que lo atractivo (Coulomb, $1/r$) se suma en $\alpha$. *Teoría:* F18 [p. 50–54].

**P18.** *El orden de magnitud para la velocidad del sonido en sólidos podría estimarse de la relación de dispersión $\omega(q)$. Para ello, debe considerarse:* a. solamente la primera derivada de la relación de dispersión · b. la segunda derivada de la relación de dispersión y su comportamiento a frecuencias altas · c. la segunda derivada y su comportamiento a frecuencias bajas · d. la pendiente de la relación de dispersión en cada punto de la región comprendida entre $-\pi/a$ y $\pi/a$ · e. la derivada primera de la relación de dispersión y su valor en $q\to\pi/a$ · f. el comportamiento de la primera derivada de la relación de dispersión a valores pequeños de $q$.
**Respuesta: f.**
*Por qué:* $v_s=\lim_{q\to0}d\omega/dq$ (pendiente a $q$ pequeño, régimen continuo $\omega=v_sq$). En $q\to\pi/a$, $v_g\to0$ (e falsa); la pendiente en cada punto es $v_g(q)$, no $v_s$ (d falsa). Ej.: $v_g=v_s\cos(qa/2)\to v_s$ cuando $q\to0$. *Teoría:* F1, F11 [p. 114–116, 121–124].

**Clave rápida:** 1b 2c 3b 4b 5b 6c 7c 8e 9e 10a 11d 12d 13c 14c 15c 16c 17c 18f. *(Menos seguras: 5, 9, 10.)*

---

### 3.2 `Parcial I (SS2020).pdf` — Universidad Nacional de Colombia, Dpto. de Física, Física del Estado Sólido, Parcial I (SS 2020)

**Enunciado completo.**
1. *Experimentalmente se encuentra que a temperaturas superiores a la temperatura de Debye, la conductividad térmica de los aisladores es inversamente proporcional a la temperatura. Determinar esta dependencia a partir de la expresión aproximada para el número de fonones excitados a temperaturas elevadas.*
2. *La relación de dispersión de una cadena de longitud $L$ de $N$ átomos de masa $M$ puede aproximarse mediante $\omega^2=\left(\dfrac2M\right)\left[A(1-\cos ka)+B(1-\cos2ka)\right]$. En esta ecuación $a$ representa el parámetro de red y $A$ y $B$ constantes de acoplamiento entre primeros y segundos vecinos, respectivamente.* a. determinar la velocidad de grupo de las ondas elásticas en la cadena. b. determinar qué longitudes de onda producen ondas estacionarias. c. determinar la velocidad de propagación del sonido. d. determinar la densidad de modos generada, la de Debye y el vector de onda de Debye ($k_D$).
3. *En el caso de una red diatómica lineal, la relación de dispersión para las ondas de la red es dada por $\omega^2=C\left(\frac1{M_1}+\frac1{M_2}\right)\pm\left[\left(\frac1{M_1}+\frac1{M_2}\right)^2-\frac{4\sin^2(qa/2)}{M_1M_2}\right]^{1/2}$. La interacción se da solo entre los vecinos más próximos y con la misma constante de fuerza $C$. Si $C=5\times10^3$ dyn cm⁻¹, calcular los valores posibles de las frecuencias en el límite de la primera zona de Brillouin para el caso que $M_1=5.9\times10^{-23}$ g y $M_2=3.8\times10^{-23}$ g.*
4.1. *Razonar brevemente sobre la veracidad o falsedad de las siguientes afirmaciones:* a. A $T=80$ K, la capacidad calorífica de un sólido con temperatura de Debye de 100 K será mayor que la de otro con temperatura de Debye de 200 K. b. La mínima longitud de onda de los fonones en un sólido será menor cuanto más grande sea su constante de red. c. Hay tantos tipos de fonones posibles como átomos. d. Podemos escuchar las vibraciones térmicas.
4.2. a. *¿Qué tipo de fonones proporciona una contribución mayor a la energía total de vibración de un cristal a temperatura $T$?* b. *En el modelo de Einstein, átomos son tratados como osciladores independientes. El modelo de Debye trata los átomos como osciladores acoplados vibrando colectivamente. Sin embargo, los modos colectivos son considerados como independientes. Explicar el significado de esta independencia y contrastarlo con el modelo de Einstein.* c. *¿Es posible encontrar ondas de sonido en moléculas pequeñas? Si no es posible, ¿cómo se puede explicar la propagación del sonido en sustancias gaseosas?*
8. *Calcular el momento lineal total de un cristal monoatómico unidimensional de $N$ átomos de masa $M$. En este cristal, un fonón con vector de onda $\vec q$ está excitado.*
*(El examen salta de la pregunta 4 a la 8: así viene numerado en el PDF.)*

#### Q1 — $K\propto1/T$ para $T>\theta_D$
**Teoría:** F8 (número medio de fonones), F7 ($C_V$ cte), F14 ($K=\tfrac13C_Vv\ell$) [p. 103, 92–93, 174–175, 183–186].
**Solución.** A $T\gg\theta_D$, $\hbar\omega/k_BT\ll1$ ⇒ $e^x\approx1+x$ ⇒ $\bar n=\dfrac{1}{e^{\hbar\omega/k_BT}-1}\approx\dfrac{k_BT}{\hbar\omega}\propto T$: el número de fonones crece linealmente con $T$. El camino libre medio lo fija la dispersión fonón–fonón (Umklapp), cuya tasa es proporcional al número de fonones presentes ⇒ $\ell\propto1/\bar n\propto1/T$. Además $C_V=3Nk_B$ es constante (Dulong-Petit) y $v\approx v_s$ constante. Con $K=\tfrac13C_Vv\ell$ ⇒ $\boxed{K\propto1/T}$.
> **Contraste con tu manuscrito:** coincide (usas $\langle n\rangle\approx k_BT/\hbar\omega$ y $\ell\propto1/T$).

#### Q2 — Cadena con 1os y 2os vecinos (F12; ver `notas/01b` monoat.2) [p. 110–126, 136–139 + sin p.]
**a) Velocidad de grupo.** Derivando $\omega^2$: $2\omega\dfrac{d\omega}{dk}=\dfrac2M\left[Aa\sin ka+2Ba\sin2ka\right]$ ⇒
$$v_g=\frac{d\omega}{dk}=\frac{a\left[A\sin ka+2B\sin2ka\right]}{M\,\omega(k)}.$$
**b) Ondas estacionarias** ⇔ $v_g=0$ con $\omega\neq0$ (Bragg, [p. 125–126]). Como $\sin2ka=2\sin ka\cos ka$: $A\sin ka+4B\sin ka\cos ka=\sin ka\,(A+4B\cos ka)=0$.
- $\sin ka=0$ ⇒ $k=n\pi/a$, $\lambda=2a/n$; dentro de la 1ª ZB, $k=\pi/a$, $\boxed{\lambda=2a}$ (el $k=0$ no cuenta: $\omega=0$, y el límite es $v_g\to v_s$).
- $\cos ka=-A/4B$ (existe solo si $A\le4B$): $k_0=\frac1a\arccos(-A/4B)$, $\lambda_0=\dfrac{2\pi a}{\arccos(-A/4B)}$ — extremo interior de $\omega(k)$ que añade el 2º vecino.

**c) Velocidad del sonido.** $k\to0$: $1-\cos x\approx x^2/2$ ⇒ $\omega^2\approx\frac2M\left[\frac{Aa^2k^2}{2}+\frac{B(2ak)^2}{2}\right]=\frac{a^2k^2}{M}(A+4B)$ ⇒ $\boxed{v_s=a\sqrt{\dfrac{A+4B}{M}}}$ (el 2º vecino pesa 4 veces: $(2a)^2/a^2$).
**d) Densidad de modos y Debye.** Cond. de frontera periódicas $k=2\pi m/L$ ⇒ $L/2\pi$ estados por unidad de $k$; con $\pm k$ (factor 2): $g(k)\,dk=\dfrac Ldk/\pi$ y $g(\omega)\,d\omega=g(k)\,dk$ ⇒ $\boxed{g(\omega)=\dfrac{L}{\pi}\dfrac{1}{v_g(\omega)}}$ (en el cálculo exacto se usa el $v_g$ de a). *Debye:* $\omega=v_sk$ ⇒ $g_D=\dfrac{L}{\pi v_s}$ (constante). Normalización $\int_0^{\omega_D}g_D\,d\omega=N$ ⇒ $\omega_D=\dfrac{N\pi v_s}{L}=\dfrac{\pi v_s}{a}$ (con $L=Na$) ⇒ $\boxed{k_D=\dfrac{\omega_D}{v_s}=\dfrac\pi a}$ (el propio borde de zona: el número de modos no depende de cuántos vecinos se acoplen).
> **Contraste con tu manuscrito:** coincide en $v_g$, en $\lambda=2\pi a/\cos^{-1}(-A/4B)$, en $v_s=a\sqrt{(A+4B)/M}$, en $g(\omega)=L/(\pi v_g)$ y $k_D=\pi/a$.

#### Q3 — Cadena diatómica numérica ✅ (F13) [p. 142–153]
**Datos:** $C=5\times10^3$ dyn/cm $=5$ N/m; $M_1=5.9\times10^{-23}$ g $=5.9\times10^{-26}$ kg; $M_2=3.8\times10^{-23}$ g $=3.8\times10^{-26}$ kg (⚠️ aquí $M_2$ es la **ligera**).
⚠️ *Errata del enunciado:* la $C$ debe multiplicar también la raíz: $\omega^2=C(\tfrac1{M_1}+\tfrac1{M_2})\pm C\sqrt{\cdots}$ (si no, no tiene unidades de $\omega^2$).
**En el borde de la 1ª ZB** ($q=\pi/a$ en la convención del enunciado, $\sin^2=1$): $\sqrt{(\tfrac1{M_1}+\tfrac1{M_2})^2-\tfrac4{M_1M_2}}=|\tfrac1{M_1}-\tfrac1{M_2}|$ ⇒
- Acústica: $\omega^2=\dfrac{2C}{M_{pesada}}=\dfrac{2(5)}{5.9\times10^{-26}}=1.695\times10^{26}$ ⇒ $\boxed{\omega_{ac}=1.30\times10^{13}\ \text{rad/s}}$ ($\nu=2.07$ THz).
- Óptica: $\omega^2=\dfrac{2C}{M_{ligera}}=\dfrac{10}{3.8\times10^{-26}}=2.632\times10^{26}$ ⇒ $\boxed{\omega_{ópt}=1.62\times10^{13}\ \text{rad/s}}$ ($\nu=2.58$ THz).
- Gap: $1.30<\omega<1.62\times10^{13}$ rad/s. (Para completar: $q=0$: acústica $0$; óptica $\sqrt{2C(1/M_1+1/M_2)}=2.08\times10^{13}$ rad/s.)
> **Contraste con tu manuscrito:** aparece $2.163\times10^{26}$ s⁻² $=C(1/M_1+1/M_2)$: es el **centro** de las dos bandas; el borde se obtiene sumando/restando $C|1/M_1-1/M_2|=0.468\times10^{26}$ ⇒ $2.631\times10^{26}$ y $1.695\times10^{26}$ ✓ (coinciden con los valores de arriba).

#### Q4.1 — Verdadero / Falso
**Teoría:** F7, F6, F11, F13, F8 [p. 90–94, 128–141, 153, 114–116].
- **a. VERDADERO.** $C_V$ es función creciente de $T/\theta_D$ (curva universal [p. 90]): $T/\theta_D=0.8$ (A) frente a $0.4$ (B) ⇒ $C_A>C_B$ (A está más cerca de $3R$). Cuanto menor $\theta_D$, más "clásico" a una $T$ dada.
- **b. FALSO.** $\lambda_{min}=2\pi/q_{max}=2\pi/(\pi/a)=2a$: crece con $a$ (más constante de red ⇒ $\lambda_{min}$ **mayor**, no menor).
- **c. FALSO.** No hay "tantos tipos como átomos": hay $3N$ modos (grados de libertad), agrupados en **ramas** (3 acústicas + $3(r-1)$ ópticas para $r$ átomos por celda). Los "tipos" (acústico/óptico, LA/TA) dependen de la estructura de la celda, no del número de átomos.
- **d. FALSO.** El oído detecta $\lesssim20$ kHz; los fonones térmicos tienen $\nu\sim10^{12}$–$10^{13}$ Hz.
> **Contraste con tu manuscrito:** V, F, F, F — coincide.

#### Q4.2 — Conceptuales
**a. ¿Qué fonones contribuyen más a la energía a $T$?** (F8 [p. 102, 84–85]) $dE=\hbar\omega\,g(\omega)\bar n\,d\omega\propto\dfrac{\omega^3}{e^{\hbar\omega/k_BT}-1}$ (Debye). Para $T\ll\theta_D$ el máximo está en $\hbar\omega\approx2.82\,k_BT$ (modos acústicos de baja frecuencia, $\lambda$ larga: son los únicos excitados). Para $T\gtrsim\theta_D$, $\bar n\approx k_BT/\hbar\omega$ y $dE\approx k_BT\,g\,d\omega$ con $g\propto\omega^2$: dominan los de **alta frecuencia**, cerca de $\omega_D$ ($\lambda\to2a$).
**b. Independencia de los modos colectivos** [p. 82–84, 99]: en la aproximación armónica el hamiltoniano se diagonaliza en coordenadas normales, $H=\sum_k\left(\tfrac{p_k^2}{2M}+\tfrac12M\omega_k^2Q_k^2\right)$: cada modo colectivo es un oscilador independiente (no intercambian energía entre sí; cada uno tiene su $\bar n_k$ de BE). Los **átomos**, en cambio, **sí** están acoplados (el desplazamiento de cada átomo es la superposición de todos los modos). Contraste: en Einstein los osciladores independientes son los **átomos individuales** (cada uno vibra en un pozo con los vecinos fijos) y todos tienen **la misma** $\omega_E$ ⇒ un solo nivel de energía; en Debye los osciladores independientes son los **modos** y tienen un **espectro continuo** de $\omega$ ($0\le\omega\le\omega_D$) ⇒ reproduce $T^3$.
**c. Sonido en moléculas pequeñas / gases.** Una onda de sonido (fonón) es una excitación colectiva que necesita $N$ grande y $\lambda\gg a$ en un medio continuo; una molécula pequeña solo tiene modos normales de vibración discretos (no propaga ondas). En gases el sonido no son fonones de red sino **ondas de presión**: la perturbación se transmite por colisiones moleculares (la distancia entre colisiones $\ll\lambda$), el gas se comporta como un medio continuo compresible [p. 45–46, 169–175].
> **Contraste con tu manuscrito:** coincide en lo esencial (fonones colectivos; en gases, ondas de presión por colisiones).

#### Q8 — Momento lineal total con un fonón $q$ ✅ (F16) [sin p.; relacionado con p. 99–100, 110–113]
Modo normal: $u_n(t)=A\,e^{i(qna-\omega t)}$, $q=2\pi m/(Na)$ (cond. periódicas). $P=M\sum_{n=0}^{N-1}\dot u_n=-iM\omega A\,e^{-i\omega t}\displaystyle\sum_{n=0}^{N-1}e^{iqna}$. La suma geométrica es $\dfrac{1-e^{iqNa}}{1-e^{iqa}}=\dfrac{1-e^{2\pi im}}{1-e^{iqa}}=0$ para $m\not\equiv0\pmod N$. $\boxed{P=0}$ (tomando la parte real, lo mismo). Es decir, el fonón **no** transporta momento lineal real: $\hbar q$ es **momento cristalino**, definido solo módulo $\hbar G$ (conservación en colisiones, procesos normales/Umklapp); para $q=0$ el modo es una traslación rígida (no hay fonón).
> **Contraste:** tu manuscrito llega a $P=0$ por la misma suma geométrica.

---

### 3.3 Imágenes `Parcial 1 - 2025-01.jpg` y `Parcial 1(2) - 2025-01.jpg`

**`Parcial 1 - 2025-01.jpg`** contiene, textualmente, **los problemas 1 y 2 del Parcial SS2020**: (1) *conductividad térmica de aisladores $\propto1/T$ a $T>\theta_D$ a partir del número de fonones excitados*; (2) *cadena de $L$, $N$ átomos, $\omega^2=\frac2M[A(1-\cos ka)+B(1-\cos2ka)]$, con a. velocidad de grupo, b. longitudes de onda de ondas estacionarias, c. velocidad del sonido, d. densidad de modos, la de Debye y $k_D$*. **Enunciado y solución completos: ver §3.2, Q1 y Q2** (misma teoría: F8, F7, F14, F12).

**`Parcial 1(2) - 2025-01.jpg` — Problema 5 (jellium).**
*Considerar iones puntuales de masa $M$ y carga $e$ inmersos en un mar uniforme de electrones de conducción. Suponer que los iones están en equilibrio estable cuando ocupan los puntos de la red regular. Si un ion se desplaza una pequeña distancia $r$ de su posición de equilibrio, la fuerza restauradora se debe fundamentalmente a la carga eléctrica dentro de la esfera de radio $r$ centrada en la posición de equilibrio. Tomando la densidad numérica de iones (o electrones de conducción) como $(3/4)\pi R^3$ [sic: debe ser $n=3/(4\pi R^3)$], que define $R$, a. demostrar que la frecuencia de un solo ion que entra en oscilación es $\omega=\left(e^2/\pi\varepsilon_0MR^3\right)^{1/2}$. b. Estimar los valores de esta frecuencia para el sólido. c. A partir de a. y b. estimar el orden de magnitud de la velocidad del sonido en el metal. Sugerencia: usar la ley de Gauss y el teorema de la divergencia.* (La figura muestra una esfera de radio $R$ con densidad de carga $\rho^-$, y el ion $e^+$ desplazado $r$ del centro.)
**Resolución en §3.4, Q4** (es el mismo problema que el Taller SS2020 Q4).

---

### 3.4 `Taller Vibraciones de red(SS2020).pdf` — Taller (8 problemas)

#### Q1. *Usando el modelo de Debye calcular el calor específico de una red monoatómica unidimensional a temperaturas pequeñas comparadas con la temperatura de Debye $\theta_D=\dfrac{\hbar\pi v}{k_Ba}$, donde $v$ es la velocidad del sonido y $a$ la constante de red.* ✅ (F9, F5) [p. 59–62, 84–89 + calor.8 sin p.]
$g(\omega)=\dfrac{L}{\pi v}$ (1D, constante). $E=\int_0^{\omega_D}\dfrac{\hbar\omega\,g}{e^{\hbar\omega/k_BT}-1}d\omega$. A $T\ll\theta_D$ el límite superior $\theta_D/T\to\infty$ (el integrando decae antes) ⇒ con $x=\hbar\omega/k_BT$: $E=\dfrac{L}{\pi v}\dfrac{(k_BT)^2}{\hbar}\int_0^\infty\dfrac{x}{e^x-1}dx=\dfrac{L}{\pi v}\dfrac{(k_BT)^2}{\hbar}\dfrac{\pi^2}{6}=\dfrac{\pi L(k_BT)^2}{6\hbar v}$.
$$\boxed{C_V=\frac{dE}{dT}=\frac{\pi Lk_B^2}{3\hbar v}\,T=\frac{\pi^2}{3}Nk_B\frac{T}{\theta_D}}\quad(L=Na).$$
Lineal en $T$ (en 3D sería $T^3$, en 2D $T^2$).
> **Contraste:** tu manuscrito integra con $\int x/(e^x-1)=\pi^2/6$ ⇒ coincide.

#### Q2. *Considerar una red vibrante $d$-dimensional a temperatura cero. La densidad es $\eta$ y los átomos tienen una masa $m$. Usando la aproximación de Debye y asumiendo que todas las ondas de sonido tienen una velocidad $v$, evaluar: a. el desplazamiento cuadrático medio $\langle R^2\rangle$ para $d=3$. b. $\langle R^2\rangle$ para $d=1$ y discutir su relevancia para el experimento. c. la deformación cuadrática media $\langle(\partial R/\partial x)^2\rangle$ para $d=1$.* (F10, F9) [sin p.; p. 84–88 para Debye]
**Planteamiento.** Modos normales independientes: $\langle R^2\rangle=\dfrac1N\sum_{modos}\dfrac{\hbar}{2m\omega}(2\bar n+1)$. A $T=0$ ($\bar n=0$), con $g_d(\omega)=\dfrac{d^2N\omega^{d-1}}{\omega_D^d}$ (normalizada a $dN$ modos): $\langle R^2\rangle=\dfrac{\hbar}{2mN}\displaystyle\int_0^{\omega_D}\frac{g_d(\omega)}{\omega}d\omega=\frac{d^2\hbar}{2m\omega_D^d}\int_0^{\omega_D}\omega^{d-2}d\omega$.
**a) $d=3$:** $\omega_D=v(6\pi^2\eta)^{1/3}$ ⇒ $\boxed{\langle R^2\rangle=\dfrac{9\hbar}{4m\omega_D}=\dfrac{9\hbar}{4mv(6\pi^2\eta)^{1/3}}}$ (finito; es el mismo resultado del Q7: el punto cero).
**b) $d=1$:** $g=N/\omega_D$ y $\langle R^2\rangle=\dfrac{\hbar}{2m\omega_D}\displaystyle\int\dfrac{d\omega}{\omega}=\dfrac{\hbar}{2m\omega_D}\ln\dfrac{\omega_D}{\omega_{min}}$ → **diverge logarítmicamente** cuando $\omega_{min}\to0$ (modos de $\lambda$ larga, $\omega_{min}\sim\pi v/L$ ⇒ $\langle R^2\rangle\sim\ln N$). *Relevancia:* en 1D el desplazamiento atómico crece sin límite con el tamaño: no hay orden cristalino de largo alcance (ni siquiera a $T=0$), así que el factor de Debye-Waller $e^{-q^2\langle R^2\rangle}$ destruye los picos de Bragg ⇒ no se observa un cristal 1D con difracción nítida (Peierls/Mermin-Wagner). En 3D es finito y el cristal existe.
**c) $d=1$, deformación:** $\partial R/\partial x\to iqR_q$ con $q=\omega/v$ ⇒ $\langle(\partial R/\partial x)^2\rangle=\dfrac{\hbar}{2mv^2N}\displaystyle\int_0^{\omega_D}g\,\omega\,d\omega=\dfrac{\hbar}{2mv^2}\dfrac{\omega_D}{2}=\boxed{\dfrac{\hbar\omega_D}{4mv^2}=\dfrac{\pi\hbar\eta}{4mv}}$ (con $\omega_D=\pi v\eta$): **finito**. Aunque el desplazamiento absoluto diverge, la distorsión *entre vecinos* es pequeña ⇒ el orden local (distancias a primeros vecinos) sobrevive.

#### Q3. *Un material de densidad $\rho$ tiene una red FCC con un cubo de lado $a_0$ y una temperatura de Einstein $\theta_E$. En el límite de temperaturas altas ($T\gg\theta_E$) expresar el desplazamiento cuadrático medio atómico en la dirección $x$ ($\langle u_x^2\rangle$) en términos de $\rho$, $a_0$ y $\theta_E$, más las constantes físicas necesarias.* (F10, F3, F4) [p. 68–71, 77–80; FCC: `notas/00` §5–6]
Una celda cúbica convencional FCC contiene **4 átomos** ⇒ $M=\dfrac{\rho a_0^3}{4}$. Einstein: oscilador 1D independiente de frecuencia $\omega_E=k_B\theta_E/\hbar$. Alta $T$: equipartición, energía potencial media $\tfrac12M\omega_E^2\langle u_x^2\rangle=\tfrac12k_BT$ ⇒
$$\boxed{\langle u_x^2\rangle=\frac{k_BT}{M\omega_E^2}=\frac{\hbar^2T}{Mk_B\theta_E^2}=\frac{4\hbar^2\,T}{\rho\,a_0^3\,k_B\,\theta_E^2}}$$
Comprobación de unidades: $\hbar^2T/(Mk_B\theta_E^2)=\text{J}^2\text{s}^2\cdot\text{K}/(\text{kg}\cdot\text{J/K}\cdot\text{K}^2)=\text{J s}^2/\text{kg}=\text{m}^2$ ✓. (⚠️ el OCR del enunciado dice "$\langle M_x^2\rangle$": es $\langle u_x^2\rangle$.) ∝ $T$: el desplazamiento crece linealmente con $T$ (clásico).

#### Q4. Jellium — *Considerar iones puntuales de masa $M$ y carga $e$ inmersos en un mar uniforme de electrones de conducción… (idéntico al enunciado de §3.3, Parcial 1(2) 2025-01).* ✅ (F17) [p. 42 + enlace.9 sin p.]
**a) Derivación.** $n=\dfrac{3}{4\pi R^3}$ (un electrón por esfera de radio $R$). Densidad de carga $\rho^-=-ne$. Ion desplazado $r\ll R$ del centro: por simetría esférica y **ley de Gauss**, $\oint\vec E\cdot d\vec S=Q_{enc}/\varepsilon_0$ con $Q_{enc}=-ne\cdot\tfrac43\pi r^3=-e(r/R)^3$ ⇒ $E(r)\,4\pi r^2=\dfrac{-e(r/R)^3}{\varepsilon_0}$ ⇒ $E=-\dfrac{er}{4\pi\varepsilon_0R^3}$. Fuerza sobre el ion ($+e$): $F=eE=-\dfrac{e^2}{4\pi\varepsilon_0R^3}\,r$ (restauradora, lineal ⇒ armónico). $M\ddot r=-\dfrac{e^2}{4\pi\varepsilon_0R^3}r$ ⇒ $$\boxed{\omega=\left(\frac{e^2}{4\pi\varepsilon_0MR^3}\right)^{1/2}=\left(\frac{ne^2}{3\varepsilon_0M}\right)^{1/2}}$$ ⚠️ *El enunciado imprime $\pi\varepsilon_0$ (sin el 4): la derivación da $4\pi\varepsilon_0$; la dependencia funcional $\omega\propto\sqrt{e^2/\varepsilon_0MR^3}$ es la misma.*
**b) Estimación (Na).** $n=2.65\times10^{28}$ m⁻³ ⇒ $R=\left(\tfrac{3}{4\pi n}\right)^{1/3}=2.08$ Å; $M=23\,u=3.82\times10^{-26}$ kg ⇒ $\omega=\sqrt{\dfrac{(1.602\times10^{-19})^2}{4\pi(8.854\times10^{-12})(3.82\times10^{-26})(2.08\times10^{-10})^3}}=2.6\times10^{13}\ \text{rad/s}$ ✅ (mismo orden que las frecuencias de red, $10^{13}$ s⁻¹ [p. 111, 152]).
**c) Velocidad del sonido.** $v_s\sim\omega R\approx2.6\times10^{13}\times2.08\times10^{-10}\approx5\times10^3\ \text{m/s}$ ($\sim5\times10^5$ cm/s), del orden correcto (Na real $\approx3\times10^3$ m/s). Idea: $v_s\sim\omega_{max}a/2$ [p. 114–116].
> **Contraste:** tu manuscrito obtiene $\omega=\sqrt{e^2/(4\pi\varepsilon_0MR^3)}$ por Gauss y estima $v_s\approx\omega R$ del orden de $10^3$ m/s ✓ (legible en parte).

#### Q5. *En un cristal de índice de refracción $n=1.5$, en el que la velocidad del sonido es $v=4\times10^5$ cm/s, tiene lugar la dispersión de un fotón de vector de onda $\vec k$ con la absorción de un fonón de vector de onda $\vec q$. Si $k$ y $q$ son del mismo orden de magnitud, calcular la frecuencia de los fonones que se absorben cuando el ángulo de dispersión es $30^\circ$ y la longitud de onda utilizada es de 6000 Å.* ✅ (F15) [sin p.; fonón p. 99–100]
Conservación de energía y de momento cristalino: $\hbar\omega_f=\hbar\omega_i+\hbar\Omega$, $\vec k_f=\vec k_i+\vec q$. Como $\Omega\ll\omega_i$, $|k_f|\approx|k_i|=k=\dfrac{2\pi n}{\lambda_0}$ (λ₀ = longitud de onda en el vacío; $E=\hbar ck/n$) y por la ley de cosenos $q^2=2k^2(1-\cos\theta)=4k^2\sin^2(\theta/2)$:
$k=\dfrac{2\pi(1.5)}{6\times10^{-7}\text{ m}}=1.571\times10^7$ m⁻¹ ⇒ $q=2k\sin15^\circ=8.13\times10^6$ m⁻¹ ⇒ $\Omega=vq=(4\times10^3)(8.13\times10^6)=\boxed{3.25\times10^{10}\ \text{rad/s}}$ ($\nu\approx5.2$ GHz, dispersión de Brillouin). *(Si se interpretara 6000 Å como $\lambda$ dentro del cristal, $k=2\pi/\lambda$ y $\Omega=2.2\times10^{10}$ rad/s.)* La relación lineal $\Omega=vq$ es válida: $q\ll\pi/a$.

#### Q6. *Considerar una red cuadrada bidimensional con un átomo de masa $m$ por punto de red, interactuando solamente con los vecinos más próximos con una constante de fuerza $K$ (la relación de dispersión es $\omega(q)=(4K/m)^{1/2}\sin(qa/2)$). a. Obtener la densidad de estados fonónicos $g(\omega)=dN/d\omega$, es decir el número de modos de vibración por intervalo de frecuencia. b. A temperaturas altas ($k_BT\gg\hbar\omega$), encontrar el desplazamiento cuadrático medio de un átomo de su posición de equilibrio y comentar sobre la estabilidad de cristales bidimensionales.* (F2, F9, F3) [p. 61–66, 136–139 + calor.8 sin p.]
**a)** $\omega_m=\sqrt{4K/m}$, $\omega=\omega_m\sin(qa/2)$ con $q=|\vec q|$ (aproximación isótropa). Estados en $q$ (2D): densidad $A/(2\pi)^2$ ($A=L^2=Na^2$); número con módulo $<q$: $N(q)=\dfrac{A}{4\pi}q^2$ ⇒ $g(\omega)=\dfrac{dN}{d\omega}=\dfrac{A}{2\pi}q\dfrac{dq}{d\omega}$. Con $q=\tfrac2a\arcsin(\omega/\omega_m)$ y $\dfrac{dq}{d\omega}=\dfrac{2}{a\sqrt{\omega_m^2-\omega^2}}$:
$$\boxed{g(\omega)=\frac{2N}{\pi}\frac{\arcsin(\omega/\omega_m)}{\sqrt{\omega_m^2-\omega^2}}}\quad\Big(\xrightarrow{\ \omega\ll\omega_m\ }\ \tfrac{A\omega}{2\pi v^2}\ \text{lineal, Debye 2D}\Big).$$
⚠️ Integrada hasta $\omega_m$ da $\pi N/4$, no $N$: el círculo $|q|\le\pi/a$ cubre $\pi/4$ de la zona cuadrada. Para contar exactamente $N$ se integra sobre el cuadrado de la ZB (o se corta en un $q_D$ con $\pi q_D^2/(4\pi^2)\,A=N$).
**b)** Alta $T$: equipartición, $\tfrac12m\omega_q^2\langle u_q^2\rangle=\tfrac12k_BT$ (modos clásicos). $\langle u^2\rangle=\dfrac1N\sum_q\dfrac{k_BT}{m\omega_q^2}=\dfrac{a^2}{(2\pi)^2}\displaystyle\int\dfrac{k_BT}{m\omega_m^2\sin^2(qa/2)}2\pi q\,dq$. Para $q\to0$: $\sin^2(qa/2)\approx q^2a^2/4$ ⇒ integrando $\approx\dfrac{4}{a^2q}\cdot\dfrac{k_BT}{m\omega_m^2}\cdot\dfrac{a^2}{2\pi}$ ⇒ $\langle u^2\rangle\approx\dfrac{2k_BT}{\pi m\omega_m^2}\ln\dfrac{q_{max}}{q_{min}}=\boxed{\dfrac{k_BT}{2\pi K}\ln\dfrac{L}{a}}$ (con $m\omega_m^2=4K$, $q_{min}\sim2\pi/L$, $q_{max}\sim\pi/a$, hasta factores de orden 1 dentro del log). *Estabilidad:* **diverge logarítmicamente con $L$** ⇒ en 2D el desplazamiento crece sin límite con el tamaño a $T>0$ (Mermin-Wagner/Peierls): no hay orden cristalino de largo alcance estricto (sí cuasi-orden, y el crecimiento es muy lento: $\ln(L/a)$; por eso existen láminas 2D finitas como el grafeno).
> **Contraste:** tu manuscrito llega a $\langle u^2\rangle\sim\dfrac{k_BT}{2\pi K}\ln(\cdots)$ ✓ (legible en parte).

#### Q7. *Estimar el desplazamiento cuadrático medio de los átomos de Li metálico en el límite $T\to0$ debido a la energía de punto cero. La temperatura de Debye del Li es 344 K. Considerar que el desplazamiento cuadrático medio en función del espectro vibracional se expresa como $|u|^2=\dfrac{9\hbar}{M\omega_D^3}\displaystyle\int_0^{\omega_D}(\langle n_\omega\rangle+1/2)\omega\,d\omega$.* ✅ (F10) [sin p.; Debye p. 84–88]
$T\to0$: $\langle n_\omega\rangle=\dfrac{1}{e^{\hbar\omega/k_BT}-1}\to0$ para todo $\omega$ ⇒ solo queda el punto cero: $|u|^2=\dfrac{9\hbar}{M\omega_D^3}\cdot\dfrac12\cdot\dfrac{\omega_D^2}{2}=\dfrac{9\hbar}{4M\omega_D}=\boxed{\dfrac{9\hbar^2}{4Mk_B\theta_D}}$ (con $\hbar\omega_D=k_B\theta_D$). Numérico: $M=6.941\,u=1.153\times10^{-26}$ kg: $|u|^2=\dfrac{9(1.0546\times10^{-34})^2}{4(1.153\times10^{-26})(1.381\times10^{-23})(344)}=4.6\times10^{-22}\ \text{m}^2$ ⇒ $u_{rms}\approx2.1\times10^{-11}$ m $=0.21$ Å ($\sim7\%$ de la distancia interatómica, 3 Å): efecto cuántico notable por ser un átomo ligero y blando.
> **Contraste:** tu valor $4.55\times10^{-22}$ m² coincide (diferencia ≈1 % por el redondeo de la masa: $6.941\,u=11.53\times10^{-27}$ kg).

#### Q8. *Calcular el momento lineal total de un cristal monoatómico unidimensional de $N$ átomos de masa $M$. En este cristal, un fonón con vector de onda $\vec q$ está excitado.*
Mismo problema que Parcial SS2020 Q8: **ver §3.2, Q8** ($P=0$, $\hbar q$ es momento cristalino). F16.

---

### 3.5 `Taller I (2025 II).pdf` (= `Taller I(2025 II).doc`) — Taller I (2025 II), 7 problemas

#### Q1. *Calcular el momento lineal total de un cristal monoatómico unidimensional de $N$ átomos de masa $M$. En este cristal, un fonón con vector de onda $\vec q$ está excitado.*
Igual que §3.2 Q8: $P_{mec}=0$ (F16).

#### Q2. *Las ondas de red de una cadena lineal diatómica puede escribirse como $\omega^2(k)=\alpha(1/M_1+1/M_2)\pm\alpha\left[(1/M_1+1/M_2)^2-4\sin^2(qa/2)/M_1M_2\right]^{1/2}$. Si el valor de $\alpha=5\times10^{13}$ dynas/cm, $M_1=5.9\times10^{-23}$ y $M_2=3.9\times10^{-23}$ g, calcular los valores de las frecuencias permitidas dentro de la primera zona de Brillouin.* ✅ (F13) [p. 142–153]
⚠️ *Errata:* $\alpha=5\times10^{13}$ dyn/cm daría $\omega\sim10^{18}$ rad/s (≈ keV, absurdo); el valor coherente con el Parcial SS2020 es $5\times10^{3}$ dyn/cm (si se usa el valor literal, todas las frecuencias se multiplican por $10^5$).
Con $\alpha=5\times10^3$ dyn/cm $=5$ N/m, $M_1=5.9\times10^{-26}$ kg, $M_2=3.9\times10^{-26}$ kg: la 1ª ZB es $-\pi/a<q\le\pi/a$ (convención del enunciado). Frecuencias permitidas: **dos bandas** separadas por un gap.
- $q=0$: acústica $\omega=0$; óptica $\omega=\sqrt{2\alpha(1/M_1+1/M_2)}=2.06\times10^{13}$ rad/s.
- $q=\pi/a$ (borde): acústica $\sqrt{2\alpha/M_1}=\sqrt{10/5.9\times10^{-26}}=1.30\times10^{13}$ rad/s; óptica $\sqrt{2\alpha/M_2}=\sqrt{10/3.9\times10^{-26}}=1.60\times10^{13}$ rad/s.
- **Banda acústica:** $0\le\omega\le1.30\times10^{13}$; **gap:** $1.30$–$1.60\times10^{13}$; **banda óptica:** $1.60\le\omega\le2.06\times10^{13}$ rad/s.
(El mínimo de la rama óptica está en el borde, el máximo en $q=0$, porque $\omega_{ópt}$ decrece al alejarse de $q=0$.)
> **Contraste:** tu manuscrito evalúa $q=0$ y $q=\pi/a$ y usa $|1/M_1-1/M_2|$ en el borde ✓ (legible en parte).

#### Q3. *La relación de dispersión para una red monoatómica lineal se representa por $\omega^2(k)=(4\alpha/M)^{1/2}\sin(qa/2)$ [⚠️ errata: debe ser $\omega(q)=(4\alpha/M)^{1/2}|\sin(qa/2)|$]. ¿Cuáles serían los valores de $q$ para los cuales las ondas no se propagarían?* (F11) [p. 117–126, 128–134]
"No se propaga" ⇔ $v_g=\dfrac{d\omega}{dq}=0$ (no transporta energía): $\dfrac{d\omega}{dq}=\sqrt{\dfrac{4\alpha}{M}}\dfrac a2\cos\dfrac{qa}{2}=0$ ⇒ $\dfrac{qa}{2}=(2n+1)\dfrac\pi2$ ⇒ $\boxed{q=\dfrac{(2n+1)\pi}{a}}$, $n=0,\pm1,\dots$ En la 1ª ZB: $\boxed{q=\pm\pi/a}$ ($\lambda=2a$): onda estacionaria por reflexión de Bragg ($2a=n\lambda$), los vecinos oscilan en contrafase y $\omega=\omega_m$ [p. 117, 125–127]; los demás valores son el mismo modo físico ($q\equiv q+2\pi/a$). *Segunda lectura:* para $\omega>\omega_m=2\sqrt{\alpha/M}$ no existe $q$ real (filtro pasa-bajos, $q$ complejo ⇒ onda evanescente) [p. 114–116].
> **Contraste:** tu manuscrito: $q=(2n+1)\pi/a$, ondas solo se propagan fuera de $\pm\pi/a$ ✓.

#### Q4. *El modelo de Debye permite calcular la energía del punto cero de un cristal. Un ejemplo sería la estimación de este valor para el helio en estado sólido. En este caso, y similar a los otros gases nobles, la temperatura de Debye es del orden de 24 K.* ✅ (F10) [sin p.; Debye p. 84–88]
$E_0=\int_0^{\omega_D}\tfrac12\hbar\omega\,g(\omega)\,d\omega$ con $g=\dfrac{9N\omega^2}{\omega_D^3}$ ⇒ $E_0=\dfrac{9N\hbar}{2\omega_D^3}\dfrac{\omega_D^4}{4}=\boxed{\tfrac98N\hbar\omega_D=\tfrac98Nk_B\theta_D}$. Para He sólido: por átomo $\tfrac98k_B(24\text{ K})=27\,k_B\cdot\text{K}=3.7\times10^{-22}$ J $=2.3$ meV; por mol $\tfrac98R\,\theta_D=225$ J/mol. (La "forma por volumen" equivalente es $E_0=\dfrac{3V\hbar\omega_D^4}{16\pi^2v_s^3}$.) Es una energía enorme comparada con $k_BT$ a esas temperaturas ⇒ por eso el He solo solidifica bajo presión.
*(Ver también §3.6 Q3: mismo problema; en el `Taller 1 – 01-2025` tu solución llega a la forma $E=3\hbar V\omega_D^4/16\pi^2v_s^3$.)*

#### Q5. *Se tiene un cristal bidimensional a temperaturas bajas. Determinar la dependencia del calor específico con la temperatura para este sistema.* ✅ (F9) [calor.8 sin p.; p. 94–95]
2D: $g(\omega)=\dfrac{A\omega}{2\pi v^2}$ (círculo en $q$ + $\omega=vq$). $T\ll\theta_D$: $E=\dfrac{A}{2\pi v^2\hbar^2}(k_BT)^3\displaystyle\int_0^\infty\dfrac{x^2}{e^x-1}dx=\dfrac{A\zeta(3)(k_BT)^3}{\pi v^2\hbar^2}$ ⇒ $\boxed{C_V=\dfrac{3\zeta(3)Ak_B^3}{\pi\hbar^2v^2}T^2\ \propto T^2}$ ($\zeta(3)=1.202$; con más de una polarización de igual $v$ se multiplica por ese factor). Argumento rápido: modos excitados $\propto q^2\propto T^2$, cada uno $k_BT$ ⇒ $E\propto T^3$.
> **Contraste:** tu manuscrito: $E\propto T^3$ ⇒ $C_V\propto T^2$ ✓.

#### Q6. *Los fonones emitidos por un cristal a una temperatura determinada pueden dispersar a los neutrones. Si la longitud de onda antes de la dispersión es 3.14 Å y luego de esta 5 Å, determinar la longitud de onda del fonón involucrado en la dispersión. El ángulo formado por el vector de onda de los neutrones dispersados ($\vec q'$) y el de los incidentes ($\vec q$) es de 45 grados.* ✅ (F15) [sin p.]
⚠️ *No confundir con el problema del fotón (30°/6000 Å) del Taller SS2020 Q5.*
$k_i=\dfrac{2\pi}{3.14\ \text{Å}}=2.001\times10^{10}$ m⁻¹, $k_f=\dfrac{2\pi}{5\ \text{Å}}=1.257\times10^{10}$ m⁻¹ ($k_f<k_i$: el neutrón pierde energía ⇒ se **crea** un fonón). Conservación de momento cristalino: $\vec k_i=\vec k_f+\vec q_{fon}$ ⇒ ley de cosenos en el triángulo con $\theta=45^\circ$:
$q_{fon}^2=k_i^2+k_f^2-2k_ik_f\cos45^\circ=(4.004+1.579-3.556)\times10^{20}=2.027\times10^{20}$ ⇒ $q_{fon}=1.42\times10^{10}$ m⁻¹ ⇒ $\boxed{\lambda_{fon}=\dfrac{2\pi}{q_{fon}}=4.41\ \text{Å}}$.
*Frecuencia del fonón (bonus, conservación de energía):* $\hbar\Omega=E_i-E_f=\dfrac{\hbar^2(k_i^2-k_f^2)}{2m_n}=8.05\times10^{-22}\ \text{J}=5.0\ \text{meV}$ ⇒ $\Omega=7.6\times10^{12}$ rad/s ($1.2$ THz); $v_{fase}=\Omega/q=5.4\times10^2$ m/s (consistente con un fonón de zona intermedia).

#### Q7. *(a) Si la teoría clásica del calor específico de los sólidos, ¿cuál sería la energía térmica de un mol de Cu a la temperatura $T=\theta_D$? $\theta_D$ del Cu es 340 K. Calcular la energía térmica real de acuerdo con el modelo de Debye (usar la curva de calor específico para el cobre discutida en clase) y compararlo con el valor clásico obtenido en (a). Nota: es posible aproximar la curva de Debye por una línea recta juntando el origen con el punto sobre la curva donde $T=\theta_D$.* ✅ (F3, F5, F7) [p. 68–71, 89–94]
**Clásico:** $E_{cl}=3RT=3(8.314)(340)=\boxed{8.48\ \text{kJ/mol}}$ (3 oscilaciones por átomo, $k_BT$ c/u; $N_Ak_B=R$).
**Debye con la recta de la nota:** $C_V(T)\approx C_V(\theta_D)\dfrac{T}{\theta_D}$ para $0\le T\le\theta_D$ con $C_V(\theta_D)=0.95\times3R=23.7$ J/mol·K [p. 93] ⇒ $E=\displaystyle\int_0^{\theta_D}C_VdT=\tfrac12C_V(\theta_D)\theta_D=\tfrac12(23.7)(340)=\boxed{\approx4.0\ \text{kJ/mol}}$ (≈ 0.48 del clásico).
**Debye exacto (verificación):** $E=9Nk_BT(T/\theta_D)^3\int_0^{\theta_D/T}\frac{x^3}{e^x-1}dx\to9R\theta_D\int_0^1\frac{x^3}{e^x-1}dx=9(8.314)(340)(0.2248)=5.72$ kJ/mol (≈ 0.67 del clásico).
**Conclusión:** la energía térmica real a $T=\theta_D$ es **menor** que la clásica (≈ 50–70 %), porque a $T=\theta_D$ los modos de alta frecuencia aún no están totalmente excitados (la $E$ clásica $3RT$ se alcanza solo a $T\gg\theta_D$). La recta subestima (la curva real es cóncava), por eso 4.0 < 5.7.

---

### 3.6 `Taller 1 - 01-2025(Solucion).pdf` — Taller 1 (2025-01), 4 problemas, con **tu** solución

(Los enunciados son los que aparecen escritos en tu hoja. Los problemas 1–4 coinciden con los de los talleres anteriores.)

#### Q1. *Considerar la relación de dispersión de una red monoatómica lineal $\omega=(4\alpha/M)^{1/2}\sin(ka/2)$. Encontrar los valores de $k$ para los cuales la onda no se propaga.*
Igual que §3.5 Q3: $v_g=0\Rightarrow k=\dfrac\pi a(2n+1)$, $n=0,1,2,\dots$; en la 1ª ZB, $k=\pm\pi/a$. **Tu solución:** exactamente esto (con el recuadro rojo) ✓.

#### Q2. *Estimar el desplazamiento cuadrático medio de los átomos de Li metálico en el límite $T\to0$ debido a la energía de punto cero. $\theta_D(Li)=344$ K. $|u|^2=\dfrac{9\hbar}{M\omega_D^3}\displaystyle\int_0^{\omega_D}(\langle n_\omega\rangle+1/2)\omega\,d\omega$.*
Igual que §3.4 Q7: $|u|^2=\dfrac{9\hbar^2}{4Mk_B\theta_D}\approx4.6\times10^{-22}$ m². **Tu solución:** $4.547\times10^{-22}$ m² ✓ (la pequeña diferencia viene de la masa).

#### Q3. *Calcular la energía de punto cero de un cristal a partir del modelo de Debye. Estimar dicho valor para el helio sólido suponiendo una temperatura del orden de 24 K (valor comparable al de los otros gases nobles).*
Igual que §3.5 Q4: $E_0=\tfrac98Nk_B\theta_D$ ⇒ $\approx2.3$ meV/átomo, 225 J/mol. **Tu solución:** integras $\tfrac12\hbar\omega\,g(\omega)$ con $g=\dfrac{3V\omega^2}{2\pi^2v_s^3}$ [p. 65–66, ec. 3.20] y obtienes $E=\dfrac{3\hbar V\omega_D^4}{16\pi^2v_s^3}$ ✓ (equivale a $\tfrac98N\hbar\omega_D$ usando $\omega_D^3=6\pi^2nv_s^3$). Observación tuya correcta: aquí **no** hay que promediar $\bar\varepsilon=\hbar\omega/(e^{x}-1)$ porque a $T=0$ solo hay $n=0$.

#### Q4. *(a) ¿Si la teoría clásica del calor específico fuera válida, cuál sería la energía de un mol de Cu a la temperatura $T=T_D$? $T_D$ del cobre es 340 K. (b) Calcular la energía térmica real de acuerdo con la teoría de Debye y compare el resultado con el valor clásico (sugerencia: aproximar la curva de Debye por una línea recta uniendo el origen a un punto en la curva de Debye a $T=T_D$). (c) ¿Cuál es el orden de magnitud del desplazamiento máximo de un átomo de Cu a la temperatura de Debye? Comparar este desplazamiento con la distancia interatómica.* ✅ (F3, F5, F10)
**(a)** $E=3RT=3(8.314)(340)=8480$ J/mol. **Tu solución:** $8480.28$ J/mol ✓.
**(b)** Ver §3.5 Q7: recta ⇒ $\approx4.0$ kJ/mol; exacto ⇒ $5.72$ kJ/mol (tú integraste la fórmula de Debye con $x=\hbar\omega/k_BT$ y el valor $\int_0^1x^3/(e^x-1)dx=0.2248$ ✓).
**(c)** Energía por oscilador a $T=\theta_D$: $\sim k_B\theta_D$; si todo es energía de un oscilador con $\omega=\omega_D=k_B\theta_D/\hbar$ y amplitud $A$: $\tfrac12M\omega_D^2A^2=k_B\theta_D$ ⇒ $A=\sqrt{\dfrac{2k_B\theta_D}{M\omega_D^2}}=\sqrt{\dfrac{2\hbar^2}{Mk_B\theta_D}}$. Cu: $M=63.5\,u=1.055\times10^{-25}$ kg ⇒ $A=\sqrt{\dfrac{2(1.1122\times10^{-68})}{(1.055\times10^{-25})(1.381\times10^{-23})(340)}}=6.7\times10^{-12}$ m $=0.067$ Å. Distancia a primeros vecinos en Cu (FCC, $a=3.61$ Å): $2.56$ Å ⇒ $A/d\approx2.6\%$ (**pequeño**: la aproximación armónica es buena; el criterio de Lindemann para fusión es $\sim10$ %). **Tu solución:** $A=\sqrt{2\hbar^2/(Mk_B\theta_D)}$ ✓.

---

### 3.7 `Parcial I (SS2020) - Mi solucion.pdf` y `Talleres Parcial 1 - Mi Solucion.pdf`

Son **tus** manuscritos (a: SS2020 parcial; b: Taller SS2020 y Taller 2025-II). No contienen preguntas nuevas; el "Contraste" de cada problema está en los cuadros de §3.2, §3.4, §3.5 y §3.6. Notas:
- En el cuaderno de talleres hay además una síntesis tuya "**Resumen de los modelos**" (Einstein vs. Debye: supuestos, dominio de validez, por qué Debye reproduce $T^3$ y Einstein no). Si te falla esa comparación, **recupérala de ahí** antes de reexplicarla (ver `analisis_temas.md`).
- La resolución de las imágenes impide verificar cada número; las comparaciones indicadas se hicieron sobre lo legible.

### 3.8 `Apuntes P1-Vibraciones de la Red- E.pdf` (49 pp.)
No contiene preguntas: son los apuntes de clase ya condensados en `notas/*.md`. Úsalos como fuente de teoría (ver §1).

---

## 4. 🍰 PASTEL — lo mínimo que más rinde (leer 10 min antes del parcial)

**A. Los 8 temas que más se repiten (en este orden)**
1. **Debye vs Einstein:** Einstein = osciladores atómicos independientes, **una** $\omega_E$ ⇒ $C_V\sim e^{-\theta_E/T}$ a T baja (falla). Debye = **modos colectivos**, $g\propto\omega^2$ hasta $\omega_D$ ⇒ $C_V\propto T^3$. Ambos → $3R$ a T alta. $\theta_D\propto v_s\propto\sqrt{Y/\rho}$: rígido y ligero ⇒ $\theta_D$ alto.
2. **$C_V\propto T^D$** a T baja (1D: $T$; 2D: $T^2$; 3D: $T^3$). Razón: $g\propto\omega^{D-1}$ / "esfera térmica".
3. **Red:** $\lambda_{min}=2a$; 1ª ZB $|q|\le\pi/a$ ($q\equiv q+2\pi/a$); en $q=\pi/a$, $v_g=0$ = onda estacionaria (Bragg); $\omega\to0$ en $q=0$ pero $v_g\to v_s\ne0$.
4. **Diatómica:** dos ramas (acústica/óptica) por 2 átomos/celda; gap entre $\sqrt{2\alpha/M_{pes}}$ y $\sqrt{2\alpha/M_{lig}}$; acústica $q\to0$: átomos en fase ($A_2/A_1=1$); óptica: contrafase ($-M_1/M_2$), absorbe IR.
5. **Fonón:** BE, $\mu=0$, $\bar n\in(0,\infty)$; $\hbar q$ = momento **cristalino** ($P_{mec}=0$).
6. **$K=\tfrac13C_Vv\ell\propto1/T$** a $T>\theta_D$ ($\bar n\propto T\Rightarrow\ell\propto1/T$, $C_V$=cte). Solo Umklapp resiste.
7. **Punto cero:** no aparece en $C_V$ (constante); $E_0=\tfrac98Nk_B\theta_D$; $\langle u^2\rangle_0=\dfrac{9\hbar^2}{4Mk_B\theta_D}$ (grande si $M$ pequeña / $\theta_D$ baja: Li, He).
8. **NaCl estable:** repulsión cuántica de corto alcance ($A/r^b$, solo 1os vecinos); niveles discretos evitan el colapso; $\alpha_{NaCl}=1.7476$, $\alpha_{1D}=2\ln2$.

**B. Las 12 fórmulas**
| | |
|---|---|
| Monoatómica | $\omega=2\sqrt{\alpha/M}\,\lvert\sin\tfrac{qa}2\rvert$, $v_s=a\sqrt{\alpha/M}$, $v_g=v_s\cos\tfrac{qa}2$ |
| 2os vecinos | $v_s=a\sqrt{(A+4B)/M}$, $v_g=0$ en $\sin ka(A+4B\cos ka)=0$ |
| Diatómica | $\omega^2=\alpha(\tfrac1{M_1}+\tfrac1{M_2})\pm\alpha\sqrt{(\cdots)^2-\tfrac{4\sin^2}{M_1M_2}}$; borde: $\sqrt{2\alpha/M_{pes}}$, $\sqrt{2\alpha/M_{lig}}$; $q=0$ óptica $\sqrt{2\alpha(\tfrac1{M_1}+\tfrac1{M_2})}$ |
| $g(\omega)$ | 1D $L/\pi v$ · 2D $A\omega/2\pi v^2$ · 3D $3V\omega^2/2\pi^2v^3$ · genérica $L/\pi v_g$ |
| $\omega_D$ | $v_s(6\pi^2n)^{1/3}$; $k_B\theta_D=\hbar\omega_D$ |
| Ocupación | $\bar n=1/(e^{\hbar\omega/k_BT}-1)\approx k_BT/\hbar\omega$ (alta T) |
| Einstein | $C_V=3Nk_B x^2e^x/(e^x-1)^2$, $x=\theta_E/T$; $x=1\Rightarrow0.92\cdot3R$ |
| Debye | $C_V=9R(T/\theta_D)^3\!\int_0^{\theta_D/T}\!\frac{x^4e^x}{(e^x-1)^2}dx$; T baja $\frac{12\pi^4}5Nk_B(T/\theta_D)^3$; $T=\theta_D\Rightarrow0.95\cdot3R$ |
| Energía | $E=9Nk_BT(T/\theta_D)^3\!\int_0^{\theta_D/T}\!\frac{x^3}{e^x-1}dx$ ($\int_0^1=0.2248$); pico de $\omega^3/(e^x-1)$ en $x=2.82$ |
| Punto cero | $E_0=\tfrac98Nk_B\theta_D$; $\langle u^2\rangle_0=9\hbar^2/(4Mk_B\theta_D)$ |
| Dispersión inelástica | $E_i=E_f\mp\hbar\Omega$; $q^2=k_i^2+k_f^2-2k_ik_f\cos\theta$; fotón $q=2k\sin\frac\theta2$, $k=2\pi n/\lambda_0$; neutrón $E=\hbar^2k^2/2m_n$ |
| Jellium / otras | $\omega^2=e^2/(4\pi\varepsilon_0MR^3)$; $K=\tfrac13C_Vv\ell$; clásico $3RT=8.5$ kJ/mol (T=340 K) |

**C. Recetas de una línea (los 4 problemas que se repiten)**
- **Diatómica numérica:** pasa a SI → ω en borde = $\sqrt{2C/M}$ (ligera=óptica, pesada=acústica); $q=0$ óptica $=\sqrt{2C(1/M_1+1/M_2)}$.
- **Fotón/neutrón + fonón:** conservación de $E$ y de $\vec k$ → ley de cosenos → $q$ → $\lambda_{fon}=2\pi/q$; $\Omega=vq$ (fotón) o $\hbar\Omega=E_i-E_f$ (neutrón).
- **Punto cero / $\langle u^2\rangle$ / Cu a $\theta_D$:** $\hbar\omega_D=k_B\theta_D$; $T\to0$ ⇒ solo $\tfrac12$; $T=\theta_D$ ⇒ $E\sim3RT\times(0.5\text{–}0.7)$; amplitud $A=\sqrt{2\hbar^2/(Mk_B\theta_D)}$.
- **$C_V$ en $D$ dimensiones:** escribe $g\propto\omega^{D-1}$, integra $\int\hbar\omega\,g/(e^x-1)$ extendiendo a $\infty$ ⇒ $T^D$.

**D. 5 trampas**
1. **rad/s vs Hz** y **cgs vs SI** (dyn/cm→N/m ×10⁻³; g→kg ×10⁻³).
2. En el borde de zona: **ligera ⇒ óptica, pesada ⇒ acústica** (ojo: en SS2020 $M_2$ es la ligera).
3. **Erratas conocidas:** $C$ falta fuera de la raíz (SS2020 Q3); $\alpha=5\times10^{13}$ (debe ser $5\times10^3$); jellium con $\pi\varepsilon_0$ (es $4\pi\varepsilon_0$); $\omega^2=(4\alpha/M)^{1/2}\sin$ (debe ser $\omega=\cdots|\sin|$); P11 en "m/s" (es rad/s).
4. **FCC: 4 átomos por celda convencional** ⇒ $M=\rho a_0^3/4$.
5. $v_g=0$ en $q=\pi/a$ **no** significa que no haya energía: es onda estacionaria; y $\omega=0$ en $q=0$ **no** significa $v_g=0$.

**E. Patrones de opción múltiple (2026-1S)**
- Si la opción dice "**clásico**", "**contribución electrónica**", "**expansión**" o "**$\lambda=a/2$**" → casi siempre distractor.
- Respuestas ganadoras repiten la **causa física**: *medio continuo* (Debye), *distinguibilidad* (MB en Einstein), *Bose-Einstein* (fonones), *niveles discretos* (NaCl estable), *dispersión no trivial* (fonón ≠ fotón), *modos de baja frecuencia* (Debye > Einstein a T baja), *propiedades mecánicas* (θ_D), *primeros vecinos* (Madelung-Born), *pendiente a q pequeño* (velocidad del sonido).
- Verifica unidades antes de elegir en las numéricas (P11: la única con cuenta).

---

## 5. Correcciones detectadas en el banco existente

- `banco_preguntas.md` (calor.10) lista el *Taller 2025-II #6* como "λ=6000 Å, ángulos 30°/45°". **Es**: neutrones con $\lambda_i=3.14$ Å, $\lambda_f=5$ Å y ángulo de 45° (§3.5 Q6). El fotón con $n=1.5$, $v=4\times10^5$ cm/s, 30° y 6000 Å es el *Taller SS2020 #5* (§3.4 Q5).
- `banco_preguntas.md` (calor.6) resume *2026-1S #6* como "los de λ→a"; la respuesta coherente con el curso es **$2a$** (§3.1 P6).
- `banco_preguntas.md` (diatom.1) atribuye el $M_2=3.9\times10^{-23}$ g "según versión" al mismo examen; en realidad pertenece al Taller 2025-II (donde además aparece la errata $\alpha=5\times10^{13}$), mientras que el Parcial SS2020 usa $M_2=3.8\times10^{-23}$ g (§3.2 Q3, §3.5 Q2).

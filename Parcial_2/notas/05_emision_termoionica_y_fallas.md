# Emisión termoiónica y fallas del modelo del e⁻ libre (bloque 5)

> **Nota de origen:** cubre las páginas 92-105 de `Diapositivas/Metales 2021.pdf`.

## 17. Emisión termoiónica y ecuación de Richardson-Dushman (`term.1`)

**Idea:** los e⁻ están ligados al metal por la **función trabajo** $\phi=E_{vacío}-E_F$ (altura de la barrera superficial; el pozo infinito cuadrado es muy simple, se usa un pozo de altura finita). [p. 92-93, 97]

Funciones trabajo ($\phi$ en eV): W 4.5; Ta 4.2; Ni 4.6; Ag 4.8; Cs 1.8; Pt 5.3. [p. 93]

**Mecanismo fundamental:** la energía térmica media de traslación es $\tfrac32k_BT=3.7\times10^{-2}$ eV a 300 K $\ll\phi$: no basta para liberar un e⁻ ni "al rojo incandescente". Pero a cada $T$, la cola de Fermi-Dirac contiene e⁻ con $E\gtrsim E_F+\phi$ (energía ~1 eV por encima de $E_F$) en la fracción $\sim e^{-\phi/k_BT}$ (**factor de Boltzmann**): esos e⁻, si viajan hacia la superficie con momento normal suficiente, escapan. [p. 94-95]

Ejemplo: película de Cs sobre W, $\phi=1.36$ eV $=2.2\times10^{-19}$ J: $e^{-\phi/k_BT}=5\times10^{-24}$ (300 K) y $1.5\times10^{-7}$ (1000 K). [p. 95]

**Otros mecanismos** (partículas externas $\gg$ energía): emisión **fotoeléctrica** (choques con fotones), emisión por **campo** eléctrico intenso. La termoiónica es por choques con partículas vecinas (agitación térmica). [p. 92, 96]

**Corriente de saturación:** si $v_d$ homogénea, $J=nev_d$; en general $J_x=\frac{e}{V}\sum_{\mathbf k}v_x(\mathbf k)$ sobre los estados con $v_x>0$ y energía $E\ge E_F+\phi$, con densidad de estados en $\mathbf k$ igual a $2\cdot V/(2\pi)^3$ y $f$ de Fermi-Dirac → en la cola, $f\to$ Maxwell-Boltzmann ($f\approx e^{E_F/k_BT}e^{-E/k_BT}$). [p. 98-100] Integrando (gaussianas en $k_y,k_z$ e integral de $k_x$ con límite inferior $k_{x,min}=[2m(E_F+\phi)/\hbar^2]^{1/2}$): [p. 100-101]

$$\boxed{J_s=\frac{4\pi m e}{h^3}(k_BT)^2e^{-\phi/k_BT}=A\,T^2e^{-\phi/k_BT}},\qquad A=\frac{4\pi mek_B^2}{h^3}=120\ \text{A/cm}^2\text{K}^2$$

(ecuación de **Richardson-Dushman**; $A$ es un factor universal). $J_s$ crece exponencialmente con $T$ hasta la fusión. [p. 101-102]

**Supuestos y correcciones:** se supuso 100 % de probabilidad de escape para $E_x>E_F+\phi$; en MC la probabilidad de transmisión en el escalón es <1 (y $=0$ para $E=\phi$), lo que añade un factor que reduce $J_s$. [p. 102]

**Efecto Schottky** (dependencia de $\phi$ con el campo eléctrico): $\phi'=\phi-\sqrt{e^3E/4\pi\varepsilon_0}$; combina la fuerza de imagen de Coulomb con el potencial del campo externo ($E\sim10^7$-$10^8$ V/cm baja la barrera ~1 eV). [p. 103]

**Determinación de $\phi$:** (1) obtener $J_{s0}$ (saturación a $E=0$) por extrapolación a campo cero; (2) graficar $\ln(J_{s0}/T^2)$ vs. $1/T$ → pendiente $=-\phi/k_B$. [p. 104]

### Puntos clave para dominar este tema
- Definir $\phi=E_{vacío}-E_F$ y explicar por qué $\tfrac32k_BT$ medio no basta y qué electrones escapan (cola de FD, factor $e^{-\phi/k_BT}$). (`P-2025-01 #4e`)
- Recordar $J_s=AT^2e^{-\phi/k_BT}$, $A=4\pi mek_B^2/h^3=120$ A/cm²K², y el procedimiento de Richardson (gráfica $\ln(J/T^2)$ vs. $1/T$).
- Distinguir termoiónica (térmica), fotoeléctrica (fotones) y por campo; explicar el efecto Schottky.

---

## 18. Fallas del modelo del e⁻ libre (`falla.1`)

1. $\sigma=Ne^2\tau_F/m^*\sim N$: predice $\sigma$ proporcional a la concentración, pero los divalentes/trivalentes y los semimetales no lo cumplen. [p. 105]
2. $R_H>0$ en Be, Zn, Cd: portadores positivos (huecos) que no existen en el modelo.
3. La superficie de Fermi **no es esférica** en la mayoría de metales.
4. No explica por qué hay aislantes/semiconductores. **Solución:** teoría más sofisticada que incluya la interacción e⁻-red (potencial periódico → bandas). (Ver `extra.1` en `06_temas_de_examen_fuera_del_pdf.md`.)

### Puntos clave para dominar este tema
- Listar al menos tres fallas (σ∝N, $R_H>0$, SF no esférica, ausencia de aislantes) y la salida (potencial periódico → bandas).

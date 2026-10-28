# Temas de examen que NO vienen de las diapositivas (bloque 6)

> **Nota de origen:** este archivo **no** sale de `Metales 2021.pdf` y por eso no lleva citas `[p. N]`. Son vacíos detectados en los exámenes viejos de `Parcial_2/Talleres_Parciales/` (ver `examenes/analisis_temas.md`): bandas con electrones casi libres (`P-2025-2S #4b-f`), condición análoga del efecto Zener (`T-SS2020 #1`) y escalas relativistas/astrofísicas (`T-2025-II #3`, `P-2025-2S #2`). Se escribió con conocimiento estándar de la materia; verifícalo contra el material de clase.

## 19. Electrones casi libres: bandas, gaps y la clasificación metal / semiconductor / aislante (`extra.1`)

- **Idea:** al incluir un potencial periódico débil $U(\mathbf r)=U(\mathbf r+\mathbf R)$ sobre el gas libre, los estados con $\mathbf k$ cerca de un plano de Bragg se mezclan: $\mathbf k$ y $\mathbf k-\mathbf G$ con $|\mathbf k|=|\mathbf k-\mathbf G|$, es decir $k=\pm\pi/a$ en 1D (frontera de la zona de Brillouin). Se forma una **brecha** (gap) $E_g=2|U_G|$ en esos valores de $k$; lejos de ellos $\varepsilon(\mathbf k)\approx\hbar^2k^2/2m$ (el modelo libre sigue valiendo).
- **Cuál electrón se afecta más:** el de $\mathbf k$ más cercano a una frontera de zona (donde el libre y el desplazado son degenerados). Ej. $\mathbf k=(\pi,\pi/3,0)$ Å⁻¹ con $a=1$ Å está **sobre** el plano $k_x=\pi/a$ → es el más afectado; $\mathbf k=(10^{-2},0,0)$ está en el centro (el menos afectado). (`P-2025-2S #4f`)
- **Conteo de estados:** cada banda tiene $N$ celdas primitivas → $2N$ estados (con espín). Un cristal con **número par de e⁻ de valencia por celda primitiva** puede llenar bandas completas (aislante o semiconductor) **solo si no hay solapamiento** de bandas; si hay solapamiento (ej. Be, Mg, Zn, Ca: divalentes) es **metal** o semimetal. Por tanto la respuesta a "¿par ⇒ aislante siempre?" es **no**. (`P-2025-2S #4e`)
- **Número impar** de e⁻ por celda primitiva → una banda parcialmente llena → **metal** (alcalinos, nobles).
- **Aislante vs. semiconductor:** misma estructura (banda de valencia llena, banda de conducción vacía, gap $E_g$); el semiconductor tiene $E_g\lesssim2$-3 eV y portadores por excitación térmica ($\sim e^{-E_g/2k_BT}$); el aislante tiene $E_g$ grande.
- **1D:** con e⁻ casi libres sí aparecen gaps en $k=n\pi/a$, así que se pueden tener conductores (banda semillena) y aislantes/semiconductores (bandas llenas) igual que en 3D; la diferencia es que en 3D los gaps de distintas direcciones pueden **solaparse en energía** (sin gap global → metal aunque haya número par de e⁻), mientras que en 1D el gap en $k=\pm\pi/a$ es siempre global. (`P-2025-2S #4b`)
- **Grafito vs. diamante** (`P-2025-2S #4c`): ambos son carbono. En el diamante (sp³, enlaces covalentes localizados) la banda de valencia (llena) y la de conducción (vacía) están separadas por un gap grande ($\approx5.5$ eV) → aislante. En el grafito (sp² en planos + un orbital $p_z$ deslocalizado) las bandas $\pi$ y $\pi^*$ se tocan o solapan ligeramente → conduce en el plano (semimetal).
- **Por qué los alcalinos siguen el modelo de e⁻ libres** (`P-2025-2S #4d`): tienen **un** e⁻ de valencia $s$ por átomo, banda semillena, $E_F$ lejos de las fronteras de zona, seudopotencial muy débil (core compacto, apantallado) y SF casi esférica. Al, Bi (trivalente/semimetal) tienen SF que cruza varias zonas y se deforman.
- **$T_F$ alta y calor específico** (`P-2025-01 #4b`): $T_F\sim5\times10^4$ K implica que a 300 K solo una fracción $T/T_F\sim10^{-2}$ de los e⁻ se excita ⇒ $C_e\propto T$ y ~1 % del clásico; la mayoría de e⁻ están "congelados" por Pauli.

### Puntos clave para dominar este tema
- Explicar cómo un potencial periódico débil abre gaps en las fronteras de zona y cuál electrón es el más afectado.
- Clasificar metal/semiconductor/aislante por llenado de bandas y por la paridad de e⁻ por celda **incluyendo la condición de solapamiento**.
- Interpretar grafito vs. diamante y por qué los alcalinos siguen el modelo libre.

---

## 20. Condición análoga al efecto Zener con campo magnético (`extra.2`)

Efecto Zener: un campo eléctrico fuerte excita e⁻ a través del gap si $eEaE_F/E_g^2>1$. Análogo magnético (ruptura magnética): se sustituye $eE\to e v_FB$ (fuerza de Lorentz) y $ak_F\sim1$:

$$e\,v_F\,B\,a\,\frac{E_F}{E_g^2}>1\ \Rightarrow\ \hbar\omega_c\,E_F\gtrsim E_g^2,\qquad \omega_c=\frac{eB}{m}$$

(`T-SS2020 #1`; no hay solución oficial, contrasta con el enunciado.)

---

## 21. Escalas relativistas y astrofísicas del gas de Fermi (`extra.3`)

- Número de e⁻ de una estrella de masa $M$: $N\approx M/m_p$ (un e⁻ por protón, ionizado); con neutrones, $N\approx M/2m_p$. Sol: $2\times10^{30}$ kg → $N\approx1.2\times10^{57}$.
- Enana blanca ($R=2\times10^9$ cm, `T-2025-II #3a`): $n\approx3.6\times10^{34}$ m⁻³ y $E_F=\frac{\hbar^2}{2m}(3\pi^2n)^{2/3}\approx4\times10^4$ eV $\approx0.08\,mc^2$ (régimen casi no relativista).
- **Límite relativista** ($E\gg mc^2$): $E=pc=\hbar kc$ con el mismo conteo de estados, $k_F=(3\pi^2n)^{1/3}$ ⇒ $\boxed{E_F\approx\hbar c\,(3\pi^2N/V)^{1/3}\sim\hbar c\,(N/V)^{1/3}}$.
- Pulsar ($R=10$ km, `T-2025-II #3c`): $n\approx2.9\times10^{44}$ m⁻³ → $E_F\approx4\times10^8$ eV $\sim10^8$ eV.
- Sol colapsado ($M=2\times10^{30}$ kg, $R=7\times10^8$ m, `P-2025-2S #2`): $E_F\approx32$ eV ($N=M/m_p$) o 20 eV ($N=M/2m_p$), $T_F=E_F/k_B\approx3.7\times10^5$ K, $\langle v\rangle=\tfrac34v_F\approx2.5\times10^6$ m/s.

### Puntos clave para dominar este tema
- Estimar $N$ de una estrella y calcular $E_F$ no relativista; reconocer cuándo $E_F\gtrsim mc^2$ y usar $E_F\approx\hbar c(3\pi^2n)^{1/3}$.
- Dar $T_F$, $v_F$ y $\langle v\rangle=\tfrac34v_F$ para el gas degenerado.

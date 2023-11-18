# Newtonian mechanics of a free falling and bouncing ball
The goal of this is to accurately predict how a point mass will fall onto a curve and bounce off of it, but all inside a single continuous differential equation, where the only discontinuous operator allowed is the $\mathrm{sgn}(x)$ function defined as follows:
```math
\begin{equation}
\mathrm{sgn}(x)=
    \begin{cases}
        -1 & \text{if } x < 0\\
        0 & \text{if } x = 0\\
        1 & \text{if } x > 0
    \end{cases}
\end{equation}
```
## Illustration of the situation
Let $f$ be a continuous (differentiable) function, and a point $A$ of coordinates $(x, y)$ to represent our ball. 

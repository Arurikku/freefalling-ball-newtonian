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
Let $f$ be a continuous (differentiable) function, and a point $A$ of coordinates $(x, y)$ to represent our ball.\
![image_2023-11-19_082242308](https://github.com/Arurikku/freefalling-ball-newtonian/assets/61802068/246e54ee-9350-4860-bb84-1608abd391f3)

In our situation, the ball is either touching the curve or not touching it which can be translated by the following number:
```math
\begin{equation}
\mathrm{\delta_1}(x,y)=
    \begin{cases}
        1 & \text{if } y - f(x) <= 0\\
        0 & \text{if } y - f(x) > 0
    \end{cases}
\end{equation}
```
```math
\text{Which can be rewritten simply as: } \delta_1(x,y) = \frac{1}{2}(1-\mathrm{sgn}(y-f(x)))
```

We will split the force $\overrightarrow{F_n}$ into the force to counteract gravity ($\overrightarrow{F_g}$, and the force to transfer the speed of the ball for the actual bounce ($\overrightarrow{F_v}$), and $\overrightarrow{F_n} = \overrightarrow{F_g} + \overrightarrow{F_v}$.\
For finding $\overrightarrow{F_g}$ and $\overrightarrow{F_v}$ we need to find $\overrightarrow{N}$ the vector normal to the curve at the point $(x,y)$.\
Some quick maths yields $\overrightarrow{N} = \langle -f'(x), 1 \rangle$ (note that this vector is not normalised yet).
```math
\begin{aligned}
&\overrightarrow{F_g}\text{ can be calculated extremely quickly, simply by normalising } \overrightarrow{N} \text{ and scaling it by } ||\overrightarrow{G}||\text{:}\\
&\overrightarrow{F_g} = \frac{||\overrightarrow{G}||}{||\overrightarrow{N}||}\overrightarrow{N}
\end{aligned}
```

## Calculating the force for the bounce
![image_2023-11-19_085901356](https://github.com/Arurikku/freefalling-ball-newtonian/assets/61802068/25c154a0-6802-4885-b486-66cd563a66b2)\
Firstly, we only want the ball to bounce off if the ball is going towards the curve, translated by the following number:
```math
\delta_2(x,y) = \frac{1}{2}(1-\mathrm{sgn}(\overrightarrow{V} \cdot \overrightarrow{N}))
```
Additionally can see that the vector $\overrightarrow{V_{out}}$ is the vector $\overrightarrow{V_{in}}$ reflected through $\overrightarrow{N}$.\
Using the vector reflection formula:
$$\overrightarrow{V_{out}} = \overrightarrow{V_{in}} - 2 \frac{\overrightarrow{V_{in}} \cdot \overrightarrow{N}}{||\overrightarrow{N}||^2} \overrightarrow{N}$$
This can help us find an acceleration induced by $\overrightarrow{F_v}$:
```math
\begin{aligned}
&\overrightarrow{a_v} = \frac{\overrightarrow{V_{out}} - \overrightarrow{V_{in}}}{\Delta t}\\
&\overrightarrow{F_v} = m\overrightarrow{a_v}\\
&\iff \overrightarrow{F_v} = -\frac{2m\overrightarrow{V_{in}} \cdot \overrightarrow{N}}{\Delta t||\overrightarrow{N}||^2}\overrightarrow{N}
\end{aligned}
```
Putting this together with $\overrightarrow{F_g}$, we have: 
```math
\begin{aligned}
&\overrightarrow{F_n} = \delta_1(x,y)\delta_2(x,y)\Bigl(\frac{g}{||\overrightarrow{N}||} - \frac{2\overrightarrow{V_{in}} \cdot \overrightarrow{N}}{\Delta t||\overrightarrow{N}||^2}\Bigr)m\overrightarrow{N}\\
&\text{Applying Newton's second law:}\\
&\overrightarrow{a} = \frac{1}{4}(1-\mathrm{sgn}(y-f(x)))(1-\mathrm{sgn}(\overrightarrow{V} \cdot \overrightarrow{N}))\Bigl(\frac{g}{||\overrightarrow{N}||} - \frac{2\overrightarrow{V_{in}} \cdot \overrightarrow{N}}{\Delta t||\overrightarrow{N}||^2}\Bigr)\overrightarrow{N} + \frac{1}{m}\overrightarrow{G}\\
\end{aligned}
```
## The final differential equation
In the end we have:
```math
\begin{aligned}
\ddot{x} = \frac{1}{4}(1-\mathrm{sgn}(y-f(x)))(1-\mathrm{sgn}(\dot{y} - \dot{x}f'(x)))\Bigl(2\frac{\dot{y} - \dot{x}f'(x)}{\Delta t(1+f'(x)^2)} - \frac{g}{\sqrt{1+f'(x)^2}}\Bigr)f'(x)\\
\ddot{y} = \frac{1}{4}(1-\mathrm{sgn}(y-f(x)))(1-\mathrm{sgn}(\dot{y} - \dot{x}f'(x)))\Bigl(\frac{g}{\sqrt{1+f'(x)^2}} - 2\frac{\dot{y} - \dot{x}f'(x)}{\Delta t(1+f'(x)^2)}\Bigr) - g\\
\end{aligned}
```

Numerically solving this for a few thousand balls with cool initial positions results in some spectacular visuals:
https://github.com/Arurikku/freefalling-ball-newtonian/assets/61802068/1b04f477-c32c-43ff-872f-ccec3a2abd8e

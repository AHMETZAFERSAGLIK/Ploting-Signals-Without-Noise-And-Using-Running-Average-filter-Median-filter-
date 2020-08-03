# Ploting-Signals-Without-Noise-And-Using-Running-Average-filter-Median-filter
Part 4
Discrete time signal x[n] is given input to a linear time-invariant (LTI) FIR filter
with an impulse response of h[n] and the corresponding output signal is y[n],
where x[n] and h[n] are as follows:
x[n] = [n] 􀀀 [n 􀀀 5] + 4[n + 3]; (1)
h[n] = [n] 􀀀 [n + 2] 􀀀 7[n 􀀀 3]:
(a) Write down the difference equation for this signal, and find y[n] by substituting
(1) for input in the difference equation.
(b) Find the output signal y[n] using Python. Plot x[n], h[n] and y[n].

Part 5

Use
 Running Average filter
 Median filter 1
with different parameters on ”suphi noisy.wav”. To do this, you should write
your own convolution function. When implementing convolution, instead of
using many for loops try to adapt numpy operations to faster the process.




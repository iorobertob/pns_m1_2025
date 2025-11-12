import numpy as np
import scipy.io.wavfile as wavfile
from scipy.signal import fftconvolve

# Load the sweep and sweep-wet audio files
sweep_rate, sweep     = wavfile.read("sweep.wav")
wet_rate,   sweep_wet = wavfile.read("sweep_wet.wav")

# Ensure the sampling rates are the same
if sweep_rate != wet_rate:
    raise ValueError("Sampling rates don't match")

# Ensure the input lengths are appropriate
if len(sweep_wet) < len(sweep):
    raise ValueError("'length of sweep_wet' must be longer than 'sweep.wav'.")

# Convolution and Deconvolution operations need a specific 
# length of the buffers. Here we make sure the lengths 
# are correct, and add zeros at the end if they are not.
# Estimating the original length of the impulse response 
# L = lenght of sweep-wet, M = lenght of sweep, 
# N = estimated lenght of impulse response
# if  L = M + N - 1 ,then 

M =  len(sweep)
L =  len(sweep_wet)

N = L - M + 1

# We make the length of L to be a power of 2. 
# It makes the algorithm more efficient.
closest_power_2 = np.ceil(np.log2(L))
new_L           = 2**closest_power_2

sweep     = np.pad(sweep,    (0,int(new_L-M)))
sweep_wet = np.pad(sweep_wet,(0,int(new_L-L)))

######################## 
# START YOUR CODE HERE #
########################

# STEP 1. Peform Fast Fourier Transform on both signals
sweep_fft   = None
wet_fft     = None

# STEP 2. Perform deconvolution in the frequency domain
impulse_fft = None

# STEP 3. Convert back to the time domain
impulse_response = None

######################## 
#  END YOUR CODE HERE  #
########################

impulse_response = impulse_response[0:N]

# Normalize the impulse response to prevent clipping
impulse_response /= np.max(np.abs(impulse_response))



# Save the impulse response to a new file
ir_filename = "ir.wav"
wavfile.write(	ir_filename, 
			sweep_rate, 
			(impulse_response*32767).astype(np.int16))

# Plot the impulse response for visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.title("Impulse Response")
plt.plot(impulse_response)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()

print(f"Impulse response saved to '{ir_filename}'")
# Import necessary libraries
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from skimage.restoration import denoise_wavelet
import noisereduce as nr

# Read the audio file
Fs, x = wavfile.read(
    "files/voice_mono.wav"
)  # Fs is the sampling frequency, x is the audio data

# Normalize the audio signal to the range [-1, 1]
x = x / np.abs(x).max()

# Assuming x_noisy is the noisy version of the signal (use x directly if x is already noisy)
x_noisy = nr.reduce_noise(
    y = x, 
    sr = Fs,
    thresh_n_mult_nonstationary = 0.1,
    sigmoid_slope_nonstationary = 5
    )

# Apply wavelet denoising
x_denoise = denoise_wavelet(
    x_noisy,
    method="VisuShrink",
    mode="soft",
    wavelet_levels=10,
    wavelet="sym20",
    rescale_sigma="True",
)

# Save the denoised audio signal back to a WAV file
wavfile.write("files/voice_mono_denoise.wav", Fs, (x_denoise * 32767).astype(np.int16))


# Function to plot spectrogram in a subplot
def plot_spectrogram(signal, subplot, title, Fs):
    plt.subplot(subplot)
    plt.specgram(signal, Fs=Fs, NFFT=1024, noverlap=512, cmap="viridis")
    plt.title(title)
    plt.ylabel("Frequency (Hz)")
    plt.xlabel("Time (s)")
    plt.colorbar(label="Intensity (dB)")


# Create a figure for plotting
plt.figure(figsize=(12, 8))

# Plot spectrograms for the original and denoised signals
plot_spectrogram(x, 211, "Original Signal Spectrogram", Fs)
plot_spectrogram(x_denoise, 212, "Denoised Signal Spectrogram", Fs)

# Show the plot
plt.tight_layout()
plt.savefig("files/print.png")
plt.show()

import argparse
from pathlib import Path

import numpy as np
import soundfile as sf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.signal import stft


def rd_wav(p, sec=None):
    x, sr = sf.read(p, always_2d=True, dtype="float32")
    if sec is not None:
        n = int(sec * sr)
        x = x[:n]
    return x, sr


def wr_wav(p, x, sr):
    m = np.max(np.abs(x)) if x.size else 0.0
    if m > 0:
        x = 0.99 * x / m
    sf.write(p, x, sr, subtype="PCM_16")


def rfft_filt(x, sr, keep):
    n = x.shape[0]
    xf = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(n, d=1 / sr)
    m = keep(f).astype(np.float32)[:, None]
    y = np.fft.irfft(xf * m, n=n, axis=0).astype(np.float32)
    return y


def lowpass(x, sr, fc):
    return rfft_filt(x, sr, lambda f: f <= fc)


def highpass(x, sr, fc):
    return rfft_filt(x, sr, lambda f: f >= fc)


def bandpass(x, sr, f1, f2):
    return rfft_filt(x, sr, lambda f: (f >= f1) & (f <= f2))


def notch(x, sr, f0, bw):
    f1, f2 = f0 - bw / 2, f0 + bw / 2
    return rfft_filt(x, sr, lambda f: ~((f >= f1) & (f <= f2)))


def plt_wave(png, x, sr, ttl):
    t = np.arange(x.shape[0]) / sr
    y = x[:, 0]
    plt.figure(figsize=(10, 4))
    plt.plot(t, y, linewidth=0.6)
    plt.title(ttl)
    plt.xlabel("time, s")
    plt.ylabel("amp")
    plt.tight_layout()
    plt.savefig(png, dpi=160)
    plt.close()


def plt_spec(png, x, sr, ttl):
    y = x[:, 0]
    n = y.shape[0]
    yf = np.fft.rfft(y)
    f = np.fft.rfftfreq(n, d=1 / sr)
    mag = 20 * np.log10(np.maximum(np.abs(yf), 1e-9))
    plt.figure(figsize=(10, 4))
    plt.plot(f, mag, linewidth=0.6)
    plt.title(ttl)
    plt.xlabel("freq, Hz")
    plt.ylabel("mag, dB")
    plt.xlim(0, min(22050, sr / 2))
    plt.tight_layout()
    plt.savefig(png, dpi=160)
    plt.close()


def plt_stft(png, x, sr, ttl):
    y = x[:, 0]
    f, t, z = stft(y, fs=sr, nperseg=4096, noverlap=3072)
    s = 20 * np.log10(np.maximum(np.abs(z), 1e-9))
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, s, shading="auto")
    plt.title(ttl)
    plt.xlabel("time, s")
    plt.ylabel("freq, Hz")
    plt.ylim(0, min(12000, sr / 2))
    plt.colorbar(label="dB")
    plt.tight_layout()
    plt.savefig(png, dpi=160)
    plt.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    ap.add_argument("--sec", type=float, default=30.0)
    ap.add_argument("--out_dir", default="data/out")
    ap.add_argument("--plt_dir", default="plots")
    a = ap.parse_args()

    outd = Path(a.out_dir)
    pld = Path(a.plt_dir)
    outd.mkdir(parents=True, exist_ok=True)
    pld.mkdir(parents=True, exist_ok=True)

    x, sr = rd_wav(a.inp, sec=a.sec)

    plt_wave(pld / "wave_orig.png", x, sr, "original waveform")
    plt_spec(pld / "spec_orig.png", x, sr, "original spectrum (FFT)")
    plt_stft(pld / "stft_orig.png", x, sr, "original spectrogram (STFT)")

    y1 = lowpass(x, sr, 300.0)
    y2 = highpass(x, sr, 3000.0)
    y3 = bandpass(x, sr, 300.0, 3000.0)
    y4 = notch(x, sr, 1000.0, 200.0)

    wr_wav(outd / "lowpass_300Hz.wav", y1, sr)
    wr_wav(outd / "highpass_3kHz.wav", y2, sr)
    wr_wav(outd / "bandpass_300-3000Hz.wav", y3, sr)
    wr_wav(outd / "notch_1kHz_bw200.wav", y4, sr)

    plt_spec(pld / "spec_lowpass_300Hz.png", y1, sr, "lowpass 300Hz spectrum")
    plt_spec(pld / "spec_highpass_3kHz.png", y2, sr, "highpass 3kHz spectrum")
    plt_spec(pld / "spec_bandpass_300-3000Hz.png", y3, sr, "bandpass 300-3000Hz spectrum")
    plt_spec(pld / "spec_notch_1kHz.png", y4, sr, "notch 1kHz (bw 200Hz) spectrum")

    print("sr:", sr, "sec:", x.shape[0] / sr)
    print("saved wav to:", outd)
    print("saved plots to:", pld)


if __name__ == "__main__":
    main()
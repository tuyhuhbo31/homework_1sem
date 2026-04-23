import argparse
import soundfile as sf


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inp", required=True)
    a = ap.parse_args()

    f = sf.SoundFile(a.inp)
    print("path:", a.inp)
    print("samplerate:", f.samplerate)
    print("channels:", f.channels)
    print("frames:", len(f))
    print("seconds:", len(f) / f.samplerate)
    print("subtype:", f.subtype)
    f.close()


if __name__ == "__main__":
    main()
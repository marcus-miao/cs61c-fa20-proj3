import os
import subprocess

def main():
    assembly_files = os.listdir("inputs")
    assembly_files = [f for f in assembly_files if f.endswith(".s")]

    for f in assembly_files:
        cmd = f"python create-test.py inputs/{f}"
        proc = subprocess.Popen(cmd)
        proc.wait()


if __name__ == '__main__':
    main()
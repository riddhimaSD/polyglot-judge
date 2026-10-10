"""Compile and run a solution in Python, JavaScript, Java or C++ with a time limit, sandboxed in a temp dir."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

EXT = {"python": ".py", "javascript": ".js", "java": ".java", "cpp": ".cpp"}


def _java_bin(name: str) -> str:
    javac = shutil.which("javac")          # use the java that matches javac (PATH may hold an older JRE)
    return str(Path(javac).parent / name) if javac else name


@dataclass
class RunResult:
    verdict: str            # OK | TLE | RE | CE
    stdout: str = ""
    seconds: float = 0.0
    detail: str = ""


class Program:
    def __init__(self, lang: str, source: str):
        self.lang, self.source = lang, source
        self.dir = Path(tempfile.mkdtemp(prefix=f"pj_{lang}_"))
        self.cmd: list[str] | None = None
        self.compile_error = ""

    def build(self) -> bool:
        d = self.dir
        if self.lang == "python":
            (d / "main.py").write_text(self.source, encoding="utf-8")
            self.cmd = [sys.executable, "-I", str(d / "main.py")]
        elif self.lang == "javascript":
            (d / "main.js").write_text(self.source, encoding="utf-8")
            self.cmd = ["node", str(d / "main.js")]
        elif self.lang == "java":
            (d / "Main.java").write_text(self.source, encoding="utf-8")
            r = subprocess.run([_java_bin("javac"), "Main.java"], cwd=d, capture_output=True, text=True)
            if r.returncode:
                self.compile_error = r.stderr[-2000:]
                return False
            self.cmd = [_java_bin("java"), "-Xss64m", "-cp", str(d), "Main"]
        elif self.lang == "cpp":
            (d / "main.cpp").write_text(self.source, encoding="utf-8")
            exe = d / ("main.exe" if os.name == "nt" else "main")
            r = subprocess.run(["g++", "-O2", "-std=c++14", "main.cpp", "-o", exe.name], cwd=d, capture_output=True, text=True)
            if r.returncode:
                self.compile_error = r.stderr[-2000:]
                return False
            self.cmd = [str(exe)]
        else:
            raise ValueError(self.lang)
        return True

    def run(self, stdin: str, timeout_s: float) -> RunResult:
        t0 = time.perf_counter()
        try:
            r = subprocess.run(self.cmd, input=stdin, capture_output=True, text=True, timeout=timeout_s)
        except subprocess.TimeoutExpired:
            return RunResult("TLE", seconds=timeout_s)
        dt = time.perf_counter() - t0
        if r.returncode:
            return RunResult("RE", r.stdout, dt, r.stderr[-500:])
        return RunResult("OK", r.stdout, dt)

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)

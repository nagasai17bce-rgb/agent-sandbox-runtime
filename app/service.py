import subprocess
import time

class Service:
    def run(self, value: str):
        if len(value) > 1000:
            raise ValueError("input exceeds execution limit")
        started = time.time()
        process = subprocess.run(
            ["python", "-c", value],
            capture_output=True,
            text=True,
            timeout=2,
        )
        return {
            "exit_code": process.returncode,
            "stdout": process.stdout[:4000],
            "stderr": process.stderr[:4000],
            "duration_ms": round((time.time() - started) * 1000, 2),
        }

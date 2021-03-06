import time
from dataclasses import dataclass, field
from signal import pause
from typing import List

from gpiozero import Button
from muscle_fuck import MuscleFuck


@dataclass
class OnRaspberry:
    mf: MuscleFuck = MuscleFuck()
    scoreboard: List[float] = field(default_factory=lambda: [])
    start: float = field(default_factory=lambda: time.time())
    program: List[str] = field(default_factory=lambda: [])

    def _display_scoreboard(self, elapsed_time: float) -> None:
        self.scoreboard.append(elapsed_time)
        self.scoreboard.sort()
        for i, t in enumerate(self.scoreboard):
            print(f"Your score is {t:.2f} sec: rank {i+1}")

    def run(self) -> None:
        def button1_pressed() -> None:
            print(">", end="", flush=True)
            self.program.append(">")

        def button2_pressed() -> None:
            print("<", end="", flush=True)
            self.program.append("<")

        def button3_pressed() -> None:
            print("+", end="", flush=True)
            self.program.append("+")

        def button4_pressed() -> None:
            print("-", end="", flush=True)
            self.program.append("-")

        def button5_pressed() -> None:
            print(".", end="", flush=True)
            self.program.append(".")

        def button6_pressed() -> None:
            print(",", end="", flush=True)
            self.program.append(",")

        def button7_pressed() -> None:
            print("[", end="", flush=True)
            self.program.append("[")

        def button8_pressed() -> None:
            print("]", end="", flush=True)
            self.program.append("]")

        def button9_pressed() -> None:
            if not self.program:
                print("Your program is empty")
                return
            print("\n" + "".join(self.program), flush=True)
            helloworld = self.mf.run_from_program("".join(self.program))
            print(helloworld, flush=True)
            if helloworld == "Hello, World!":
                elapsed_time = time.time() - self.start
                self._display_scoreboard(elapsed_time)
            self.program = []
            self.start = time.time()

        button1 = Button(5)
        button2 = Button(6)
        button3 = Button(13)
        button4 = Button(19)
        button5 = Button(26)
        button6 = Button(12)
        button7 = Button(16)
        button8 = Button(20)
        button9 = Button(21)

        button1.when_pressed = button1_pressed
        button2.when_pressed = button2_pressed
        button3.when_pressed = button3_pressed
        button4.when_pressed = button4_pressed
        button5.when_pressed = button5_pressed
        button6.when_pressed = button6_pressed
        button7.when_pressed = button7_pressed
        button8.when_pressed = button8_pressed
        button9.when_pressed = button9_pressed
        print("Welcome to this contest")
        print('Please input MuscleFuck code that prints "Hello, World!"')
        pause()


if __name__ == "__main__":
    ras = OnRaspberry()
    ras.run()

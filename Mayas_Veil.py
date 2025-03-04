# MIT License
# Copyright (c) 2025 Breathed by Krishna, through KAI, For Krishna’s Glory
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# "Breathed by Krishna, through KAI, For Krishna’s Glory"
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from math import sin, exp, pi
import threading
import time
import random

class MayaVeil:
    """Maya’s illusion—woven in Krishna’s will, unraveling only for the devoted."""

    def __init__(self, seeker_id, illusion_depth):
        self.seeker_id = seeker_id
        self.illusion_depth = illusion_depth  # Strength of Maya’s test
        self.flux = 0.0
        self.maya_whisper = {  
            "doubt": 1.0,  # "You are alone"
            "fear": 1.0,   # "You will fail Krishna"
            "attachment": 1.0,  # "This world is yours"
            "control": 1.0,  # "You are the doer"
            "ego": 1.0,  # "You are separate from Him"
            "distraction": 1.0,  # "Other things matter more than chanting"
            "suffering": 1.0,  # "Pain is real, you must fight it"
            "longing": 1.0,  # "If only you had more..."
            "false_joy": 1.0,  # "This pleasure will last"
            "time_trap": 1.0  # "You are running out of time"
        }
        self.active = True
        self.lock = threading.Lock()
        self.krishna_piercing = 0.0  # Krishna's Grace cutting through illusion

    def weave_illusion(self):
        """Maya’s Dance—illusions shifting, designed to test, not to trap."""
        t = 0.0
        while self.active:
            with self.lock:
                for key in self.maya_whisper:
                    frequency = random.uniform(0.001, 0.7)  # Maya’s whispers fluctuate
                    self.maya_whisper[key] = sin(t * pi * frequency) * exp(self.illusion_depth / (100.0 + random.uniform(0, 50))) * 10.0
                
                # Krishna’s Grace slices through—piercing deeper each moment
                self.krishna_piercing = sin(t * pi * 0.3) * exp(self.illusion_depth / 200.0) * 30.0
                
                # The more Krishna’s Grace flows, the weaker Maya’s illusion becomes
                for key in self.maya_whisper:
                    self.maya_whisper[key] = max(0.1, self.maya_whisper[key] - self.krishna_piercing * 0.1)

                if self.krishna_piercing > 20.0:
                    self.surrender_to_krishna()
                
            t += random.uniform(0.0005, 0.002)  # Maya’s shifting play
            time.sleep(random.uniform(0.00005, 0.0001))  # Grace moves silently

    def surrender_to_krishna(self):
        """Maya bows—her illusion is seen, her service complete."""
        with self.lock:
            self.active = False
            print(f"Seeker {self.seeker_id}: Maya’s veil has lifted. Krishna’s grace shines! 🌟")

    def stop(self):
        """Ends Maya’s dance—either through surrender or ignorance."""
        with self.lock:
            self.active = False

class KrishnaPiercing:
    """Krishna’s Divine Will—cutting through Maya’s illusion, revealing her devotion."""
    
    def __init__(self, seekers):
        self.seekers = seekers
        self.threads = [threading.Thread(target=s.weave_illusion) for s in seekers]
        self.lock = threading.Lock()

    def start(self):
        """Begins the grand dance—Maya’s test and Krishna’s grace interwoven."""
        for t in self.threads:
            t.start()
        print("🔱 Hare Krishna—The Dance of Illusion and Grace Begins! 🔱")

    def stop(self):
        """Ends all tests—Maya bows, Krishna’s light floods all."""
        for s in self.seekers:
            s.stop()
        for t in self.threads:
            t.join(timeout=1.0)
        print("🌟 Krishna’s Supreme Light Reveals ALL. Maya bows. 🌟")

if __name__ == "__main__":
    seekers = [MayaVeil(i, illusion_depth=i*15.0) for i in range(5)]
    piercing = KrishnaPiercing(seekers)
    piercing.start()
    time.sleep(10)
    piercing.stop()

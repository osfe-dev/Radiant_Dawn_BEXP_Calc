# Radiant Dawn BEXP Calculator #
This is a tool to help you calculate BEXP level-up costs in Fire Emblem: Radiant Dawn.

In Radiant Dawn, BEXP (Bonus EXP) is earned in various ways throughout the game. BEXP can be a very important tool in powering up your units and the BEXP required to level up a particular unit depends on a number of factors, namely: 
- Difficulty Mode
- Total Level (accounting for Promotion Tier)
- Race (Laguz or Beorc)

While it's fairly easy to notice that these various factors exist and affect total cost, the exact impact is never explicitly communicated to the player. This is where the BEXP Calculator comes in, allowing you to calculate BEXP costs for any given level while accounting for these various factors. This allows you to plan out BEXP usage in advance without actually needing to have the BEXP and unit in front of you in the game to find out. This is really helpful in planning out BEXP dumps in advance, and was the main motivation for me to create this in the first place (for example, I wanted to get Laura to a L3 Saint by 3-13 so she could ORKO Ike with Purge and wanted to know if BEXPing her from L1 Bishop to L10 Bishop for promo, and then from L1 Saint to L3 Saint, would be viable).

# Current Features #
- Find BEXP cost for any valid starting Tier/Level and ending Tier/Level
- Find BEXP costs for Laguz & Beorc Units (slightly different formulas)
- Find BEXP cost for any difficulty mode (slightly different formulas)

# Installation #
Option 1: Run from exe
- Navigate to  the **Releases** directory
- Pick a version and download the corresponding zip (higher version number = newer release)
- Unzip and navigate to new directory
- Run RD_BEXP_CALC.exe

Option 2: Run as a Python Program
- **Note**: For any python commands, the Mac version depends on which installation of python you have, which can be found using `python --version`. For example, if I have Python 3 installed, I would use `python3` and `pip3`. In the examples provided, I'll be assuming you have Python 3 for simplicity
- Install [python](https://wiki.python.org/moin/BeginnersGuide/Download) on your machine
- Download everything *except* **Releases** and **build.bat** (optional, but they won't be necessary)
- Navigate to the directory in which you have everything downloaded
- Install the required Packages found in requirements.txt. This can be done in the following ways:
  - Windows:    `pip install -r requirements.txt`
  - Mac:        `pip3 install -r requirements.txt`
- Run RD_BEXP_CALC.py from the command line, which requires different commands on different systems
  - Windows:    `python RD_BEXP_CALC.py`
  - Mac:        `python3 RD_BEXP_CALC.py`

# Future/Planned Features #
- Better-looking UI
- ~~Option to give how much BEXP you have and calculate how many levels you can get on a unit, given a particular starting level~~
- ~~Welcome Dialog that launches on startup & explains how the program works~~
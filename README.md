# Greek-Hanke-Henry Permanent Calendar (GHH)

**A proposal for a universal, fixed calendar system featuring Greek nomenclature and ISO-8601 synchronization.**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Academic_Research-orange.svg)

## 📄 The Paper
This repository contains the reference implementation for the research paper:

> **The Greek-Hanke-Henry Permanent Calendar** > *Dennis W. K Khong & Gemini 3 Pro* > [Link to arXiv Paper] (Coming Soon)
.
## 📅 What is the GHH System?

The **Greek-Hanke-Henry (GHH)** system is a modification of the Hanke-Henry Permanent Calendar (HHPC). It solves the "Uncanny Valley" problem of calendar reform by replacing traditional Latin month names (January, February...) with the Greek Alphabet (Alpha through Mu).

### Key Characteristics:
1.  **Perpetual Structure:** The year is divided into 4 identical quarters of **30, 30, and 31 days**.
2.  **Fixed Weeks:** Every specific date (e.g., *Alpha 1*) falls on the same day of the week (*Monday*), every single year.
3.  **ISO-8601 Alignment:** The calendar is anchored to the ISO Week Date system. "Alpha 1" is always the Monday of ISO Week 1.
4.  **Omega Week:** Instead of a leap day, a 7-day "Leap Week" (named **Omega**) is added to the end of the year roughly every 5-6 years to synchronize with the solar cycle.

| Month | Name | Days | Fixed Start Day |
| :--- | :--- | :--- | :--- |
| 1 | **Alpha** | 30 | Monday |
| 2 | **Beta** | 30 | Wednesday |
| 3 | **Gamma** | 31 | Friday |
| ... | ... | ... | ... |
| 13 | **Omega** | 07 | Monday (Leap Week Only) |

## 🚀 The Python Implementation

The included script `ghh_calendar.py` is a robust calculator and visualization tool for the GHH system.

### Features
* **Date Conversion:** Convert any Gregorian date (past or future) into its GHH equivalent.
* **Omega Logic:** Automatically detects and handles "Omega Weeks" (ISO Week 53).
* **Visual Calendar:** Generates a "Box Drawing" wall calendar using Unicode characters ($U+2500$) for misalignment-proof display in word processors.

### How to Run
Prerequisites: **Python 3.x** (No external libraries required).

```bash
python3 ghh_calendar.py

# RoadScan

**English** · [Hrvatski](README_HR.md)

RoadScan is a legacy field system for mobile radio-frequency spectrum mapping.
During each measurement cycle, the software associates a position from an
external GPS receiver with a spectrum trace acquired from a Rohde & Schwarz
FSH6 spectrum analyzer, adds a UTC timestamp from the host system, and stores
the results as CSV and PNG files.

The system completed multiple real-world measurement drives during different
periods of use, including sessions lasting several hours. The hardware- and
operating-system-level workarounds found in the code should therefore be
understood in the historical and operational context in which they were
introduced, rather than as evidence that the system was not functional.

## Original Motivation

RoadScan was created to provide an indicative, independent field assessment of
how closely the actual coverage of radio and communications services matched
publicly declared information and the obligations imposed on network operators
by their assigned licenses. The measurements were not intended as conclusive
regulatory evidence or as an enforcement tool. Instead, they provided an
indicative overview of network conditions that could identify areas warranting
closer investigation and offer useful information to network operators, the
regulator, and end users.

The measured received signal level is a necessary, but not sufficient,
condition for achieving a specified connection quality. If, at a particular
location and under the conditions of the measurement, the signal level is below
the required threshold, the declared quality is not theoretically achievable
there. A level above the threshold establishes only the basic RF prerequisite;
connection quality, data rate, latency, and availability also depend on
interference, signal-to-noise ratio, capacity, network load, and other factors.

The aggregate `measlog.csv` is used for the subsequent generation of a KML
route with links to individual spectrum traces.

```text
GPS + FSH6 + INI measurement profile
          │
          v
    measurement cycle
          │
          ├── CSV for an individual trace
          ├── measlog.csv
          └── spectrum PNG
                    │
                    v
                KML export
```

The software acquires GPS and FSH6 data sequentially; the existing code does
not guarantee that they are simultaneous or that they share a common time
reference.

## Development Versions

The repository contains several generations of the application:

- `gpspectrum.py` — the original monolithic command-line application;
- `roadscan-cli.py` — a newer command-line version;
- `roadscan-gui.py` — a Tkinter GUI built on the newer hardware layer;
- `maplayer.py` and `maplayer-gui.py` — post-processing tools that export
  `measlog.csv` to KML.

The final development target was Python 2.7 on Linux. Historical operation with
the actual FSH6/GPS setup is confirmed by field measurements, but the preserved
revision has not been retested with a current Python version, a contemporary
Linux system, or a potentially different FSH6 firmware version. Dependencies
are neither pinned nor exhaustively declared. The launcher scripts document
the historical field environment rather than a currently reproducible
installation procedure.

## Documentation

A detailed description of the development branches, modules, measurement
workflow, serial protocol, data formats, visualization, and known problem areas
is available in Croatian:

- [Architecture and known problem areas](docs/arhitektura-i-poznati-problemi.md)

The documentation explicitly distinguishes confirmed software defects,
confirmed FSH6 protocol requirements, and other historical workarounds that
should be validated against captured communication with the actual hardware
before being altered.

# Automatic Music Generation System

This project uses deep learning to generate original Irish folk tunes and Bob Dylan-inspired lyrics. Leveraging Long Short-Term Memory (LSTM) networks—a type of Recurrent Neural Network (RNN)—the system captures stylistic elements unique to both Irish folk music and Bob Dylan's lyrical style.

## Table of Contents
- [Objectives](#objectives)
- [Datasets](#datasets)
- [Model Architecture](#model-architecture)
- [ABC Music Format](#abc-music-format)
- [Implementation Resources](#implementation-resources)
- [Running the Project](#running-the-project)

---

## Objectives

The project aims to:
1. **Generate Irish Folk Tunes**: Compose new tunes that follow traditional Irish folk music structure.
2. **Generate Bob Dylan-Style Lyrics**: Emulate the lyrical tone and structure characteristic of Bob Dylan’s songwriting.


## Datasets
**Irish Folk Music**: Datasets in ABC notation format compiled from:
  - [O'Neill's Irish Music Collection](http://trillian.mit.edu/~jc/music/book/oneills/1850/X/)
  - [Cobb’s Tunebook](http://cobb.ece.wisc.edu/irish/Tunebook.html)
  - [Nottingham Music Database](http://abc.sourceforge.net/NMD/)

  These were scraped, cleaned, and merged into a single file to create a robust corpus for model training.

**Bob Dylan Lyrics**: Lyrics were scraped from [Bob Dylan’s official website](http://bobdylan.com/songs/). This text corpus (~700KB) provides a small yet rich dataset suitable for training an RNN to generate Dylan-style lyrics. **Note:** Due to copyright reasons, the dataset is not included in this repository.

---

## ABC Music Format

ABC notation is a compact, text-based format for transcribing music. It uses symbols and single-letter fields to represent music data, including metadata and melody. Here's an example tune:

```
:174
T:Julia Delaney
Z: id:dc-reel-161
M:C
L:1/8
K:D Minor
A|dcAG F2DF|E2CE F2DF|dcAG F2DF|Add^c defe|!
```

- **Notation Fields**:
  - `X`: Reference number
  - `T`: Title
  - `Z`: Transcription ID
  - `M`: Meter
  - `L`: Default note length
  - `K`: Key signature

Generated ABC files can be converted to MIDI, WAV, or OGG formats for playback.

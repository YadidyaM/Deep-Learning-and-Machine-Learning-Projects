Automatic Music Generation System
This project uses deep learning to generate original Irish folk tunes and Bob Dylan-inspired lyrics. Leveraging Long Short-Term Memory (LSTM) networks—a type of Recurrent Neural Network (RNN)—the system captures stylistic elements unique to both Irish folk music and Bob Dylan's lyrical style.

Table of Contents
Objectives
Datasets
Model Architecture
ABC Music Format
Implementation Resources
Running the Project
Objectives
The project aims to:

Generate Irish Folk Tunes: Compose new tunes that follow traditional Irish folk music structure.
Generate Bob Dylan-Style Lyrics: Emulate the lyrical tone and structure characteristic of Bob Dylan’s songwriting.
Datasets
Irish Folk Music: Datasets in ABC notation format compiled from:

O'Neill's Irish Music Collection
Cobb’s Tunebook
Nottingham Music Database
These were scraped, cleaned, and merged into a single file to create a robust corpus for model training.

Bob Dylan Lyrics: Lyrics were scraped from Bob Dylan’s official website. This text corpus (~700KB) provides a small yet rich dataset suitable for training an RNN to generate Dylan-style lyrics. Note: Due to copyright reasons, the dataset is not included in this repository.

Model Architecture
The system uses a character-level Recurrent Neural Network (Char-RNN), inspired by Andrej Karpathy’s approach to RNN-based text generation. Key parameters include:

Model Type: Supports lstm, rnn, or gru, with lstm typically performing best.
Parameters:
batch_size: Number of sequences per mini-batch.
sequence_length: Number of characters per sequence.
n_cells: Number of units in each LSTM layer.
n_layers: Number of LSTM layers.
ckpt_name: Checkpoint file name for saving model weights.
learning_rate: Typically set to 0.001 or lower for gradual learning.
Why Char-RNN?
Character-level RNNs break down text into individual characters, allowing the model to learn sequences at the character level. This is effective for handling structured text formats, such as ABC notation for music and stylized lyric patterns.

ABC Music Format
ABC notation is a compact, text-based format for transcribing music. It uses symbols and single-letter fields to represent music data, including metadata and melody. Here's an example tune:

makefile
Copy code
:174
T:Julia Delaney
Z: id:dc-reel-161
M:C
L:1/8
K:D Minor
A|dcAG F2DF|E2CE F2DF|dcAG F2DF|Add^c defe|!
Notation Fields:
X: Reference number
T: Title
Z: Transcription ID
M: Meter
L: Default note length
K: Key signature
Generated ABC files can be converted to MIDI, WAV, or OGG formats for playback.

Implementation Resources
This project builds upon several resources for deep learning and music generation:

RNN-based Music Generation: Folk Music Generation by Bob Sturm
WaveNet by DeepMind: A convolutional music generation model: Keras WaveNet GitHub Repository

## CI-SDES - Aaron Urrea
 - Course: COMP-424 Computer System Security
 - Professor: Sami Al-Salman

# DES Encryption Program

## Table of Contents
- [Description](#description)
- [Implementation](#implementation)
- [Purpose](#purpose)
- [Usage](#usage)
- [License](#license)
- [Author](#author)

## Description
This repository contains a Python program that implements the Data Encryption Standard (DES) algorithm for encrypting data. DES is a symmetric key encryption algorithm that operates on 64-bit blocks of data using a 56-bit key. The program takes a 10-bit key and an 8-bit plaintext as input and produces the corresponding ciphertext using two rounds of encryption.

## Implementation
The program consists of three main files:
1. `main.py`: This file contains the main function that handles user input and calls the encryption function.
2. `encrypt.py`: This file contains the implementation of the encryption process, including initial permutation, expanded permutation, XOR operations, S-box operations, and permutation.
3. `DES.py`: This file contains the function that generates two subkeys (K1 and K2) from the 10-bit input key.

## Purpose
The purpose of this program is to demonstrate a basic implementation of the DES encryption algorithm. It is intended for educational and learning purposes only and may not be suitable for production use. The code may not be optimized for performance or security.

## Usage
To use the program, follow these steps:
1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the `main.py` script in your terminal or command prompt.
4. Enter a 10-bit key when prompted. If the input is not a valid 10-bit key, an error message will be displayed.
5. Enter an 8-bit plaintext when prompted. If the input is not a valid 8-bit plaintext, an error message will be displayed.
6. The program will display the 10-bit key, 8-bit plaintext, and the resulting ciphertext after encryption.

## License
This program is provided under the [MIT License](LICENSE).


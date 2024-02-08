# Caesar Cipher GUI

## Introduction
This is a simple graphical user interface application built with Python using the Tkinter library. It allows users to encode, decode, and perform brute-force attacks on messages using the Caesar Cipher encryption technique.

## Features
- Encode text using a specified shift value.
- Decode text using a specified shift value.
- Perform a brute-force attack to decode text by trying all possible shift values.
- Adjustable font size for the output area.
- Responsive GUI layout.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- The following Python libraries:
  - `tkinter`
  - `scrolledtext`

## Usage
1. Clone this repository to your local machine or download the files.
2. Run the `caesar_cipher.py` script using Python:
   ```bash
   python3 caesar_cipher.py
   ```
3. The GUI window will appear, allowing you to enter text, specify shift values, and perform various operations.

## Instructions
- **Encode**: Enter the text you want to encode in the "Enter Text" field, specify the shift value in the "Enter Shift" field, and click the "Encode" button.
- **Decode**: Enter the text you want to decode in the "Enter Text" field, specify the negative shift value in the "Enter Shift" field (e.g., if the text was encoded with a shift of 3, enter -3 to decode it), and click the "Decode" button.
- **Brute Force**: Enter the encoded text in the "Enter Text" field and click the "Brute Force" button to perform a brute-force attack and display all possible decoded messages for each shift value.
- **Options**: Click the "Options" button to adjust the font size of the output area.

## Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

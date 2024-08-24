# SecureImage: A Python-Based Image Encryption Decryption Tool

# Developed by Kanishk Kumar 

**SecureImage** is a Python-based tool for encrypting and decrypting images using a simple XOR encryption algorithm. It features a graphical user interface (GUI) built with Tkinter for easy interaction.

## Features

- **Image Encryption**: Encrypt images using a randomly generated key.
- **Image Decryption**: Decrypt images using the provided key.
- **Save and Load Images**: Save and load both encrypted and decrypted images.
- **Key Management**: Save and load encryption keys.
- **User-Friendly GUI**: Easy-to-use interface for performing encryption and decryption operations.

## Installation

To run this project, you'll need to have Python and some libraries installed. Follow these steps to set up the environment:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool.git
   cd SecureImage

  Install Dependencies<br>

2.You need Python 3 and the following libraries: <br>

    pip install pillow opencv-python numpy

3.Run the Application<br>

    python SecureImage.py

<h1>Usage</h1><br>
Choose an Image: Click on the "Choose" button to select an image for encryption or decryption.<br>
Encrypt: Click the "Encrypt" button to encrypt the selected image.<br>
Decrypt: Click the "Decrypt" button to decrypt an encrypted image. You need to upload the encrypted image and the corresponding encryption key.<br>
Save: Save the original, encrypted, or decrypted images using the "Save" button.<br>
Download Encrypted Image: Download the encrypted image using the "Download Encrypted Image" button.<br>
Download Key: Download the encryption key using the "Download Key" button.<br>
Upload Encrypted Image and Key: Upload an encrypted image and its corresponding key using the "Upload Encrypted Image and Key" button.<br>
Download Decrypted Image: Download the decrypted image using the "Download Decrypted" button.<br>
Reset: Reset the displayed image to its original form using the "Reset" button.<br>
<br>
<br>

[1](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/1.png)
[2](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/2.png)
[3](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/3.png)
[4](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/4.png)
[5](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/5.png)
[6](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/6.png)
[7](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/7.png)
[8](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/8.png)
[9](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/8.png)
[9](https://github.com/bleak14midwinter/SecureImage-A-python-based-image-Encryption-Decryption-Tool-using-XOR-encryption/blob/main/images/new.png)




Steps to package your application:

1.Install PyInstaller:

   pip install pyinstaller

2.Package your script: Navigate to the directory where your script is located and run the following command:

   pyinstaller --onefile --noconsole your_script.py
   
--onefile: Bundles everything into a single executable file.
--noconsole: (optional) Suppresses the terminal window when running the GUI application.
Locate the Executable: After the command runs, you’ll find the executable in the dist directory.

3. Add Application Icons:
To make your application look professional, you can add an icon:

Convert your icon image to .ico format if it isn't already.
Use the --icon option with PyInstaller:

   pyinstaller --onefile --noconsole --icon=your_icon.ico your_script.py


<h1>Example Workflow</h1><br>
Choose: Select an image file.<br>
Encrypt: Encrypt the selected image.<br>
Download Encrypted Image: Save the encrypted image to your system.<br>
Upload Encrypted Image and Key: Upload the encrypted image and the key you saved earlier.<br>
Decrypt: Decrypt the uploaded image.<br>
Download Decrypted Image: Save the decrypted image to your system.<br>

<h1>Contributing</h1><br>
Feel free to contribute to this project by submitting issues or pull requests. Please follow the project's code of conduct and contribution guidelines.<br>

<h1>License</h1><br>
This project is licensed under the MIT License - see the LICENSE file for details.<br>

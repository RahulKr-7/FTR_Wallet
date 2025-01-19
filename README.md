# Future FTR Wallet  

## Overview  
The **Future FTR Wallet** is a Python-based wallet designed to interact with the Future (FTR) blockchain. It includes features like wallet creation, balance checking, transaction signing, QR code handling, transaction history viewing, and seamless switching between testnet and mainnet environments.  

---

## Features  
### **Core Features**  
1. **Wallet Creation**:  
   - Generate a secure wallet with a private/public key pair.  
   - Import existing wallets using private keys in PEM format.  

2. **Check Balance**:  
   - Retrieve wallet balances from the FTR blockchain.  

3. **Send Transactions**:  
   - Sign transactions securely and send them to other wallet addresses.  

4. **QR Code Integration**:  
   - Generate QR codes for wallet addresses or other data.  
   - Scan QR codes to extract payment details like recipient address and amount.  

5. **Transaction History**:  
   - Fetch and display recent transactions for the wallet.  

6. **Network Switching**:  
   - Switch easily between **FTR mainnet** and **testnet** using RPC endpoints.  

---

## Installation  

### **Prerequisites**  
1. Install Python (3.8 or later).  
2. Install `pip` for managing Python packages.  

### **Steps**  
1. **Clone the Repository**:  
   git clone <repository-url>
   cd Future-FTR-Wallet

2. **Install Dependencies**:
   Run the following command to install all required Python packages:
   
   pip install -r requirements.txt

3. **Run the Wallet Application**:
    
   python ftr_wallet.py

## **How to Use**

# **Wallet Menu*
Once the wallet application starts, you'll see a menu with the following options:

1.**Create New Wallet**:
Generates a new wallet and displays the private/public key pair.

2.**Import Wallet**:
Allows you to import an existing wallet using a PEM-encoded private key.

3.**Check Balance**:
Retrieves and displays your wallet balance from the FTR blockchain.

4.**Send Transaction**:
Sends FTR to a recipient address after signing the transaction.

5.**Generate QR Code**:
Generates a QR code for wallet data and saves it as an image file.

6.**Exit**:
Exits the application.

## *Challenges Faced*

1. *Integrating JSON-RPC*: Ensuring seamless communication with the Future (FTR) blockchain required careful implementation of the JSON-RPC protocol.
   
2. *Key Management*: Private keys are securely generated and handled to prevent accidental exposure.
   
3. *Real-time QR Code Scanning*: Integrated cv2 for live QR code scanning while ensuring robust performance.
   
4. *Network Switching*: Dynamically switching between testnet and mainnet required careful endpoint handling.


## **How It Works**

**Wallet Creation**
Generates an ECDSA key pair and calculates the wallet address using SHA-256.
1. Private keys are stored securely during runtime.
   
**Balance Check**
Interacts with the FTR blockchain via the JSON-RPC API to retrieve the balance for the wallet address.

**Transaction Signing & Sending**
1.The private key is used to sign transactions securely.
2.Signed transactions are broadcast to the blockchain using the sendtoaddress RPC method.

**QR Code Features**
1.Generates QR codes for wallet addresses or other data using the qrcode library.
2.Uses cv2 to scan QR codes for payment details like recipient address and amount.


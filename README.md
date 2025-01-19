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

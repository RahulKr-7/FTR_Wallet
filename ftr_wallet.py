import os
import qrcode
import requests
import base64
import cv2
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.exceptions import InvalidSignature

# JSON-RPC Handler for Future Blockchain
class FutureRPC:
    def __init__(self, rpc_url, rpc_user, rpc_password):
        self.url = rpc_url
        self.auth = (rpc_user, rpc_password)

    def call(self, method, params=None):
        payload = {"jsonrpc": "2.0", "id": "1", "method": method, "params": params or []}
        response = requests.post(self.url, json=payload, auth=self.auth)
        if response.status_code == 200:
            return response.json().get("result")
        else:
            raise Exception(f"RPC Error: {response.text}")

# Wallet Class
class Wallet:
    def __init__(self, rpc_url, rpc_user, rpc_password):
        self.private_key = None
        self.public_key = None
        self.blockchain = FutureRPC(rpc_url, rpc_user, rpc_password)

    def create_wallet(self):
        self.private_key = ec.generate_private_key(ec.SECP256R1())
        self.public_key = self.private_key.public_key()
        print("Wallet Created!")
        self.show_keys()

    def import_wallet(self, private_key_pem):
        try:
            self.private_key = serialization.load_pem_private_key(
                private_key_pem.encode(), password=None
            )
            self.public_key = self.private_key.public_key()
            print("Wallet Imported Successfully!")
            self.show_keys()
        except Exception as e:
            print(f"Error importing wallet: {e}")

    def show_keys(self):
        private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode()
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode()
        print(f"Private Key: {private_key_pem}")
        print(f"Public Key: {public_key_pem}")

    def get_address_from_public_key(self):
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode()
        digest = hashes.Hash(SHA256())
        digest.update(public_key_pem.encode())
        return digest.finalize().hex()

    def check_balance(self):
        try:
            address = self.get_address_from_public_key()
            balance = self.blockchain.call("getbalance", [address])
            print(f"Your balance: {balance} FTR")
        except Exception as e:
            print(f"Error checking balance: {e}")

    def send_transaction(self, receiver, amount):
        try:
            sender_address = self.get_address_from_public_key()
            signature = self.sign_transaction(amount)
            result = self.blockchain.call("sendtoaddress", [receiver, amount, signature])
            if result:
                print("Transaction sent successfully!")
            else:
                print("Transaction failed.")
        except Exception as e:
            print(f"Error sending transaction: {e}")

    def sign_transaction(self, amount):
        signature = self.private_key.sign(
            str(amount).encode(), ec.ECDSA(hashes.SHA256())
        )
        return base64.b64encode(signature).decode()

    def generate_qr_code(self, data, filename="wallet_qr.png"):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filename)
        print(f"QR Code saved as {filename}")

    def scan_qr_code(self):
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            data, _, _ = detector.detectAndDecode(img)
            if data:
                print(f"Scanned QR Code Data: {data}")
                cap.release()
                cv2.destroyAllWindows()
                return data
            cv2.imshow("QR Code Scanner", img)
            if cv2.waitKey(1) == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

    def fetch_transaction_history(self, count=10):
        try:
            transactions = self.blockchain.call("listtransactions", ["*", count])
            for tx in transactions:
                print(f"Transaction ID: {tx['txid']}, Amount: {tx['amount']}, Confirmations: {tx['confirmations']}")
        except Exception as e:
            print(f"Error fetching transactions: {e}")

    def switch_network(self):
        print("1. Connect to Mainnet")
        print("2. Connect to Testnet")
        choice = input("Enter your choice: ")
        if choice == "1":
            self.blockchain.url = "http://mainnet.rpc.url:port"
        elif choice == "2":
            self.blockchain.url = "http://testnet.rpc.url:port"
        else:
            print("Invalid choice.")

# Main Menu
def main():
    rpc_url = "http://localhost:38332"  
    rpc_user = "your_rpc_user"         
    rpc_password = "your_rpc_password" 

    wallet = Wallet(rpc_url, rpc_user, rpc_password)

    while True:
        print("\nFuture (FTR) Wallet Menu:")
        print("1. Create New Wallet")
        print("2. Import Wallet")
        print("3. Check Balance")
        print("4. Send Transaction")
        print("5. Generate QR Code")
        print("6. Scan QR Code")
        print("7. Fetch Transaction History")
        print("8. Switch Network")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            wallet.create_wallet()
        elif choice == "2":
            private_key_pem = input("Enter your private key (PEM format): ")
            wallet.import_wallet(private_key_pem)
        elif choice == "3":
            wallet.check_balance()
        elif choice == "4":
            receiver = input("Enter receiver's public key: ")
            amount = float(input("Enter amount to send: "))
            wallet.send_transaction(receiver, amount)
        elif choice == "5":
            data = input("Enter data for QR code: ")
            wallet.generate_qr_code(data)
        elif choice == "6":
            wallet.scan_qr_code()
        elif choice == "7":
            wallet.fetch_transaction_history()
        elif choice == "8":
            wallet.switch_network()
        elif choice == "9":
            print("Exiting wallet. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

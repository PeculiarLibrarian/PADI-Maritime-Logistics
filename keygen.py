from nacl.signing import SigningKey
signing_key = SigningKey.generate()
verify_key = signing_key.verify_key
print("\n=== BUREAU KEY GENERATION ===\n")
print(f"PRIVATE_KEY (store in .env):\n{signing_key.encode().hex()}\n")
print(f"PUBLIC_KEY (distribute for verification):\n{verify_key.encode().hex()}\n")
print("================================\n")

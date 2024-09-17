import itertools

def generate_passwords(base_password, special_chars, suffixes, num_variations):
    passwords = set()
    for suffix in suffixes:
        for special_char in special_chars:
            passwords.add(base_password + special_char + suffix)
            # Create variations by adding suffixes
            for i in range(1, num_variations + 1):
                passwords.add(base_password + special_char + suffix + str(i))
    return passwords

def save_to_file(passwords, file_name):
    with open(file_name, 'w') as f:
        for password in passwords:
            f.write(f"{password}\n")

if __name__ == "__main__":
    base_password = "C1xxxx3!"
    special_chars = ["@", "#", "$", "%", "&"]
    suffixes = ["dc", "U", "noc", "soc"]
    num_variations = 9

    passwords = generate_passwords(base_password, special_chars, suffixes, num_variations)
    save_to_file(passwords, "passwords.txt")
    print(f"Wordlist generated with {len(passwords)} passwords.")

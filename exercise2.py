from exercise1 import ShiftCipher

def main():
    ciphertext = "GurPnrfnepvcurevfernyylrnflgboernx"
    for shift in range(26):
        cipher = ShiftCipher(shift)
        potentialcyphertext = cipher.decrypt()
        print(f"Shift: {shift:2d} Shifted text: {potentialcyphertext}")
        
if __name__ == "__main__":
    main()

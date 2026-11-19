
#Xavier Cunningham 
#zvnz0038@leeds.ac.uk
#202028992


import string

class VigenereCipher:
    """
       VigenereCipher class (TO BE COMPLETED).

       Attributes:
           keyword (str): The word to be used as the key
           offset (int): The ASCII value of the letter 'A'. A static utility attribute to help you calculate
                a letter's position in the alphabet from 0 (A) to 25 (Z).
    """
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        """
        TO BE COMPLETED

        Private method to shift a letter a number of positions forward or backward in the alphabet.

        YOU CAN REUSE YOUR METHOD FROM EXERCISE 1 WITH MINOR MODIFICATIONS

        Parameters
        ----------
        letter : str
            The letter to be shifted.
        shift: int
            The number to shift
        forward : bool
            Whether to shift forward (True) or backward (False).

        Returns
        -------
        str
            The shifted letter.
        """
        shifted_letter = ''
        alphabet = list(string.ascii_uppercase)
        index = alphabet.index(letter.upper())
        
        if forward:
            index += shift 
            index = index % 26 
            shifted_letter = alphabet[index]

        else:
            index -= shift 
            index = index % 26 
            shifted_letter = alphabet[index]
        return shifted_letter

    def __generate_shift_list(self, plaintext_length: int):
        """
        TO BE COMPLETED

        Private method to generate a list of integers. Each element is the shift to encrypt the
        plaintext letter at the same position.

        Remember that the Vigenere cipher uses the keyword, repeated as many times as required to
        have the same number of letters as the plaintext, to derive the shift values for each
        plaintext letter.

        Parameters
        ----------
        plaintext_length : int
            The length of the plaintext after whitespace and punctuation has been removed.

        Returns
        -------
        list
            A list of shifts (integers).
        """

        key_length = len(self.keyword)
        shift_list = []

        for i in range(plaintext_length):
            shift_letter = self.keyword[i % key_length]
            shift_list .append(ord(shift_letter) - self.offset)

        return shift_list
    

    def encrypt(self, plaintext: str):
        """
        TO BE COMPLETED

        Encrypts a plaintext string.
        It should:
            1. Convert lowercase input to uppercase
            2. Remove whitespace and punctuation from the input
            3. Use self.__generate_shift_list to create the list of shifts for each letter in the plaintext
            4. Use self.__shift_letter to encrypt an individual letter

        Parameters
        ----------
        plaintext : str
            The plaintext string.

        Returns
        -------
        str
            The ciphertext string.
        """
        ciphertext = ''
        cleantext = "".join(char.upper() for char in plaintext if char.isalpha())

        cleantext_length = len(cleantext)
        shift_list = self.__generate_shift_list(cleantext_length)

        count = 0 

        for char in cleantext:
            ciphertext += self.__shift_letter(char,shift_list[count],True)
            count += 1 

        return ciphertext

    def decrypt(self, ciphertext: str):
        """
        TO BE COMPLETED

        Decrypts a ciphertext string
        It should:
            1. Convert lowercase input to uppercase
            2. Remove whitespace and punctuation from the input
            3. Use self.__generate_shift_list to create the list of shifts for each letter in the plaintext
            4. Use self.__shift_letter to decrypt an individual letter

        HINT: You can use the list index notation to retrieve a character at a position in a string
        e.g., if string = "abacab" then string[2] = 'a' (3rd character in the string)

        Parameters
        ----------
        ciphertext : str
            The ciphertext string.

        Returns
        -------
        str
            The plaintext string.
        """
        count = 0
        plaintext = ''

        cleantext = "".join(char.upper() for char in ciphertext if char.isalpha() )
        cleantext_length = len(cleantext)
        shift_list = self.__generate_shift_list(cleantext_length)

        for char in cleantext:
            plaintext += self.__shift_letter(char,shift_list[count],False)
            count += 1 

        return plaintext


def main():
    vig_cipher = VigenereCipher('smarties')
    ciphertext = vig_cipher.encrypt("The quick brown fox jumps over the lazy dog")
    plaintext = vig_cipher.decrypt(ciphertext)
    assert plaintext == 'THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'


if __name__ == "__main__":
    main()
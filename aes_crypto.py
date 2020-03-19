from Crypto.Cipher import AES
from Crypto import Random


class AESEncrypt(object):

    def __init__(self, path_inp):
        self.path = path_inp
        # generate a key and an initialisation vector
        self.key = Random.new().read(AES.block_size)
        self.iv = Random.new().read(AES.block_size)

    def encrypt(self):
        with open(self.path,"rb") as fb:
            inp_data = fb.read()
        
        # using CFB mode of operarion
        cfb_cipher = AES.new(self.key, AES.MODE_CFB, self.iv)
        enc = cfb_cipher.encrypt(inp_data)

        with open("encrypted.ec","wb") as fb:
            fb.write(enc)
        print (f"Encryption key: {self.key}")
        print (f"Initializtion vector: {self.iv}")
        print ("Store the encrypion key and initialization vector securely since it is needed it to decrypt the file.")


class AESDecrypt(object):

    def __init__(self, enc_file, key, iv):
        self.path = enc_file
        self.key = key
        self.iv = iv
    
    def decrypt(self):
        with open(self.path,"rb") as fb:
            enc_file = fb.read()
            print ("file read")
        # using CFB mode of operarion
        cfb_decipher = AES.new(self.key, AES.MODE_CFB, self.iv)
        dec = cfb_decipher.decrypt(enc_file)

        with open("output.jpg","wb") as fb:
            fb.write(dec)
        print ("File is decrypted")

import argparse

parser = parser = argparse.ArgumentParser(
    description='Basic Encryption and Decryption')

parser.add_argument('-m','--mode',type=str, help="encrypt/decrypt")

parser.add_argument('-f','--file',type=str, 
    help='path to file which is to be encrypted/decrypted')

parser.add_argument('-k','--key', type=str,
    help='encryption key to be used for decrypting the file')

parser.add_argument('-iv',type=str,help="initialization vector")

if __name__ == "__main__":

    print ("For decrypting put the key and iv in the utils.py file")
    opt = parser.parse_args()
    if opt.mode=='encrypt':
        enc = AESEncrypt(opt.file)
        enc.encrypt()

    if opt.mode=='decrypt':
        from utils import key, iv
        dec = AESDecrypt(opt.file,key,iv)
        dec.decrypt()

# Ransomware_InfoSec_Project

A Ransomware POC which uses AES Algorithm to Encrypt your File System (Educational Purposes Only).

### Information Security Project Submitted by:

Kaushal Bhansali (17103299,B8)

Ankit Bathla     (17103302,B8)

Gyan Ranjan      (17103306,B8)

Harshit Bajpai   (17103293,B8)

Harsh Tyagi      (17103322,B8)

----------------------------------------------------------------------------------------------------------------------


### Warning: It is strictly recommended to run this ransomware in Virtual Machine.

Steps to make this project working on your machine:

1. Run a PHP webserver in ./Ransomware_IS_Project-master/ransomware_server/ directory.

2. Put the Domain of your webserver at line 21 of ./Ransomware_IS_Project-master/ransomware_implementation/main.py

Encryption:

3. Now execute encryption the ransomware using following command

	>python ./Ransomware_IS_Project-master/ransomware_implementation/main.py

Decryption:

4. key is needed to perform decryption which will be present at ./ransomware_server/key_db.txt of your php webserver.

5. Now execute encryption the ransomware using following command

	>python ./Ransomware_IS_Project-master/ransomware_implementation/main.py -d

Dependencies:

1. python2.

2. Crypt module of python2.

3. PHP to run a webserver.

For more details refer:

	>report.pdf



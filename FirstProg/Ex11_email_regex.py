import re

str='''An email address is simply an address that can send and receive email messages in electronic mode on a particular network.

E-mail should be in the form of username@domain.

An address consists of two parts.

The part that comes before the @ symbol is called as local-part which is often username of the recipient and the part after the @ symbol is a domain name that represents the administrative realm of the mailbox.

Here are the best examples of an email id:

nick@gmail.com

vic@gmail.com

ramesh.kumar123@gmail.com

prince@yahoo.in'''
email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][0-9a-zA-Z._+%]+",str)
print(email)
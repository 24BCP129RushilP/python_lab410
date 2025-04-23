# Create a vCard file
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
END:VCARD
"""

with open('contact.vcf', mode='w') as file:
    file.write(vcard_content)

print("vCard 'contact.vcf' created successfully.")
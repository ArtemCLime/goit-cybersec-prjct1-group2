# goit-cybersec-prjct1-group2

Team project for GO IT CyberSecurity Masters [Project 1, Group 2]

## Requirements

* rich - pretty console output

```bash
pip install -r requirements.txt
```

## Manual for Bot Assistant

Assistant bot help keep contact information in one place.  
Each contact can have multiple email and phone records.

## The next command are supported

* add [name] [phone] - Create the new record in address book
* add-field [name] [field-type] [value] - add field to the record
* change [name] [field-type] [old_value] [new_value] - change field value
* phone [name] - show all phones for given contact name
* all - show all contacts in the Address Book
* show-birthday [name] - show contact birtday
* save - save address book to the local file
* load - load address book from the local file
* help - print this help

### field-type one of the next

* phone - the phone number. min 10 digit
* email - the email
* birthday - birthday date in format dd.mm.yyyy
* address - the address

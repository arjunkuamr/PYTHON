#empty dictionary

contacts={}

while True:
  print('\n Contact Book App')
  print('1. Create  contact')
  print('2. View contact')
  print('3. Upadate contact')
  print('4. Delete contact')
  print('5. Search contact')
  print('6. Count contact')
  print('7. Exit')
  
  choice=input('Enter your choice=')
  
  if choice=='1':
    name=input('Enter your name=')
    if name in contacts:
      print(f'Contact name {name} already exists!')
    else:
      age=input('Enter your age=')
      email=input('Enter your email=')
      mobile=input('Enter your mobile number=')
      contacts[name]={'age':int(age),'email':email,'mobile':mobile}
      print(f'Contact name{name} has been created successufully!')
      
  elif choice=='2':
    name=input('Enter contact name to view=')
    if name in contacts:
      contact=contacts[name]
      print(f'Name:{name},Age:{age},Mobile Number:{mobile}')
    else:
      print('Contact not found')
      
  elif choice=='3':
    name=input('Entername to upadate contact=')
    if name in contacts:
      age=input('Enter your age=')
      email=input('Enter your email=')
      mobile=input('Enter your mobile number=')
      contacts[name]={'age':int(age),'email':email,'mobile':mobile}
    else:
      print('Contact not found')
      
  elif choice=='4':
    name=input('Enter contact name to delete=')
    if name in contacts:
      del contacts[name]
      print (f'Contact name {name} has been delete successefully!')
    else:
      print ('Contact not fount ')
    
  elif choice=='5':
    search_name=input('Enter contact name to search=')
    found=False
    for name ,contact in contact.items():
      if search_name.lower() in name.lower():
        print(f'Found -Name {name},Age:{age},Mobile Number:{mobile},Email:{email}')
        found=True
    if not found:
      print('No contact fount with that name')
      
  elif choice=='6':
    print(f'Total contacts in your book:{len(contacts)}')
  
  elif choice=='7':
    print('Good bye...Closing the program')
    break
  else:
    print ('Invalid input')
    
    
        
    
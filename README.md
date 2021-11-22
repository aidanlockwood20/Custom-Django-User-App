# Custom-Django-User-App
The repository for a custom Django User Model App to make new projects easier to start with custom user behaviour

# Chapters
1. Admin 
2. Forms
3. Models
4. URLS
5. Views 

## Admin 
This section requires the least amount of work to get the app running in your project. Simply, add the all the model fields you want to be searchable in your admin, and leave it 

## Forms 
The forms section of the app will allow you to customise the fields that will appear in the views of the project. This custom app assumes you would like to use an email field instead of Django's default username field to allow users to authenticate, so that field is there with the password1 and password2 fields partially customised. 

All you need to add to this are the fields you would like customised in the form for the RegistrationForm and the fields you would like to appear in the AdminCreationForm and the AdminChangeForm. 

## Models 

The models file of the application is the largest of this custom Django App. However, this is where the most customisation can occur. 

The EmailField on Line 55 uses the assumption that the developer wants to allow users to login with their email. If you - as the developer - want to change this behaviour, change that field to reflect how you want users to login to your app. 

As passwords are already built into the model as part of Django's AbstractBaseUser, the next step in customising this application is to expand on the fields in the model, based on what information is connected to a user. For cleanliness of code, add the required fields in line 56, and the optional fields in line 58. 

The USERNAME_FIELD variable determines how the user logs into the application. As mentioned previously, this application assumes the developer wants the user to login with their email. Change the string to whichever field you want to be used as the method of authenticating users in the app. 

The REQUIRED_FIELDS variable states which fields are to be required when creating new users in your project. If any fields are considered mandatory, add them in the list 

## URLS
If you wish to include urls within the app folder, this file allows you to create the urls, which are specific to the accounts portion of your project. 


## Views
All account views related to this app are located in this file. To be added soon are the basic account views, including login, signup and logout views, in addition to admin related views. 

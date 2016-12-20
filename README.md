# MediaClash Django Test

## Getting Started
Please fork this repository, create a virtualenvironment and install the requirements

```

git clone https://github.com/Mediaclash/mediaclash-django-test
mkvirtualenv mediaclash_test
cd mediaclash_django_test
pip install -r requirements.txt
```


## Test Goals
Our simple website has 2 main views, one for people who are interested in finding out more about our fictional company, and another for people who really are not interested. Each page has a different form for users to fill out to say why they are interested / not interested. 

The two views are at the following urls:

http://localhost:8000/interested/

http://localhost:8000/not-interested/

On both pages there is an option to sign up to the company newsletter. Inside the newsletters app, there is a utils.py file that contains the code to sign up users to the mailing list. We need both views in our app to be able to call this method if a user opts in to receive emails.

**Without changing the form classes**, please design a mixin that can be included in both views that will handle the handle newsletter signups. This mixin should be designed so that it could be included in other views that might get developed further down the line for this site. The mixin should call the 'signup_newsletter' method in '/newsletters/utils.py' supplying the arguments correctly.

We reckon this test should not take longer than an hour to complete.

##Submit your solution
When done, please submit a pull request that we can review.

###Bonus points
Provide unit / behaviour tests to show that the mixin works.


**Good luck, and thanks for your time!**



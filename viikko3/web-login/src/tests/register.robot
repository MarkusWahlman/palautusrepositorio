*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  uusikayttaja
    Set Password  Salasana1!
    Confirm Password  Salasana1!
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  Salasana1!
    Confirm Password  Salasana1!
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  uusikayttaja2
    Set Password  lyhyt2
    Confirm Password  lyhyt2
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  uusikayttaja3
    Set Password  pelkkiakirjaimia
    Confirm Password  pelkkiakirjaimia
    Submit Registration
    Registration Should Fail With Message  Username must only contain letters a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  uusikayttaja4
    Set Password  Salasana1!
    Confirm Password  Salasana2!
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  Salasana1!
    Confirm Password  Salasana1!
    Submit Registration
    Registration Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  toimivakayttaja
    Set Password  Salasana1!
    Confirm Password  Salasana1!
    Submit Registration
    Log Out
    Go To Login Page
    Set Username  toimivakayttaja
    Set Password  Salasana1!
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  toimivakayttaja
    Set Password  huonosalasana
    Confirm Password  huonosalasana
    Submit Registration
    Log Out
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Login Should Succeed

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
'''
Created on Jul 21, 2015

@author: Florida

This is where the html string definitions are;
'''


   
    
# defining default variable to go into template_values;
dummyvalue="<p>dummy Paragraph</p>";
defaultBackgroundImg='''
<img src="/images/blank.jpg" >

'''
testText='Venue Info ';    # This string was produced to make tests and debugging from the DB;

# defining the default template_values;

homeLink='''/default''';
greetings= '';
firstName='';
lastName='';
userName='userName';
comments='';
venues='';
loginForm='''
'''
venueCreationForm='<p>test venueCreationForm</p>';
testString2='''
            
'''
logOut='''
    
   
    <script>
        function logOut()
    {
        
        document.getElementsByName("userName")[0].value="logOut";
        document.getElementsByName("logOutButton")[0].value="ON";
        
        //document.getElementById("demo").innerHTML =document.getElementsByName("userName")[0].value;
        //location.reload(); //reloading the page to have the changes iterated;
    }
    </script>
    <form method ="post" id="logOutForm"  >
        <input name="userName" type="hidden" value=" ">
        <input name="logOutButton" type="hidden" value=" ">
        <button id="searchButton" onclick="logOut()" class="searchButton">logOut</button>
    </form>
'''



template_values={
                         
             'firstName':'',
             'lastName':'',
             'testP':dummyvalue,
             'greetings': greetings,
             'loginForm':loginForm,
             'comments':comments,
             'testText':testText,
             'venueCreationForm':venueCreationForm,
             'venues':venues
             
             
             
             };
             
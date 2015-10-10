#!/usr/bin/env python
#

import webapp2

callText='''
<br/>
<div style="position:fixed;top:20%;right:20%;font-size:45;">
    
        <p><b>Email us For a Free Quote !</b><a href="mailto:lmquantumllc@gmail.com?Subject=From?AngelasProfessionalClean" target="_top" >
            <img src="/images/gmailImage.png" height="150" width="150">
            </a></p>
        <p>
            
         
        </p>
    

</div>


'''


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<img src="/images/angelaFrancaHomeImage.jpg" >'+callText)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

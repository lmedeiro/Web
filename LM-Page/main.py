#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

import jinja2;
import os;



jinja_environment= jinja2.Environment(
                                      
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)+"/templates"));
    
mainCSS='''
                     body
            {
                /*background-color:#0F0F0F;*/
                background-color:#FFFFFF;
                color: grey;
                text-align: center;
                color:rgb(193,191,191);
    
            }
            div
            {
                margin-top: 0px;
                font-family: 'Julius Sans One', sans-serif;
            }
            div a
            {
                text-decoration: none;    
            }
                  ''';
mainBody='''

        <div>
            <a href="mailto:engeenhariaCreativa@yahoo.com?Subject=From?CreativeEngineering.co" target="_top" >
                <img src="myLogo4.png"  width="489" height="554">
            </a>
            <h1>
                Blog | Resume 
            </h1>

        </div>

''';

mainlinkBar='''
<h1>
                Blog | <a href="/resume" target="_top" >Resume </a> | <a href="/test" target="_top" >Test</a>
            </h1>

'''

template_values={
                         
             
             'css': mainCSS,
             'main': mainBody,
             'linkBar': mainlinkBar 
             
             };
class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world! from Eclipse');
        
        template=jinja_environment.get_template('landing.html');
        self.response.out.write(template.render(template_values));



class testHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world! from Eclipse');
        
        template=jinja_environment.get_template('test.html');
        self.response.out.write(template.render(template_values));

class resumeHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hello world! from Eclipse');
        
        template=jinja_environment.get_template('resume.html');
        self.response.out.write(template.render(template_values));

app = webapp2.WSGIApplication([
    ('/test', testHandler),
    ('/resume', resumeHandler),
    ('/', MainHandler)
], debug=True)

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">

		<title>Contact-{{site[1]}}</title>
		<meta name="keywords" content="{{site[2]}}" />
		<meta name="description" content="{{site[3]}}" />


    <!-- Le HTML5 shim, for IE6-8 support of HTML elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le styles -->
    <link href="/blog/styles/style/static_file/css/bootstrap.css" rel="stylesheet">
    <link href="/blog/styles/style/static_file/css/blog.css" rel="stylesheet">
    
  </head>

  <body>

    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container-fluid">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="/blog/">{{site[1]}}</a>
          <div class="nav-collapse">
            <ul class="nav">
              <li class="active"><a href="/">Home</a></li>
					%if not infousername:
              <li><a href="/blog/register">Register</a></li>
              %end
              <li><a href="/blog/sand">Contact</a></li>
          </ul>
          <form class="navbar-search pull-left" action="/blog/search" method="post">
            <input class="search-query span2" name="search" placeholder="Search" type="text">
          </form>
            %if not infousername:
        <form class=" navbar-form pull-right" action="/blog/login" method="post">
        <input name="username" type="text" placeholder="username" class="input-small"/>
        <input name="password" type="password" placeholder="Password" class="input-small"/>
   	  <input type="checkbox" name="box" value="1"/>
   	  <span class="navbar-text">Remember me</span>
        <button class="btn" type="submit">Go</button>
     	 </form>
      %else:           
		<ul class="nav pull-right">
		<li>		<a class="" href="/blog/new">New Blog</a></li>
				<li class="divider-vertical"/>
 			 <li class="dropdown"> 
   		 <a href="#"
        	  class="dropdown-toggle"
        		  data-toggle="dropdown">
					Account {{infousername}}
        		  <b class="caret"></b>
   			 </a>
    			<ul class="dropdown-menu">
                      <li><a href="/blog/usercp">Usercp</a></li>
                       <li class="divider"/>
                      <li><a href="/blog/signout">signout</a></li>
    			</ul>
    					
  			</li>		
	</ul>
      %end        
          </div><!--/.nav-collapse -->

        </div>
      </div>
    </div>
    <div class="container-fluid">
      <div class="row-fluid">
        <div class="span12">
        

          <div class="hero-unit">   
          <h3>Contact Form</h3><br>
                       %if error:     
                    	  <div class="alert alert-error">
  								{{error}}
                        </div>

                       %end
                     <div>                    
                        <form action="sand" method="POST">
                        
                            <div>
                            <label>Your Email</label>
                            <input name="FROM" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>Subject</label>
                            <input name="SUBJECT" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>Msg</label>
                            <textarea name="TEXT" rows="7" class="span5"></textarea>
                            </div>
                            <div>
                        	  <input type="hidden" name="random" value="{{!random}}" />	
										
										{{!image}}<br>
										<a href="{{!audio_url }}">Phonetic spelling (mp3)</a>
										
                          		 <label>captcha</label> <input name="capt" type="text"  />
                          	 </div>
									
									<div>
                            <input type="submit" name="Submit" value="Submit" class="submit_btn" />                          
                            <input type="Reset" name="Reset" value="Reset" class="submit_btn" />
                            </div>
                        </form>
                        </div>


          </div>	  
            		  
        </div><!--/span-->		
      </div><!--/row-->

      <hr>
        
      <footer>
      <a class="pull-right" href="#">Back to top</a>
        <p><a href="http://{{site[5]}}">{{site[4]}}</a> &copy; LightBlog 2012</p>
      </footer>

    </div><!--/.fluid-container-->

    
    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/blog/styles/style/static_file/js/jquery.js"></script>
    <script src="/blog/styles/style/static_file/js/bootstrap-dropdown.js"></script>

  </body>
</html>

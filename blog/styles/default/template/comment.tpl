%try:
%    from postmarkup import render_bbcode
%except ImportError:
%     pass
%end
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">

		<title>{{blog[2]}}-{{site[1]}}</title>
		<meta name="keywords" content="{{blog[6]}}" />
		<meta name="description" content="{{blog[7]}}" />
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
        <div class="span3">
          <div class="well sidebar-nav">
            <ul class=" nav nav-list">
              <li class="nav-header">Category</li>   
              <li ><a href="/blog/"><strong>All</strong></a></li>
                %if allsection:
                %for section in allsection:
                %section=section[1]
              <li><a href="/blog/section/{{section.replace(' ','-')}}"><strong>{{section}}</strong></a></li>
    					%end
   					%end
            </ul>
          </div><!--/.well -->
          <div class="well sidebar-nav">
            <ul class="nav nav-list">
              <li class="nav-header">Recent Posts</li>
          	 	%if rposts:
           		%for rpost in rposts:
						<li><p><strong>{{rpost[4][:30]}} ..<a href="/blog/comment/{{rpost[2]}}#post{{rpost[0]}}">read</a></strong> <br>{{rpost[5]}}-{{rpost[1]}}</p><hr></li>
              %end
              %end
            </ul>
          </div><!--/.well -->  
        </div><!--/span-->
        
        
        <div class="span9">      
  				
          <div class="hero-unit">
            <p><strong>{{blog[2]}}</strong></p>
            <span class="help-block"><strong>Date:</strong> {{blog[4]}} | <strong>Author:</strong> {{blog[1]}} | <strong>Category:</strong> <a href="/blog/section/{{blog[5].replace(' ','-')}}">{{blog[5]}}</a>
             %if infousername:
               | <a href="/blog/admin/blogedit/{{page}}">Edit</a>
            %end
            </span> 
            %if blog[9] !=0:
            <span class="help-block pull-right"> comments {{blog[9]}}</span>
            %end
            <hr><br>
            %try:
				<p>{{!render_bbcode(blog[3])}}</p>
				%except NameError:
				<p>{{blog[3]}}</p>
				%end
				
				
                        <br><hr>
            <ul class="thumbnails">
            <li class="span2">
				<p class="help-block"><strong>{{signatureblog[1]}}</strong></p>
            <img  class="thumbnail" src="/blog/avator/{{signatureblog[7]}}.jpeg" alt="{{signatureblog[1]}}">
            </li>
			         <li class="span9"><p class="help-block">{{!signatureblog[8]}}</p></li>
				</ul>
          </div>
              
                %if comments:
                <h3>Comments</h3><br>
      			  %for star,comment in enumerate(comments):
     				  %star+=1  
     				  <section id="post{{comment[0]}}">          
             		  <div class="hero-unit">
                  	  <ul class="thumbnails">
           					 <li class="span2">
           						 <p class="help-block"><strong>{{comment[1]}}</strong></p>
       						    <img  class="thumbnail" src="/blog/avator/{{comment[7]}}.jpeg" alt="{{comment[1]}}">
          					  </li>
           					 <li class="span9">
           					 <span class="help-block pull-right"><a href="#post{{comment[0]}}">{{star}}</a></span>
       							  <span class="help-block">{{comment[5]}}                                 
                                 %if infousername:
                                  | <a href="/blog/admin/commentedit?page={{page}}&id={{star}}">Edit</a>
                                  %end
                                </span>
                                
          					  </li>                         
											<li class="span9">
                              <p>{{!comment[4]}}</p></li>                             
                         </ul>	
         			   </div>  </section>  
              
            		  %end
            		  %end
            		  
             %if not validcommen or onvalidcommen:
	% if infousername:
            <div>		                  
            <h3>Leave your comment</h3>  <br>
                            
           <form action="sandcomment/{{page}}" method="POST">

           <div class="control-group">
         	  <label class="control-label">Comment</label>
            <div class="controls">
              <textarea name="post" class="span6" placeholder="your Comment ..." rows="7"></textarea>
            </div>
          </div>
          <input type="submit" name="Submit" value="Submit" class="btn" />
          <input type="Reset" name="Reset" value="Reset" class="btn" />
                
 
 			</form>
 
 				</div>
	%else:

            <div>		                  
            <h3>Leave your comment</h3>  <br>
                            
           <form action="sandcomment/{{page}}" method="POST">
           		                  
          <div class="control-group">
         	  <label class="control-label">Name</label>
            <div class="controls">
              <input name="name" class="span4"  placeholder="your name" type="text"/>
            </div>
          </div>
           <div class="control-group">
         	  <label class="control-label">Email</label>
            <div class="controls">
              <input name="email" class="span4" placeholder="your@email.com" type="text"/>
            </div>
          </div>
           <div class="control-group">
         	  <label class="control-label">Comment</label>
            <div class="controls">
              <textarea name="post" class="span6" placeholder="your Comment ..." rows="7"></textarea>
            </div>
          </div>

          <input type="submit" name="Submit" value="Submit" class="btn" />
          <input type="Reset" name="Reset" value="Reset" class="btn" />
                
 
 			</form>
 
 				</div>

        		%end
        		%end
            		  
            		  
            		  
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

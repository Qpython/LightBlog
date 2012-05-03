%try:
%    from postmarkup import render_bbcode
%except ImportError:
%     pass
%end
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
		<title>{{title}}</title>
		<meta name="keywords" content="{{keywords}}" />
		<meta name="description" content="{{description}}" />
    </meta>
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
	<ul class="nav pull-right">
	<li>

        <form class=" navbar-form" action="/blog/login" method="post">
        <input name="username" type="text" placeholder="username" class="input-small"/>
        <input name="password" type="password" placeholder="Password" class="input-small"/>
   	  <input type="checkbox" name="box" value="1"/>
   	  <span class="navbar-text">Remember me</span>
        <button class="btn" type="submit">Go</button>
     	 </form>

	</li>		
	</ul>
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
%if loginstat:
    <div class="alert alert-error">
    {{!loginstat}}
</div>
%end

      <div class="row-fluid">
        <div class="span3">
          <div class="well sidebar-nav">
            <ul class=" nav nav-list">
              <li class="nav-header">Sections</li>   
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
						<li><p><strong>{{!rpost[4][:30]}} ..<a href="/blog/comment/{{rpost[2]}}#post{{rpost[0]}}">read</a></strong> <br>{{rpost[5]}}-{{rpost[1]}}</p><hr></li>
              %end
              %end
            </ul>
          </div><!--/.well -->  
        </div><!--/span-->
        
        
        <div class="span9">
        %if alert:
  			  <div class="alert alert-info">
 	 		  {{alert}}
				</div>
			%end
            %if blogs:
            %star=0
  				%for blog in blogs:
  				%star+=1
  				
          <div class="hero-unit">
            <p><a href="/blog/comment/{{blog[0]}}"><strong>{{blog[2][:100]}}</strong></a></p>
            %if blog[9] !=0:
            <span class="help-block pull-right"> comments {{blog[9]}}</span>
            %end
            <span class="help-block"><strong>Date:</strong> {{blog[4]}} | <strong>Author:</strong> {{blog[1]}} | <strong>Category:</strong> <a href="/blog/section/{{blog[5].replace(' ','-')}}">{{blog[5]}}</a></span> 
            <hr> 
            %try:
				<p>{{!render_bbcode(blog[3][:1000])}}</p>
				%except NameError:
				<p>{{blog[3][:1000]}}</p>
				%end
            <a class="btn btn-primary pull-right" href="/blog/comment/{{blog[0]}}">Learn more &raquo;</a><p><br></p>
          </div>
            %end
            %lend+=star
           	%if page>1:
				<br><a class="btn" href="/blog/{{url}}{{back}}"><< back </a>
				%end
           	%if lend<lblog:
             <a class="btn" href="/blog/{{url}}{{next}}">next >> </a>

            %end  
            %else:
            <p>{{noblog}}<p>
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

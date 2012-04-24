%try:
%    from postmarkup import render_bbcode
%except ImportError:
%     pass
%end
<!DOCTYPE html>
<html dir="rtl" lang="ar">
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
              <li class="active"><a href="/">الرئيسية</a></li>
					%if not infousername:
              <li><a href="/blog/register">التسجيل</a></li>
              %end
              <li><a href="/blog/sand">إتصل بنا</a></li>
          </ul>
			%if not infousername:
        <form class=" navbar-form pull-right" action="/blog/login" method="post">
        <input name="username" type="text" placeholder="أسم المستخدم" class="input-small"/>
        <input name="password" type="password" placeholder="كلمة المرور" class="input-small"/>
   	  <input type="checkbox" name="box" value="1"/>
   	  <span class="navbar-text">إبقى متصلا</span>
        <button class="btn" type="submit">دخول</button>
     	 </form>
      %else:           
		<ul class="nav pull-right">
		<li>		<a class="" href="/blog/new">تدوينة جديدة</a></li>
				<li class="divider-vertical"/>
 			 <li class="dropdown"> 
   		 <a href="#"
        	  class="dropdown-toggle"
        		  data-toggle="dropdown">
					إعدادات {{infousername}}
        		  <b class="caret"></b>
   			 </a>
    			<ul class="dropdown-menu">
                      <li><a href="/blog/usercp">تحكم</a></li>
                       <li class="divider"/>
                      <li><a href="/blog/signout">خروج</a></li>
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
              <li class="nav-header">الأقسام</li>   
              <li ><a href="/blog/"><strong>الكل</strong></a></li>
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
              <li class="nav-header">اخر الردود</li>
          	 	%if rposts:
           		%for rpost in rposts:
						<li><p><strong>{{rpost[4][:30]}} ..<a href="/blog/comment/{{rpost[2]}}#post{{rpost[0]}}">قراءة</a></strong> <br>{{rpost[5]}}-{{rpost[1]}}</p><hr></li>
              %end
              %end
            </ul>
          </div><!--/.well -->  
        </div><!--/span-->
        
        
        <div class="span9">      
  				
          <div class="hero-unit">
            <p><strong>{{blog[2]}}</strong></p>
            <span class="help-block"><strong>التاريخ:</strong> {{blog[4]}} | <strong>الكاتب:</strong> {{blog[1]}} | <strong>القسم:</strong> <a href="/blog/section/{{blog[5].replace(' ','-')}}">{{blog[5]}}</a>
             %if infousername:
               | <a href="/blog/admin/blogedit/{{page}}">تعديل</a>
            %end
            </span> 
            %if blog[9] !=0:
            <span class="help-block pull-right"> الردود {{blog[9]}}</span>
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
                <h3>الردود</h3><br>
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
                                  | <a href="/blog/admin/commentedit?page={{page}}&id={{star}}">تعديل</a>
                                  %end

                                </span>
                                
          					  </li>                         
											<li class="span9">
                              <p>{{!comment[4]}}</p></li>                             
                         </ul>	
         			   </div> </section>  
              
            		  %end
            		  %end
            		  
              %if not validcommen or onvalidcommen:
	% if infousername:
            <div>		                  
            <h3>ضع ردك هنا</h3>  <br>
                            
           <form action="sandcomment/{{page}}" method="POST">

           <div class="control-group">
         	  <label class="control-label">الرد</label>
            <div class="controls">
              <textarea name="post" class="span6" placeholder="أكتب ردك هنا..." rows="7"></textarea>
            </div>
          </div>
          <input type="submit" name="Submit" value="إرسال" class="btn" />
          <input type="Reset" name="Reset" value="إمسح" class="btn" />
                
 
 			</form>
 
 				</div>
	%else:

            <div>		                  
            <h3>ضع ردك هنا</h3>  <br>
                            
           <form action="sandcomment/{{page}}" method="POST">
           		                  
          <div class="control-group">
         	  <label class="control-label">الأسم</label>
            <div class="controls">
              <input name="name" class="span4"  placeholder="أسمك" type="text"/>
            </div>
          </div>
           <div class="control-group">
         	  <label class="control-label">البريد الألكتروني</label>
            <div class="controls">
              <input name="email" class="span4" placeholder="your@email.com" type="text"/>
            </div>
          </div>
           <div class="control-group">
         	  <label class="control-label">الرد</label>
            <div class="controls">
              <textarea name="post" class="span6" placeholder="أكتب ردك هنا" rows="7"></textarea>
            </div>
          </div>

          <input type="submit" name="Submit" value="إرسال" class="btn" />
          <input type="Reset" name="Reset" value="إمسح" class="btn" />
                
 
 			</form>
 
 				</div>

        		%end
        		%end
	  
        </div><!--/span-->		
      </div><!--/row-->

      <hr>
        
      <footer>
      <a class="pull-right" href="#">الإنتقال إلى الأعلى</a>
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

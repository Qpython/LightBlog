<!DOCTYPE html>
<html dir="rtl" lang="ar">
  <head>
    <meta charset="utf-8">

		<title>التحكم-{{site[1]}}</title>
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
      <div class="hero-unit">   
      <div class="row-fluid">    
        <div class="span12">
          <h3>التحكم</h3><br>
                       %if error:     
                    	  <div class="alert alert-info">
  								{{error}}
                        </div>
                       %end

                     <div>                    
                        <form action="usercp" method="POST">
                        
                            <div>
                            <label>كلمة السر</label>
                            <input name="password" type="password" class="span5"/>
                            </div>
                            
                            <div>
                            <label>أعد كتابة كلمة السر</label>
                            <input name="rpassword" type="password" class="span5"/>
                            </div>
                            
                            <div>
                            <label>البريد الألكتروني</label>
                            <input name="email" type="text" value="{{infouser[3]}}" class="span5"/>
                            </div>
                            
                            <div>
                            <label>التوقيع</label>
                            <textarea name="signature" rows="7" class="span5">{{infouser[8]}}</textarea>
                            </div>
									
									<div>
                            <input type="submit" name="Submit" value="حفظ" class="submit_btn" />                          
                            </div>
                        </form>
                        </div>
									
		<div>
							<hr>
                        <form action="usercp/pic" method="POST" enctype="multipart/form-data">
                        
                    	<div class="span4">
                            <label>الصورة الرمزيه</label>
                            <input name="picture" type="file" />

                       </div> 

        		<div class="span4">
                           <img src="/blog/avator/{{infouser[7]}}.jpeg" alt="{{infouser[1]}}">
                        </div>
                        
                    	<div class="span12">
                        <input type="submit" name="save" value="حفظ" />
                       </div> 

                          </form>
		</div>


          </div>	  
            		  
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

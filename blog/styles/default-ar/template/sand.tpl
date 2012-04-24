<!DOCTYPE html>
<html dir="rtl" lang="ar">
  <head>
    <meta charset="utf-8">

		<title>إتصل بنا-{{site[1]}}</title>
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
      <div class="row-fluid">
        <div class="span12">
        

          <div class="hero-unit">   
          <h3>ناموذج الإرسال</h3><br>
                       %if error:     
                    	  <div class="alert alert-error">
  								{{error}}
                        </div>

                       %end
                     <div>                    
                        <form action="sand" method="POST">
                        
                            <div>
                            <label>أكتب بريدك</label>
                            <input name="FROM" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>العنوان</label>
                            <input name="SUBJECT" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>نص الرساله</label>
                            <textarea name="TEXT" rows="7" class="span5"></textarea>
                            </div>
                            <div>
                        	  <input type="hidden" name="random" value="{{!random}}" />	
										
										{{!image}}<br>
										<a href="{{!audio_url }}">Phonetic spelling (mp3)</a>
									
                          		 <label>رمز صورة التحقق</label> <input name="capt" type="text"  />
                          	 </div>
									
									<div>
                            <input type="submit" name="Submit" value="إرسال" class="submit_btn" />                          
                            <input type="Reset" name="Reset" value="إمسح" class="submit_btn" />
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

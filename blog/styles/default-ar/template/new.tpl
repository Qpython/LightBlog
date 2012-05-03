<!DOCTYPE html>
<html dir="rtl" lang="ar">
  <head>
    <meta charset="utf-8">
		<title>تدوينة جديدة-{{site[1]}}</title>
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
          <form class="navbar-search pull-left" action="/blog/search" method="post">
            <input class="search-query span2" name="search" placeholder="إبحث" type="text">
          </form>
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
                       %if error:     
                    	  <div class="alert alert-error">
  								{{error}}
                        </div>
                       %end						
                        %if username:
                        <div>
                        <form action="new" method="POST">
                        
                            <div>
                            <label>عنوان التدوينة</label>
                            <input name="title" type="text" class="span5"/>
                            </div>
                            <div>
                            <label>نص التدوينه</label>
                            <textarea name="titletext" class="span5"></textarea>
                            </div>

                            <div>
                            <label>الكلمات الدليليه</label>
                            <input name="keywords" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>الوصف</label>
                            <input name="description" type="text" class="span5"/>
                            </div>
                            
                            <div>
                            <label>القسم</label>
                            <select name="section">
									if sections:
									%for sectionname in sections:
									<option value="{{sectionname[1]}}">{{sectionname[1]}}</option>
									%end
									</select>
									</div>
									
									<div>
                            <input type="submit" name="Submit" value="إرسال" class="submit_btn" />                          
                            <input type="Reset" name="Reset" value="مسح" class="submit_btn" />
                            </div>
                        </form>
                        </div>
                    %end

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




                        		<script type="text/javascript" src="editor/ckeditor/ckeditor.js"></script>

                            			<script type="text/javascript">

			CKEDITOR.replace( 'titletext',
				{ 
					language : 'ar',		
					extraPlugins : 'bbcode',
					// Remove unused plugins.
					removePlugins : 'bidi,button,dialogadvtab,div,filebrowser,flash,format,forms,horizontalrule,iframe,indent,justify,liststyle,pagebreak,showborders,stylescombo,table,tabletools,templates',
					// Width and height are not supported in the BBCode format, so object resizing is disabled.
					disableObjectResizing : true,
					// Define font sizes in percent values.
					fontSize_sizes : "10/10%;30/30%;50/50%;100/100%;120/120%;150/150%;200/200%;300/300%",
					toolbar :
					[
						['Source', '-', 'Save','NewPage','-','Undo','Redo'],
						['Find','Replace','-','SelectAll','RemoveFormat'],
						['Link', 'Unlink', 'Image', 'Smiley','SpecialChar'],
						,
						['Bold', 'Italic','Underline'],
						['FontSize'],
						['TextColor'],
						['NumberedList','BulletedList','-','Blockquote'],
						['Maximize']
					],

					smiley_images :
					[
						'regular_smile.gif','sad_smile.gif','wink_smile.gif','teeth_smile.gif','tounge_smile.gif',
						'embaressed_smile.gif','omg_smile.gif','whatchutalkingabout_smile.gif','angel_smile.gif','shades_smile.gif',
						'cry_smile.gif','kiss.gif'
					],
					smiley_descriptions :
					[
						'smiley', 'sad', 'wink', 'laugh', 'cheeky', 'blush', 'surprise',
						'indecision', 'angel', 'cool', 'crying', 'kiss'
					]
					
					
			} );
			
			//]]>
			</script>
  </body>
</html>

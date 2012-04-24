<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<meta charset="utf-8">
	<title>sitemap</title>
</head>
<body>

<a href="http://{{site[5]}}/blog/index"><h1>{{site[1]}}</h1></a>
<br>
%for i in section:

<a href="http://{{site[5]}}/blog/index?section={{i[1]}}">{{i[1]}}</a>
<br>
%end

______________
<br>

%for x in blog:
<a href="http://{{site[5]}}/blog/comment/{{x[0]}}">{{x[2]}}</a>
<br>
%end

</body>
</html>

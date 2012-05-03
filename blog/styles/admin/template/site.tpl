<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta charset="utf-8">
<link href="/blog/styles/admin/static_file/css/admincp.css" rel="stylesheet" type="text/css">
</head>
<body>


<table align="center" width="100%%" cellpadding="5" cellspacing="5">
<tbody><tr>


<form method="post">


<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody><tr>
		<td class="tbl" colspan="2">edit site</td>
	</tr>
	<tr>
		<td widht="50%" class="tbl2">title:<input size="50" name="title" value="{{site[1]}}"><br></td>


	</tr>
	<tr>
		<td widht="50%" class="tbl2">keywords:<input size="50" name="keywords" value="{{site[2]}}"></td>


	</tr>
	<tr>
		<td widht="50%" class="tbl2">description:<input size="50" name="description" value="{{site[3]}}"></td>


	</tr>
	<tr>
		<td widht="50%" class="tbl2">sitename:<input size="50" name="sitename" value="{{site[4]}}"></td>


	</tr>
	<tr>
		<td widht="50%" class="tbl2">siteurl:<input size="50" name="siteurl" value="{{site[5]}}"></td>

	</tr>
	<tr>
		<td widht="50%" class="tbl2">mod site:
		%if site[6]==1:
		<input type="radio" name="modsite" value="1"  CHECKED>Open blog<input type="radio" name="modsite" value="0">Close blog
		 %else:
		<input type="radio" name="modsite" value="1"  >Open blog<input type="radio" name="modsite" value="0" CHECKED>Close blog
		 %end
		</td>
		
	<tr><br>
		<td class="tbl2">mod msg:<br>    <textarea style="width: 500px; height: 100px;" size="50" rows="4" name="modmsg" >{{site[7]}}</textarea></td>

	</tr>

	</tr>
	</tbody></table>	



</tr>

</tbody></table>
<td class="tbl2" align="center"><input class="buttons" value="submit" type="submit"></td>

</form>
</body></html>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta charset="utf-8">
<link href="/blog/styles/admin/static_file/css/admincp.css" rel="stylesheet" type="text/css">
</head>
<body>


<table align="center" width="100%" cellpadding="5" cellspacing="5">
<tbody><tr>


<form method="post">


<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody><tr>
		<td class="tbl" colspan="2">edit username</td>
	</tr>
	<tr>
		<td widht="50%" class="tbl2">Username: <input name="name" type="text" value="{{raw[1]}}" /></td>
	</tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">password:<input name="password" type="text"  /></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">email:<input name="email" type="text" value="{{raw[3]}}" /></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">valid:<input name="valid" type="text" value="{{raw[6]}}" /></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">signature:<input name="signature" type="text" value="{{raw[8]}}" /></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">ip:{{raw[4]}}</td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2"><input type="checkbox" name="box" value="delete" />delete user<br /></td>
	</tr>
</tbody></table>



<td class="tbl2" align="center"><input class="buttons" value="submit" type="submit"></td>
</form>

<table align="center" width="100%" cellpadding="5" cellspacing="5">
<tbody><tr>



<form action="pic" method="POST" enctype="multipart/form-data">

<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody><tr>
		<td class="tbl" colspan="2">edit avator</td>
	</tr>
	<tr>
		<td widht="50%" class="tbl2">Username: <input name="username" type="text" value="{{raw[1]}}" /></td>
	</tr>
</tbody></table>


<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
	
		<td widht="50%" class="tbl2"><img src="/blog/avator/{{raw[7]}}.jpeg"><input name="picture" type="file"/></td>
		
	</tr>
</tbody></table>




<td class="tbl2" align="center"><input class="buttons" value="submit" type="submit"></td>
</form>

</body></html>

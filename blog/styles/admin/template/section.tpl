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
		<td class="tbl" colspan="2">edit section</td>
	</tr>
	<tr>
<td widht="50%" class="tbl2">
<select name="section">
if sections:
%for sectionname in sections:
%sectionname=sectionname[1]
<option value="{{sectionname}}">{{sectionname}}
%end
</select>
		Rname:<input name="renamesection">
		Rkeywords:<input name="rkeywords">
		Rdescription:<input name="rdescription"></td>
</tr>

<td widht="50%" class="tbl2">new section:<input name="nsection"></tr>

<td widht="50%" class="tbl2"> keywords:<input name="keywords"></tr>

<td widht="50%" class="tbl2"> description:<input name="description"></tr>

<td widht="50%" class="tbl2"><input type="checkbox" name="box" value="delete" />delete section</tr>
</tbody></table>

<td class="tbl2" align="center"><input class="buttons" value="submit" type="submit"></td>

</form>
</body></html>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta charset="utf-8">
</head>
<body>


<table
     border="1">
    <tr><td style="vertical-align: top; background-color: rgb(202, 202, 202);">id
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">username
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">password
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">email
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">ip
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">data
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">valid
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">avator
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">signature
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">2password
</td><td style="vertical-align: top; background-color: rgb(202, 202, 202);">salt
</td>
</tr>

%for i in row:
	%a=0
	%for c in i:
	%if a==0:
		<tr>
		%a+=1
		<td><a href='/blog/admin/editusers/{{c}}'>{{c}}</a></td>
	%else:
		<td>{{c}}</td>
		%if a==len(i):
		</tr><br>
%end
%end
%end
%end

</table>
%if page>1:	
	<br><a href="?page={{back}}">back</a>
%end
%if page<=lend:
	 & <a href="?page={{next}}"> next</a>
%end


</body></html>


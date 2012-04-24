<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta charset="utf-8">
<link href="/blog/styles/admin/static_file/css/admincp.css" rel="stylesheet" type="text/css">
</head>
<body>

    <form method="post">
    <table align="center" cellpadding="2" cellspacing="2" width="100%">
    <tbody><tr>

        <td class="tbl" colspan="2">edit comment</td>
    </tr>
    <tr>
        <td class="tbl2" align="center"><textarea name="comment" rows="6" cols="80">{{comment[4]}}</textarea></td>
    </tr>
     <tr>
        <td class="tbl2" align="center"><input type="checkbox" name="box" value="delete" />delete blog</td>
    </tr>
 
     <tr>
        <td class="tbl2" align="center">ip:{{comment[6]}}</td>
    </tr>   
    <input type="hidden" name="id" value="{{comment[0]}}" />
    <tr>
        <td class="tbl2" align="center"><input class="buttons" value="save" type="submit"></td>
    </tr>

    </tbody></table>

    </form>
</body></html>

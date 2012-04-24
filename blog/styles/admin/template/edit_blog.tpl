<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<meta charset="utf-8">
<link href="/blog/styles/admin/static_file/css/admincp.css" rel="stylesheet" type="text/css">
</head>
<body>

<form method="post">

<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody><tr>
		<td class="tbl" colspan="2">edit blog</td>
	</tr>
	<tr>
		<td widht="50%" class="tbl2">title:<input name="title" type="text" size="50" value="{{blog[2]}}" /></td>
	</tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">blog:<textarea cols="60" rows="7" name="titletext">{{blog[3]}}</textarea></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">keywords:<input name="keywords" type="text" size="50" value="{{blog[6]}}" /></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td class="tbl2">description:<textarea cols="50" rows="3" name="description">{{blog[7]}}</textarea></td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2"><input type="checkbox" name="box" value="delete" />delete blog</td>
	</tr>
</tbody></table>
<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">
		
		
<select name="section" STYLE="font-size : 12pt">
if sections:
%for sectionname in sections:
%sectionname=sectionname[1]
%if sectionname !=blog[5]:
<option value="{{sectionname}}">{{sectionname}}
%else:
<option value="{{sectionname}}" SELECTED>{{sectionname}}
%end
%end
</select>
	
		
		</td>
	</tr>
</tbody></table>

<table align="center" cellpadding="0" cellspacing="0" width="100%">
	<tbody>
	<tr>
		<td widht="50%" class="tbl2">ip:{{blog[8]}}</td>
	</tr>
</tbody></table>

<td class="tbl2" align="center"><input class="buttons" value="submit" type="submit"></td>


</form>

                        		<script type="text/javascript" src="/blog/editor/ckeditor/ckeditor.js"></script>

                            			<script type="text/javascript">
			CKEDITOR.replace( 'titletext',
				{
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
						'/',
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

</body></html>

<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="gss.xsl"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.google.com/schemas/sitemap/0.84 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<url><loc>http://{{site[5]}}</loc><lastmod>{{today}}</lastmod><changefreq>daily</changefreq><priority>1.00</priority></url>
%for i in section:
<url><loc>http://{{site[5]}}/store/index?section={{i[1]}}</loc><lastmod>{{today}}</lastmod><changefreq>daily</changefreq><priority>0.70</priority></url>
%end
%for x in blog:
<url><loc>http://{{site[5]}}/store/sales/{{x[0]}}</loc><lastmod>{{today}}</lastmod><changefreq>daily</changefreq><priority>0.50</priority></url>
%end
</urlset>

#!/usr/bin/perl

#use CGI;
#my $query = CGI->new;
#my $dir = $ARGV[0]; //"hard code for terminal"
#my $argument = $query->param('dir');

my $dir = "/";

sub mkimg{
system("./public/file_counts", $dir);

open(gplot,"| gnuplot") or die "Error while piping: $! \n";
print gplot << "GNU_EOF";

set terminal jpeg font "Helvetica" 11
set output "public/file_count.jpg"
set autoscale y
set bar 1.0 front
set boxwidth 1.8
set style fill solid 0.8 border -1
set style histogram gap 1.5 
set datafile missing '-'
set style data histograms
set tics scale 0
set title "File Types in Server File System"
unset key
x = 0.0
i = 23

plot "file_count.dat" using 2:xticlabels(1)

GNU_EOF
close(gplot);
}
=pod
print "Content-type: image/jpeg\n\n";
makeimg();
open IMAGE, "file_count.jpg";
my ($image, $buff);
while (read IMAGE, $buff, 4096) {
        $image .= $buff;
}
close IMAGE;
print $image;
=cut

print "Content-type: text/html\n\n";
mkimg();
print <<EndOfHTML;
<html><head><title>File Count Test</title></head>
<body>

<font size="12" color="red"><h2 align="middle" color="red" >CS410 Webserver</h2></font>
<center><img src="file_count.jpg"></center>

</body>
</html>
EndOfHTML

exit 1;


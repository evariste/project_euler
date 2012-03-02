#import List::MoreUtils
# use POSIX;
    
use List::MoreUtils qw{mesh};

$file = "poker.txt";

open(FILE, $file) || die("Cannot open $file");

@x = qw/a b c d/;
@y = qw/1 2 3 4/;
@z = mesh @x, @y;     
print @z , "\n";

my @s = qw|a b c d e f|;
my @t = qw|1 2 3 4 5 6|;
print $s[-1], "\n";
print split ($s[-1], @s);
print "\n";
@u = mesh @s, @t;
print @u, "\n";
exit;

$n=0;
foreach $line (<FILE>) {
    chomp $line;
    print "${line}\n";

    @line = split(/ /, $line);
    @hand1 = @line[0..4];
    @hand2 = @line[5..$#line];

    @cards1 = map {unpack 'A'}  @hand1; 
    @suits1 = map {unpack 'xA'} @hand1;
    print @cards1 , "\n";
    print @suits1 , "\n";

	

    $n = $n + 1;
    if ($n > 10){
	exit;
    }
}


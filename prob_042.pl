#   The n^(th) term of the sequence of triangle numbers is given by,
#   t_(n) = ½n(n+1); so the first ten triangle numbers are:

#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#   By converting each letter in a word to a number corresponding to
#   its alphabetical position and adding these values we form a word
#   value. For example, the word value for SKY is 19 + 11 + 25 = 55 =
#   t_(10). If the word value is a triangle number then we shall call
#   the word a triangle word.

#   Using words.txt (right click and 'Save Link/Target As...'), a 16K
#   text file containing nearly two-thousand common English words, how
#   many are triangle words?

# A: 162


use POSIX;

$file = "prob_042.txt";
open(FILE, $file) || die("Cannot open $file");

$raw = <FILE>;

chomp $raw;

$raw =~ s/\"//g;


@words = split(/,/, $raw);

$maxLen = 0;
$triangleCount = 0;

foreach $word (@words){
    print "$word ";
    $n = length($word);
    $val = 0;
    
    for ($j = 0; $j < $n; $j++){
	$c = substr($word, $j, 1);
	print $c;
	$val += ord($c) - ord('A') + 1;
	print " ";
    }
    print $val;

    # Test for a triangle number:
    $test = $val - (floor(sqrt(2*$val)) +1) * floor(sqrt(2*$val)) / 2;
    if ($test == 0){
	print " x";
	$triangleCount++;
    }

    print "\n";
}

print 1 + $#words;
print "\n";

print "max : $maxLen";
print "\n";

print "Triangle count : $triangleCount\n";




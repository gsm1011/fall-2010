#!/usr/bin/perl -w
# This script is to abbrevations within the paragrpah; 
# The goal is to differentiate between common abbrevations
# and the sentence boundaries. 

while (<STDIN>) {
    # preprocessing. 
    # if (m/(( [^ \.]+){3})\.([A-Z][^ \.]+ .{20})/) {
    # 	printf "%40s.%-40s\n", $1, $3;
    # 	printf "%40s. %-40s\n", $1, $3;
    # }
    print $_ . "\n"; 
    LOOPIN:while ($_ =~ m/ ([A-Za-z0-9]+\.).? /) {
	$abbr = $1; 
	print $abbr . "\n";
	next LOOPIN;
    }
}

#!/usr/bin/env perl

use strict;
use warnings;

# first argument should be what python is on the computer
# my path to python is simply `python` however the example uses `python3`
my @cmd = ("python3", "main.py");

my @args;
if (defined ($ARGV[1])) {
    @args = ($ARGV[0], $ARGV[1]);
} else {
    @args = ($ARGV[0]);
}

print "@cmd\n";
print "@args\n";

system((@cmd, @args)) == 0 or die "Python script returned error $?";
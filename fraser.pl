#!/usr/bin/perl
# Marco Guardigli, mgua@tomware.it 11 jan 2007
# fraser.pl: random sentences generator
#
# coded for my kind friend Klaudija Stefan, who is an english teacher
# to use this in windows, you need to install a perl interpreter
# for example: www.activestate.com
#
# this code is GPL. see www.gnu.org
#
#
# fraser is a simple software for generating random sentences.
# sentence structure is selected among a list of possibile templates
# each template identifies a sequence of entities (words)
# each entity is randomly chosen from a list.
#
# customization is very easy.
# translation in other languages is very easy
# if you use or improve or extend this software, and like it, let me know.
#


use POSIX;
$DEBUG=0;
@structures = ("sbj tv adv obj", "sbj adv tv obj", "sbj itv", "sbj pv sbj");

# subjects
@sbj = ("the man", "the woman", "a kangaroo", "a turtle", 
		"my cousin's dog", "a white cat", "a donkey",
		"the small yellow bird", "a big elephant", 
		"Fred", "Dorothy", "Helen", "Jack");

# passive verbs		
@pv =	("was killed by", "was hit by"); 

# intransitive verbs (dont want a target entity)
@itv =	("ran away", "was crying", "was laughing", "jumped", "fell down");

# transitive verbs (want a target entity)
@tv =  ("eat", "ate", "loves", "kissed", "licked", "greeted", 
		"killed", "kicked in the ass");

# adverbs
@adv = ("gently", "strongly", "fiercely", "softly", "barely", 
		"kindly", "rudely", "passionately");

# objects
@obj = ("a dead fish", "the policeman", "a jazzman", 
		"a clown", "a kid", "the princess", 
		"one passing man", "a nude woman", "a painting" );


$s = $structures[floor(rand() * (1 + $#structures))]; # select a casual structure
print "$s\n";
foreach $p (split(/ /,$s)) {	#identify elements one by one
	print "$p:[" if $DEBUG;
	print $$p[floor(rand() * (1 + $#$p))];
	print "]" if $DEBUG;
	print " ";
}
print "\n";


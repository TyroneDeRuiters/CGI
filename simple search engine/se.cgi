#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use WWW::Mechanize;
use URI::Escape;

my $q = CGI->new();
my $query = $q->param("query");
my $search = $q->param("search");

print CGI::header();
#my $url   = "http://www.domain.com/webpage.html";
my $interface;
my $file = "se.html";
{
  local $/;
  open my $fh, '<', $file or die "can't open $file: $!";
  $interface = <$fh>;
}
#my $output;
my %ranks;
print $interface;
if(defined $search){
  my @comp = split(/\s+/,$query);
  my $var1 = $comp[0];
  my $url = "http://www.google.com/search?q=$query";
  my $mech  = WWW::Mechanize->new();
  $mech->get($url);
  #print "test";
  my @links = $mech->links();
  my $cnt = 0;
  foreach my $link (@links) {
    if($cnt > 10){
      last;
    }
    if($link->url() =~ /(http|https)/ && $link->text() =~ /$var1/){
      my $cur_link = $link->url();
      $cur_link =~ s/.*(https|http)/http/;
      my @arr = split(/\&/,$cur_link);
      $cur_link = $arr[0];
      print("DESCRIPTION (google): ".$link->text()."<br></br>");
      print("LINK: "."<a href=".$cur_link.">".$cur_link."</a>"."<br></br>");
      $cnt = $cnt + 1;
    }
  }
  my $q2 = uri_escape($query);
  my $url = "http://www.bing.com/search?q=$q2";
  #my $mech  = WWW::Mechanize->new();
  $mech->get($url);
  my $cnt = 0;
  my @links = $mech->links();
  foreach my $link (@links) {
    if($cnt > 10){
      last;
    }
    if($link->url() =~ /https|http/ && $link->url() =~ "$var1"){
      #my $cur_link = $link->url();
      #$cur_link =~ s/.*(https|http)/http/;
      #my @arr = split(/\&/,$cur_link);
      #s$cur_link = $arr[0];
      #if(!(defined $ranks{$cur_link})){
      #  $ranks{$cur_link} = 1;
      #}
      #else{
      #  $ranks{$cur_link} = $ranks{$cur_link} + 1;
      #}
      print("DESCRIPTION (bing): ".$link->text()."<br></br>");
      print("LINK: "."<a href=".$link->url().">".$link->url()."</a>"."<br></br>");
      #$output = $output."DESCRIPTION (bing): ".$link->text()."<br></br>";
      #$output = $output."LINK: "."<a href=".$cur_link.">".$cur_link."</a>"."<br></br>";
      #$cnt = $cnt + 1;
    }
  }

  #my $mech  = WWW::Mechanize->new();
  #my $q1 = $query;
  my $q1 =  uri_escape($query);
  my $url = "http://search.yahoo.com/search?p=$q1";
  #print "$url<br></br>";
  my $cnt = 0;
  $mech->get($url);
  #print $mech -> content;
  my @links = $mech->links();
  #my $size = @links;
  #print "number of links: ".$size."<br></br>";

  foreach my $link (@links) {
    if($cnt > 10){
      last;
    }
    #print $var1."<br></br>";
    if($link->url() =~ "$var1" && $link->text() =~ "$var1"){
      #$cur_link =~ s/.*(https|http)/http/;
      #my @arr = split(/\&/,$cur_link);
      #$cur_link = $arr[0];
      print("DESCRIPTION (yahoo): ".$link->text()."<br></br>");
      print("LINK: "."<a href=".$link->url().">".$link->url()."</a>"."<br></br>");
      #$output = $output."DESCRIPTION (yahoo): ".$link->text()."<br></br>";
      #$output = $output."LINK: "."<a href=".$link->url().">".$link->url()."</a>"."<br></br>";
      $cnt = $cnt + 1;
    }
  }
  #print $output;
}
#print $interface.$output;

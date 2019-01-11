$data = shift;
$dir=$data;

$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python3 adaptive_least_squares.py $data.data $data.trainlabels.$i > p_out");
  $err[$i] = `perl error.pl $data.labels p_out`;
  print "$err[$i]\n";
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Perceptron error = $mean ($sd)\n";

$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python3 adaptive_hinge.py $data.data $data.trainlabels.$i > p_out");
  $err[$i] = `perl error.pl $data.labels p_out`;
  print "$err[$i]\n";
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Hinge error = $mean ($sd)\n";

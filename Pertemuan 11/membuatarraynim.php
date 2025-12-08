<?php
25
$nim = readline("Masukkan NIM: ");

$digit_string = str_split($nim); 
$digit = [];
foreach ($digit_string as $d) {
    $digit[] = (int)$d; 
}

echo "\nArray Digit: " . implode(", ", $digit) . "\n";

$total_digit = 0;
$maksimum_digit = -1; 
$minimum_digit = 10;
$jumlah_elemen = count($digit);

foreach ($digit as $d) {
    $total_digit += $d;
    
    if ($d > $maksimum_digit) {
        $maksimum_digit = $d;
    }
        
    if ($d < $minimum_digit) {
        $minimum_digit = $d;
    }
}

if ($jumlah_elemen > 0) {
    $rata_rata_digit = $total_digit / $jumlah_elemen;
} else {
    $rata_rata_digit = 0;
}

$reverse_array = [];
for ($i = $jumlah_elemen - 1; $i >= 0; $i--) {
    $reverse_array[] = $digit[$i];
}


echo "\n--- Hasil Perhitungan ---\n";
echo "Total seluruh digit: " . $total_digit . "\n";
echo "Nilai maksimum digit: " . $maksimum_digit . "\n";
echo "Nilai minimum digit: " . $minimum_digit . "\n";
echo "Nilai rata-rata digit: " . number_format($rata_rata_digit, 2) . "\n"; 
echo "Reverse array: " . implode(", ", $reverse_array) . "\n";

?>
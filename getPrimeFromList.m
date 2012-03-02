function p_n = getPrimeFromList(n)
% Return the nth prime

[~, b] = system(['sed -n ''' num2str(n) ' p'' firstMillionPrimes.txt']);

p_n = str2double(b);




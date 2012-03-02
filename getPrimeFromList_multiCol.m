function p_n = getPrimeFromList_multiCol(n)

file = 'firstMillionPrimes.txt';

row = 1 + floor(n / 8);

col = mod(n, 8);

if col == 0
  col = 8;
  row = row -1;
end

cmd = ['awk ''{print $' num2str(col) '}'' ' file ' '];
cmd = [cmd '| sed -n ''' num2str(row) ' p''' ];

[retVal, b] = system(cmd);

p_n = str2num(b);



